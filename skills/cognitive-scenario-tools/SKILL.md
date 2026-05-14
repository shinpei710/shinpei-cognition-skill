---
name: cognitive-scenario-tools
description: Use when a specific human, social, relationship, negotiation, collaboration, resource, growth, or communication scenario needs specialized models after general analysis
---

# Cognitive Scenario Tools

## Overview

This is the scenario-specific layer. Use it only after the main problem has been defined and the general analysis layer has identified the domain.

Do not use these tools as universal explanations. They are situational lenses.

## Structured Resources

Load only what the task needs:

- `description.md`: human-readable intent, scope, non-goals, and usage notes.
- `schema.json`: input and output contract for scenario analysis.
- `workflow.yaml`: routing and scenario analysis workflow.
- `trigger_rules.json`: activation, routing, caution, and over-inference rules.
- `model_cards.json`: machine-readable scenario model catalog.
- `examples.json`: example scenario invocations and expected output behavior.
- `eval_cases.json`: regression cases for scenario reasoning.
- `failure_cases.json`: known failure modes and recovery behavior.
- `version.json`: behavior version and change history.

## Scenario Routing

| Scenario | Use these models |
|---|---|
| Relationship and communication | signal theory, information asymmetry, double bind, framing effect, control dichotomy |
| Negotiation and cooperation | prisoner's dilemma, zero-sum/non-zero-sum, signal theory, opportunity cost, safety margin |
| Shared resources and organizations | tragedy of the commons, rent dissipation, bottleneck, feedback loop, path dependence |
| Competition and strategy | asymmetric warfare, ability circle, safety margin, black swan, antifragility |
| Personal growth | comfort zone, influence circle, compound effect, capability emergence, hyperbolic discounting |
| Public expression and persuasion | framing effect, signal theory, map-territory, appeal to authority, confirmation bias |

## Scenario Model Cards

### 25. Tragedy of the Commons
Use when individual rational choices damage a shared resource. Look for missing ownership, missing cost feedback, or weak governance.

### 28. Rent Dissipation
Use when people compete away the value of a resource. Check whether the contest costs more than the prize is worth.

### 34. Prisoner's Dilemma
Use when mutual cooperation would be better but incentives push each side toward betrayal or defensiveness.

### 35. Information Asymmetry
Use when one side knows more than the other. Identify hidden information, screening mechanisms, and verification signals.

### 36. Signal Theory
Use when words are cheap but actions reveal intent. Look for costly signals, consistent behavior, and incentives behind communication.

### 37. Zero-Sum and Non-Zero-Sum Games
Use when deciding whether the situation is competition for a fixed pie or cooperation to expand the pie.

### 45. Asymmetric Warfare
Use when facing a stronger opponent or constraint. Do not compete head-on; use unique advantages against the other side's weak point.

### 48. Double Bind
Use when every available response seems wrong. Identify contradictory demands and move the conversation to meta-level clarification.

### 49. Control Dichotomy
Use when anxiety comes from trying to control the uncontrollable. Separate controllable actions from uncontrollable outcomes.

### 50. Influence Circle
Use when attention is wasted on issues outside practical influence. Move energy from concern to influence to direct control.

## Relationship Analysis Pattern

1. Separate facts, interpretations, emotions, and desired actions.
2. Identify current relationship stage and mutual investment level.
3. Check signal quality: words, repeated actions, cost, consistency.
4. Check asymmetry: what does each side know, need, fear, or hide?
5. Identify whether the issue is attraction, trust, rhythm, boundary, reality pressure, or commitment.
6. Choose a small verifiable action instead of acting on imagined certainty.

## Negotiation Pattern

1. Define each side's visible position and likely underlying interest.
2. Identify information asymmetry and incentives.
3. Determine whether the game can become non-zero-sum.
4. Use costly signals and small commitments to test trust.
5. Keep a safety margin and walk-away option.

## Personal Growth Pattern

1. Pick the current bottleneck.
2. Decide whether the user is in comfort zone, learning zone, or overload zone.
3. Create a small repeatable action with compounding payoff.
4. Add a feedback loop and review cadence.
5. Preserve what works as a rule, template, or habit.

## Common Mistakes

- Treating game theory as proof that others are hostile.
- Confusing a signal with a guarantee.
- Using double-bind language to avoid making a difficult choice.
- Trying to control outcomes instead of controllable actions.
- Turning scenario models into excuses for over-inference.

## Output Standard

For any scenario analysis, output:

- facts observed
- model used and why
- strongest interpretation
- plausible alternatives
- risk of over-inference
- next verifiable action
