# 术语表 · Glossary — AAE

*每个词都用一句人话解释 · Every term explained in one plain sentence*

> 本表只收录**接口契约**相关术语。动力学系数与调参相关的实现层术语不在本表，也不在公开层。

## 中文

| 术语 Term | 中文 | 一句话人话 · Plain meaning |
|---|---|---|
| **SPL Pure Core** | SPL 纯内核 | 一个不依赖大模型、不用随机数的「心理状态计算器」。 |
| **Interoceptive vector** | 内感受向量 | 把外界事件翻译成一组「内心感受」数值（归属感、威胁感……），再喂给内核。 |
| **Emotion Fluid** | 情绪流体 | 把情绪拆成 8 个可连续变化的量（喜·怒·惧·信任·疏离·紧张·愧疚·羞耻），而不是只有「开心 / 不开心」。 |
| **Continuous-state** | 连续状态 | 情绪像水位一样缓慢涨落，不是非黑即白的开关。 |
| **Deterministic / Replayable** | 确定性 / 可复现 | 同一串事件跑两遍，结果分毫不差——前提是先注入虚拟时钟。 |
| **Virtual clock** | 虚拟时钟 | 测试时用一个假的时间源，让「可复现」这句承诺真正成立。不注入就走真实时间，两次结果会不一样。 |
| **NarrativeMapper** | 人格映射层 | 可替换的一层，负责把「被侮辱了」这类事件翻译成内核能吃的数值。 |
| **Personality layer** | 人格层 | 决定这个人偏乐观、偏多疑还是偏厌世；换掉它不影响内核。 |
| **Trauma reconsolidation** | 创伤再巩固 | 旧创伤每次被回忆都会被重新写入一次，记忆不是冷冻的。 |
| **Ebbinghaus forgetting** | 艾宾浩斯遗忘 | 记忆随时间自然衰减的那条曲线。 |
| **Suppression–rebound** | 压抑–反弹 | 越是被强行压住的情绪，越容易在之后集中爆发。 |
| **Latent pressure** | 隐压 | 尚未爆发的累积压力；越过阈值后触发雪崩。 |
| **Max-trust erosion** | 信任上限侵蚀 | 长期冷落不是让信任掉一点，而是把「能信任的上限」整体调低。 |
| **Slow-variable mood** | 慢变量心境 | 比情绪变化慢得多的底色，决定这段时间整体偏积极还是偏低落。 |
| **Self-esteem dynamics** | 自尊动力学 | 自尊也会被事件推动涨落，并有下限保护。 |
| **Expectation system** | 期望系统 | 希望 / 焦虑 / 失望三个量，让角色会「期待」而不只是「反应」。 |
| **Defence compartment** | 防御机制仓 | 压抑 / 否认 / 合理化三者的载荷；机制级削减，非输出侧过滤。 |
| **Token metering** | Token 计量 | 统计每次调用大模型花了多少 token，可按模型分类并导出 JSON。 |
| **Audit logger** | 审计日志 | 自动记录每次大模型调用的耗时、用量与成败。 |
| **Snapshot** | 快照 | 某一时刻角色全部内部状态的字典，键集固定。 |
| **Delta** | 状态转移归因 | 一次输入造成了哪些字段的多少变化，逐字段记差。 |
| **Wired / not wired** | 已接入 / 未接入 | 标注某个模块是真的接进内核在跑，还是仅作设计参考。 |
| **Minor-protection variant** | 未成年人保护变体 | 主引擎的合规改造版：不建模创伤、无防御机制仓，另加合规保护报告。 |

## English

| Term | Plain meaning |
|---|---|
| **SPL Pure Core** | A "mental state calculator" that needs no large model and no random numbers. |
| **Interoceptive vector** | Translates outside events into a set of inner-feeling values (belonging, threat …) and feeds them to the core. |
| **Emotion Fluid** | Emotion split into eight continuously varying quantities (joy · anger · fear · trust · alienation · tension · guilt · shame) instead of just happy / unhappy. |
| **Continuous-state** | Emotion rises and falls slowly like a water level, not as a black-or-white switch. |
| **Deterministic / Replayable** | Run the same event sequence twice and get byte-identical results — provided a virtual clock is injected first. |
| **Virtual clock** | A fake time source used in tests so the "replayable" promise actually holds without one, real time is used and two runs differ. |
| **NarrativeMapper** | A replaceable layer translating events like "was insulted" into numbers the core can digest. |
| **Personality layer** | Decides whether a person leans optimistic, suspicious or world-weary; swapping it doesn't touch the core. |
| **Trauma reconsolidation** | An old trauma is rewritten every time it is recalled — memory is not frozen. |
| **Ebbinghaus forgetting** | The curve along which memories naturally decay over time. |
| **Suppression–rebound** | Emotion forced down hardest tends to burst out later, all at once. |
| **Latent pressure** | Accumulated pressure not yet released; crossing a threshold triggers an avalanche. |
| **Max-trust erosion** | Chronic neglect doesn't lower trust a bit — it lowers the ceiling of how much trust can ever be given. |
| **Slow-variable mood** | A backdrop far slower than emotion, setting whether this period is overall positive or low. |
| **Self-esteem dynamics** | Self-esteem is pushed up and down by events too, with a floor that protects it. |
| **Expectation system** | Hope, anxiety and disappointment — three quantities that let a character expect, not merely react. |
| **Defence compartment** | The load of suppression / denial / rationalisation; reduced at mechanism level, not filtered at output. |
| **Token metering** | Counts tokens spent per LLM call, broken down by model and exportable as JSON. |
| **Audit logger** | Records latency, usage and success or failure of every LLM call automatically. |
| **Snapshot** | The dictionary of a character's full internal state at one instant, with a fixed key set. |
| **Delta** | Per-field attribution of how much each field changed because of one input. |
| **Wired / not wired** | Marks whether a module actually runs inside the core or exists only as design guidance. |
| **Minor-protection variant** | A compliance-adapted build: no trauma modelling, no defence compartment, plus a compliance protection report. |
