<div align="center">

# 📖 术语表 · Glossary

**ANTHROPOMORPHIC-AGENT-ENGINE**

*每个词都用一句人话解释 · Every term explained in one plain sentence*

</div>

---

> 英文术语保留原样，方便你对照 README 与代码。
> The English term is kept as-is so you can match it against the README and the source code.

| 术语 Term | 中文 | 一句话人话 · Plain meaning |
|---|---|---|
| **SPL Pure Core** | SPL 纯内核 | 一个不依赖大模型、不用随机数的「心理状态计算器」。 |
| **Interoceptive vector** | 内感受向量 | 把外界事件翻译成一组「内心感受」数值（归属感、威胁感……），再喂给内核。 |
| **8-Dimensional Emotion Fluid** | 8 维情绪流体 | 把情绪拆成 8 个可连续变化的量（喜·怒·惧·信任·疏离·紧张·愧疚·羞耻），而不是只有「开心 / 不开心」。 |
| **Continuous-state** | 连续状态 | 情绪像水位一样缓慢涨落，不是非黑即白的开关。 |
| **Deterministic / Replayable** | 确定性 / 可复现 | 同一串事件跑两遍，结果分毫不差——前提是先注入虚拟时钟。 |
| **Virtual clock** | 虚拟时钟 | 测试时用一个假的时间源，让「可复现」这句承诺真正成立。不注入就走真实时间，两次结果会不一样。 |
| **NarrativeMapper** | 人格映射层 | 可替换的一层，负责把「被侮辱了」这类事件翻译成内核能吃的数值。 |
| **Personality layer** | 人格层 | 决定这个人偏乐观、偏多疑还是偏厌世；换掉它不影响内核。 |
| **Trauma reconsolidation** | 创伤再巩固 | 旧创伤每次被回忆都会被重新写入一次，记忆不是冷冻的。 |
| **Ebbinghaus forgetting** | 艾宾浩斯遗忘 | 记忆随时间自然衰减的那条曲线。 |
| **Suppression–rebound** | 压抑–反弹 | 越是被强行压住的情绪，越容易在之后集中爆发。 |
| **Latent pressure avalanche** | 潜在压力雪崩 | 压力长期累积到临界点后的连锁崩溃。 |
| **Max-trust erosion** | 信任上限侵蚀 | 长期冷落不是让信任掉一点，而是把「能信任的上限」整体调低。 |
| **Slow-variable mood** | 慢变量心境 | 比情绪变化慢得多的底色，决定这段时间整体偏积极还是偏低落。 |
| **Self-esteem dynamics** | 自尊动力学 | 自尊也会被事件推动涨落，并有下限保护。 |
| **Expectation system** | 期望系统 | 希望 / 焦虑 / 失望三个量，让角色会「期待」而不只是「反应」。 |
| **Token metering** | Token 计量 | 统计每次调用大模型花了多少 token，可按模型分类并导出 JSON。 |
| **Audit logger** | 审计日志 | 自动记录每次大模型调用的耗时、用量与成败。 |
| **Wired / not wired** | 已接入 / 未接入 | 标注某个模块是真的接进内核在跑，还是仅作设计参考。 |
| **Minor-protection variant** | 未成年人保护变体 | 主引擎的合规改造版：去掉创伤模拟、压低下限，并加装四层保护。 |

---

## ✦ English Glossary

*Every term explained in one plain sentence.*

| Term | Plain meaning |
|---|---|
| **SPL Pure Core** | A "mental state calculator" that needs no large model and no random numbers. |
| **Interoceptive vector** | Translates outside events into a set of inner-feeling values (belonging, threat …) and feeds them to the core. |
| **8-Dimensional Emotion Fluid** | Emotion split into eight continuously varying quantities (joy · anger · fear · trust · alienation · tension · guilt · shame) instead of just happy / unhappy. |
| **Continuous-state** | Emotion rises and falls slowly like a water level, not as a black-or-white switch. |
| **Deterministic / Replayable** | Run the same event sequence twice and get byte-identical results — provided a virtual clock is injected first. |
| **Virtual clock** | A fake time source used in tests so the "replayable" promise actually holds; without it, real time is used and two runs differ. |
| **NarrativeMapper** | A replaceable layer that translates events like "was insulted" into numbers the core can digest. |
| **Personality layer** | Decides whether a person leans optimistic, suspicious or world-weary; swapping it doesn't touch the core. |
| **Trauma reconsolidation** | An old trauma is rewritten every time it is recalled — memory is not frozen. |
| **Ebbinghaus forgetting** | The curve along which memories naturally decay over time. |
| **Suppression–rebound** | Emotion that is forced down hardest tends to burst out later, all at once. |
| **Latent pressure avalanche** | A chain collapse after pressure accumulates past a critical point. |
| **Max-trust erosion** | Chronic neglect doesn't lower trust a bit — it lowers the ceiling of how much trust can ever be given. |
| **Slow-variable mood** | A backdrop far slower than emotion, setting whether this period is overall positive or low. |
| **Self-esteem dynamics** | Self-esteem is pushed up and down by events too, with a floor that protects it. |
| **Expectation system** | Hope, anxiety and disappointment — three quantities that let a character expect, not merely react. |
| **Token metering** | Counts how many tokens each LLM call spent, broken down by model and exportable as JSON. |
| **Audit logger** | Automatically records latency, usage and success or failure of every LLM call. |
| **Wired / not wired** | Marks whether a module actually runs inside the core or exists only as design guidance. |
| **Minor-protection variant** | A compliance-adapted build of the main engine: trauma simulation removed, floors lowered, four protection layers added. |

---

<div align="center">

[← 返回 README](./README.md) &nbsp;·&nbsp; [中文说明](./README-zh.md)

<sub>NOHN AI · ANTHROPOMORPHIC-AGENT-ENGINE</sub>

</div>
