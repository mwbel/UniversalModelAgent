#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BACKEND_ENV="${ROOT_DIR}/.run-logs/static-backend.env"
FRONTEND_ENV="${ROOT_DIR}/.run-logs/static-frontend.env"

service_responding_once() {
  local url="$1"
  curl -fsSI --max-time 2 "${url}" >/dev/null 2>&1 || curl -fsS --max-time 2 "${url}" >/dev/null 2>&1
}

show_recent_log() {
  local label="$1"
  local file="$2"
  if [[ -f "${file}" ]]; then
    echo
    echo "Recent ${label} log:"
    tail -n 30 "${file}" || true
  fi
}

cleanup() {
  echo
  echo "Stopping static stack..."
  if [[ -n "${FRONTEND_PID:-}" ]] && kill -0 "${FRONTEND_PID}" 2>/dev/null; then
    kill "${FRONTEND_PID}" 2>/dev/null || true
  fi
  if [[ -n "${BACKEND_PID:-}" ]] && kill -0 "${BACKEND_PID}" 2>/dev/null; then
    kill "${BACKEND_PID}" 2>/dev/null || true
  fi
}

trap cleanup EXIT INT TERM

"${ROOT_DIR}/start_backend.sh"

# shellcheck disable=SC1090
source "${BACKEND_ENV}"

BACKEND_URL="${BACKEND_URL}" "${ROOT_DIR}/start_frontend.sh"

# shellcheck disable=SC1090
source "${FRONTEND_ENV}"

echo
echo "Static stack ready"
echo "  Backend : ${BACKEND_URL}"
echo "  Frontend: ${FRONTEND_URL}"
echo "  Home    : ${FRONTEND_URL}/index.html"
echo "  Tester  : ${FRONTEND_URL}/model-tester.html"
echo
echo "Keep this terminal open while using the app. Press Ctrl+C to stop."

while true; do
  if [[ -n "${BACKEND_PID:-}" ]] && ! kill -0 "${BACKEND_PID}" 2>/dev/null; then
    echo "Backend process exited."
    show_recent_log "backend" "${BACKEND_LOG:-}"
    exit 1
  fi

  if [[ -n "${FRONTEND_PID:-}" ]] && ! kill -0 "${FRONTEND_PID}" 2>/dev/null; then
    echo "Frontend process exited."
    show_recent_log "frontend" "${FRONTEND_LOG:-}"
    exit 1
  fi

  if ! service_responding_once "${BACKEND_HEALTH_URL}"; then
    echo "Backend is not responding: ${BACKEND_HEALTH_URL}"
    show_recent_log "backend" "${BACKEND_LOG:-}"
    exit 1
  fi

  if ! service_responding_once "${FRONTEND_URL}"; then
    echo "Frontend is not responding: ${FRONTEND_URL}"
    show_recent_log "frontend" "${FRONTEND_LOG:-}"
    exit 1
  fi

  sleep 2
done
