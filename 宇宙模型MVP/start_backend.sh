#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_DIR="${ROOT_DIR}/.run-logs"
PID_FILE="${LOG_DIR}/backend.pid"
ENV_FILE="${LOG_DIR}/backend.env"
LOG_FILE="${LOG_DIR}/backend.log"
APP_HOST="${APP_HOST:-127.0.0.1}"
APP_PORT_START="${APP_PORT:-8787}"

mkdir -p "${LOG_DIR}"

require_command() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "Missing required command: $1" >&2
    exit 1
  fi
}

port_in_use() {
  local port="$1"
  lsof -tiTCP:"${port}" -sTCP:LISTEN >/dev/null 2>&1
}

find_free_port() {
  local port="$1"
  while port_in_use "${port}"; do
    port=$((port + 1))
  done
  echo "${port}"
}

write_env_file() {
  local port="$1"
  cat > "${ENV_FILE}" <<EOF
BACKEND_HOST=${APP_HOST}
BACKEND_PORT=${port}
BACKEND_URL=http://${APP_HOST}:${port}
BACKEND_HEALTH_URL=http://${APP_HOST}:${port}/api/health
BACKEND_LOG=${LOG_FILE}
EOF
}

wait_for_backend() {
  local url="$1"
  local pid="$2"

  for _ in $(seq 1 25); do
    if curl -fsS --max-time 2 "${url}" >/dev/null 2>&1; then
      return 0
    fi
    if ! kill -0 "${pid}" 2>/dev/null; then
      echo "Backend exited before becoming ready." >&2
      tail -n 40 "${LOG_FILE}" >&2 || true
      return 1
    fi
    sleep 1
  done

  echo "Backend did not become ready: ${url}" >&2
  tail -n 40 "${LOG_FILE}" >&2 || true
  return 1
}

require_command python3
require_command lsof
require_command curl

cleanup_stale_state() {
  if [[ -f "${PID_FILE}" ]]; then
    existing_pid="$(cat "${PID_FILE}" 2>/dev/null || true)"
    if [[ -z "${existing_pid}" ]] || ! kill -0 "${existing_pid}" 2>/dev/null; then
      rm -f "${PID_FILE}" "${ENV_FILE}"
    fi
  fi
}

cleanup_stale_state

if [[ -f "${PID_FILE}" ]]; then
  existing_pid="$(cat "${PID_FILE}")"
  if [[ -n "${existing_pid}" ]] && kill -0 "${existing_pid}" 2>/dev/null; then
    if [[ -f "${ENV_FILE}" ]]; then
      # shellcheck disable=SC1090
      source "${ENV_FILE}"
      if [[ -n "${BACKEND_HEALTH_URL:-}" ]] && curl -fsS --max-time 2 "${BACKEND_HEALTH_URL}" >/dev/null 2>&1; then
        echo "Backend already running: ${BACKEND_URL} (PID ${existing_pid})"
        exit 0
      fi
    fi
  fi
fi

BACKEND_PORT="$(find_free_port "${APP_PORT_START}")"
BACKEND_URL="http://${APP_HOST}:${BACKEND_PORT}"
BACKEND_HEALTH_URL="${BACKEND_URL}/api/health"

: > "${LOG_FILE}"
pushd "${ROOT_DIR}" >/dev/null
nohup env APP_HOST="${APP_HOST}" APP_PORT="${BACKEND_PORT}" python3 -m backend.server >"${LOG_FILE}" 2>&1 < /dev/null &
BACKEND_PID=$!
popd >/dev/null

echo "${BACKEND_PID}" > "${PID_FILE}"
write_env_file "${BACKEND_PORT}"
wait_for_backend "${BACKEND_HEALTH_URL}" "${BACKEND_PID}"

echo "Backend started"
echo "  URL   : ${BACKEND_URL}"
echo "  Health: ${BACKEND_HEALTH_URL}"
echo "  PID   : ${BACKEND_PID}"
echo "  Log   : ${LOG_FILE}"
