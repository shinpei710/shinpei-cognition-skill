---
name: cognitive-analysis-tools
description: Use after the core problem is defined when deeper model selection, tradeoff comparison, uncertainty handling, risk evaluation, bias checking, system diagnosis, product stage-gate evaluation, or structured retrospective is needed. Avoid for simple direct execution.
---

# Cognitive Analysis Tools

## Overview

Use this general-purpose reasoning toolbox only after `cognitive-operating-system` has defined the problem and identified the need for deeper analysis.

Do not use every model. Select the smallest set that changes the next action.

## Structured Resources

Load only what the task needs:

- `description.md`: human-readable intent, scope, non-goals, and usage notes.
- `schema.json`: input and output contract for model-based analysis.
- `workflow.yaml`: model selection and application workflow.
- `trigger_rules.json`: activation, model-selection, and caution rules.
- `model_cards.json`: machine-readable model catalog and aliases.
- `system_completeness.json`: product or workflow stage-gate standards for MVP, self-use, friend alpha, initial release, and broader rollout.
- `examples.json`: example invocations and expected output behavior.
- `eval_cases.json`: regression cases for model selection and analysis quality.
- `failure_cases.json`: known failure modes and recovery behavior.
- `version.json`: behavior version and change history.

## Selection Protocol

1. Identify the task type: cognition, decision, system, uncertainty, feedback, growth, product readiness, or mixed.
2. Pick one to three models that directly attack the key contradiction.
3. State why each model is being used.
4. Apply the model to facts, not vibes.
5. Convert insight into a decision, test, next action, or stage-gate judgment.

## General Tool Categories

| Category | Use when | Typical models |
|---|---|---|
| Cognitive calibration | beliefs, assumptions, bias, weak evidence | Occam, confirmation bias, falsifiability, Dunning-Kruger, map-territory |
| Decision optimization | options, tradeoffs, prioritization, cost | first principles, inversion, second-order thinking, opportunity cost, decision matrix, safety margin |
| System diagnosis | dependencies, bottlenecks, feedback, stages | systems thinking, feedback loop, bottleneck, emergence, path dependence, entropy |
| Product readiness | MVP, self-use, alpha, release, rollout, system completeness | systems thinking, bottleneck, feedback loop, safety margin, opportunity cost |
| Uncertainty handling | probabilities, new evidence, rare shocks | probability thinking, Bayes, survivorship bias, black swan, antifragility, ergodicity |
| Feedback and iteration | review, correction, compounding | compound effect, regression to mean, redundancy, capability emergence |

## System Completeness Protocol

Use `system_completeness.json` when the task asks how complete a product, workflow, or agentic system must be before the next stage.

1. Name the current stage and the next target stage.
2. Score the system dimensions from 0 to 3 using evidence.
3. Treat safety, privacy, cost, and a broken core value loop as blockers regardless of total score.
4. Identify the smallest system increment that unlocks the next stage.
5. Define exit evidence for the next version.
6. Move non-stage requirements into a deferred backlog.

For product work, evaluate the system as a value loop: target user, input, process, output, feedback, recovery, maintenance, and distribution.

## Common Mistakes

- Loading too many models and losing the main thread.
- Using models as decoration instead of decision support.
- Treating a model as proof.
- Ignoring stage, weight, and context differences.
- Treating feature count as system completeness.
- Trying to perfect a later-stage requirement before the current-stage value loop works.
- Forgetting that the goal is action and verification.

## Handoff to Scenario Tools

If the key issue is relationship, communication, coordination, incentives, public expression, or personal growth, use `cognitive-scenario-tools` after selecting the relevant general models.
