# Data Provenance

This artifact contains synthetic data and frozen model-output artifacts used to support the belief-attribution paper.

## Synthetic Submissions

The `authentic_seeded/` directory contains synthetic Java submissions generated for controlled evaluation. Despite the historical directory name, these are not authentic student submissions.

Included assignments:

| Assignment | Synthetic students | Java files | Manifest |
| --- | ---: | ---: | --- |
| A1 | 100 | 400 | `authentic_seeded/a1/manifest.json` |
| A2 | 100 | 400 | `authentic_seeded/a2/manifest.json` |
| A3 | 100 | 400 | `authentic_seeded/a3/manifest.json` |

Each synthetic student has four submissions. The design assigns one misconception-seeded submission and three behaviorally correct submissions per synthetic student.

## Detection Outputs

The `detections/` directory contains frozen raw LLM detection outputs grouped by assignment and prompting strategy:

- `baseline`
- `taxonomy`
- `cot`
- `socratic`

Each detection JSON records model outputs for the model configurations used in the paper analysis.

## Final Analysis Artifacts

The final checked-in analysis artifacts are:

- `runs/run_final_main/`
- `runs/run_final_ablation/`

These directories contain reports, metrics, cross-validation fold summaries, compliance summaries, sensitivity analyses, per-detection result tables, and generated figures.

## Restoration Source

The original working repository removed the raw synthetic submissions and detection outputs from public `master` in commit `532ab02a` with the message `Remove research datasets from public branch`. For this public artifact repository, those directories were restored from the immediately preceding commit, `532ab02a^`.

Recovered payload:

- `2,400` Java files under `authentic_seeded/`
- `4,818` JSON files under `detections/` plus manifests and stats
- `7,218` recovered files total

## Privacy and Ethics

The submissions in this artifact are synthetic. The repository should not be interpreted as containing human student submissions or as validating student-facing diagnosis. The artifact is intended to support transparent inspection of a controlled benchmark and its paper-facing analysis pipeline.

