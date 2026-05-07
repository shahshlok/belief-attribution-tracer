# Belief Attribution TRACER Artifact

## Purpose and scope

This repository is a public artifact for the paper **Notional Machines, Not Just Errors: Toward Belief Attribution with Instructor-Facing LLMs**. It contains all materials needed to inspect the experimental design, the frozen primary outputs, and the post-hoc analysis artifacts behind the paper results.

The artifact is intentionally narrow: it documents a controlled benchmark for belief-attribution behavior, not a production system or classroom deployment.

The two core research questions represented in the artifacts are:

- Can LLM outputs be used to hypothesize **what misconception a student may hold**, not just where code is wrong?
- How does model behavior differ when misconception category text is hidden during matching versus shown?

## What this repository contains

| Path | Purpose |
| --- | --- |
| `authentic_seeded/` | Synthetic CS1 Java submissions and manifests for A1–A3 |
| `detections/` | Frozen LLM detection outputs used by all paper analyses |
| `runs/run_final_main/` | Frozen publication artifact for the label-exclusive condition |
| `runs/run_final_ablation/` | Frozen publication artifact for the ablation (label-inclusive matching) |
| `data/` | Assignment prompts, rubrics, tests, and ground-truth files |
| `docs/` | Methodology, matching logic, metric interpretation, and technical notes |
| `analyze.py` | Cross-validation and analysis pipeline |
| `miscons.py` | Detection generation orchestrator |

## Reproducibility ladder

Use this in ascending cost order:

1. **Inspect frozen results (no API keys needed)**
   - Read `runs/run_final_main/` and `runs/run_final_ablation/` summaries.
2. **Re-run analysis from existing detections (requires OpenAI embeddings key)**
   - Recompute report artifacts from frozen detection JSONs.
3. **Re-run detections (requires provider keys and substantial API budget)**
   - Regenerate raw LLM outputs from the seeded submissions.

## Repository map for first-time reviewers

1. Start with **`docs/methodology.md`** to understand the 5-fold split, calibration policy, and why this is a controlled benchmark.
2. Read **`docs/matching.md`** for semantic matching and why label leakage mattered for the ablation.
3. Read **`docs/metrics-guide.md`** for precision/recall/specificity interpretation in this setting.
4. Validate claims quickly using **`ARTIFACT.md`** and **`RUNS`** metrics files.
5. If you want reproducibility commands, use **`REPRODUCIBILITY.md`**.

## What the final numbers mean

The artifact includes two publication conditions:

- `run_final_main` (label-exclusive):
  - Precision `0.577`
  - Recall `0.872`
  - Specificity `0.848`
- `run_final_ablation` (label-inclusive):
  - Precision `0.511`
  - Recall `0.982`
  - Specificity `0.774`

The difference is not “better or worse in every dimension”; it is an explicit precision-recall tradeoff where exposing misconception text increases sensitivity and raises false-positive risk.

## Data and evidence boundaries

- The benchmark is synthetic, with controlled generation of misconception-seeded and clean submissions.
- The artifact is suitable for replication of analysis and interpretation, but not for claiming ecological validity to real student populations.
- The repository does not claim to recover ground-truth student belief, and it should not be interpreted as a grading-grade diagnostic system.

## Quickstart commands

```bash
uv sync

# No-key checks (frozen outputs)
cat runs/run_final_main/metrics.json
cat runs/run_final_ablation/metrics.json

# Rerun main and ablation from frozen detections
export OPENAI_API_KEY="sk-..."
uv run python analyze.py analyze-publication --run-name reviewer_main --include-label-text false
uv run python analyze.py analyze-publication --run-name reviewer_ablation --include-label-text true
```

Reproduced outputs are written under `runs/v2/`.

Optional regeneration path (full-cost):

```bash
export OPENAI_API_KEY="sk-..."
export ANTHROPIC_API_KEY="sk-ant-..."
export GOOGLE_API_KEY="..."

uv run python miscons.py all-strategies --assignment a1
uv run python miscons.py all-strategies --assignment a2
uv run python miscons.py all-strategies --assignment a3
```

## Documentation package

In addition to this README, use:

- `docs/architecture.md`
- `docs/analysis-pipeline.md`
- `docs/notional-machines.md`
- `docs/matching.md`
- `docs/cli-reference.md`
- `ARTIFACT.md`
- `REPRODUCIBILITY.md`
- `DATA_PROVENANCE.md`

## Citation and reuse

If you reuse this artifact, cite the repository with the provided `CITATION.cff` and make sure to carry forward the claim boundaries above when summarizing results.

```bibtex
@software{shah2026tracer,
  author = {Shah, Shlok},
  title = {Belief Attribution TRACER Artifact},
  year = {2026},
  url = {https://github.com/shahshlok/belief-attribution-tracer}
}
```

## For reviewers and re-runners

See [docs/reviewer-onboarding.md](docs/reviewer-onboarding.md) for a full non-code walkthrough from study question to final metric interpretation.
