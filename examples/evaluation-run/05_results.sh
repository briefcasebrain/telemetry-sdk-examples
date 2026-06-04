#!/usr/bin/env bash
set -euo pipefail

# Step 5/5 — Fetch results.
# Prints a --depth=bench scorecard. With beta scoring access in place, this includes
# the XOR 'accept' verdict.

echo ">> Results for run 'demo' (--depth=bench scorecard):"
briefcase run results demo
