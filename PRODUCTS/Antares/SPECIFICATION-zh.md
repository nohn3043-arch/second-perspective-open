# Antares — GFSIP v1.0 规范（Specification）

> **文档信息**：版本 v1.0（接口冻结，2026-07-16）｜状态：实现就绪候选规范｜编制：NOHN AI
> **编制依据**：`GFSIP_v1.0_protocol_spec.md`（33 节，全文权威）、CONFORMANCE-zh、README-zh / GLOSSARY
>
> 本文件是 **GFSIP（Global Federated Stable Interoperability Protocol，全局联邦稳定互操作协议）v1.0** 的规范索引与一致性声明入口。**规范正文以 `GFSIP_v1.0_protocol_spec.md` 为准**；机器可读工件（JSON Schema/注册表/检查表）与规范正文冲突时，以规范正文为准。

## 1. 范围与定位

### 1.1 定位

为服务、AI 智能体、设备与组织提供**加密、多路复用、可恢复的跨域通信**，无需中心权威。以 QUIC 为强制传输层 + 确定性 CBOR 序列化，内置会话恢复、幂等去重与可选因果审计。

### 1.2 目标（八条，§1）

1. 加密双向认证 Session；
2. 多 Channel 隔离复用；
3. 断网恢复；
4. 窗口去重；
5. 结构化错误；
6. 可选签名因果事件；
7. 多信任根跨域互操作；
8. 单域故障隔离。

### 1.3 不是（§2 明列）

- 不替代 IP / BGP / DNS / QUIC / TLS；
- 不提供全球唯一控制权；不承诺零故障；不提供无物理路径通信；
- 不提供无限时间的 Exactly Once；不自动确定法律责任；
- **不把时间先后自动解释为因果关系**；
- 不要求全球唯一身份根或目录。

## 2. 术语与定义

| 术语 | 定义 |
|---|---|
| GFSIP | 全局联邦稳定互操作协议 |
| 44 字节定长头 | 线格式帧头：Magic "GFS1" / Major=1 / Minor=0 / Type / Flags / Header Length / Reserved / Payload Length / Session ID 128 位 / Sequence 64 位 / Channel ID 32 位 |
| 确定性 CBOR | 大端、最短编码、拒绝重复 Map 键、无限长串禁止 |
| 因果前驱 | 时间更早 / 网络先到 / Trace ID 相同均**不自动**构成父事件 |
| DomainDescriptor | 域描述符，联邦加入凭据 |
| 信任锚 | 跨域互操作的信任根集合 |
| 档位 | Core/1（强制）、Audit/1（可选）、Federation/1（可选） |

## 3. 核心规范

### 3.1 传输与承载

- 强制：QUIC，ALPN `gfsip/1`；可选：TCP + TLS 1.3。
- 跨主机明文承载：**MUST NOT**。
- `frame_length = 44 + header_length + payload_length`。

### 3.2 消息与标志

- 18 种标准消息类型 `0x01`–`0x16`（CLIENT_HELLO … STATE_SYNC）；`0x17–0x7F` 保留；`0x80–0xFF` 私有实验。
- Flags 8 位：`ACK_REQUIRED / AUDIT_PRESENT / END_CHANNEL / IDEMPOTENT / COMPRESSED / EARLY_DATA`。
- 错误注册表 `gfsip-error-registry.json`：35 个数值错误码（code 为线路稳定标识，name 仅诊断）。
- 消息 Schema：`gfsip-state-machine.json` / `gfsip-message-schema.json`。

### 3.3 会话状态机

- 8 状态：`NEW → NEGOTIATING → AUTHENTICATING → ESTABLISHED → DEGRADED → RESUMING → DRAINING → CLOSED`，附 9 条强制不变量。
- 0-RTT 只允许 `PING` 与只读查询；禁止 0-RTT 副作用（`EARLY_DATA_REJECTED`）。

### 3.4 Channel 规则

- Initiator 奇数 / Responder 偶数；0 为控制通道；不复用。
- 默认资源限制（含最大协商值）：max_header 32KiB / max_frame 1MiB / max_channels 128 / max_inflight 64 / max_parent_events 8 / unauthenticated_lifetime 10s / descriptor_size 64KiB / route_max_hops 8。

### 3.5 认证与压缩

- 认证方法：`mtls` / `signed-token` / `psk`（仅封闭域）/ `hardware-attested`。
- 压缩：`none` 强制，`zstd` 可选。

## 4. 边界与禁令

- 签名只证明密钥签署了字节表示，不证明现实事件真实；
- EVENT 默认不记录 Payload 原文；
- Gateway 不得读取端到端加密业务载荷；
- 日志不得记录恢复令牌 / 凭据 / 私钥；
- 共享凭据只能锚定到凭据，不能锚定自然人；恢复不得提升权限。

## 5. 审计与合规

- Audit/1：签名 EVENT（actor / rule_version / state_before / after_hash / logical_clock）；拒绝自环与已知环；默认最大父事件数 8；缺失父事件标 `unresolved`。
- §27 一致性声明：宣称 `Core Conformant` 的 6 条硬性要求（固定帧头 / 确定性 CBOR / QUIC + gfsip/1 / 通过全部 Core Mandatory 测试 / 发布版本与测试报告 / 无已知未修复 Critical 安全问题）；Audit/1 与 Federation/1 须独立声明。
- §28 九个最小测试向量（下限非度量）。
- `gfsip-conformance-checklist.csv`：34 条全部 Mandatory（Core 24：CORE-001…024 + FED 6 + AUDIT 4）。
- §30 责任闭环：9 类决策的最小责任单元（协议目标 / 线格式 / 状态机 / 安全配置 / 默认限制 / 参考实现 / 安全结论 / 一致性结论 / 发布）；无法区分时输出"责任模糊区"声明。
- §29 SPL 映射：E1→E2 状态转换、Guard+Action、Hᵢ 前置条件、ΔD 可观测指标变化。

## 6. 一致性声明（Summary）

完整一致性要求见 `gfsip-conformance-checklist.csv`（34 项 Mandatory）。参考实现 Python `reference-impl/gfsip`：9/9 一致性通过（作者自测 2026-10-08，Python 3.13.14 / Windows）。独立第二实现进行中；公开互操作报告与生产试点域为待办。

## 7. 版本与变更

- v1.0 接口冻结（2026-07-16）；v1.0 冻结项 9 条（§31，含 44 字节帧头、Channel 奇偶规则、0x01–0x16 语义等），改动必须升 Major。
- 已知限制 10 条（§32）；实施顺序 12 步（§33）。

## 8. 许可与参考

- **开放许可**（区别于生态内其他项目）：代码 Apache-2.0；规范文档 CC BY 4.0；v1.0（含）以前版本整体已以 CC BY 4.0 发布、不可撤销。
- PyPI 包：`gfsip`。
- 参考：`GFSIP_v1.0_protocol_spec.md`（权威）、`gfsip-error-registry.json`、`gfsip-state-machine.json`、`gfsip-message-schema.json`、`gfsip-conformance-checklist.csv`。