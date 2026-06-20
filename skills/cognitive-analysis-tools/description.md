# Cognitive Analysis Tools

## Purpose

Use this module when the core operating skill has already defined the problem
and the next bottleneck requires deeper reasoning. It provides a compact
toolbox for model selection, tradeoff comparison, uncertainty handling, risk
evaluation, bias checking, system diagnosis, and structured retrospective.

## Applicable Scenarios

- multiple plausible explanations compete
- options must be compared across criteria
- incentives, constraints, feedback loops, or bottlenecks shape the outcome
- uncertainty or downside risk matters
- a belief needs bias checking or falsification
- a project or decision needs a postmortem
- a product, workflow, or agentic system needs a stage-gate readiness check
- MVP, self-use, friend alpha, initial release, or rollout standards are unclear

## Non-Goals

- Do not load this module before the core problem is defined.
- Do not apply every model.
- Do not use model names as decoration.
- Do not let an elegant model override observed facts.

## Usage Notes

Pick one to three models that directly attack the key contradiction. State why
each model is being used, apply it to known facts, and convert the result into a
decision, test, or next action.

## System Completeness Note

For product or workflow work, load `system_completeness.json` when the question is about MVP scope, self-use readiness, friend alpha, initial release, broader rollout, or whether the system is complete enough for the next stage.
