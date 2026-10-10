# Second-Perspective（GCAE）规范（Specification）

> **文档信息**：版本 1.x（随 `SPE_VERSION` 演化）｜状态：已通过 IMDA AI Verify 评估（总分 95）｜编制：NOHN AI
> **编制依据**：README-zh / ARCHITECTURE / TESTING-zh / GLOSSARY / 语言标准 2026.1–2026.3
>
> 本规范描述 **GCAE 全局认知审计引擎** 的公开规范面：十算子流水线、决策结构语言、状态与信号、不变式与收敛语义。引擎内核为单文件实现（6496 行，无 `plugins/` 包），核心逻辑属保密交付物。

## 1. 范围与定位

### 1.1 定位

中立的、核心离线的、与决策无关的认知偏差审计引擎：为 AI 系统与企业决策提供**第三方结构审计**，不提供建议、排名或评分。

### 1.2 不是什么

- 不检测"偏见"：无统计公平性检验、无群体差异度量、无训练数据审计；
- 不让模型不出错；不做医学 / 法律 / 金融 / 安全专业判断；不管运行时安全；
- 不让无解变有解；`AWAITING_HUMAN` 是常态，引擎永不自行生成修正。

## 2. 术语与定义

| 术语 | 定义 |
|---|---|
| GCAE | Global Cognitive Audit Engine，全局认知审计引擎 |
| 十算子 | ⊙GA→⊗NS→⊕IAP→⊿LCH→⊞LFT→BFC→⚙CCS→⇄GRF→META→⊚ACC，顺序由 `PIPELINE_ORDER` 唯一定义 |
| BFC | Binary Fact Check，二元事实校验，**无第三真值** |
| META | 元因果账本：混沌 / 无极 / 虚幻 / 天道 / 轮回 五条元基 |
| `.spd` | 决策结构语言（`decision.ebnf`，ISO/IEC 14977） |
| `.tpg` | 拓扑语言（`topology.ebnf`，语法扩展 2026.3） |
| ΔD | 决策可观测指标变化；因果语义 `¬A ⇒ ΔD` |
| 审计证书 | SHA-256 哈希链，跨机可复算 |

## 3. 核心规范

### 3.1 算子流水线

- 十算子按 `PIPELINE_ORDER` 顺序执行；无语义拓扑底座四类并行校验（□ / → / ⦿ / △ / ◇）。
- 编排语义：
  - `reconstruct()`：线性覆盖；
  - `spiral()`：叠加螺旋，冻结已收敛子图；
  - `limit_reconstruct()`：无限收敛至 S∞ = S*；
  - `evolve()`：只提案，不自主。

### 3.2 扩展 API

- 唯一扩展入口 `register_operator()`，四道闸门：ASCII 名字且不与官方算子重名；权限层仅限 `T2_SIGNAL` / `T3_NARRATIVE`；`after` 必填；`_register()` 收口。
- `report['operator_manifest']` 与 `operator_set_hash` 参与哈希链。

### 3.3 决策结构语言

- `.spd`：决策结构语言（`decision.ebnf`，ISO/IEC 14977）；`.tpg`：拓扑语言（`topology.ebnf`，2026.3）。
- 校验器 `dsl.py`：子命令 `check / gen / codes`，20 条诊断码。
- 拓扑层诊断码 T101–T308：T303 因果悖论、T305 分叉、T307 序倒置、T308 序不可赋值。

### 3.4 状态与信号

- 决策上下文输入字段：origin / goal / resources / decision / assumptions / outcome / dependencies / branches / facts / observations / gray_levels / commit_ratio / feedback。
- 状态与信号：`BLOCKED`、`SKIPPED`、`VERDICT_UNDECLARED`、`AWAITING_HUMAN`、`EVIDENCE_VACUUM`、`ORIGIN_DRIFT`、`SUPERPOSITION_VIOLATION`、`BUDGET_EXHAUSTED`、`LIMIT_REACHED` / `FLAT_SPIRAL` / `NOT_MONOTONE`。

### 3.5 收敛语义

- 收敛秩 =（风险集规模, 是否有未决假设）字典序。
- 停机判据参数门槛：`limit_layers >= 2`、`plateau_layers >= 1`、`is_static` 固定 3 层。
- 收敛五状态 C-1..C-3 定义于 TESTING 文档（五态：真收敛 / 非收敛判定）。

### 3.6 不变式

- I-1..I-6：非猜测 / 原点不漂移 / 叠加不覆盖 / 时间不可剥离 / 进化不自主 / 度量不阻断。
- L-1..L-3：LLM 三层权限 T1（标注）/ T2（提案）/ T3（叙述），**永不裁决**。
- `AWAITING_HUMAN` 为常态；META 永不阻断；外部算子不得发 `BLOCKED`。

## 4. 边界与禁令

- `binary=None` 只表示未声明，绝非第三真值。
- 不给出修正、不重排备选、不翻转假设状态。
- LLM 增强默认关闭；启用须国内端点 + 脱敏 + 同意。

## 5. 审计与合规

- IMDA AI Verify 评估 95 分（因果审计赛道）。
- 可复现证书：同输入 + 同 nonce + 同 clock → 同链根，不依赖任何模型厂商。
- V3b WARN：证书不绑定原始输入，须主动声明覆盖范围。
- 哈希链事件类型 10 种（AUDIT / DELTA_APPLIED 等）；哈希输入含事件序号 idx，事件数量 / 顺序改变即失效。
- 洁净室声明：推定实质性衍生侵权。
- 测试方法学 v1.0：Wilson 95% CI、精确 McNemar、Cohen's κ ≥ 0.70、Hollow 率 > 20% → HALT。

## 6. 一致性声明

符合本规范的实现应满足：

1. 流水线顺序与 `PIPELINE_ORDER` 一致，十算子语义与 §3.1 一致；
2. `.spd` / `.tpg` 解析与 `dsl.py` 校验器输出一致（20 条诊断码）；
3. 全部 I-1..I-6 与 L-1..L-3 不变式成立；
4. 审计证书可跨机复算（同输入 → 同链根）。

## 7. 版本与变更

- `SPE_VERSION` 1.2.1；链根 `ca07e5e4…`（1.2.1 代际变更后生效，接替 1.2.0 的 `aece60f5…`）。
- 语言标准：2026.1（五算子）/ 2026.2（拓扑）/ 2026.3（元因果）。
- `CognitiveAuditEngine` 保留为别名（v1 兼容）。

## 8. 许可与参考

- 非开源双轨授权：个人非商业研究免费；政府 / 企业书面付费授权。
- 参考：README-zh / ARCHITECTURE / TESTING-zh / GLOSSARY / `language-standard/`（grammar、decision.ebnf、topology.ebnf、dsl.py、examples）。