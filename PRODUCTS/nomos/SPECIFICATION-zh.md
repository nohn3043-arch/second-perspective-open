# NOMOS 规范（Specification）

> **文档信息**：版本 v0.5.0（2026-10-07）｜状态：企业控制平面已交付｜编制：NOHN AI
> **编制依据**：README-zh / GLOSSARY / CHANGELOG / IMDA_AI_Verify_Causal_Audit_Report
>
> 本规范描述 **NOMOS 二阶因果决策框架** —— 带 LLM 护栏的可审计确定性决策内核的公开规范面：REST 接口、二阶因果语义、不变量、人工闸门与哈希链报告。引擎从不输出最终结论——结论由人签署。

## 1. 范围与定位

### 1.1 定位

嵌入现有 ERP / CRM / 风控 / 合规 / 投决 / HR 系统之后的**确定性决策内核**；将结构化评估、细粒度算法审计、声明式假设交互（二阶因果复合）、有界三层重建、反事实重选、压力测试、认知挑战、信息排序与人类治理统一为一份哈希链报告。

### 1.2 不是什么

- 不输出最终结论（结论由人签）；
- 引擎从不估计缺失的交互强度、权重、概率或责任方；
- LLM 永不裁决；认知扫描器不诊断人、不读取动机，不替代法律、医疗、金融或安全专业人士；
- 领域控制包仅观测，绝不篡改引擎结论。

## 2. 术语与定义

| 术语 | 定义 |
|---|---|
| 一阶失效 | 单一因素导致的失效 |
| 二阶交互 | 两因素组合效应：协同（conjunctive, Δ>0）/ 冗余（disjunctive, Δ<0）/ 退化（degenerate, Δ=0） |
| Δ 交互强度 | 必须由责任人**显式声明**，引擎绝不估计或学习 |
| 三层因果重建 | 有界形式化重建，带确定性收敛证明 |
| DeltaVar | 假设改写路径，三形式：`"A2"` / `"criteria.K1.weight"` / `"alternatives.S1.metrics.cost"` |
| LLM Gate | T1 标注 / T2 提案 / T3 叙述，永不裁决 |
| session_root_hash | 单次分析会话的哈希链根 |

## 3. 核心规范

### 3.1 REST 接口（v0.5）

| 端点 | 方法 | 说明 |
|---|---|---|
| `/health` | GET | 健康检查 |
| `/v1/auth/me` | GET | 当前主体 |
| `/v1/hub/analyze` | POST | 会话分析 |
| `/v1/hub/reports/{hub_run_id}` | GET | 会话报告 |
| `/v1/decisions/evaluate` | POST | 决策评估 |
| `/v1/decisions/{decision_id}` | GET | 决策详情 |
| `/v1/decisions/{decision_id}/approval` | POST | 人工批准闸门 |
| `/v1/decisions/{id}/history` | GET | 决策历史 |
| `/v1/metrics` | GET | 指标 |

### 3.2 鉴权与上下文

- 鉴权：`Authorization: Bearer <SP_API_KEY>`。
- 租户上下文：`X-Tenant-Id`（或 OIDC `tid`）。
- 响应头：`X-Nomos-Kms-Signature`、`X-Process-Time-Ms`。
- 环境变量：`SP_ENV`、`SP_API_KEY`、`SP_DATABASE_DSN`、`SP_OIDC_ISSUER`、`SP_AUTHZ_ENFORCE`、`SP_KMS_SECRET`、`SP_RATE_LIMIT`、`SP_PUBLIC_BASE_URL`。

### 3.3 二阶因果语义

- 交互声明：`DecisionRequest.interaction_declaration`（可选，默认 None，向后兼容）。未提供时与 v0.4 行为完全一致。
- 不变量 I-1..I-4：非臆测 / 阶数守恒 / 效应有界 / 单调。
- I-3 效应有界：累积交互效应 ≤ `amplification_ceiling` × Σ|一阶|；冗余（负向）交互不做下限钳制。
- 收敛五态：`FIXED_POINT` / `NO_GAIN` 为真收敛；`BUDGET_EXHAUSTED` / `DIVERGED` / `BLOCKED` 非收敛。`BUDGET_EXHAUSTED` 必须报告为非收敛（`is_true_convergence` 防误判）。

### 3.4 人工闸门

- `advance()` 恰好执行一轮后停在 `AWAITING_HUMAN`。
- T2 提案需显式人工批准方可生效；T3 叙述从决策图剥离；任何 LLM 输出不能翻转假设状态或备选方案排序。

### 3.5 审计与报告

- 哈希链算法审计 + 只追加 `DomainEvent` 事件流（`InMemoryEventStore` / `PostgresEventStore`）+ 只追加 `DecisionRecord`。
- KMS 分离式 HMAC-SHA256 签名（未配置前为透明 no-op）。
- 响应字段：`counterfactuals`、`algorithm_audit`、`algorithm_audit_root_hash`。

## 4. 边界与禁令

- LLM 永不裁决（三条栅栏：T2 人工批准 / T3 剥离 / 输出不得翻转状态与排序）。
- v0.5 新能力全部环境变量门控、默认关闭。
- 领域控制包只观测，不篡改引擎结论。
- 认知扫描器只挑战**结构性风险**。

## 5. 审计与合规

- IMDA AI Verify：95/100（因果审计赛道），审计报告 `IMDA_AI_Verify_Causal_Audit_Report.pdf`。
- 合规文档：PRC（上海合规说明、隐私政策 CN、数据处理协议 CN）；国际（EU AI Act、GDPR、新加坡 PDPA）；框架对齐（NIST AI RMF 1.0、ISO/IEC 42001:2023）。

## 6. 一致性声明

符合本规范的实现应满足：

1. 端点 / 鉴权 / 上下文语义与 §3.1–§3.2 一致；
2. 交互声明经 I-1..I-4 校验；未声明交互时行为等同于 v0.4；
3. 人工闸门语义：LLM 输出不得翻转任何状态或排序；
4. 哈希链报告可验证、事件流只追加。

## 7. 版本与变更

- v0.5.0（2026-10-07）：企业控制平面；v0.4.0（2026-09-22）：二阶因果框架；v0.3.0（2026-09-19）。
- 遵循 SemVer 与 Keep a Changelog；测试：402 项通过 0 失败（v0.4 发布时），现载 412 项通过。
- 生产加固待办（未捆绑）：共享限流存储、云 KMS 信封加密、文档级租户分区、多区域高可用、SLA 工具。

## 8. 许可与参考

- 非开源双轨授权：中国境内 → 上海霖铭均华科技有限公司 + 中国法律；境外 → NOHN AI TECHNOLOGY PTE. LTD. + 新加坡法律 + SIAC 仲裁。
- 参考：README-zh / GLOSSARY / CHANGELOG / `export_openapi.py`（OpenAPI schema 导出）。