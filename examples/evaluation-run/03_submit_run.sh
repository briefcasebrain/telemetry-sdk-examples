#!/usr/bin/env bash
set -euo pipefail

# Step 3/5 — Submit the run.
# A run is defined by: name (demo), dataset (xor), repository (candidate),
# checkpoint (baseline), and entry point (gate mode is the default here).
#
# BASELINE / CANDIDATE env vars override the seeded refs from "make seed".

BASELINE="${BASELINE:-gym-base}"
CANDIDATE="${CANDIDATE:-gym-cand}"

echo ">> Submitting run 'demo'"
echo "   baseline (checkpoint): ${BASELINE}"
echo "   candidate (repository): ${CANDIDATE}"
briefcase run submit demo \
  --repository "${CANDIDATE}" \
  --dataset xor \
  --checkpoint "${BASELINE}" \
  --metric f1
