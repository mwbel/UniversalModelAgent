#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_DIR="${ROOT_DIR}/.run-logs"
BACKEND_LOG="${LOG_DIR}/backend.log"
FRONTEND_LOG="${LOG_DIR}/frontend.log"
BACKEND_ENV="${LOG_DIR}/backend.env"
FRONTEND_ENV="${LOG_DIR}/frontend.env"

BACKEND_HOST="${APP_HOST:-127.0.0.1}"
BACKEND_PORT_REQUESTED="${APP_PORT:-8788}"
FRONTEND_HOST="${FRONTEND_HOST:-127.0.0.1}"
FRONTEND_PORT_REQUESTED="${FRONTEND_PORT:-5174}"
PORT_SEARCH_LIMIT="${PORT_SEARCH_LIMIT:-80}"
STRICT_PORTS="${STRICT_PORTS:-0}"

BACKEND_PID=""
FRONTEND_PID=""
BACKEND_OWNED=0
FRONTEND_OWNED=0

require_command() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "Missing required command: $1" >&2
    exit 1
  fi
}

require_integer() {
  local name="$1"
  local value="$2"
  if ! [[ "${value}" =~ ^[0-9]+$ ]]; then
    echo "${name} must be an integer, got: ${value}" >&2
    exit 1
  fi
}

url_host_for() {
  local host="$1"
  if [[ "${host}" == "0.0.0.0" || "${host}" == "::" ]]; then
    echo "127.0.0.1"
  else
    echo "${host}"
  fi
}

pid_for_port() {
  local port="$1"
  lsof -tiTCP:"${port}" -sTCP:LISTEN 2>/dev/null | head -n 1 || true
}

cwd_for_pid() {
  local pid="$1"
  lsof -a -p "${pid}" -d cwd -Fn 2>/dev/null | awk '/^n/ { sub(/^n/, "", $0); print; exit }'
}

is_pid_from_path() {
  local pid="$1"
  local expected_path="$2"
  local cwd
  cwd="$(cwd_for_pid "${pid}")"
  [[ -n "${cwd}" && "${cwd}" == "${expected_path}" ]]
}

project_pid_on_port() {
  local port="$1"
  local expected_path="$2"
  local pid
  pid="$(pid_for_port "${port}")"
  if [[ -n "${pid}" ]] && is_pid_from_path "${pid}" "${expected_path}"; then
    echo "${pid}"
  fi
}

find_free_port() {
  local start_port="$1"
  local label="$2"
  local limit="$3"
  local port
  local end_port=$((start_port + limit))

  for ((port=start_port; port<=end_port; port++)); do
    if [[ -z "$(pid_for_port "${port}")" ]]; then
      echo "${port}"
      return 0
    fi
  done

  echo "Could not find a free ${label} port from ${start_port} to ${end_port}." >&2
  exit 1
}

resolve_port() {
  local label="$1"
  local requested_port="$2"
  local expected_path="$3"
  local pid
  local cwd
  local next_port

  pid="$(pid_for_port "${requested_port}")"
  if [[ -z "${pid}" ]]; then
    echo "${requested_port}"
    return 0
  fi

  if is_pid_from_path "${pid}" "${expected_path}"; then
    echo "Reusing existing project ${label} on port ${requested_port} (PID ${pid})." >&2
    echo "${requested_port}"
    return 0
  fi

  cwd="$(cwd_for_pid "${pid}")"
  echo "Port ${requested_port} is already in use by a non-project ${label} process." >&2
  lsof -nP -iTCP:"${requested_port}" -sTCP:LISTEN >&2 || true
  if [[ -n "${cwd}" ]]; then
    echo "${label} cwd: ${cwd}" >&2
  fi

  if [[ "${STRICT_PORTS}" == "1" ]]; then
    echo "STRICT_PORTS=1, so startup stops instead of selecting another port." >&2
    exit 1
  fi

  next_port="$(find_free_port "$((requested_port + 1))" "${label}" "${PORT_SEARCH_LIMIT}")"
  echo "Using ${label} port ${next_port} instead." >&2
  echo "${next_port}"
}

service_responding_once() {
  local url="$1"
  curl -fsSI --max-time 2 "${url}" >/dev/null 2>&1 || curl -fsS --max-time 2 "${url}" >/dev/null 2>&1
}

show_recent_logs() {
  local label="$1"
  local file="$2"
  if [[ -f "${file}" ]]; then
    echo
    echo "Recent ${label} log:"
    tail -n 20 "${file}" || true
  fi
}

wait_for_http() {
  local label="$1"
  local url="$2"
  local pid="${3:-}"
  local log_file="$4"
  local attempts="${5:-30}"

  for ((i=1; i<=attempts; i++)); do
    if service_responding_once "${url}"; then
      echo "${label} is ready: ${url}"
      return 0
    fi
    if [[ -n "${pid}" ]] && ! kill -0 "${pid}" 2>/dev/null; then
      echo "${label} exited before becoming ready." >&2
      show_recent_logs "${label}" "${log_file}"
      return 1
    fi
    sleep 1
  done

  echo "${label} did not become ready within ${attempts} seconds: ${url}" >&2
  show_recent_logs "${label}" "${log_file}"
  return 1
}

cleanup() {
  if [[ "${FRONTEND_OWNED}" -eq 1 ]] && [[ -n "${FRONTEND_PID}" ]] && kill -0 "${FRONTEND_PID}" 2>/dev/null; then
    kill "${FRONTEND_PID}" 2>/dev/null || true
  fi
  if [[ "${BACKEND_OWNED}" -eq 1 ]] && [[ -n "${BACKEND_PID}" ]] && kill -0 "${BACKEND_PID}" 2>/dev/null; then
    kill "${BACKEND_PID}" 2>/dev/null || true
  fi
}

monitor_service() {
  local label="$1"
  local pid="$2"
  local owned="$3"
  local url="$4"
  local log_file="$5"

  if [[ "${owned}" -eq 1 ]]; then
    if ! kill -0 "${pid}" 2>/dev/null; then
      echo "${label} exited."
      show_recent_logs "${label}" "${log_file}"
      exit 1
    fi
    return 0
  fi

  if ! service_responding_once "${url}"; then
    echo "${label} is no longer responding at ${url}."
    show_recent_logs "${label}" "${log_file}"
    exit 1
  fi
}

write_env_files() {
  {
    echo "APP_HOST=${BACKEND_HOST}"
    echo "APP_PORT=${BACKEND_PORT}"
    echo "BACKEND_URL=${BACKEND_URL}"
    echo "BACKEND_HEALTH_URL=${BACKEND_HEALTH_URL}"
  } > "${BACKEND_ENV}"

  {
    echo "FRONTEND_HOST=${FRONTEND_HOST}"
    echo "FRONTEND_PORT=${FRONTEND_PORT}"
    echo "FRONTEND_URL=${FRONTEND_URL}"
    echo "OCR_WORKBENCH_URL=${OCR_WORKBENCH_URL}"
    echo "APP_HOST=${BACKEND_HOST}"
    echo "APP_PORT=${BACKEND_PORT}"
    echo "BACKEND_URL=${BACKEND_URL}"
  } > "${FRONTEND_ENV}"
}

trap cleanup EXIT INT TERM

mkdir -p "${LOG_DIR}"

require_command python3
require_command npm
require_command lsof
require_command curl
require_integer APP_PORT "${BACKEND_PORT_REQUESTED}"
require_integer FRONTEND_PORT "${FRONTEND_PORT_REQUESTED}"
require_integer PORT_SEARCH_LIMIT "${PORT_SEARCH_LIMIT}"

BACKEND_PORT="$(resolve_port "backend" "${BACKEND_PORT_REQUESTED}" "${ROOT_DIR}")"
BACKEND_PID="$(project_pid_on_port "${BACKEND_PORT}" "${ROOT_DIR}")"

FRONTEND_PORT="$(resolve_port "frontend" "${FRONTEND_PORT_REQUESTED}" "${ROOT_DIR}/frontend-react")"
FRONTEND_PID="$(project_pid_on_port "${FRONTEND_PORT}" "${ROOT_DIR}/frontend-react")"

if [[ "${BACKEND_PORT}" != "${BACKEND_PORT_REQUESTED}" && -n "${FRONTEND_PID}" ]]; then
  echo "Backend moved from ${BACKEND_PORT_REQUESTED} to ${BACKEND_PORT}; starting a fresh frontend so the proxy follows it." >&2
  FRONTEND_PORT="$(find_free_port "$((FRONTEND_PORT + 1))" "frontend" "${PORT_SEARCH_LIMIT}")"
  FRONTEND_PID=""
fi

BACKEND_URL_HOST="$(url_host_for "${BACKEND_HOST}")"
FRONTEND_URL_HOST="$(url_host_for "${FRONTEND_HOST}")"
BACKEND_URL="http://${BACKEND_URL_HOST}:${BACKEND_PORT}"
BACKEND_HEALTH_URL="${BACKEND_URL}/api/health"
FRONTEND_URL="http://${FRONTEND_URL_HOST}:${FRONTEND_PORT}/"
OCR_WORKBENCH_URL="http://${FRONTEND_URL_HOST}:${FRONTEND_PORT}/?ocr=1"

write_env_files

if [[ -z "${BACKEND_PID}" ]]; then
  echo "Starting backend on ${BACKEND_URL} ..."
  : > "${BACKEND_LOG}"
  (
    cd "${ROOT_DIR}"
    APP_HOST="${BACKEND_HOST}" APP_PORT="${BACKEND_PORT}" python3 -m backend.server
  ) >"${BACKEND_LOG}" 2>&1 &
  BACKEND_PID=$!
  BACKEND_OWNED=1
fi

if [[ -z "${FRONTEND_PID}" ]]; then
  echo "Starting frontend on ${FRONTEND_URL} ..."
  : > "${FRONTEND_LOG}"
  (
    cd "${ROOT_DIR}/frontend-react"
    FRONTEND_HOST="${FRONTEND_HOST}" FRONTEND_PORT="${FRONTEND_PORT}" APP_HOST="${BACKEND_HOST}" APP_PORT="${BACKEND_PORT}" npm run dev
  ) >"${FRONTEND_LOG}" 2>&1 &
  FRONTEND_PID=$!
  FRONTEND_OWNED=1
fi

echo
echo "Backend PID       : ${BACKEND_PID}"
echo "Frontend PID      : ${FRONTEND_PID}"
echo "Backend URL       : ${BACKEND_URL}"
echo "Backend health    : ${BACKEND_HEALTH_URL}"
echo "Frontend URL      : ${FRONTEND_URL}"
echo "OCR workbench URL : ${OCR_WORKBENCH_URL}"
echo "Backend log       : ${BACKEND_LOG}"
echo "Frontend log      : ${FRONTEND_LOG}"
echo "Backend env       : ${BACKEND_ENV}"
echo "Frontend env      : ${FRONTEND_ENV}"
echo "Press Ctrl+C to stop services started by this script."
echo

BACKEND_WAIT_PID=""
FRONTEND_WAIT_PID=""
if [[ "${BACKEND_OWNED}" -eq 1 ]]; then
  BACKEND_WAIT_PID="${BACKEND_PID}"
fi
if [[ "${FRONTEND_OWNED}" -eq 1 ]]; then
  FRONTEND_WAIT_PID="${FRONTEND_PID}"
fi

if [[ "${BACKEND_OWNED}" -eq 1 ]]; then
  wait_for_http "Backend" "${BACKEND_HEALTH_URL}" "${BACKEND_WAIT_PID}" "${BACKEND_LOG}"
else
  echo "Backend is already running under this project; reusing PID ${BACKEND_PID}."
fi

if [[ "${FRONTEND_OWNED}" -eq 1 ]]; then
  wait_for_http "Frontend" "${FRONTEND_URL}" "${FRONTEND_WAIT_PID}" "${FRONTEND_LOG}"
else
  echo "Frontend is already running under this project; reusing PID ${FRONTEND_PID}."
fi

echo
echo "All services are ready."
echo "Open: ${FRONTEND_URL}"
echo "OCR : ${OCR_WORKBENCH_URL}"
echo

while true; do
  if [[ "${BACKEND_OWNED}" -eq 1 ]]; then
    monitor_service "Backend" "${BACKEND_PID}" "${BACKEND_OWNED}" "${BACKEND_HEALTH_URL}" "${BACKEND_LOG}"
  fi
  if [[ "${FRONTEND_OWNED}" -eq 1 ]]; then
    monitor_service "Frontend" "${FRONTEND_PID}" "${FRONTEND_OWNED}" "${FRONTEND_URL}" "${FRONTEND_LOG}"
  fi
  sleep 1
done
