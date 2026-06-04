#!/usr/bin/env bash
set -euo pipefail

# Step 2/5 — Store a secret.
# 'secret list' prints KEYS only, never values.

echo ">> Setting secret OCI_JJ_S3_ENDPOINT"
briefcase secret set OCI_JJ_S3_ENDPOINT=http://127.0.0.1:9000

echo ">> Stored secret keys (values are never printed):"
briefcase secret list
