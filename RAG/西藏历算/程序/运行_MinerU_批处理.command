#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

python3 "$SCRIPT_DIR/mineru_batch.py" --root "$SCRIPT_DIR" "$@"

echo
read -n 1 -s -r -p "处理结束，按任意键退出..."
