#!/usr/bin/env bash
set -euo pipefail

# Step 1/5 — Register the dataset.
# 'synthetic://xor' is self-contained: no external data, no S3 objects, no files on disk.

echo ">> Registering dataset 'xor' (synthetic://xor)"
briefcase dataset register xor --uri synthetic://xor

echo ">> Registered datasets:"
briefcase dataset list
