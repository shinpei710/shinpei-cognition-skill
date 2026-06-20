# Cognitive Skill Module Spec

## Purpose

This repository treats a skill as a versionable cognitive module, not as a
long prompt. The module should be usable by both people and agents:

- humans read the intent, scope, and examples
- agents inspect schemas, trigger rules, workflow steps, and eval cases
- maintainers can diff and version behavior over time

## Required Files

Each skill directory should include:

| File | Purpose |
|---|---|
| `SKILL.md` | Lightweight Codex entrypoint and resource map |
| `description.md` | Human-readable purpose, scope, non-goals, and usage notes |
| `schema.json` | Machine-readable input, output, and evidence contract |
| `workflow.yaml` | Ordered execution flow with checkpoints and artifacts |
| `trigger_rules.json` | Conditions for use, escalation, and refusal or caution |
| `examples.json` | Positive examples of inputs and expected outputs |
| `eval_cases.json` | Test cases for behavior and regression checks |
| `failure_cases.json` | Known failure modes and recovery rules |
| `version.json` | Version, release date, status, and change history |

Optional files are allowed when they reduce ambiguity, for example
`model_cards.json`, `system_completeness.json`, `tone_rules.json`, or `templates/`.

## Design Principles

1. Keep `SKILL.md` small. It should tell Codex when to use the skill and
   which resource to load next.
2. Prefer structured resources over long prose when behavior must be
   validated or reused.
3. Put judgment logic in `trigger_rules.json`; put process in
   `workflow.yaml`; put examples and tests in their own files.
4. Every workflow step should have an observable output or checkpoint.
5. Every eval case should name the expected behavior and the failure it guards
   against.
6. Preserve failure cases. A skill becomes stronger when it remembers where it
   can go wrong.
7. Use version records for behavior changes, not only file changes.

## Minimal Compatibility Contract

A consumer should be able to:

1. Read `SKILL.md` to decide whether the skill applies.
2. Read `schema.json` to understand the required task facts and response
   contract.
3. Read `trigger_rules.json` to determine activation, escalation, and caution.
4. Read `workflow.yaml` to execute the skill.
5. Run `eval_cases.json` manually or in a test harness to check regressions.

## Evaluation Standard

A module is publishable when:

- JSON resources parse successfully.
- YAML workflows parse successfully or pass a basic syntax check.
- `SKILL.md` references the important structured resources.
- At least two eval cases exist: one normal case and one edge or failure case.
- Failure cases include a recovery behavior, not just a warning.
