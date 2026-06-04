# Evaluation Run

> Learning path: ~15 minutes (about 5 minutes to read, ~10 minutes to run end to end against a live stack).

A runnable walkthrough of a full evaluation **run lifecycle** with the `briefcase` CLI: register a
dataset, store a secret, submit a run, monitor it, and fetch the verdict scorecard.

## What this shows

A run in Briefcase is defined by five things:

1. a descriptive **name** (the run's handle)
2. a registered **dataset**
3. a **repository** (the candidate environment ref/family)
4. a **checkpoint** (the baseline ref to score against)
5. an **entry point** (the run mode: `gate` or `hunt`)

This example wires all five together and walks the lifecycle:

```
register a dataset  ->  store secrets  ->  submit a run  ->  monitor (list/inspect/logs)  ->  fetch results
```

It uses the self-contained `synthetic://xor` dataset, submits a `gate`-mode run named `demo`, and ends
by printing a `--depth=bench` scorecard that includes the XOR `accept` verdict.

## Prerequisites

Real (non `--dry-run`) runs need a live local stack and beta scoring access. You can read and rehearse
the whole flow without any of this — see [Rehearse with `--dry-run`](#rehearse-with---dry-run) below.

- **Docker** — the local stack runs in containers.
- **The CLI installed with the `[run]` extra:** `pip install 'briefcase-ai==3.3.0'`. The `[run]` extra
  pulls the gRPC client deps so the CLI drives the engine over server reflection (no generated stubs).
- **The engine stack up.** `briefcase stack up` pulls the pinned, published engine images via a bundled
  docker-compose (no `oci-jj` checkout, no Rust toolchain) and seeds the refs. It seeds the family
  `rl-gym-env`, the baseline `rl-gym-env:cuda-base`, and the candidate `rl-gym-env:cartpole` this
  example scores against.
- **(Optional) The private-beta scorer.** The `verdict-worker` is a private GHCR image — run
  `docker login ghcr.io` with beta read access before `briefcase stack up`. Without it, run
  `briefcase stack up --no-scorer`; a run is still enqueued, but it is not scored.
- **verdictml scoring — PRIVATE BETA.** Scoring is in private beta. **Request access**; once you are
  granted access, `docker login ghcr.io` lets `stack up` pull the `verdict-worker` image. Until access
  is granted, a run is still enqueued, but it is not scored.
- **Preflight:** `briefcase doctor` checks Docker, image pull access, gRPC server reflection, and prints
  the compatibility matrix before you submit.

## How to run

Install the CLI, bring up the stack, then run the preflight:

```bash
pip install 'briefcase-ai==3.3.0'
docker login ghcr.io     # optional — private-beta scorer
briefcase stack up       # pulls pinned engine images, seeds refs
briefcase doctor         # preflight: Docker, image pull, reflection, compat matrix
```

Then run the whole lifecycle in one shot:

```bash
./run_demo.sh
```

Or run the numbered scripts in order, so you can inspect each step on its own:

```bash
./01_register_dataset.sh   # register dataset 'xor' (synthetic://xor)
./02_set_secret.sh         # store OCI_JJ_S3_ENDPOINT
./03_submit_run.sh         # submit run 'demo' in gate mode
./04_monitor.sh            # run list / inspect / logs
./05_results.sh            # fetch the --depth=bench scorecard
```

The seeded refs are `rl-gym-env:cuda-base` (baseline) and `rl-gym-env:cartpole` (candidate). Override
them with environment variables if you seeded different names:

```bash
BASELINE=my-base CANDIDATE=my-cand ./run_demo.sh
```

## Expected output

When the stack is up (`briefcase stack up`) and beta scoring access is in place:

- A run named `demo` appears in `briefcase run list`.
- The worker logs report it recorded the verdicts, e.g. `recorded N verdict(s)`.
- `briefcase run results demo` prints a `--depth=bench` scorecard that includes the XOR `accept` verdict.

## A note on the dataset

`synthetic://xor` is **self-contained** — it needs no external data, no S3 objects, and no files on
disk. That makes this example reproducible anywhere the stack runs.

## Rehearse with `--dry-run`

Every command in this example accepts `--dry-run`. With it, the CLI prints exactly what it would do
without contacting the stack, so **you can rehearse the entire lifecycle with no stack and no beta
access**. This is the recommended way to read through the flow before you stand up the real thing:

```bash
briefcase --dry-run run submit demo --repository rl-gym-env:cartpole --dataset xor --checkpoint rl-gym-env:cuda-base --metric f1
```

## State

The CLI keeps datasets, secrets, and runs as JSON under `~/.briefcase` (override with `$BRIEFCASE_HOME`).
The run **name** is its handle — use it with `inspect`, `logs`, `results`, `stop`, and `delete`.

## Appendix: from source

`briefcase stack up` pulls the published engine images, so you never need the engine source. If you are
developing the engine itself, run it from a local `oci-jj` checkout instead:

- **Check out the `oci-jj` repo and run `make up`.** This brings up Postgres+AGE, MinIO, the registry,
  the `oci-jj-server`, and the `verdict-worker`.
- **Build the `oci-jj` binary and put it on `PATH`.** In the `oci-jj` repo: `cd oci-jj/rust && cargo build`.
  This binary is only needed for the `BRIEFCASE_ENGINE=cli` subprocess fallback; the default gRPC path
  needs no binary. The CLI honors `$BRIEFCASE_OCIJJ_BIN`, `$OCI_JJ_SERVER`, and `$OCI_JJ_REPO` if you
  need to point at a non-default binary, server, or repo.
- **Seed the refs with `make seed`.** Running `make seed` in the `oci-jj` repo creates the baseline and
  candidate refs the example scores against.
