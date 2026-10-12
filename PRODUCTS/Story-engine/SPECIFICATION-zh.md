# Story Engine 规范（Specification）

> **文档信息**：版本 v2.2（`engine_for_business.py`）｜状态：健壮性加固完成（2026-08）｜编制：NOHN AI
> **编制依据**：README-zh / GLOSSARY
>
> 本规范描述仓库内**两款产品**的公开规范面：面向创作者 / 大众的**长篇叙事一致性引擎**，与面向企业的**离线文档合规复核引擎**。
> 英文版本：[`SPECIFICATION.md`](./SPECIFICATION.md)

## 1. 范围与定位

### 1.1 叙事一致性引擎（Creator）

自动审计人物设定、因果时间线与记忆线（人设 / 时间线 / 记忆一致性），将直觉校对转化为结构化流程。

### 1.2 文档合规复核引擎（Business）

对合同、法规、公文、通用文本做条款级规则扫描与文档级审计，输出可追溯报告。**完全不依赖 LLM**：纯 JSON 规则库、零第三方依赖、离线运行。

## 2. 术语与定义

| 术语 | 定义 |
|---|---|
| Consistency audit | 一致性审计（人设 / 时间线 / 记忆） |
| ResponsibilityAccount | 责任闭环锚定：每条结论挂到具名责任节点（谁 / 角色 / 阶段） |
| CausalNode | 携带 `implicit_assumptions` 与 `vulnerability_score` 的因果节点 |
| OOC | Out Of Character，人设崩坏 |
| SPL 四阶段 | `STRIP_NARRATIVE → SCAN_ASSUMPTION → HEDGE_RISK → LOCK_RESPONSIBILITY` |
| RuleEngine / Hit=verdict | 规则引擎命中即裁定，无概率输出 |
| TraceLog | 全链路可追溯日志 |

## 3. 核心规范

### 3.1 叙事编辑流水线（SPL 四阶段）

- `STRIP_NARRATIVE`（剥离叙述）→ `SCAN_ASSUMPTION`（扫描假设）→ `HEDGE_RISK`（对冲风险）→ `LOCK_RESPONSIBILITY`（锁定责任）。
- 阶段由 `SPLStage` 枚举定义。

### 3.2 节点状态

- 节点状态五态：`RAW / STRIPPED / AUDITED / PRUNED / ACTIVE`。

### 3.3 合规复核引擎接口（CLI）

- `python -m compliance_engine audit --type contract --input … --output …`
- `python -m compliance_engine list-rules`
- `python -m compliance_engine demo`
- 规则库外部扩展：`--rules-dir <dir>`；规则库文件 `rules/*.json`，四类：`contract / regulation / official_doc / common`。

### 3.4 风险与报告

- 风险等级四档：`SAFE / WARNING / CRITICAL / FATAL`。
- 报告三格式：HTML / JSON / Markdown。
- 文档级审计四维度：要素完整性 / 一致性 / 权责对等 / 格式。

### 3.5 引擎隔离

- `_ENGINE_FINGERPRINT` + `check_engine_isolation()`：两个引擎混用同一进程立即告警，防止同名异质数据类互相覆盖。

### 3.6 LLM 后端

- 可替换 LLM 后端：`DeepSeekProvider` / `MockLLM`。

## 4. 边界与禁令

- 企业支线不依赖 LLM、离线运行、判定确定性（命中即裁定，无概率输出）。
- 人名提取"宁可缺失不要噪声"：排除代词 / 动词短语 / 天气场景词。
- 世界观提取按最长后缀匹配整词；连接词不被吞并。
- 修复含全量跳词修复与全文修订替换（生硬过渡词：突然 / 莫名 / 鬼使神差 等）。

## 5. 审计与合规

- 责任闭环锚定：每条结论可回溯到具名责任节点。
- TraceLog 全链路可追溯：每步判断可倒查原始依据。
- 文档级审计四维度 + 评分。

## 6. 一致性声明

符合本规范的实现应满足：

1. 四阶段流水线顺序与 `SPLStage` 语义一致；
2. 规则库格式与 `--rules-dir` 协议一致，命中即裁定；
3. 风险分级与报告格式（HTML / JSON / Markdown）一致；
4. 引擎隔离检测生效。

## 7. 版本与变更

- `engine_for_business.py` v2.2；健壮性加固修复（2026-08）。
- 命令入口：`Story Engine for Creator.py`、`engine for business.py`。

## 8. 许可与参考

- 非开源双轨授权：中国境内 → 上海霖铭均华科技有限公司；境外 → NOHN AI TECHNOLOGY PTE. LTD.，SIAC 仲裁。
- 参考：README-zh / GLOSSARY / `rules/`（四类规则库）。