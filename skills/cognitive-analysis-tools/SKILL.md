---
name: cognitive-analysis-tools
description: Use when a task requires deeper analysis, model selection, tradeoff comparison, uncertainty handling, risk evaluation, bias checking, system diagnosis, or structured retrospective
---

# Cognitive Analysis Tools

## Overview

This is the general-purpose model toolbox. Use it only after `cognitive-operating-system` has defined the problem and identified the need for deeper reasoning.

Do not use every model. Select the smallest set that clarifies the task.

## Selection Protocol

1. Identify the task type: cognition, decision, system, uncertainty, feedback, growth.
2. Pick 1-3 models that directly attack the key contradiction.
3. State why each model is being used.
4. Apply the model to facts, not vibes.
5. Convert insight into a decision, test, or next action.

## General Tool Categories

| Category | Use when | Typical models |
|---|---|---|
| Cognitive calibration | beliefs, assumptions, bias, weak evidence | Occam, confirmation bias, falsifiability, Dunning-Kruger, map-territory |
| Decision optimization | options, tradeoffs, prioritization, cost | first principles, inversion, second-order thinking, opportunity cost, decision matrix, safety margin |
| System diagnosis | dependencies, bottlenecks, feedback, stages | systems thinking, feedback loop, bottleneck, emergence, path dependence, entropy |
| Uncertainty handling | probabilities, new evidence, rare shocks | probability thinking, Bayes, survivorship bias, black swan, antifragility, ergodicity |
| Feedback and iteration | review, correction, compounding | compound effect, regression to mean, redundancy, capability emergence |

## Model Cards

### 1. Ability Circle
Use when deciding where to act. Stay inside known competence for high-stakes decisions; expand the boundary through low-risk experiments.

### 2. Occam's Razor
Use when multiple explanations fit the facts. Prefer the explanation with fewer extra assumptions until evidence requires complexity.

### 3. First Principles
Use when inherited assumptions block progress. Break the problem down to non-negotiable facts and rebuild from there.

### 4. Dunning-Kruger Effect
Use when confidence is high but evidence or skill is thin. Treat early certainty as a risk signal.

### 5. Hanlon's Razor
Use when tempted to attribute harm to malice. Check incompetence, confusion, incentives, or context first.

### 6. Confirmation Bias
Use when the user or agent is collecting evidence that only supports a preferred conclusion. Actively search for disconfirming facts.

### 7. Falsifiability
Use when a claim cannot be tested. Convert it into observable predictions or mark it as speculation.

### 8. Straw Man Fallacy
Use when arguing against an easier version of another view. Reconstruct the strongest version before critique.

### 9. Slippery Slope Fallacy
Use when a small event is expanded into catastrophic inevitability. Identify required intermediate steps and their probabilities.

### 10. Appeal to Authority
Use when authority is replacing evidence. Treat authority as a clue, not proof.

### 11. Inversion
Use when success criteria are vague. Ask what would guarantee failure, then prevent those failure paths.

### 12. Second-Order Thinking
Use when the first consequence is obvious but later effects matter. Ask what happens after the immediate result.

### 13. Pareto Principle
Use when effort is scattered. Find the small set of causes or actions likely to drive most impact.

### 14. Opportunity Cost
Use when choosing one path hides what is being sacrificed. Compare against the best alternative use of time, money, attention, or trust.

### 15. Decision Matrix
Use when options involve multiple criteria. Score each option by weighted criteria, then inspect whether the result matches reality.

### 16. Sunk Cost Fallacy
Use when past investment is pressuring continued action. Decide based on future value, not unrecoverable cost.

### 17. Comfort Zone
Use when growth requires discomfort. Separate productive stretch from destructive overload.

### 18. Safety Margin
Use when failure cost is high. Add buffers for time, money, capacity, quality, and reversibility.

### 19. Hyperbolic Discounting
Use when short-term rewards override long-term interests. Add friction to impulsive choices and rewards to delayed benefits.

### 20. Framing Effect
Use when wording changes judgment. Reframe the same facts in gain, loss, cost, risk, and opportunity language.

### 21. Systems Thinking
Use when outcomes arise from interactions rather than one cause. Map elements, relationships, flows, incentives, and feedback.

### 22. Feedback Loop
Use when behavior reinforces or corrects itself. Identify reinforcing loops and balancing loops.

### 23. Critical Mass
Use when progress is slow until a threshold is reached. Ask what accumulation or condition triggers phase change.

### 24. Bottleneck Theory
Use when the whole system is constrained by one weak link. Improve the bottleneck before optimizing elsewhere.

### 26. Emergence
Use when the whole behaves differently from the parts. Look for new properties created by interaction.

### 27. Path Dependence
Use when early choices constrain later options. Identify lock-in, switching costs, and path-reset opportunities.

### 29. Entropy
Use when systems decay without maintenance. Add routines, constraints, and energy input to preserve order.

### 30. Reductionism and Holism
Use when analysis is either too fragmented or too vague. Zoom between parts and whole until both explain the result.

### 31. Probability Thinking
Use when tempted to think in yes/no terms. Estimate likelihoods, confidence, and what evidence would change the estimate.

### 32. Bayesian Updating
Use when new information arrives. Update belief strength instead of flipping from certainty to certainty.

### 33. Survivorship Bias
Use when learning only from visible winners. Ask what failed cases are missing from the sample.

### 38. Black Swan
Use when rare, high-impact events matter. Reduce fragility instead of pretending to predict everything.

### 39. Antifragility
Use when volatility can be used for growth. Design small losses, optionality, and learning loops.

### 40. Ergodicity
Use when average outcomes hide individual ruin. Avoid strategies that look good in aggregate but can wipe out the actor.

### 41. Map Is Not Territory
Use when a model feels too elegant. Remember the model is a simplification; reality can violate it.

### 42. Regression to Mean
Use when extreme performance is over-interpreted. Expect some natural return toward baseline.

### 43. Asimov's Technology Law
Use when evaluating technology trends. Avoid overestimating short-term change and underestimating long-term change.

### 44. Redundancy Backup
Use when failure is costly. Build backup paths, reserves, and fallback plans.

### 46. Capability Emergence
Use when combined skills may create a new ability. Look for non-linear effects from skill stacking.

### 47. Compound Effect
Use when small repeated actions matter. Favor routines with accumulation and compounding payoff.

## Common Mistakes

- Loading too many models and losing the main thread.
- Using models as decoration instead of decision support.
- Treating a model as proof.
- Ignoring stage, weight, and context differences.
- Forgetting that the goal is action and verification.

## Handoff to Scenario Tools

If the key issue is relationship, communication, coordination, incentives, public expression, or personal growth, use `cognitive-scenario-tools` after selecting the relevant general models.
