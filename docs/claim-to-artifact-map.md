# Claim-to-Artifact Map

Use this table to jump from interpretation claims to reproducible artifacts.

| Claim | Evidence artifacts | Verification steps |
| --- | --- | --- |
| TRACER supports instructor-facing belief attribution claims in a controlled benchmark | `data/ground truth and manifests`, `runs/run_final_main/`, `docs/methodology.md` | Confirm synthetic construction in `data/`, then check final metrics and run summaries in `runs/run_final_main/`. |
| Main result is precision/recall/specificity tradeoff with label-exclusive matching | `runs/run_final_main/metrics.json`, `runs/run_final_main/report.md`, `runs/run_final_main/fold_results.csv` | Read metric table, then confirm fold-level behavior in fold results. |
| Ablation with label-inclusive matching increases recall and lowers specificity | `runs/run_final_ablation/metrics.json`, `docs/metrics-guide.md`, `ARTIFACT.md` | Compare main vs ablation metrics and read matching rationale in methodology docs. |
| Cross-validation prevents overfitting threshold settings | `docs/methodology.md`, `runs/*/fold_results.csv` | Check fold-by-fold split and threshold calibration text; confirm fold summaries exist for each fold. |
| Semantic matching controls terminology mismatch | `docs/matching.md`, `runs/run_final_main/report.md` | Inspect matching description and check matching output summaries in final run artifacts. |
| False positives are a key boundary and should constrain interpretation | `docs/metrics-guide.md`, `runs/run_final_main/metrics.json`, `runs/run_final_main/report.md` | Verify specificity and clean-case behavior in metric tables. |
| Synthetic data is synthetic and not classroom-grade beliefs | `DATA_PROVENANCE.md`, `ARTIFACT.md`, `README.md` | Read provenance and claim boundaries before writing any deployment conclusion. |
| Reproducible artifact-level rerun is possible without regenerating raw detections | `REPRODUCIBILITY.md`, `detections/` + `runs/*` | Re-run analysis commands in `REPRODUCIBILITY.md` and compare output paths. |
