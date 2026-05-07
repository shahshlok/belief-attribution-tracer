# Artifact Guide

This repository is a reviewer-facing artifact for the belief-attribution paper. It is intended to let a researcher inspect the data generation setup, raw model outputs, final metrics, and analysis code without needing access to the original working repository.

## What Is Included

| Path | Purpose |
| --- | --- |
| `authentic_seeded/` | Synthetic Java submissions and manifests for A1-A3. |
| `detections/` | Raw LLM outputs, grouped by assignment and prompting strategy. |
| `runs/run_final_main/` | Final label-exclusive analysis used for the main paper result. |
| `runs/run_final_ablation/` | Final label-inclusive ablation analysis. |
| `data/` | Assignments, rubrics, tests, and misconception ground truth. |
| `docs/` | Methodology and implementation documentation. |
| `analyze.py` | Cross-validation, semantic matching, metrics, and plotting pipeline. |
| `miscons.py` | Detection runner for regenerating model outputs. |

## Frozen Results

Main label-exclusive run:

- Precision: `0.577`
- Recall: `0.872`
- Specificity: `0.848`

Label-inclusive ablation:

- Precision: `0.511`
- Recall: `0.982`
- Specificity: `0.774`

The corresponding files are:

- `runs/run_final_main/metrics.json`
- `runs/run_final_ablation/metrics.json`
- `runs/run_final_main/fold_results.csv`
- `runs/run_final_ablation/fold_results.csv`

## Rerun Levels

### Level 1: Inspect frozen artifacts

No API keys are required. Read the checked-in reports and CSV/JSON artifacts under `runs/`.

### Level 2: Rerun analysis from frozen detections

Requires `OPENAI_API_KEY` for semantic embeddings.

```bash
uv sync
uv run python analyze.py analyze-publication --run-name reviewer_main --include-label-text false
uv run python analyze.py analyze-publication --run-name reviewer_ablation --include-label-text true
```

New output appears under `runs/v2/`.

### Level 3: Regenerate raw detections

Requires provider keys for the model families used by `miscons.py`:

```bash
export OPENAI_API_KEY="sk-..."
export ANTHROPIC_API_KEY="sk-ant-..."
export GOOGLE_API_KEY="..."
```

Then run, for example:

```bash
uv run python miscons.py all-strategies --assignment a1
uv run python miscons.py all-strategies --assignment a2
uv run python miscons.py all-strategies --assignment a3
```

Model availability may change over time, so the checked-in `detections/` directory is the authoritative frozen raw-output layer for verifying the submitted paper results.

## Provenance

The code and final paper-facing artifacts were exported from the current `master` branch of the original TRACER working repository. The synthetic submissions and raw detection outputs were restored from the pre-removal commit immediately before `532ab02a` (`Remove research datasets from public branch`), where those files were still present.

Recovered raw payload:

- `2,400` Java files under `authentic_seeded/`
- `4,818` JSON files under `detections/` and manifests/stats
- `7,218` recovered files total

## Claim Boundaries

This artifact supports inspection of a controlled synthetic benchmark for instructor-facing belief attribution. It does not establish recovery of true student beliefs, classroom deployment readiness, grading validity, or student-facing authoritative diagnosis.
