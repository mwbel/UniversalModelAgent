#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VERSION_DIR="${ROOT_DIR}/versions/宇宙模型-v0.2"

cd "${VERSION_DIR}/frontend-react"
FRONTEND_HOST="${FRONTEND_HOST:-127.0.0.1}" \
FRONTEND_PORT="${FRONTEND_PORT:-5174}" \
APP_HOST="${APP_HOST:-127.0.0.1}" \
APP_PORT="${APP_PORT:-8788}" \
npm run dev
