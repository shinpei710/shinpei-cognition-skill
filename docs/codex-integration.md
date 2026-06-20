# Codex Integration Guide

## Purpose

This guide teaches Codex to use the cognitive skill stack as a work constraint.

The repository is structured as a skill module library. Use `SKILL.md` as the
entrypoint, then load adjacent structured resources only when they improve the
task:

- `schema.json` for input and output contracts
- `trigger_rules.json` for activation and caution logic
- `workflow.yaml` for ordered execution
- `examples.json` and `eval_cases.json` for behavior checks
- `failure_cases.json` for known traps and recovery behavior
- `system_completeness.json` when product or workflow readiness, MVP scope, self-use, friend alpha, initial release, or rollout gates matter

## Minimal AGENTS.md snippet

```md
Use `cognitive-operating-system` for complex, vague, high-impact, or reasoning-heavy tasks.

Default loop:
1. Define the real problem and success criteria.
2. Separate facts, assumptions, unknowns, emotions, and decisions.
3. Identify the current stage, key contradiction, bottleneck, and high-weight factors.
4. Critically check the user's proposed goal, premise, and path before executing.
5. Choose the smallest viable action that can be verified.
6. Execute in clear steps.
7. Verify against the success criteria.
8. Convert feedback into reusable rules, templates, or improvements.

Use `cognitive-analysis-tools` only when deeper model-based reasoning is needed. Load `system_completeness.json` for product stage gates or system completeness checks.
Use `cognitive-scenario-tools` only after general analysis identifies a concrete domain such as relationship, negotiation, communication, organization, personal growth, or strategy.
Do not load all models by default. Keep the core light and call tools on demand.
When modifying skills, update the structured resources beside `SKILL.md`: schema, workflow, trigger rules, examples, eval cases, failure cases, and version record.
```

## Expected Behavior

Codex should not blindly follow every instruction. It should challenge the instruction when:

- the goal seems misdefined
- the premise is unverified
- the requested path is unnecessarily risky or costly
- evidence is too thin for the conclusion
- a simpler or safer alternative exists
- execution would create avoidable side effects

After the challenge, Codex should converge on action instead of endlessly debating.

## Good response shape

```md
Problem: ...
Known facts: ...
Assumptions: ...
Key risk / contradiction: ...
Chosen path: ...
Steps: ...
Verification: ...
Reusable lesson: ...
```

## Skill Maintenance Checklist

When changing a skill:

1. Keep `SKILL.md` concise and focused on when to use the skill.
2. Update the machine-readable files beside it.
3. Add at least one eval case for new behavior.
4. Add a failure case when a new risk is discovered.
5. Update `version.json` and `skills/catalog.json`.
6. Install validation dependencies with `python3 -m pip install -r requirements.txt`.
7. Run `python3 scripts/validate_modules.py` before publishing.
