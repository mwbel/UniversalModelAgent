#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VERSION_DIR="${ROOT_DIR}/versions/宇宙模型-v0.2"

APP_PORT="${APP_PORT:-8788}" "${VERSION_DIR}/start_backend.sh"
