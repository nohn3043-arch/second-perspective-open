# Anthropomorphic-Agent-Engine 规范（Specification）

> **文档信息**：版本 SPL Pure Core V8.0 ｜状态：内核稳定，未成年人保护变体合规推进中｜编制：NOHN AI
> **编制依据**：README-zh / GLOSSARY / `docs/agent-standard.md`（内感受向量契约 §4.1、§4.5）
>
> 本规范描述 **确定性拟人心理引擎** 的公开规范面：内感受向量契约、八维情绪流体、时钟与可复现性、未成年人保护变体。

## 1. 范围与定位

### 1.1 定位

构建于 SPL Pure Core V8.0 之上的**确定性拟人心理引擎**：将情绪、心境、记忆、创伤、信任、自尊、睡眠与预期建模为单内核（`SPL-anthropic-engine.py`）内的确定性连续状态子系统。**无 LLM、无随机性、完全可逐比特回放**（前提：注入虚拟时钟）。

### 1.2 核心设计目标

- 八维情绪流体：喜悦 / 愤怒 / 恐惧 / 信任 / 疏离 / 紧张 / 内疚 / 羞耻；
- V8.0 扩展：心境慢变量层、独立羞耻维度、自尊动力学、睡眠 / 梦境（REM 巩固 + 恐惧消退 + 睡眠债）、期望系统（希望 / 焦虑 / 失望）、认知失调、扩展防御机制；
- Token 计量（`TokenUsage` / `TokenStats`，JSON 导出）+ `AuditLogger` 自动记录每次 LLM 调用。

## 2. 术语与定义

| 术语 | 定义 |
|---|---|
| SPL 纯内核 | 无随机、可回放的确定性内核 |
| 内感受向量 | 引擎的输入契约向量（见 `docs/agent-standard.md` §4.1） |
| 虚拟时钟 | 可复现性前提；未注入则回退 `time.time()` |
| 创伤再巩固 | 创伤记忆的随迭代减弱机制 |
| 信任上限侵蚀 | 信任维度的负向钳制 |
| L0–L3 | 未成年人保护四层防护 |

## 3. 核心规范

### 3.1 内核接口

- 核心文件是库，无 `__main__`，须 `importlib` 加载。
- `SPLPureCoreV7_3().process_vector({...}, time)`：状态推进；
- `core.snapshot()`：状态快照；
- `core.set_clock(t)`：虚拟时钟注入；
- `NarrativeMapper.map_event("insult", intensity=1.0)`：事件映射；
- 内感受向量契约：见 `docs/agent-standard.md` §4.1。

### 3.2 可复现性

- **"完全可回放"仅在注入虚拟时钟后成立**；不注入则回退 `time.time()`。
- 任何可复现性声称须声明此前提；`tests/` S1–S4 断言含反向测试（自然时钟下不可复现为预期行为）。

### 3.3 未成年人保护变体

- 机制级风险削减 + 四层保护 L0–L3，零第三方依赖：
  - L0 年龄核验 + 监护人同意；
  - L1 输入把关（红线关键词库 → `gate_crisis`）；
  - L2 引擎缓解；
  - L3 危机信号（`protective.risk_level == HIGH` → 关怀话术 + 监护人通知 + webhook + 转介统计）。
- API（默认 `http://localhost:8788`）：`/api/chat`、`/api/consent`、`/api/guardian/register`、`/api/guardian/block`、`/api/state`、`/api/export`、`/api/delete`、`/api/logout`、`/api/terms`、`/api/referrals`、`/api/complain`。
- 环境变量：`SPL_MINOR_CRISIS_HOTLINE`（默认 12356）、`AI_DISCLOSE_INTERVAL`（默认 3600）。
- 与主引擎差异：创伤移除、羞耻侵蚀增益 ×0.4（阈值提至 0.7）、负向钳制 0.75、依恋 / 信任上限 0.8、自尊下限 0.15、人格排除亲密 / 对抗类。

## 4. 边界与禁令

- `feature-guide/` 扩展模块（Goal / Identity / bias / value / world）未接入内核；其 `tension_base` 键不在内感受向量契约内（规范 §4.5）。
- 未成年人变体年龄 / 监护人同意为自述 + 声明，不含权威核验。
- 生产部署前置义务：法律审查、DPIA / 安全评估 / 算法备案、接入真实监护人通知与危机资源。

## 5. 审计与合规

- 运行期审计日志：`logs/` JSONL（.gitignore）。
- 未成年人合规能力清单按条款 / 法域映射：COPPA、EU Measures Art. 8–21、GDPR Art. 17、CA SB 243 等。
- IMDA AI Verify 因果审计报告：`IMDA_AI_Verify_Causal_Audit_Report.pdf`（仓库根）。
- 双轨授权：个人非商业免费；政府 / 企业付费；评估用途 60 日例外（LICENSE 1.3 条）。

## 6. 一致性声明

符合本规范的实现应满足：

1. 内感受向量契约与 `docs/agent-standard.md` §4.1 一致；
2. 虚拟时钟注入即可逐比特回放；未注入则明确回退语义；
3. 未成年人变体四层保护 L0–L3 与差异参数（§3.3）一致；
4. 审计日志只追加、可回溯。

## 7. 版本与变更

- SPL Pure Core V8.0（类名 `SPLPureCoreV7_3`）。
- PyPI 包 `spl-agent-engine`：最新 0.4.0（2026-09-02），不跟随仓库源码；0.4.1 未上传。
- 在线演示：www.nohnlins.com/your-soulmate/。

## 8. 许可与参考

- 非开源双轨授权：个人非商业研究免费；政府 / 企业书面付费授权。
- 参考：README-zh / GLOSSARY / `docs/agent-standard.md` / LICENSE（1.3 条评估例外）。