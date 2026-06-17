#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FRONTEND_DIR="${ROOT_DIR}/frontend"
LOG_DIR="${ROOT_DIR}/.run-logs"
PID_FILE="${LOG_DIR}/static-frontend.pid"
ENV_FILE="${LOG_DIR}/static-frontend.env"
BACKEND_ENV_FILE="${LOG_DIR}/static-backend.env"
LOG_FILE="${LOG_DIR}/static-frontend.log"
RUNTIME_CONFIG_FILE="${FRONTEND_DIR}/runtime-config.js"
FRONTEND_HOST="${FRONTEND_HOST:-127.0.0.1}"
FRONTEND_PORT_START="${FRONTEND_PORT:-8001}"

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

resolve_backend_url() {
  if [[ -n "${BACKEND_URL:-}" ]]; then
    echo "${BACKEND_URL}"
    return 0
  fi

  if [[ -f "${BACKEND_ENV_FILE}" ]]; then
    # shellcheck disable=SC1090
    source "${BACKEND_ENV_FILE}"
    if [[ -n "${BACKEND_URL:-}" ]]; then
      echo "${BACKEND_URL}"
      return 0
    fi
  fi

  echo "http://127.0.0.1:8787"
}

write_runtime_config() {
  local backend_url="$1"
  local frontend_port="$2"

  cat > "${RUNTIME_CONFIG_FILE}" <<EOF
window.__UMA_RUNTIME_CONFIG__ = {
  apiBaseUrl: "${backend_url}",
  backendUrl: "${backend_url}",
  frontendUrl: "http://${FRONTEND_HOST}:${frontend_port}",
  generatedAt: "$(date '+%Y-%m-%d %H:%M:%S')"
};
EOF
}

write_env_file() {
  local port="$1"
  local backend_url="$2"
  local pid="$3"
  cat > "${ENV_FILE}" <<EOF
FRONTEND_HOST=${FRONTEND_HOST}
FRONTEND_PORT=${port}
FRONTEND_URL=http://${FRONTEND_HOST}:${port}
FRONTEND_LOG=${LOG_FILE}
FRONTEND_RUNTIME_CONFIG=${RUNTIME_CONFIG_FILE}
FRONTEND_BACKEND_URL=${backend_url}
FRONTEND_PID=${pid}
EOF
}

wait_for_frontend() {
  local url="$1"
  local pid="$2"

  for _ in $(seq 1 20); do
    if curl -fsSI --max-time 2 "${url}" >/dev/null 2>&1 || curl -fsS --max-time 2 "${url}" >/dev/null 2>&1; then
      return 0
    fi
    if ! kill -0 "${pid}" 2>/dev/null; then
      echo "Frontend exited before becoming ready." >&2
      tail -n 40 "${LOG_FILE}" >&2 || true
      return 1
    fi
    sleep 1
  done

  echo "Frontend did not become ready: ${url}" >&2
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

FRONTEND_URL=""
if [[ -f "${PID_FILE}" ]]; then
  existing_pid="$(cat "${PID_FILE}")"
  if [[ -n "${existing_pid}" ]] && kill -0 "${existing_pid}" 2>/dev/null; then
    if [[ -f "${ENV_FILE}" ]]; then
      # shellcheck disable=SC1090
      source "${ENV_FILE}"
      if [[ -n "${FRONTEND_URL:-}" ]] && (curl -fsSI --max-time 2 "${FRONTEND_URL}" >/dev/null 2>&1 || curl -fsS --max-time 2 "${FRONTEND_URL}" >/dev/null 2>&1); then
        backend_url="$(resolve_backend_url)"
        write_runtime_config "${backend_url}" "${FRONTEND_PORT}"
        echo "Frontend already running: ${FRONTEND_URL} (PID ${existing_pid})"
        exit 0
      fi
    fi
  fi
fi

backend_url="$(resolve_backend_url)"
FRONTEND_PORT="$(find_free_port "${FRONTEND_PORT_START}")"
FRONTEND_URL="http://${FRONTEND_HOST}:${FRONTEND_PORT}"

write_runtime_config "${backend_url}" "${FRONTEND_PORT}"
: > "${LOG_FILE}"
pushd "${FRONTEND_DIR}" >/dev/null
nohup python3 -m http.server "${FRONTEND_PORT}" --bind "${FRONTEND_HOST}" >"${LOG_FILE}" 2>&1 < /dev/null &
FRONTEND_PID=$!
popd >/dev/null

echo "${FRONTEND_PID}" > "${PID_FILE}"
write_env_file "${FRONTEND_PORT}" "${backend_url}" "${FRONTEND_PID}"
wait_for_frontend "${FRONTEND_URL}" "${FRONTEND_PID}"

echo "Frontend started"
echo "  URL   : ${FRONTEND_URL}"
echo "  Index : ${FRONTEND_URL}/index.html"
echo "  Tester: ${FRONTEND_URL}/model-tester.html"
echo "  API   : ${backend_url}"
echo "  PID   : ${FRONTEND_PID}"
echo "  Log   : ${LOG_FILE}"
