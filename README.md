# Cognitive Agent Skills

一套面向 Agent 的认知与做事方法论 skill 仓库。

目标不是让 Agent 变成“更听话的执行器”，而是让 Agent 在处理任务时具备更稳定的判断、拆解、质疑、执行、验证和迭代能力。

## Layer 1: 主控核心 skill

- `cognitive-operating-system`
  - 只包含核心原则、工作闭环、批判性校验、脑补干预规则和按需调用规则。
  - 使用时先加载它，不要一开始就加载所有模型。

## Layer 2: 通用分析工具层

- `cognitive-analysis-tools`
  - 提供跨场景高频使用的认知、决策、系统、概率与反馈模型。
  - 只有在任务需要深入分析、方案比较、风险判断、复盘校正时才调用。

## Layer 3: 场景专题工具层

- `cognitive-scenario-tools`
  - 在通用工具层之下按需调用。
  - 用于关系沟通、博弈协作、资源分配、个人成长、传播表达等具体场景。

## Recommended Codex usage

把下面这段放进项目的 `AGENTS.md` 或 Codex 的项目说明里：

```md
Use the `cognitive-operating-system` skill as the default working constraint for complex tasks.
Do not jump directly into execution. First define the real problem, success criteria, known facts, unknowns, constraints, and risks.
Use `cognitive-analysis-tools` only when the task requires deeper reasoning, model selection, tradeoff analysis, risk evaluation, or retrospection.
Use `cognitive-scenario-tools` only when a concrete scenario requires specialized models such as relationship analysis, communication, game theory, resource coordination, or personal growth.
Keep the main skill lightweight. Load deeper tools only when needed.
```

## Source note

The 50 mental model names are organized from a public directory page of 《格物之道》 by 诺亚书房. This repository does not reproduce the original book text; it only uses the model names as an index and provides original, agent-oriented summaries and invocation rules.

Source page: https://www.nuoyashufang.com/4071.html
