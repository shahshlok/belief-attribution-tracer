# Paper Writing Context Brief

> Use this with `abstract.md` and run reports when refining the paper.

---

## Target Venue

**ITiCSE 2026** (Innovation and Technology in Computer Science Education)
- ACM SIGCSE venue, 6-10 pages (two-column ACM format)
- Audience: CS educators, learning scientists, educational technology researchers
- Review focus: novelty, rigor, and classroom relevance

---

## Current Paper Title

**"Notional Machines, Not Just Errors: Toward Belief Attribution with Instructor-Facing LLMs"**

---

## Core Claim

LLMs in CS1 should not be framed only as automated bug fixers. A distinct and valuable use is **instructor-facing belief attribution**: generating plausible hypotheses about student notional machines, grounded in code evidence, with explicit uncertainty and abstention.

---

## Key Results to Report (5-Fold CV)

### Main Condition: Label-Exclusive Matching

| Metric | Value |
| --- | --- |
| Precision | 0.577 |
| Recall | 0.872 |
| Specificity | 0.848 |

### Ablation: Label-Inclusive Matching

| Metric | Value |
| --- | --- |
| Precision | 0.511 |
| Recall | 0.982 |
| Specificity | 0.774 |

Interpretation: exposing misconception labels inflates recall but harms safety by increasing over-diagnosis.

---

## Dataset and Evaluation Scope

- 1,200 synthetic CS1 Java submissions
- 300 synthetic students, 4 submissions each
- Per student: 1 misconception-seeded + 3 behaviorally correct programs
- 18 notional machines
- Model families: GPT-5.2, Claude 4.5 Haiku, Gemini 3 Flash
- Variants: non-reasoning and reasoning (6 total model configurations)

TRACER is used as a **controlled capability probe**, not a claim of classroom-ready autonomous diagnosis.

---

## Framing Terms

- **Notional machine:** course-level explanatory execution model
- **Mental model:** student's internal approximation
- **Misconception:** coherent but incorrect operational rule
- **Diagnostic humility:** prioritize specificity, uncertainty, and abstention over blanket coverage

---

## Structural vs Semantic Misconceptions

- **Structural:** visible signature in code (e.g., Human Indexing, Void Machine)
- **Semantic:** inferred intent mismatch with execution model (e.g., Spreadsheet View, Independent Switch, Dangling Else)

Use this distinction when discussing blind spots and reliability limits.

---

## Safety-First Reporting Expectations

When documenting outcomes, always include:

1. False positives on clean submissions
2. Specificity (true negative rate)
3. Misconception-family blind spots (structural vs semantic)
4. Any abstention mechanism and its trade-offs

Do not report accuracy/F1 alone as sufficient evidence.

---

## Abstention Mechanisms Used in Practice

- Semantic score filtering (low-score hypotheses treated as noise)
- Secondary confidence/noise floor for borderline cases
- Ensemble agreement (e.g., 2 of 6 models) before surfacing a diagnosis

In TRACER reporting, ensemble agreement reduced false positives substantially while keeping true positives largely intact.

---

## Scope Boundaries (Must State Explicitly)

- No claim to recover a student's true beliefs
- No student-facing authoritative diagnosis
- No grading use
- No ecological-validity claim from synthetic data alone

Position the system as instructor decision support for hypothesis generation.

---

## Writing Guidance

- Lead with the risk asymmetry argument: false positive diagnosis is more harmful than abstaining
- Emphasize over-diagnosis on correct code as the dominant error mode
- Treat "no diagnosis" as responsible behavior, not model failure
- Keep causal claims conservative; report measured behavior, not unverified mechanisms

---

## Previous: [Development](development.md) | Back to [README](../README.md)
