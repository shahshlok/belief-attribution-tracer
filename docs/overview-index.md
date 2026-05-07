# TRACER Documentation Index

## What this package is for

This repository is a reviewer artifact for the belief-attribution study. The goal of this index is to give you a complete reading order that does not require opening source files.

## Recommended reading order (non-technical)

1. `README.md`
   - What the project is, what questions it answers, and how to verify the headline numbers.
2. `docs/overview-index.md` (this file)
   - Navigation map and terminology.
3. `docs/reviewer-onboarding.md`
   - Step-by-step reviewer path from claims to outputs.
4. `ARTIFACT.md`
   - Final artifact contents and high-level verification sequence.
5. `REPRODUCIBILITY.md`
   - Exact commands to re-run the published artifact layer.
6. `DATA_PROVENANCE.md`
   - Synthetic data origin, restoration, and privacy context.

## Recommended reading order (method-first)

1. `docs/methodology.md`
2. `docs/matching.md`
3. `docs/analysis-pipeline.md`
4. `docs/architecture.md`
5. `docs/metrics-guide.md`
6. `docs/cli-reference.md`

## Claim-to-artifact validation map

Use `docs/claim-to-artifact-map.md` as the direct trace from each publication claim to one or more artifact files.

## Directory walkthrough

- `authentic_seeded/`
  - 2,400 synthetic Java submissions and manifests.
- `detections/`
  - Frozen model detection JSONs used in analysis.
- `runs/run_final_main/`
  - Paper primary condition (label-exclusive).
- `runs/run_final_ablation/`
  - Paper ablation condition (label-inclusive).
- `docs/`
  - Full procedural and interpretation documentation.
- `data/`
  - Ground-truth definitions, prompts, and rubric files.

## Minimal reproduction flow

- Level A: no API keys
  - Inspect `runs/run_final_main/metrics.json` and `runs/run_final_ablation/metrics.json`.
- Level B: re-run from frozen detections
  - Use commands in `REPRODUCIBILITY.md`.
- Level C: regenerate raw detections
  - Use `analyze.py`/`miscons.py` with provider keys.

## Glossary

- **Primary condition**: label-exclusive analysis (`--include-label-text false`).
- **Ablation**: label-inclusive matching (`--include-label-text true`) used for leakage risk comparison.
- **Specificity**: true negative rate; central to false-positive risk.
- **Synthetic ground truth**: known misconception labels injected by design.

## How to interpret disagreements

If two docs disagree, follow this precedence:

1. `ARTIFACT.md` and `REPRODUCIBILITY.md` (publication-facing verification).
2. `docs/methodology.md` and `docs/matching.md` (analysis design and thresholds).
3. `docs/analysis-pipeline.md` (end-to-end data flow).
4. Remaining topic notes (`prompts.md`, `complexity-gradient.md`, `notional-machines.md`).
