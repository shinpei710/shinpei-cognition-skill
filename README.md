# Cognitive Agent Skills

A versionable cognitive skill module library for agents.

一套面向 Agent 的可版本管理认知技能模块库。目标不是收藏长
prompt，而是把认知方法论拆成可阅读、可执行、可评测、可迭代的
模块。

This repository is not a prompt collection. Each skill is designed as a
small, inspectable module with both human-readable guidance and
machine-readable structure:

- applicable scenarios
- input and output schemas
- trigger and judgment rules
- execution workflow
- examples
- failure cases
- evaluation cases
- version records

`SKILL.md` remains the lightweight Codex entrypoint. The deeper module
assets live beside it and should be loaded only when the task needs them.

## Module Layout

Each skill should follow this shape:

```text
skills/<skill-name>/
  SKILL.md
  description.md
  schema.json
  workflow.yaml
  trigger_rules.json
  examples.json
  eval_cases.json
  failure_cases.json
  version.json
```

Specialized skills may add focused resources, such as `model_cards.json`,
as long as `SKILL.md` points to when they should be read.

See `docs/module-spec.md` for the repository standard and
`skills/catalog.json` for the current module index.

## Layer 1: Core Operating Skill

- `cognitive-operating-system`
  - Defines the default operating loop: define, calibrate, frame, choose,
    execute, verify, reflect, preserve.
  - Use it first for complex, vague, high-impact, emotionally loaded, or
    reasoning-heavy tasks.
  - Keep it light. Do not load all model tools by default.

## Layer 2: General Analysis Tools

- `cognitive-analysis-tools`
  - Provides cross-domain models for cognition, decision-making, systems,
    uncertainty, risk, and feedback.
  - Load it only when the core operating skill identifies a need for deeper
    model-based reasoning.

## Layer 3: Scenario Tools

- `cognitive-scenario-tools`
  - Provides concrete scenario lenses for relationship, communication,
    negotiation, collaboration, resources, personal growth, and public
    expression.
  - Load it only after the general analysis layer identifies a scenario
    where specialized models improve action.

## Recommended Codex Usage

把下面这段放进项目的 `AGENTS.md` 或 Codex 的项目说明里：

```md
Use the `cognitive-operating-system` skill as the default working constraint for complex tasks.
Do not jump directly into execution. First define the real problem, success criteria, known facts, unknowns, constraints, and risks.
Use `cognitive-analysis-tools` only when the task requires deeper reasoning, model selection, tradeoff analysis, risk evaluation, or retrospection.
Use `cognitive-scenario-tools` only when a concrete scenario requires specialized models such as relationship analysis, communication, game theory, resource coordination, or personal growth.
Keep the main skill lightweight. Load deeper tools only when needed.
```

## Development Rule

When adding or changing a skill, update the structured resources together:

1. Keep `SKILL.md` concise and action-oriented.
2. Put schemas, trigger logic, workflows, examples, failures, and evaluations
   in separate files.
3. Add or update `skills/catalog.json`.
4. Validate JSON, YAML, catalog entries, and `SKILL.md` resource references:

```bash
python3 -m pip install -r requirements.txt
python3 scripts/validate_modules.py
```

## Source note

The 50 mental model names are organized from a public directory page of 《格物之道》 by 诺亚书房. This repository does not reproduce the original book text; it only uses the model names as an index and provides original, agent-oriented summaries and invocation rules.

Source page: https://www.nuoyashufang.com/4071.html
