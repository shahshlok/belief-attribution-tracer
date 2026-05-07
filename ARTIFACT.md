# Artifact Guide

This repository is the reviewer-facing research artifact for the TRACER belief-attribution study.

## Purpose of this artifact

The artifact is designed so a reviewer can:

- Verify the exact evidence that supported the paper claims.
- Understand the full processing flow without reading implementation details first.
- Rerun analysis from frozen outputs.
- Optionally regenerate model detections under the same experimental structure.

The artifact is intentionally *not* a deployment package and does not claim classroom use.

## Included components

| Path | What it contributes |
| --- | --- |
| `authentic_seeded/` | Synthetic submission set with one seeded misconception plus clean control submissions per synthetic student. |
| `data/` | Ground-truth misconception definitions, assignment prompts, rubrics, and tests. |
| `detections/` | Raw LLM detection JSONs used by the analysis pipeline. |
| `runs/run_final_main/` | Frozen main analysis for the label-exclusive condition. |
| `runs/run_final_ablation/` | Frozen ablation analysis for the label-inclusive condition. |
| `docs/` | Method write-ups on methodology, matching, prompts, and metric interpretation. |
| `analyze.py` | Publication analysis pipeline (cross-validation, matching, scoring, bootstrapped summaries). |
| `miscons.py` | Detection orchestration for model runs over all configurations. |

## Primary interpretive split

The artifact distinguishes two publication conditions:

- `run_final_main`: label-exclusive matching (recommended primary condition).
- `run_final_ablation`: label-inclusive matching (explicit ablation).

The main recommendation is to interpret paper claims using the label-exclusive condition and treat the ablation as a cautionary comparison showing recall-specificity tradeoffs.

## Artifact verification sequence

1. Read high-level claims and framing in:
   - `README.md`
   - `docs/context.md`
   - `docs/methodology.md`
2. Inspect frozen outputs in:
   - `runs/run_final_main/metrics.json`
   - `runs/run_final_main/fold_results.csv`
   - `runs/run_final_ablation/metrics.json`
   - `runs/run_final_ablation/fold_results.csv`
3. Reproduce analysis from frozen detections (API-key-assisted) via:
   - `analyze.py analyze-publication`
4. Optionally regenerate detections with `miscons.py`.

## Reproducibility and rerun policy

No external API calls are needed to validate the final published values; they are present in `runs/`.

Re-creating those values from frozen detections is allowed and controlled through a stable command path.

Re-generating raw detections is intentionally optional because it depends on current provider availability and versioning.

## Evidence boundaries

- Synthetic data and frozen outputs are authoritative for artifact-level replication.
- Exact equality of reruns with regenerated detections is not guaranteed over time due to model API drift.
- The results are synthetic and do not assert actual student belief states.

## Key metrics reported

Main run:

- Precision: `0.577`
- Recall: `0.872`
- Specificity: `0.848`

Ablation:

- Precision: `0.511`
- Recall: `0.982`
- Specificity: `0.774`

## Related documentation

- `REPRODUCIBILITY.md` for command-level rerun instructions.
- `DATA_PROVENANCE.md` for source and restoration constraints.
- `docs/analysis-pipeline.md` for end-to-end processing sequence.
- `docs/matching.md` for semantic matching and threshold choices.
- `docs/metrics-guide.md` for interpretation guardrails.
- `docs/cli-reference.md` for available entry points.

## Claim boundaries

The artifact supports controlled-method inspection in a synthetic benchmark.
It does not claim:

- that the model recovers true student cognition from real classes,
- student-facing diagnosis quality,
- or direct classroom deployment readiness.

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
