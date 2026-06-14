#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

"${ROOT_DIR}/start_backend.sh"

# shellcheck disable=SC1090
source "${ROOT_DIR}/.run-logs/backend.env"

BACKEND_URL="${BACKEND_URL}" "${ROOT_DIR}/start_frontend.sh"

# shellcheck disable=SC1090
source "${ROOT_DIR}/.run-logs/frontend.env"

echo
echo "Static stack ready"
echo "  Backend : ${BACKEND_URL}"
echo "  Frontend: ${FRONTEND_URL}"
echo "  Home    : ${FRONTEND_URL}/index.html"
echo "  Tester  : ${FRONTEND_URL}/model-tester.html"
