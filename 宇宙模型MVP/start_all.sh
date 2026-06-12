#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BACKEND_PID=""
FRONTEND_PID=""
BACKEND_OWNED=0
FRONTEND_OWNED=0
LOG_DIR="${ROOT_DIR}/.run-logs"
BACKEND_LOG="${LOG_DIR}/backend.log"
FRONTEND_LOG="${LOG_DIR}/frontend.log"
BACKEND_HOST="${APP_HOST:-127.0.0.1}"
BACKEND_PORT="${APP_PORT:-8787}"
FRONTEND_HOST="${FRONTEND_HOST:-127.0.0.1}"
FRONTEND_PORT="${FRONTEND_PORT:-5173}"
BACKEND_HEALTH_URL="http://${BACKEND_HOST}:${BACKEND_PORT}/api/health"
FRONTEND_URL="http://${FRONTEND_HOST}:${FRONTEND_PORT}/"

require_command() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "Missing required command: $1" >&2
    exit 1
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

service_responding_once() {
  local url="$1"
  curl -fsSI --max-time 2 "${url}" >/dev/null 2>&1 || curl -fsS --max-time 2 "${url}" >/dev/null 2>&1
}

service_responding() {
  local url="$1"
  local attempts="${2:-3}"

  for ((i=1; i<=attempts; i++)); do
    if service_responding_once "${url}"; then
      return 0
    fi
    sleep 1
  done

  return 1
}

resolve_service_pid() {
  local label="$1"
  local port="$2"
  local expected_path="$3"
  local pid
  local cwd

  pid="$(pid_for_port "${port}")"
  if [[ -z "${pid}" ]]; then
    return 0
  fi

  cwd="$(cwd_for_pid "${pid}")"
  if is_pid_from_path "${pid}" "${expected_path}"; then
    echo "Reusing existing project ${label} on port ${port} (PID ${pid})." >&2
    echo "${pid}"
    return 0
  fi

  echo "Port ${port} is already in use by a non-project ${label} process." >&2
  lsof -nP -iTCP:"${port}" -sTCP:LISTEN || true
  if [[ -n "${cwd}" ]]; then
    echo "${label} cwd: ${cwd}" >&2
  fi
  exit 1
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
  local attempts="${5:-20}"

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

trap cleanup EXIT INT TERM

mkdir -p "${LOG_DIR}"

require_command python3
require_command npm
require_command lsof
require_command curl

BACKEND_PID="$(resolve_service_pid "backend" "${BACKEND_PORT}" "${ROOT_DIR}")"
FRONTEND_PID="$(resolve_service_pid "frontend" "${FRONTEND_PORT}" "${ROOT_DIR}/frontend-react")"

if [[ -z "${BACKEND_PID}" ]]; then
  echo "Starting backend on http://${BACKEND_HOST}:${BACKEND_PORT} ..."
  : > "${BACKEND_LOG}"
  (
    cd "${ROOT_DIR}"
    python3 -m backend.server
  ) >"${BACKEND_LOG}" 2>&1 &
  BACKEND_PID=$!
  BACKEND_OWNED=1
fi

if [[ -z "${FRONTEND_PID}" ]]; then
  echo "Starting frontend on http://${FRONTEND_HOST}:${FRONTEND_PORT} ..."
  : > "${FRONTEND_LOG}"
  (
    cd "${ROOT_DIR}/frontend-react"
    npm run dev
  ) >"${FRONTEND_LOG}" 2>&1 &
  FRONTEND_PID=$!
  FRONTEND_OWNED=1
fi

echo
echo "Backend PID : ${BACKEND_PID}"
echo "Frontend PID: ${FRONTEND_PID}"
echo "Backend log : ${BACKEND_LOG}"
echo "Frontend log: ${FRONTEND_LOG}"
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
