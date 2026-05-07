# Metrics Guide

This document explains the evaluation metrics used for TRACER's belief-attribution setting.

---

## Why Metrics Differ Here

Belief attribution is risk-asymmetric:
- A **false positive** (diagnosing a misconception that is not present) can mislead instruction.
- A **false negative** is often less harmful than a confident wrong diagnosis.

So we report **specificity** and clean-code false positives as first-class metrics, not only recall.

---

## Core Metrics

### Precision

```
Precision = TP / (TP + FP)
```

How trustworthy positive diagnoses are.

### Recall

```
Recall = TP / (TP + FN)
```

How often real misconception signals are detected.

### Specificity

```
Specificity = TN / (TN + FP)
```

How often clean/negative cases are correctly left undiagnosed.

---

## Primary Reported Results (5-Fold CV)

| Condition | Precision | Recall | Specificity |
| --- | ---: | ---: | ---: |
| Label-exclusive matching (main) | 0.577 | 0.872 | 0.848 |
| Label-inclusive matching (ablation) | 0.511 | 0.982 | 0.774 |

Interpretation:
- Label-inclusive matching boosts recall but increases over-diagnosis (specificity drop).
- Main run better reflects diagnostic humility goals.

---

## Error Profile to Track

- Most false positives arise on **behaviorally correct submissions** (invented bug diagnoses).
- This pattern is more important for classroom safety than aggregate recall gains.

When reporting, include:
1. FP on clean programs
2. Specificity
3. Structural vs semantic subgroup performance

---

## Structural vs Semantic Breakdown

- **Structural misconceptions** are usually easier (visible code signatures).
- **Semantic misconceptions** are harder (intent-level inference required).

Always separate these in analysis to avoid masking observability gaps.

---

## Abstention and Filtering

TRACER supports conservative filtering via:
- semantic similarity thresholds
- noise-floor handling for borderline matches
- optional ensemble agreement before surfacing diagnoses

Abstention should be interpreted as a safe output mode.

---

## Practical Rule of Thumb

For instructor-facing deployment discussions:
- optimize for **specificity-first** behavior
- treat broad-recall settings as exploratory
- require human verification before intervention

---

## Previous: [Analysis Pipeline](analysis-pipeline.md) | Next: [Matching](matching.md)
