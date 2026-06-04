#!/usr/bin/env bash
set -euo pipefail

# run_demo.sh — full evaluation run lifecycle with the 'briefcase' CLI.
#
# Lifecycle: register a dataset -> store secrets -> submit a run -> monitor -> fetch results.
#
# PREREQUISITES for a real (non --dry-run) run:
#   1. Install the CLI with the run extra: pip install 'briefcase-ai==3.3.0'.
#   2. Bring up the engine stack: "briefcase stack up" (pulls pinned images, seeds refs).
#   3. For scoring, log in to the private-beta scorer image: docker login ghcr.io (beta read access).
#      Without it, run "briefcase stack up --no-scorer"; runs enqueue but are not scored.
#   4. Preflight: "briefcase doctor" (checks Docker, image pull, gRPC reflection, compat matrix).
#
# "briefcase stack up" seeds the family rl-gym-env with the baseline + candidate refs below.
# BASELINE / CANDIDATE env vars override the seeded refs:
#   BASELINE=my-base CANDIDATE=my-cand ./run_demo.sh

BASELINE="${BASELINE:-rl-gym-env:cuda-base}"
CANDIDATE="${CANDIDATE:-rl-gym-env:cartpole}"

banner() {
  echo
  echo "=================================================================="
  echo ">> $1"
  echo "=================================================================="
}

banner "Step 1/5 — Register dataset 'xor' (synthetic://xor, self-contained)"
briefcase dataset register xor --uri synthetic://xor

banner "Step 2/5 — Store secret OCI_JJ_S3_ENDPOINT"
briefcase secret set OCI_JJ_S3_ENDPOINT=http://127.0.0.1:9000

banner "Step 3/5 — Submit run 'demo' (gate mode: score CANDIDATE against BASELINE)"
echo "   baseline (checkpoint): ${BASELINE}"
echo "   candidate (repository): ${CANDIDATE}"
briefcase run submit demo \
  --repository "${CANDIDATE}" \
  --dataset xor \
  --checkpoint "${BASELINE}" \
  --metric f1

banner "Step 4/5 — Monitor (list, then inspect)"
briefcase run list
briefcase run inspect demo

banner "Step 5/5 — Fetch results (--depth=bench scorecard with the XOR 'accept' verdict)"
briefcase run results demo

echo
echo "Done. The run 'demo' is registered; results above show the verdict scorecard."
