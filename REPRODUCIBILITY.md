# Reproducibility Instructions

This document gives a deterministic verification path for external reviewers.

## Scope of reproducibility

The artifact supports three reproducibility levels.

### Level A — Artifact inspection (no keys)

Purpose: Verify that the public artifact contains all publication-level artifacts.

Commands:

```bash
cat runs/run_final_main/metrics.json
cat runs/run_final_ablation/metrics.json
```

Expected values for quick checks:

- `run_final_main`: precision `0.577`, recall `0.872`, specificity `0.848`
- `run_final_ablation`: precision `0.511`, recall `0.982`, specificity `0.774`

### Level B — Deterministic reanalysis from frozen detections

Purpose: Recompute reports from existing frozen detection JSONs.

Requirements:

- `uv`
- `OPENAI_API_KEY` (for embeddings used in semantic matching)

Commands:

```bash
uv sync
export OPENAI_API_KEY="sk-..."

uv run python analyze.py analyze-publication \
  --run-name reviewer_main \
  --include-label-text false

uv run python analyze.py analyze-publication \
  --run-name reviewer_ablation \
  --include-label-text true
```

Outputs:

- `runs/v2/run_reviewer_main/`
- `runs/v2/run_reviewer_ablation/`

### Level C — Full regeneration (optional and cost-sensitive)

Purpose: Reproduce raw detections from scratch.

Requirements:

- API keys for OpenAI, Anthropic, Google
- Runtime and rate-limit budget suitable for full LLM submission grid

Commands:

```bash
export OPENAI_API_KEY="sk-..."
export ANTHROPIC_API_KEY="sk-ant-..."
export GOOGLE_API_KEY="..."

uv run python miscons.py all-strategies --assignment a1
uv run python miscons.py all-strategies --assignment a2
uv run python miscons.py all-strategies --assignment a3
```

This command path is for completeness and should not be treated as the default reproducibility target, since provider versions and outputs drift over time.

## Environment setup

```bash
uv sync
```

## Interpretation policy

The principal artifact for paper claims is `runs/run_final_main/` (label-exclusive) and `runs/run_final_ablation/` (label-inclusive comparison). Use the ablation only to evaluate robustness of the interpretation, not as a replacement primary claim.

Specificity and false-positive control are primary interpretation points in this benchmark because false positive errors are more harmful than misses in the instructor-facing setting this work studies.

## Failure checks

If outputs are missing:

- confirm the working directory is this artifact repository,
- confirm `runs/run_final_main/` and `runs/run_final_ablation/` are present,
- confirm dependency install with `uv sync`,
- ensure `OPENAI_API_KEY` is set before Level B reruns.
