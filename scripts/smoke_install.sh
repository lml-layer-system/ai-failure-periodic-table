#!/usr/bin/env bash
# Editable install smoke test (clean venv). Run from repo root:
#   bash scripts/smoke_install.sh
# Or: bash scripts/smoke_install.sh /path/to/ai-failure-periodic-table
set -euo pipefail

ROOT="$(cd "${1:-.}" && pwd)"
TMP="${TMPDIR:-/tmp}/aift-smoke-$$"
cleanup() { rm -rf "$TMP"; }
trap cleanup EXIT

python3 -m venv "$TMP/venv"
# shellcheck source=/dev/null
source "$TMP/venv/bin/activate"
pip install -q -U pip build
(cd "$ROOT" && pip install -q -e ".[mcp]")

SMOKE_TEXT="The model fabricated a scientific citation that doesn't exist"

cd "$ROOT"
python -m src.cli --daily-driver "$SMOKE_TEXT" \
  | python -c "import json,sys; d=json.load(sys.stdin); assert d.get('in_table') is True; print('smoke: --daily-driver OK')"
python -m src.cli --json "$SMOKE_TEXT" \
  | python -c "import json,sys; d=json.load(sys.stdin); assert d.get('in_table') is True; print('smoke: --json OK')"

WHEEL_DIR="$TMP/wheels"
# Building on ExFAT/network volumes can litter AppleDouble files (._*) that break setuptools;
# stage a clean copy on the default temp filesystem (usually APFS) then build there.
BUILDSRC="$TMP/buildsrc"
rm -rf "$BUILDSRC"
mkdir -p "$BUILDSRC"
export COPYFILE_DISABLE=1
rsync -a \
  --exclude '.git' \
  --exclude '__pycache__' \
  --exclude '*.pyc' \
  --exclude '.pytest_cache' \
  --exclude '._*' \
  --exclude '.venv' \
  "$ROOT/" "$BUILDSRC/"
(cd "$BUILDSRC" && python -m build --wheel --outdir "$WHEEL_DIR" >/dev/null)
pip uninstall -y ai-failure-periodic-table 2>/dev/null || true
pip install -q "$WHEEL_DIR"/*.whl "mcp>=1.2"

cd "$TMP"
python -m src.cli --json "$SMOKE_TEXT" \
  | python -c "import json,sys; d=json.load(sys.stdin); assert d.get('in_table') is True; print('smoke: wheel --json OK')"

echo "smoke_install.sh: all OK"
