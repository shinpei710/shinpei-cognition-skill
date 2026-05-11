# Codex Integration Guide

## Purpose

This guide teaches Codex to use the cognitive skill stack as a work constraint.

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

Use `cognitive-analysis-tools` only when deeper model-based reasoning is needed.
Use `cognitive-scenario-tools` only after general analysis identifies a concrete domain such as relationship, negotiation, communication, organization, personal growth, or strategy.
Do not load all models by default. Keep the core light and call tools on demand.
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
