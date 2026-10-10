<div align="center">

# 📖 术语表 · Glossary

**STORY-ENGINE**

*每个词都用一句人话解释 · Every term explained in one plain sentence*

</div>

---

> 英文术语保留原样，方便你对照 README、文档与代码。
> The English term is kept as-is so you can match it against the README, the docs and the code.

| 术语 Term | 中文 | 一句话人话 · Plain meaning |
|---|---|---|
| **Story Engine** | 故事引擎 | 面向创作者的长篇一致性引擎，自动审角色设定、因果时间线与记忆线。 |
| **Document Review Engine** | 文档审查引擎 | 面向企业的离线合规审查引擎，零依赖、纯规则库、不联网也能跑。 |
| **Consistency audit** | 一致性审计 | 检查「人设有没有崩、时间线有没有打结、记忆有没有对不上」。 |
| **ResponsibilityAccount** | 责任闭环锚定 | 每一项检查都挂到一个有名有姓的责任节点（谁 · 什么角色 · 哪个阶段）。 |
| **CognitiveAuditEngine** | 认知审计引擎 | 执行审计的主体，可挂载多个审计维度。 |
| **AuditPlugin** | 审计插件 | 可插拔的审计维度——想多加一条检查，就多插一个插件。 |
| **CausalNode** | 因果节点 | 剧情里的一步；它携带「隐含假设」和「脆弱度分数」。 |
| **implicit_assumptions** | 隐含假设 | 剧情往下走时没有说出口、但必须成立的前提。 |
| **vulnerability_score** | 脆弱度 | 这个前提一旦不成立，剧情会崩得多厉害。 |
| **NarrativeStripper** | 叙事剥离器 | 删掉修辞与情绪词，只留下事实链。 |
| **ImplicitAssumptionDetector** | 隐含假设探测器 | 把读者（和作者）没说出口的预设挑出来。 |
| **VulnerabilityAssessor** | 脆弱性评估器 | 给每个假设打分，找出最容易被推翻的那一环。 |
| **OOC (out of character)** | 人设崩坏 | 角色的言行与既定设定不符。 |
| **WorldBuilder** | 世界观构建器 | 从正文里按词级抽取门派、地理、势力等设定。 |
| **SPL four-stage pipeline** | SPL 四阶段流水线 | 剥离叙述 → 扫描假设 → 对冲风险 → 锁定责任。 |
| **STRIP_NARRATIVE / SCAN_ASSUMPTION / HEDGE_RISK / LOCK_RESPONSIBILITY** | 四个阶段 | 上面四步在代码里的正式名字。 |
| **CausalIntersectionBroker** | 因果交汇中介 | 把多条世界线 / 情节线合并成一条自洽的主线。 |
| **Risk levels (SAFE / WARNING / CRITICAL / FATAL)** | 风险等级 | 从「没问题」到「致命」，四档分级。 |
| **TraceLog** | 全链路日志 | 每一步判断都能倒查回它的原始依据。 |
| **RuleEngine** | 规则引擎 | 加载纯 JSON 规则库；命中即判，不做概率推测。 |
| **Hit = verdict** | 命中即判 | 规则命中就是结论，没有「大概 / 可能」。 |
| **Engine isolation check** | 引擎隔离检测 | 两个同名但不同的引擎被混用时立刻告警，防止数据互相覆盖。 |

---

## ✦ English Glossary

*Every term explained in one plain sentence.*

| Term | Plain meaning |
|---|---|
| **Story Engine** | A long-form consistency engine for creators: it audits character settings, causal timelines and memory lines automatically. |
| **Document Review Engine** | An offline compliance review engine for businesses: zero dependencies, pure rule base, runs without a network. |
| **Consistency audit** | Checks whether characters went out of character, timelines tangled, or memories stopped matching. |
| **ResponsibilityAccount** | Every check is anchored to a named responsibility node (who · which role · which stage). |
| **CognitiveAuditEngine** | The subject that performs the audit and can carry multiple audit dimensions. |
| **AuditPlugin** | A pluggable audit dimension — want another check, plug in another plugin. |
| **CausalNode** | One step of the plot; it carries implicit assumptions and a vulnerability score. |
| **implicit_assumptions** | The premises that are never stated but must hold for the plot to continue. |
| **vulnerability_score** | How badly the plot breaks if that premise turns out to be false. |
| **NarrativeStripper** | Removes rhetoric and emotional wording, leaving only the chain of facts. |
| **ImplicitAssumptionDetector** | Surfaces the premises that readers (and the author) never said out loud. |
| **VulnerabilityAssessor** | Scores every assumption to find the link most likely to be knocked down. |
| **OOC (out of character)** | A character acts or speaks against their established setting. |
| **WorldBuilder** | Extracts factions, geography and other settings from the text at word level. |
| **SPL four-stage pipeline** | Strip the narrative → scan assumptions → hedge the risk → lock responsibility. |
| **STRIP_NARRATIVE / SCAN_ASSUMPTION / HEDGE_RISK / LOCK_RESPONSIBILITY** | The four stages' formal names in code. |
| **CausalIntersectionBroker** | Merges multiple world lines / plot lines into one self-consistent main line. |
| **Risk levels (SAFE / WARNING / CRITICAL / FATAL)** | Four severity tiers, from "no problem" to "fatal". |
| **TraceLog** | Every judgement can be traced back to the evidence it came from. |
| **RuleEngine** | Loads a pure-JSON rule base; a hit is a verdict, with no probabilistic guessing. |
| **Hit = verdict** | A rule hit is the conclusion — no "probably", no "maybe". |
| **Engine isolation check** | Alerts immediately when two same-named but different engines get mixed up, preventing data from overwriting each other. |

---

<div align="center">

[← 返回 README](./README.md) &nbsp;·&nbsp; [中文说明](./README-zh.md)

<sub>NOHN AI · STORY-ENGINE</sub>

</div>
