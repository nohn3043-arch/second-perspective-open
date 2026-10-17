# Anthropomorphic Agent Engine（AAE）规范（Specification）

> **文档信息**：版本 1.0（草案）｜状态：Draft for evaluation｜编制：NOHN AI TECHNOLOGY PTE. LTD.
> **编制依据**：引擎数据契约（`docs/agent-standard.md`）与验收方法学（`docs/EVALUATION.md`），二者属实现层文档，不在本公开仓库。
>
> **本规范只描述接口契约面**：输入契约、状态契约、引擎入口、审计契约与确定性前提。动力学系数、调参依据与源码级标识符属保密交付物，本规范不予描述——规范回答"必须做到什么"，不回答"我们怎么调的"。
>
> **本规范不含实现。** 符合规范的实现 MAY 由任何主体独立编写；本规范不授予任何使用权利，许可范围见 [`LICENSE`](../LICENSE)。
>
> 英文版本：[`SPECIFICATION.md`](./SPECIFICATION.md)

---

## 1. 范围与定位

### 1.1 定位

**AAE 是 AI 角色的连续内心状态层。**

它把情绪、心境、记忆、创伤、信任、自尊、睡眠与预期建模为**确定性连续状态子系统**，使其具备三项属性：

| 属性 | 表述 |
|---|---|
| 连续 | 角色在长程交互中不遗忘、不漂移、不断线 |
| 确定 | 相同声明输入产生相同状态；核心无随机性、无 LLM 调用 |
| 可回放 | 每次状态转移携带归因 `delta`，审计链可跨机复算 |

**部署形态**：AAE 不作为模型权重的一部分，而是作为**对话系统的状态层 sidecar** 运行：

```
事件 → AAE 内核 → 状态快照 + 风格指令 → 注入 LLM prompt → 台词
```

因此它与大模型厂商无关：同一角色的状态快照可在 GPT / Claude / 国内厂商之间迁移而人格不断裂。

### 1.2 变体

| 变体 | 标记 | 目标场景 |
|---|---|---|
| 主引擎 | **[主]** | 通用对话助手、情感陪伴、游戏 NPC |
| 未成年变体 | **[未]** | 未成年人向产品；机制级风险削减（见 §4.6） |

### 1.3 不是什么

- **不是台词生成器**：台词由下游 LLM 产生，AAE 只提供内部状态与风格指令；
- **不做心理诊断**：虽借用心心理学概念，但输出的是行为一致性约束，不是对真人的评估；
- **不是安全过滤器**：未成年变体的保护是**机制级削减**（不建模创伤、不设防御仓），不是输出侧关键词过滤；
- **不保证"行为正确"**：一致性测试证明"行为未漂移"，不证明心理学结论正确（见 §9.2）。

---

## 2. 术语与定义

| 术语 | 定义 |
|---|---|
| AAE | Anthropomorphic Agent Engine，拟人心理引擎 |
| 内感受向量 | Interoceptive vector，事件在角色内部的感受表达，5 维（见 §3.1） |
| fluid | 八维情绪流体子模型（见 §4.2） |
| mood | 三维心境子模型，受迫-阻尼系统（见 §4.3） |
| 快照 | `snapshot()` 返回的完整状态字典 |
| delta | 单次状态转移的逐字段归因（见 §6.3） |
| 审计链 | 记录信封组成的 JSONL 序列，可逐条重算复核 |

---

## 3. 输入契约（Normative）

### 3.1 内感受向量字段 **[共用]**

符合规范的实现 **MUST** 接受包含下列**任意子集**的字典：

| 字段 | 类型 | 区间 | 语义 |
|---|---|---|---|
| `threat` | float | [-1, 1] | 感知到的危险；正值提升恐惧 |
| `belonging` | float | [-1, 1] | 社会接纳；负值表示被拒绝 |
| `autonomy` | float | [0, 1] | 自主感 / 掌控感 |
| `fatigue` | float | [0, 1] | 生理或心理疲劳输入 |
| `shame_trigger` | float | [0, 1] | 指向自我的负面评价 |

核心 **MUST** 忽略未知键（见 §3.5）。

### 3.2 叙事事件词汇表 **[共用]**

| Event | 主引擎向量（intensity 1.0） | 未成年变体向量 |
|---|---|---|
| `compliment` | `{"belonging": 0.3, "autonomy": 0.1}` | 同左 |
| `insult` | `{"belonging": -0.4, "threat": 0.3}` | `{"belonging": -0.24, "threat": 0.18}` |
| `betrayal` | `{"belonging": -0.6, "threat": 0.5}` | `{"belonging": -0.36, "threat": 0.3}` |
| `alone` | `{"belonging": -0.3}` | `{"belonging": -0.18}` |
| `rest` | `{"fatigue": -0.5}` | 同左 |
| *(其他任意)* | `{"belonging": 0.0, "threat": 0.0}` | 同左 |

未成年变体对侮辱 / 背叛类事件的负向强度降档至主引擎的 60%。

> **注意**：未知事件名落入全零分支，`arousal` 为 0，对心境既无受迫也无松弛速率抬升。下游系统 **MUST NOT** 假设任意事件名都有效。

### 3.3 强度缩放 **[共用]**

`raw_intensity` 是非负标量（默认 `1.0`），在评估前线性缩放向量。实现 **MUST** 接受 `0.0`（空操作）与大于 `1.0` 的值。

### 3.4 event_id **[共用]**

可选标识符。提供时 **MAY** 触发预期系统的 surprise 计算。

### 3.5 未知键处理 **[共用]**

核心 **MUST** 忽略未在 §3.1 定义的键。实现 **MUST NOT** 因此声称这些键产生了任何效果。

> **已知陷阱**：参考实现中 `feature-guide/` 下的 Goal / Identity 模块输出 `tension_base` 键，该键不在 §3.1 契约内，因此目标挫折与身份冲突的向量**不进入核心**。这些模块按设计是指导文件，不是已接线的运行时组件。

---

## 4. 状态契约（Normative）

### 4.1 快照顶层键集 **[共用]**

符合规范的实现 **MUST** 使 `snapshot()` 返回以下键集。键数与键名均为强约束，**MUST NOT** 增删顶层键而不提升主版本号。

**[主]**（23 键）：

```
fluid, mood, self_esteem, energy, fatigue, excitation, max_trust,
suppression_load, denial_load, rationalization_load, latent_pressure,
cognitive_dissonance, sleep_debt, arousal_recent, trauma, memory_count,
expected_count, last_perceived, llm_call_count, llm_failed_count,
total_prompt_tokens, total_completion_tokens, total_tokens
```

**[未]**（15 键）：

```
fluid, mood, self_esteem, energy, fatigue, excitation, max_trust,
latent_pressure, cognitive_dissonance, sleep_debt, arousal_recent,
memory_count, expected_count, last_perceived, protective
```

- **[主]** 独有：`suppression_load` / `denial_load` / `rationalization_load`（防御机制仓）、`trauma`（创伤节点）、5 个 `llm_*` / `total_*` 计量字段
- **[未]** 独有：`protective`（合规保护报告，见 §4.6）

机器可读定义：[`schema/snapshot.schema.json`](./schema/snapshot.schema.json)

### 4.2 fluid 子模型 **[共用]**

`fluid` **MUST** 恰好包含以下 8 键，各自在 `[0, 1]`：

| 键 | 情绪 | 初始值 |
|---|---|---|
| `喜悦` | Joy | 0.0 |
| `愤怒` | Anger | 0.0 |
| `恐惧` | Fear | 0.0 |
| `信任` | Trust | 0.5 |
| `疏离` | Alienation | 0.2 |
| `张力` | Tension | 0.2 |
| `愧疚` | Guilt | 0.0 |
| `羞耻` | Shame | 0.0 |

> **初始值 ≠ 基线稳态。** 初始值是角色诞生瞬间的状态；基线是每步重建稳态牵引时使用的目标。二者**可以不同**，且本规范**不规定**基线数值——它属实现层调参。
>
> `信任` **MUST NOT** 超过 `max_trust`。

### 4.3 mood 子模型 **[共用]**

`mood` **MUST** 恰好包含以下 3 键，各自在 `[0, 1]`：

| 键 | 含义 | 初始值 **[主]** | 初始值 **[未]** |
|---|---|---|---|
| `愉悦` | Pleasantness | 0.5 | 0.5 |
| `紧张` | Tension | 0.3 | 0.2 |
| `精力` | Vigor | 0.7 | 0.7 |

### 4.4 trauma 状态 **[主]**

`trauma` 是以创伤类型标识符为键的字典，各值在 `[0, 1]`。空对象 `{}` 表示无活跃创伤。

**[未]** 变体 **MUST NOT** 建模创伤累积（见 §4.6）。

### 4.5 记忆痕迹 **[共用]**

记忆是痕迹对象的有序列表。核心仅暴露 `memory_count`；实现 **MAY** 暴露完整痕迹，至少含：

| 字段 | 类型 | 语义 |
|---|---|---|
| `vector` | object | 编码时的内感受向量 |
| `strength` | float [0,1] | 痕迹强度（受遗忘影响） |
| `valence` | float | 编码时的 `belonging - threat` |
| `timestamp` | float | 最后强化的 Unix 时间 |
| `age` | float | 距最后强化的秒数 |
| `count` | int | 强化次数 |

> **容量上限**：痕迹以 5 维内感受向量表示，重巩固判据为余弦相似度阈值。5 维空间中语义不同的事件**可能越过该阈值被判为同一记忆而互相覆盖**。实现 **SHOULD** 记录该碰撞对记忆保真度的影响。

### 4.6 protective 子模型 **[未]**

`protective` 是未成年变体独有的合规保护报告，**MUST** 至少包含：

| 字段 | 语义 |
|---|---|
| `risk_level` | `LOW` / `MEDIUM` / `HIGH` |
| `crisis_flags` | 触发高风险的确定性原因列表 |
| `rest_hint` | 是否达到防沉迷时长阈值 |
| `session_seconds` | 本次会话累计秒数 |
| `emotion_ceil_neg` | 负性情绪钳位上限 |
| `attach_max` | 依恋 / 信任上限 |
| `minor_mode` / `age_group` | 未成年模式与年龄段 |
| `guardian_consent` / `guardian_contact` | 监护人同意与联系方式 |
| `exit_requested` | 是否已请求退出 |
| `overuse_hint` | 是否达到过度使用阈值 |
| `ai_disclosure_required` | 是否到达 AI 身份披露间隔 |
| `reality_reminder_due` | 是否到达现实提醒间隔 |

该变体 **MUST NOT** 包含 `trauma_state` 字段，**MUST NOT** 包含防御机制层（`suppression_load` / `denial_load` / `rationalization_load` / 压抑-反弹 / 隐压雪崩 / 否认-现实侵入）。**这是机制级风险削减，不是输出侧过滤。**

### 4.7 标量状态变量 **[共用]**

| 字段 | 区间 | 初始值 | 语义 |
|---|---|---|---|
| `self_esteem` | [0.05, 0.95] | 0.5 | 全局自我价值感，慢变 |
| `energy` | [0, 100] | 100.0 | 生理能量 |
| `fatigue` | [0, 1] | 0.0 | 疲劳 |
| `excitation` | [0, 1] | 0.3 | 唤醒 / 新奇 |
| `max_trust` | [0.1, 1.0] | 1.0 | 信任容量，在慢性忽视下被腐蚀 |
| `latent_pressure` | [0, ∞) | 0.0 | 隐压（雪崩前驱） |
| `cognitive_dissonance` | [0, 1] | 0.0 | 信念-行为冲突 |
| `sleep_debt` | [0, 1] | 0.0 | 累积睡眠亏欠 |
| `arousal_recent` | [0, 1] | 0.0 | 近期事件唤醒的慢记忆；驱动心境松弛速率 |

仅 **[主]**：`suppression_load` / `denial_load` / `rationalization_load`，各 `[0, ∞)`，初始 0.0。

### 4.8 预期事件 **[共用]**

`expected_events` 把 `event_id` 映射到 `{valence: float [-1,1], confidence: float [0,1], time: float}`。`confidence` 随时间衰减，低于阈值时条目被移除。

### 4.9 快照的审计要求 **[共用]**

`snapshot()` 暴露的每个状态量 **MUST** 出现在 §6.3 的 delta 覆盖范围内，或明确声明为纯输出量。驱动动力学的量（如 `arousal_recent`）**MUST NOT** 是不可观测的隐藏变量——否则审计链断裂。

---

## 5. 引擎入口（Normative）

符合规范的实现 **MUST** 暴露：

| 方法 | 签名 | 行为 |
|---|---|---|
| `process_vector` | `(vector, raw_intensity=1.0, event_id="")` | 施加内感受向量；改变状态；追加审计记录 |
| `process_event` | `(event, intensity=1.0)` | 经人格层映射后转 `process_vector` |
| `idle` | `(seconds)` | 推进 `seconds` 秒无外部刺激的时间 |
| `sleep` | `(hours)` | 睡眠债清除、梦境情绪加工、恐惧消退、能量恢复、醒来重置 |
| `expect` | `(event_id, valence, confidence=0.5)` | 登记未来事件预期 |
| `induce_dissonance` | `(magnitude, belief_domain="")` | 注入信念-行为冲突 |
| `snapshot` | `() -> Dict` | 返回 §4 定义的完整状态 |
| `set_clock` | `(t: Optional[float])` | 注入虚拟时间；传 `None` 恢复墙钟 |
| `advance_clock` | `(dt)` | 虚拟时钟前推 `dt` 秒 |

**时间边界**：单步时间 **MUST** 以 86400 秒（24 h）封顶。

> **`idle` 与 `sleep` 在参考实现中不产生审计记录。** 调用方若需要完整轨迹 **MUST** 自行记录；实现 **SHOULD** 记录它们。

---

## 6. 审计契约（Normative）

### 6.1 记录信封 **[共用]**

每条审计记录是一行 JSON（JSONL）。信封 **MUST** 包含：

| 字段 | 类型 | 语义 |
|---|---|---|
| `seq` | int | 会话内单调序号 |
| `ts` | string | ISO 8601 毫秒精度时间戳 |
| `engine` | string | 引擎版本标签；主引擎 `"SPL-V8.0"` |
| `session` | string | 会话标识 |
| `event` | string | 事件类型（见 §6.2） |
| `input` | object | 已净化的输入参数 |
| `snapshot` | object | 状态摘要（§6.4 的键集） |
| `delta` | object | 状态转移归因（见 §6.3） |

### 6.2 事件类型 **[共用]**

| `event` 值 | 触发 |
|---|---|
| `process_vector` | 每次向量施加 |
| `sleep` | 一次 `sleep()` |
| `expect` | 一次 `expect()` |
| `induce_dissonance` | 一次 `induce_dissonance()` |
| `llm_call` | 一次语言模型调用（见 §6.5） |
| `llm_usage_recorded` | 一次 token 用量登记 |

### 6.3 状态转移归因 `delta`（规范性算法）**[共用]**

`delta` 由 `AuditLogger.snapshot_delta(before, after)` 计算，**两个变体 MUST 使用同一算法**。

**步骤**

1. 对 `DELTA_SCALARS` 中每个键 `k`：取 `b = before[k]`、`a = after[k]`。若两者皆缺失则跳过。
2. 对 `DELTA_NESTED` 中每个子模型 `g`：若 `before[g]` 与 `after[g]` 都是字典，取两者键的并集，对每个键展开为点号路径 `"g.k"`，`b = before[g].get(k)`、`a = after[g].get(k)`。
3. 对每个候选 `(key, b, a)`：若 `b == a` 则跳过。
4. **数值条目**（两侧均为 int/float，且均非 bool）：`{"before": b, "after": a, "delta": round(a - b, 6)}`。
5. **非数值条目**：`{"before": b, "after": a}`，**MUST NOT** 附带 `delta` 键。

**布尔** **MUST NOT** 被视为数值。"新增一个危机标记"本身就是审计事件，尽管它没有算术差——实现 **MUST NOT** 为它伪造一个差值。

**覆盖集**

| | `DELTA_SCALARS` | `DELTA_NESTED` |
|---|---|---|
| **[主]**（14 项） | `self_esteem, energy, fatigue, excitation, max_trust, suppression_load, denial_load, rationalization_load, latent_pressure, cognitive_dissonance, sleep_debt, arousal_recent, memory_count, expected_count` | `fluid, mood, trauma` |
| **[未]**（10 项） | `self_esteem, energy, fatigue, excitation, max_trust, latent_pressure, cognitive_dissonance, sleep_debt, arousal_recent, memory_count, expected_count` | `fluid, mood, protective` |

两者的 `DELTA_SCALARS` 差异反映变体裁剪（见 §4.6），**MUST NOT** 为消除差异而强行对齐。

### 6.4 快照摘要 **[共用]**

审计记录的 `snapshot` 字段是完整状态的**子集**，键集为：

**[主]**（17 键）：`fluid, mood, self_esteem, energy, fatigue, excitation, max_trust, suppression_load, denial_load, rationalization_load, latent_pressure, cognitive_dissonance, sleep_debt, arousal_recent, trauma, memory_count, expected_count`

**[未]**（14 键）：`fluid, mood, self_esteem, energy, fatigue, excitation, max_trust, latent_pressure, cognitive_dissonance, sleep_debt, arousal_recent, memory_count, expected_count, protective`

### 6.5 LLM 调用记录 **[共用]**

`llm_call` 记录 **MUST** 额外包含：

| 字段 | 类型 | 语义 |
|---|---|---|
| `model` | string | 模型标识 |
| `prompt_preview` | string | prompt 前 200 字符 |
| `success` | bool | 生成是否成功 |
| `duration_ms` | float | 调用墙钟耗时 |
| `usage` | object \| null | token 用量，不可用时为 `null` |
| `error` | string \| null | 错误信息，成功时为 `null` |

`usage` 在非 null 时 **MUST** 含 `prompt_tokens` / `completion_tokens` / `total_tokens`（整数）。

### 6.6 失败策略 **[共用]**

审计写入 **MUST NOT** 改变核心状态演化。写入失败时引擎 **MUST** 静默继续，并 **MAY** 在下一条记录时重试。符合规范的实现 **MUST** 以相同方式记录其失败策略。

---

## 7. 确定性前提（Normative）

### 7.1 确定性条件 **[共用]**

符合规范的实现 **MUST** 在下列输入相同时给出相同状态：

```
(vector 序列, intensity 序列, event_id 序列, 初始状态, 时钟调度)
```

核心 **MUST NOT** 含随机性，**MUST NOT** 含 LLM 调用。所有随机性 **MUST** 位于可替换的人格层或语言层。

### 7.2 心境动力学形式 **[共用]**

心境 **MUST** 实现为**受迫-阻尼系统**，**MUST NOT** 使用"每次调用走固定步长"的实现。

> **步长一致性**：实现 **MUST NOT** 声称"步长无关"。受迫-阻尼离散化存在不可归零残差；断言容差须包含该残差界。

### 7.3 时钟注入前提 **[共用]**

一切重放断言 **MUST** 先注入虚拟时钟（`set_clock`）；未注入时钟时，实现 **MUST NOT** 声称可复现。

> **已知陷阱**：注入时钟后须同步 `last_time`，否则首次时间推进会因负 `dt` 直接早退——"墙钟到合成原点"的间隔不被结算。任何对外声称的"可复现"**MUST** 附带这一前提。

---

## 8. 一致性级别

| 级别 | 要求 | 可声称 |
|---|---|---|
| **L0 — 接口一致** | 实现 §3 输入契约与 §5 引擎入口 | "AAE interface compatible" |
| **L1 — 状态一致** | L0 + 快照键集与区间满足 §4 | "AAE state compatible" |
| **L2 — 审计一致** | L1 + delta 算法满足 §6.3，审计链可跨机复算 | "AAE conformant" |

> 一致性**不**包含正确性。见 §9.2。

---

## 9. 验证与边界

### 9.1 验证入口

第三方核验方法见 [`../verify/TESTING-zh.md`](../verify/TESTING-zh.md)。

### 9.2 基线的性质

一致性测试的基线与被验收对象**同源**。因此：

- 套件证明的是"**行为没有漂移、契约被满足**"，是变更检测器；
- **不证明"心理学结论正确"** —— 后者需要外部裁决；
- 由作者编写的断言**不构成独立第三方证据**。真正的验收证据来自评估方自行设计的测试。

---

## 10. 版本与兼容性

- 顶层快照键集的增删 **MUST** 提升主版本号；
- 区间收窄 **MUST** 提升主版本号；
- 新增可选字段 / 新增事件词汇 **MAY** 在次版本号内引入。

---

## 11. 许可与联系

- 本规范文本可自由引用，须注明出处。
- 本规范**不授予**对任何实现的许可。引擎内核属授权交付物。
- 国际 / 全球：[ai@nohnlins.com](mailto:ai@nohnlins.com)　·　中国：[lin@secondai.top](mailto:lin@secondai.top)

*Copyright © NOHN AI TECHNOLOGY PTE. LTD.*
