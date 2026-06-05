---
title: 从 Skill 到元认知：OpenClaw、Hermes 与 OpenSquilla 的演化综述
status: publish-draft
article_type: 架构综述
core_thesis: Agent 系统的下一步不是继续堆技能，而是让系统显式理解、监控、修正自己使用技能的方式。
created_at: 2026-06-05
---

# 从 Skill 到元认知：OpenClaw、Hermes 与 OpenSquilla 的演化综述

讨论 AI agent 的时候，我们很容易被一个问题吸住：它到底会不会做事？

于是工具越来越多，插件越来越多，skill 越来越多。今天能读文件，明天能开浏览器，后天能发消息、跑 cron、调 MCP、写代码、做研究。这个方向当然重要。一个智能系统如果不能行动，就只能停留在语言层面。

但真正的分水岭不在这里。

一个足够成熟的智能系统，不只是“有很多技能”。它还要知道什么时候该用哪个技能，为什么这样组合技能，执行中哪里可能出错，失败以后如何调整，成功以后如何把经验沉淀成新的工作方式。

这就是从 skill 到 metaskill，再到元认知的演化。

本文把 OpenClaw、Hermes Agent 和 OpenSquilla 放在同一条线上看。它不是严格意义上的历史考据，而是一篇架构综述：这些项目分别代表了 agent 系统演化中的三个台阶。OpenClaw 把 agent 带进个人工作区和真实工具链；Hermes 把 agent 做成可以跨平台运行、积累记忆和技能的 runtime；OpenSquilla 则开始把“技能组合方式”本身抽象成可复用、可审计的 MetaSkill。

资料截点是 2026-06-05。本文优先使用各项目的官方文档、GitHub README 和发布说明；涉及“下一步应该是什么”的部分，是作者的架构判断，不把推演伪装成已经实现的事实。

在这个判断的基础上，下一块拼图就很清楚了：元认知。

## 一、OpenClaw：让 agent 进入真实工作区

OpenClaw 的意义，不在于它拥有某个神奇模型，而在于它把 agent 放进了一个可以行动的环境里。

从官方文档看，OpenClaw 的定位是本地 AI agent，能够使用文件系统、终端、浏览器、编辑器、任务列表和历史记录等工具。它不是一个只在聊天框里回答问题的助手，而更像一个可以在个人电脑和项目目录里工作的执行体。

这一阶段的核心问题是：

> AI 如何从“会说”变成“会做”？

所以 OpenClaw 的架构重心自然落在工具和工作区上：

- 它需要知道自己在哪个 workspace 里工作；
- 它需要读写文件、执行命令、浏览网页；
- 它需要有 persona、用户信息、长期记忆和任务状态；
- 它需要把一次次操作接到现实世界，而不是只停留在文本生成。

这一步看起来朴素，但很关键。因为一旦 agent 真正进入工具世界，问题就变了。

过去的问题是“模型回答得对不对”。现在的问题变成“它会不会误操作”“它有没有权限边界”“它记不记得以前做过什么”“它能不能把复杂任务拆成可执行步骤”“出了错能不能恢复”。

也就是说，OpenClaw 把 agent 从语言系统推进到了行动系统。

但行动系统天然会暴露下一层矛盾：工具再多，如果没有更好的记忆、技能组织和自我改进机制，agent 还是会像一个每次醒来都要重新熟悉世界的人。

这就是 Hermes 出场的地方。

## 二、Hermes：从工具型 agent 到自改进 runtime

Hermes Agent 相比 OpenClaw 的关键推进，是把 agent 做成了更完整的运行时系统。

Hermes 官方 README 把它描述为 self-improving AI agent：它可以从经验中创建技能，在使用中改进技能，主动持久化知识，搜索过往对话，并在跨会话中建立对用户的持续理解。它还支持 Telegram、Discord、Slack、WhatsApp、Signal、CLI 等多入口，提供统一 gateway、cron 调度、memory、skills hub、插件和 dashboard。

如果说 OpenClaw 的重点是“让 agent 可以在我的机器上做事”，Hermes 的重点就是：

> 让 agent 可以长期活在一个运行时里，并且逐渐变得更会做事。

Hermes v0.2.0 的发布说明很能说明这个转向。这个版本强调多平台消息 gateway、MCP client、70+ bundled/optional skills、provider router、editor integration、worktree isolation、filesystem checkpoint/rollback，以及数千个测试。这已经不是一个单纯聊天助手的形态，而是 agent operating system 的雏形。

更重要的是，Hermes 明确提供了从 OpenClaw 迁移的工具。迁移脚本会处理 OpenClaw 的 persona、workspace instructions、memory、user profile、messaging settings、skills、MCP servers、cron jobs、browser/tool settings、approvals、memory backend 和 UI identity 等内容。

这件事很有象征意义。

它说明 OpenClaw 时代沉淀出来的，不只是代码和配置，而是一整套“agent footprint”：身份、记忆、技能、工具、权限、渠道、任务状态。Hermes 要接住这些 footprint，就必须把它们拆成可迁移、可管理、可组合的模块。

这一步的本质，是从“agent 会用工具”进入“agent 有长期运行结构”。

但 Hermes 也暴露了新的边界：skills 很多，memory 很强，gateway 很完整，不等于系统已经知道“如何选择、组合、验证和改进自己的技能”。

这就是 metaskill 的问题。

## 三、OpenSquilla：把技能组合方式本身变成协议

OpenSquilla 走到的是另一个抽象层。

OpenSquilla 官方 glossary 把 MetaSkill 定义为可复用、可审计的 workflow protocol，用来组合 skills、tools、LLM 调用、checkpoint 和输出步骤。它的 0.3.0 发布说明也明确把 MetaSkills 作为重要版本能力：系统可以把复杂任务封装成结构化 workflow，而不是每次临场拼提示词。

这一步的价值很大。

因为 skill 解决的是“我会做什么”，metaskill 解决的是“我如何组织一组能力去完成一个目标”。

比如“写一篇研究综述”不是一个单一 skill。它至少包含：

- 定义问题；
- 收集资料；
- 区分事实、判断和推测；
- 建立时间线；
- 比较不同系统的架构差异；
- 提炼核心论点；
- 写作；
- 校对引用；
- 检查是否过度推断。

如果每次都靠模型即时发挥，结果就会不稳定。MetaSkill 的意义，是把这种复杂任务变成可以复用、检查和 replay 的流程。

OpenSquilla 还把 MetaSkills 和 memory、Replay、Dream Mode、诊断等机制放在一起。这个组合很关键：只有 workflow，没有执行轨迹和记忆，metaskill 只是流程模板；有了 replay 和 memory，系统才有机会复盘“这个流程到底好不好”。

所以 OpenSquilla 已经不是简单地扩展技能库，而是在做一个更抽象的事：

> 把 agent 的工作方法变成对象。

skill 是能力对象。  
metaskill 是方法对象。  
memory 是经验对象。  
replay 是行为证据。  
diagnostics 是系统自查入口。

这个方向已经很接近元认知了。

但它还不是完整的元认知。

## 四、MetaSkill 还不是元认知

这点需要说清楚。

MetaSkill 很强，但它本质上仍然是一种“流程能力”。它回答的是：

> 我该怎样组织能力完成任务？

元认知要回答的则是：

> 我现在为什么这样组织能力？这种组织可靠吗？我是否正在犯错？我应该继续、暂停、改道，还是请求人类介入？

心理学里的元认知通常被理解为对认知活动的监控和控制。放到 agent 系统里，我们不必先争论 AI 是否真的有主观意识。工程上更重要的问题是：系统是否能显式表示自己的状态，并且根据这个状态干预自己的行动。

所以元认知不是“再加一个高级 skill”。它应该是覆盖在 skill 和 metaskill 之上的自我调节层。

一个没有元认知的 agent 可以很会执行，但也可能很会把错误执行到底。

它可能在资料不足时继续写结论；在用户目标有歧义时假装理解；在工具失败后重复同一个动作；在引用不足时编造来源；在权限风险很高时仍然推进；在任务已经偏离目标时还觉得自己很忙。

这类问题不是靠多装几个 skill 就能根治的。因为问题不在能力数量，而在系统有没有观察和校准自己能力使用方式的机制。

## 五、下一块拼图：工程化元认知层

如果把 OpenClaw、Hermes、OpenSquilla 串起来，未来的方向会变得很清楚。

OpenClaw 解决行动入口。  
Hermes 解决长期运行和技能生态。  
OpenSquilla 解决技能组合和 workflow 协议。  
下一步要解决的是：agent 如何管理自己的可靠性。

我认为工程化元认知至少应该包含六个部分。

### 1. 自我状态模型

系统要显式维护自己的当前状态，而不是把所有东西都塞进上下文窗口里。

这个状态至少包括：

- 当前目标；
- 成功标准；
- 已知事实；
- 待验证假设；
- 当前计划；
- 正在使用的 skill / metaskill；
- 置信度；
- 风险等级；
- 权限边界；
- 上下文缺口；
- 已失败尝试。

没有这个状态模型，系统就很难知道自己正在做什么，更不用说知道自己哪里可能错了。

### 2. 执行监控器

系统需要一个持续观察执行过程的 monitor。

它不负责直接完成任务，而是检查执行有没有出现危险信号：

- 目标漂移；
- 过度推断；
- 证据不足；
- 工具结果和计划不一致；
- 多次重复失败；
- 输出无法验证；
- 引用缺失；
- 权限或隐私风险升高；
- 用户意图和系统行动开始脱节。

这就是元认知里的 monitoring。

### 3. 自我干预策略

监控本身不够。发现问题以后，系统还要知道怎么干预自己。

可选动作包括：

- 暂停并向用户确认；
- 降低结论强度；
- 改成搜索或实验；
- 拆小任务；
- 切换 skill；
- 重写计划；
- 回滚操作；
- 要求更强验证；
- 退出当前路径。

这就是元认知里的 control。

很多 agent 现在最大的问题不是不会执行，而是不会停。会停、会问、会改道，反而是更高级的智能。

### 4. 证据化 replay

元认知不能只靠自我感觉。

每一次 agent 执行都应该留下可检查轨迹：当时的目标是什么，选择了哪个 metaskill，用了哪些工具，得到了什么证据，哪里失败，最后为什么认为任务完成。

Replay 的意义就在这里。它不是日志装饰，而是元认知的证据底座。

没有 replay，复盘只能靠印象。  
有了 replay，系统才可能比较不同策略，发现哪个 workflow 更稳，哪个 skill 容易误触，哪个检查点经常被跳过。

### 5. 复盘到记忆和技能更新

元认知的最后一步不是“意识到问题”，而是把问题转化成系统改进。

复盘结果应该能沉淀到：

- memory；
- checklist；
- skill patch；
- metaskill patch；
- failure case；
- eval case；
- routing rule；
- permission policy。

这一步非常重要。否则每次复盘只是一次漂亮总结，下次还会犯同样的错。

真正成熟的 agent，要能把失败变成结构。

### 6. 治理边界

元认知越强，系统越需要治理。

如果 agent 可以自己改 skill、改 metaskill、改记忆、改策略，那就必须有版本控制、审计、回滚、权限分级和人类确认机制。

否则所谓自我改进，很容易变成不可解释的自我漂移。

所以未来架构不应该只追求“更自主”，还要追求“自主行为可被看见、可被质疑、可被撤销”。

## 六、一个更完整的 agent 架构图

把这些合在一起，一个更成熟的智能系统应该不是单层 agent，而是多层架构：

```text
用户 / 外部世界
    ↓
感知与工具层
    - 文件、终端、浏览器、API、消息平台、MCP、数据库
    ↓
任务理解层
    - 目标、成功标准、约束、事实、未知项
    ↓
Skill 层
    - 单项能力：搜索、写作、编程、诊断、图像、数据分析
    ↓
MetaSkill 层
    - 复杂任务 workflow：组合 skill、工具、检查点、输出步骤
    ↓
元认知层
    - 自我状态模型、执行监控、自我干预、置信度、风险校准
    ↓
验证与治理层
    - 测试、replay、审计、权限、回滚、人类确认
    ↓
学习沉淀层
    - memory、skill 更新、metaskill 更新、failure/eval cases
    ↺
进入下一轮
```

这里的关键不是层数，而是闭环。

工具让系统接触现实。  
skill 让系统具备能力。  
metaskill 让系统组织能力。  
元认知让系统管理自己的可靠性。  
验证和治理让系统不被自己的叙事带跑。  
记忆和更新让系统把经验变成下一次的优势。

这才是 agent operating system 真正要走向的东西。

## 七、结论：真正的 AGI 不应该只是一个超强模型

从 OpenClaw 到 Hermes，再到 OpenSquilla，我们看到的不是简单的项目替代，而是一条能力抽象的升级路径。

第一阶段，agent 要能行动。  
第二阶段，agent 要能长期运行。  
第三阶段，agent 要能组织技能。  
第四阶段，agent 要能监控和修正自己。

也就是说，真正的 AGI，从来都不应该只是一个超强模型。

它更像一个有工具、有记忆、有方法、有自查、有复盘、有治理边界的智能系统。

OpenClaw 让 agent 进入工作区。  
Hermes 让 agent 进入持续运行的生态。  
OpenSquilla 让 agent 的工作方法变成可复用协议。  
而未来的元认知层，要让 agent 知道自己正在怎样工作，以及这种工作方式是否值得信任。

这才是最后一块拼图。

不是让 AI 宣称“我有意识”。  
而是让它在每一次行动里，都能回答：

我在做什么？  
我为什么这么做？  
我凭什么相信这是对的？  
如果错了，我如何发现？  
发现以后，我如何改变？

一个系统能持续回答这些问题，它就已经不只是技能集合了。

它开始接近一个真正意义上的智能操作系统。

## 参考资料

- OpenClaw Documentation: https://docs.openclaw.ai/
- OpenClaw Tools Documentation: https://docs.openclaw.ai/tools
- Hermes Agent README: https://github.com/NousResearch/hermes-agent
- Hermes Agent v0.2.0 release notes: https://github.com/NousResearch/hermes-agent/releases/tag/v2026.3.12
- Hermes OpenClaw migration helper: https://github.com/NousResearch/hermes-agent/tree/main/optional-skills/migration/openclaw-migration
- OpenSquilla Glossary: https://opensquilla.ai/docs/glossary/
- OpenSquilla MetaSkills: https://opensquilla.ai/docs/features/meta-skills/
- OpenSquilla Memory: https://opensquilla.ai/docs/features/memory/
- OpenSquilla v0.3.0 release notes: https://opensquilla.ai/docs/releases/0-3-0/
- Metacognition and AI Agents position paper: https://arxiv.org/abs/2605.23981
