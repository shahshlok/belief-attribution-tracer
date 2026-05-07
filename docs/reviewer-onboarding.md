# Reviewer Onboarding Guide

This guide is written for researchers who want to verify the TRACER paper results without reading implementation details first.

## 1) Start here: what question was tested

The paper studies belief attribution in a controlled CS1 setting. It does not attempt to claim real student belief recovery. Instead, it asks whether language-model outputs align with seeded misconception ground truth when the evidence is synthetically controlled.

Primary interpretation questions:

- Is the model identifying *what is wrong* (bug-centric) or *what the student might be thinking* (misconception-centric)?
- How stable are these claims under threshold calibration and bootstrap variation?
- What is the false-positive risk profile, especially on clean submissions?

## 2) Read the frozen evidence before running anything

Inspect these in order:

1. `runs/run_final_main/metrics.json`
2. `runs/run_final_main/fold_results.csv`
3. `runs/run_final_main/report.md`
4. `runs/run_final_main/compliance_report.md` (if present in your snapshot)
5. `runs/run_final_ablation/*` for the label-inclusive comparison

Record that the label-exclusive condition is the primary analysis and the inclusive condition is an ablation.

## 3) Match results to study claims

For each file:

- `metrics.json` gives aggregate precision, recall, and specificity.
- `fold_results.csv` shows per-fold behavior and confirms that thresholding and reporting are not fold-specific artifacts.
- report markdown includes strategy/model/assignment summaries used in interpretation.
- run-level figures (if present) provide visual cross-checks.

If you want a direct claim mapping, continue to [docs/claim-to-artifact-map.md](claim-to-artifact-map.md).

## 4) Reproduce with minimal external dependencies

Reproduce frozen-output analysis with:

```bash
uv run python analyze.py analyze-publication --run-name reviewer_main --include-label-text false
uv run python analyze.py analyze-publication --run-name reviewer_ablation --include-label-text true
```

Only `OPENAI_API_KEY` is required for this layer (for semantic matching embeddings).

## 5) Run-level semantics to avoid misinterpretation

Important distinctions:

- **Precision:** proportion of non-null model outputs that are correct matches.
- **Recall:** ability to recover seeded misconceptions in this synthetic setting.
- **Specificity:** how often clean students are correctly left unmarked (most important for false-positive risk).
- **Label-exclusive vs label-inclusive:** The difference estimates overestimation risk introduced by label leakage.

Do not treat any single metric in isolation; the paper and artifact report treat specificity and false positives as decisive for practical safety.

## 6) If you need the full pipeline evidence

The full data-flow is documented in:

- `docs/architecture.md` (overall pipeline)
- `docs/analysis-pipeline.md` (from submissions to metrics)
- `docs/matching.md` (semantic matching and thresholds)
- `docs/methodology.md` (cross-validation and calibration)
- `docs/metrics-guide.md` (interpretation guide)
- `docs/context.md` (paper framing and language discipline)

## 7) Provenance check

When reporting this artifact in writing:

1. State that synthetic data was generated and injected with known labels.
2. State that final artifact totals are frozen in `runs/run_final_main` and `runs/run_final_ablation`.
3. State no claims of classroom readiness are implied by these results.

## 8) Where to find command-line details

- CLI entry behavior and options: `docs/cli-reference.md`
- Development and workflow notes: `docs/development.md`

## 8) Data layout sanity checklist

```text
authentic_seeded/
  a1/
    manifest.json
  a2/
  a3/
detections/
  a1_multi/
  a2_multi/
  a3_multi/
runs/
  run_final_main/
  run_final_ablation/
```

For each of the above, verify that file names and manifest links resolve before drawing conclusions. If a link is missing, rely on the closest available frozen artifact and document that limitation.
