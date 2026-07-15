#!/usr/bin/env bash
#
# run_tests.sh — the session-start test command.
#
# PROJECT_BRIEF §1.3 / §8: run the FULL test suite at session start AND before
# every commit. No commit with failing tests. A silently corrupted foundational
# table poisons everything downstream.
#
# Usage (from repo root or anywhere):
#     bash formal/tests/run_tests.sh
#
# Skeleton behaviour: with no test modules yet, this reports a clean pass so the
# session ritual is exercisable from day one. As the formal layer lands, drop
# test_*.py files anywhere under formal/ and they are discovered automatically.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT"

echo "== 命理 · astrology · tarot research system — test harness =="
echo "root: $ROOT"

# Discover test modules under the formal layer.
mapfile -t TESTS < <(find formal -type f \( -name 'test_*.py' -o -name '*_test.py' \) 2>/dev/null | sort)

if [ "${#TESTS[@]}" -eq 0 ]; then
  echo "No test modules yet (formal layer not implemented — bedrock skeleton)."
  echo "PASS: 0 tests, 0 failures."
  exit 0
fi

echo "discovered ${#TESTS[@]} test module(s)."

if command -v pytest >/dev/null 2>&1; then
  exec pytest -q formal
elif command -v python3 >/dev/null 2>&1; then
  exec python3 -m unittest discover -s formal -p 'test_*.py' -t "$ROOT"
else
  echo "ERROR: neither pytest nor python3 found; cannot run tests." >&2
  exit 2
fi
