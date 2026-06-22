#!/usr/bin/env bash
set -euo pipefail

LIMIT="${1:-30}"

echo "== Memory snapshot =="
date "+%Y-%m-%d %H:%M:%S %Z"
echo

echo "== Top processes by memory =="
top -l 1 -o mem -stats pid,command,threads,mem,cpu -n "$LIMIT"
echo

echo "== Relevant Codex / Node / Python / browser processes =="
pgrep -fl 'codex|node|python|uvicorn|http.server|vite|npm|Chrome|chromium' || true
echo

echo "== Listening TCP ports =="
lsof -iTCP -sTCP:LISTEN -nP | egrep 'COMMAND|Python|node|codex|Chrome|chromium' || true
echo

cat <<'NOTE'
Note:
- macOS reports reliable memory at process level, not per thread.
- The "threads" column shows thread count; memory is shared by the process and cannot be accurately attributed to individual threads.
- For thread CPU details for a process, run: ps -M -p <PID>
NOTE
