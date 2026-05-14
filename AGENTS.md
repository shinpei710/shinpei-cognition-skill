# Agent Instructions

## Repository Goal

This repository is a versionable cognitive skill module library for agents.
Do not treat it as a prompt dump.

## Change Rules

- Keep `SKILL.md` concise. It is the Codex entrypoint and resource map.
- Put machine-readable behavior in adjacent structured files:
  `schema.json`, `workflow.yaml`, `trigger_rules.json`, `examples.json`,
  `eval_cases.json`, `failure_cases.json`, and `version.json`.
- If a skill relies on a catalog of reusable concepts, add a focused resource
  such as `model_cards.json` and reference it from `SKILL.md`.
- Update `skills/catalog.json` when adding, removing, renaming, or materially
  changing modules.
- Add eval cases for new behavior and failure cases for newly discovered traps.
- Validate JSON and YAML before publishing.

## Style

- Prefer short, operational instructions over long motivational prose.
- Separate facts, assumptions, judgment rules, workflow steps, and examples.
- Preserve progressive disclosure: load deeper resources only when needed.
