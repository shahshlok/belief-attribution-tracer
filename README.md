# Belief Attribution TRACER Artifact

This repository is the public research artifact for the paper:

**Notional Machines, Not Just Errors: Toward Belief Attribution with Instructor-Facing LLMs**

It contains the source code, synthetic CS1 Java submissions, raw LLM detection outputs, final analysis artifacts, figures, and documentation needed to inspect and rerun the TRACER evidence reported in the paper.

TRACER, **Taxonomic Research of Aligned Cognitive Error Recognition**, is a controlled research framework for evaluating whether large language models can generate plausible hypotheses about student notional-machine misconceptions from source code. The artifact is designed for reviewer and researcher inspection. It is not a classroom deployment system, grading tool, or student-facing diagnostic service.

## Research Purpose

The paper argues for an instructor-facing framing of LLM support in CS1. Rather than asking only whether a model can identify or repair a bug, TRACER asks whether a model can generate evidence-grounded hypotheses about the mental model that may have produced a student submission.

The central distinction is:

- Bug detection asks what is wrong with the program.
- Belief attribution asks what notional-machine belief may explain the program.
- Diagnostic humility requires treating such outputs as hypotheses, with abstention and specificity prioritized over broad coverage.

## Artifact Contents

| Path | Description |
| --- | --- |
| `authentic_seeded/` | Synthetic Java submissions and manifests for A1-A3. |
| `detections/` | Frozen raw LLM detection outputs used by the paper analysis. |
| `runs/run_final_main/` | Final label-exclusive publication analysis artifacts. |
| `runs/run_final_ablation/` | Final label-inclusive ablation artifacts. |
| `figures/` | Paper-facing figure exports. |
| `data/` | Assignment prompts, rubrics, tests, and notional-machine ground truth. |
| `analyze.py` | Publication analysis, semantic matching, threshold calibration, and 5-fold cross-validation. |
| `miscons.py` | LLM detection runner for regenerating model outputs. |
| `docs/` | Methodology, matching, metrics, prompts, architecture, and development notes. |

## Headline Results

The checked-in final runs reproduce the metrics reported in the paper.

Main condition: label-exclusive matching

| Metric | Value |
| --- | ---: |
| Precision | 0.577 |
| Recall | 0.872 |
| Specificity | 0.848 |

Ablation: label-inclusive matching

| Metric | Value |
| --- | ---: |
| Precision | 0.511 |
| Recall | 0.982 |
| Specificity | 0.774 |

The label-inclusive ablation increases recall while reducing specificity, illustrating how evaluation shortcuts can inflate apparent capability while worsening the safety-relevant false-positive profile.

## Dataset and Evaluation Scope

- 1,200 synthetic CS1 Java submissions.
- 300 synthetic students across three assignments.
- Four submissions per synthetic student.
- One misconception-seeded submission and three behaviorally correct submissions per synthetic student.
- 18 notional-machine misconception categories.
- Four prompting strategies.
- Six model configurations across GPT, Claude, and Gemini families.
- 5-fold stratified cross-validation with threshold calibration on development folds and evaluation on held-out folds.

The dataset is synthetic by design. This enables controlled ground-truth evaluation of injected misconceptions, but it does not establish ecological validity for authentic classroom submissions.

## Quick Start

Install dependencies:

```bash
uv sync
```

Inspect final results without API keys:

```bash
cat runs/run_final_main/metrics.json
cat runs/run_final_ablation/metrics.json
```

Rerun the main publication analysis from the frozen detection outputs:

```bash
export OPENAI_API_KEY="sk-..."

uv run python analyze.py analyze-publication \
  --run-name reviewer_main \
  --include-label-text false
```

Rerun the label-inclusive ablation:

```bash
uv run python analyze.py analyze-publication \
  --run-name reviewer_ablation \
  --include-label-text true
```

New analysis outputs are written to `runs/v2/`.

## Regenerating Raw Detections

The repository includes the frozen detection outputs used for the paper. Regenerating them is optional and more expensive because it calls external model providers.

To regenerate detections, configure provider keys:

```bash
export OPENAI_API_KEY="sk-..."
export ANTHROPIC_API_KEY="sk-ant-..."
export GOOGLE_API_KEY="..."
```

Then run:

```bash
uv run python miscons.py all-strategies --assignment a1
uv run python miscons.py all-strategies --assignment a2
uv run python miscons.py all-strategies --assignment a3
```

Model names and provider availability may change over time. For verifying the submitted paper results, the checked-in `detections/` directory is the authoritative frozen raw-output layer.

## Documentation Map

- `ARTIFACT.md` - concise artifact guide and rerun levels.
- `REPRODUCIBILITY.md` - step-by-step reproduction instructions.
- `DATA_PROVENANCE.md` - provenance of the synthetic submissions and detection outputs.
- `docs/methodology.md` - cross-validation and threshold calibration.
- `docs/matching.md` - semantic matching and label-exclusive versus label-inclusive comparison.
- `docs/metrics-guide.md` - precision, recall, specificity, and false-positive interpretation.
- `docs/notional-machines.md` - misconception taxonomy.
- `docs/context.md` - paper framing and reporting guidance.

## Claim Boundaries

This artifact supports inspection of a controlled benchmark for instructor-facing belief attribution. It does not claim to recover students' true beliefs, support grading, validate student-facing authoritative diagnosis, or demonstrate classroom deployment readiness.

## Citation

If you use this artifact, please cite the paper and this repository. A machine-readable citation file is provided in `CITATION.cff`.

```bibtex
@software{shah2026tracer,
  author = {Shah, Shlok},
  title = {Belief Attribution TRACER Artifact},
  year = {2026},
  url = {https://github.com/shahshlok/belief-attribution-tracer}
}
```

