#!/usr/bin/env bash
set -euo pipefail

# Step 4/5 — Monitor the run.
# 'run list' shows the local run registry; 'run inspect' shows provenance for the candidate.
# Tail worker logs with: briefcase run logs demo -f

echo ">> All runs:"
briefcase run list

echo ">> Inspecting run 'demo':"
briefcase run inspect demo

echo ">> Recent worker logs for 'demo' (use -f to follow):"
briefcase run logs demo
