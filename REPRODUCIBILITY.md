# Reproducibility Instructions

This document describes the expected reproduction path for the TRACER belief-attribution artifact.

## Environment

The project uses Python and `uv`.

```bash
uv sync
```

The final result files can be inspected without API keys. Rerunning semantic matching requires `OPENAI_API_KEY` because the analysis embeds model outputs and ground-truth misconception descriptions. Regenerating detections also requires provider keys for OpenAI, Anthropic, and Google.

## Verify Checked-In Results

The final paper-facing metrics are checked in:

```bash
cat runs/run_final_main/metrics.json
cat runs/run_final_ablation/metrics.json
```

Expected main-run values:

- Precision: `0.577`
- Recall: `0.872`
- Specificity: `0.848`

Expected label-inclusive ablation values:

- Precision: `0.511`
- Recall: `0.982`
- Specificity: `0.774`

## Rerun Analysis from Frozen Detections

Set the embedding key:

```bash
export OPENAI_API_KEY="sk-..."
```

Run the main condition:

```bash
uv run python analyze.py analyze-publication \
  --run-name reviewer_main \
  --include-label-text false
```

Run the ablation:

```bash
uv run python analyze.py analyze-publication \
  --run-name reviewer_ablation \
  --include-label-text true
```

The outputs are written to:

- `runs/v2/run_reviewer_main/`
- `runs/v2/run_reviewer_ablation/`

Because embedding providers can change over time, exact numerical equality is not guaranteed indefinitely. The checked-in `runs/run_final_main/` and `runs/run_final_ablation/` directories are the frozen paper artifacts.

## Regenerate Raw Detections

This step is optional. It is slower, more expensive, and depends on current external model availability.

```bash
export OPENAI_API_KEY="sk-..."
export ANTHROPIC_API_KEY="sk-ant-..."
export GOOGLE_API_KEY="..."

uv run python miscons.py all-strategies --assignment a1
uv run python miscons.py all-strategies --assignment a2
uv run python miscons.py all-strategies --assignment a3
```

Detection outputs are written under:

- `detections/a1_multi/`
- `detections/a2_multi/`
- `detections/a3_multi/`

## Interpretation

The primary analysis is label-exclusive. It compares the model's generated student-thinking hypothesis to the ground-truth misconception description without exposing the misconception label text. The label-inclusive condition is an ablation intended to show how evaluation shortcuts can inflate recall while degrading specificity.

Specificity and false positives are central to the artifact because belief attribution is risk-asymmetric: falsely diagnosing a misconception can be more harmful than abstaining.

