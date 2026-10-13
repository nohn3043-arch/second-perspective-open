# Second-Reality（SPL-Virtual-World-Base）规范（Specification）

> **文档信息**：版本 1.x｜状态：可运行基础设施，地理分布式为 horizon-2｜编制：NOHN AI
> **编制依据**：README-zh / GLOSSARY / `system/protocol.py`（JSON-Schema）/ 真实基线标准 V3.0 / 身份标准 V2.2 / 原始框架规范
>
> 本规范描述 **虚拟世界与元宇宙基础设施基座** 的公开规范面："宪法—法律—桥"三级栈、真实性基准、账户分层、共识与审计语义。
> 英文版本：[`SPECIFICATION.md`](./SPECIFICATION.md)

## 1. 范围与定位

### 1.1 定位

端到端账户与世界运行时：哈希链账本、≥2/3 公投共识、需求驱动智能体、无头 tick 循环、REST + WebSocket API；第二视角认知审计器作为中立裁判；AR / 边缘接入；规则创世锁定为只读信任根。

### 1.2 设计边界

- 结构性真实而非数值真实；
- 真随机被禁止：创世种子为公开整数，同种子 → 同世界；
- 虚幻只允许存在于表征层，永不进入执行层；
- 轮回实现为"守恒律 + 链式因果闭合"，**绝不**实现为环（否则 `trace_chain(depth=-1)` 永不终止）。

## 2. 术语与定义

| 术语 | 定义 |
|---|---|
| 宪法与创世锁定 | 创世规则只读，任何人可重跑复验 |
| Reality Baseline R1–R5 | 真实性基准：创世锁定 / 全域一致 / 因果闭合 / 公示即执行 / 反应表完备 |
| 灵魂哈希 | 个体身份哈希（长度恒定，见 `NOHN_LAW_AXIOMS`） |
| 公投共识 | ≥2/3 超级多数 |
| 原始框架六条 | 第负一章的六条原始法则（规格见第五份标准） |
| M1 入章纪律 | 法律入章四要件：生产者 / 消费者 / 复算式 / 边界条款 |
| 守恒残差 | 经济与能量守恒的残差度量 |

## 3. 核心规范

### 3.1 REST / WebSocket 接口

`GET /health`、`GET /world`、`POST /world/tick`、`GET /world/snapshot`、`GET /audit`、`GET /audit/full`、`POST /agent/spawn`、`POST /protocol/validate`、`/auth/*`、`/credentials/*`、`/aa/*`、`/keys/*`、`POST /identity/root/generate`、`/roaming/*`、`/recovery/*`、`/economy/*`、`/ws/world`。

### 3.2 存储与后端

- STORAGE 四后端：`sqlite / memory / redis / postgres`。
- 环境：Python ≥ 3.8，仅依赖 `cryptography`（Ed25519）。

### 3.3 真实性基准（入驻门禁，强制）

R1 创世锁定 / R2 全域一致 / R3 因果闭合 / R4 公示即执行 / R5 反应表完备 —— 由 `ProtocolValidator` 入驻校验。

### 3.4 账户分层（五层 L0–L4）

- L0 身份根 → L1 凭据 → L2 会话 → L3 分级授权 → L4 社交恢复（3-of-5 + 7 天可取消时间锁）。
- 私钥永不离开设备；账本只存公钥与哈希。

### 3.5 法律与常量

- `NOHN_LAW_AXIOMS` 为共享常量唯一权威来源：重力、时间膨胀、单位尺度、灵魂哈希长度、预言机最小信源数、创世熵种子长度、守恒容差。
- 法律标准五份：通信 / 经济 / 身份（V2.2 凭据恢复）/ 真实性基准（V3.0）/ 原始框架规范；机器可读 JSON-Schema 在 `system/protocol.py`。

### 3.6 经济与共识

- 周期性经济：UBI 每 10 tick、财富税每 30 tick、通胀每 50 tick、财富硬顶。
- 共识：≥2/3 超级多数公投。

### 3.7 地理分布（horizon-2）

- HLC（混合逻辑时钟）、空间分片、AOI 增量同步、Merkle 差异合并、分层共识（真实 TCP）。

## 4. 边界与禁令

- 原始数据（灵魂 / 资产 / 记忆 / 世界状态）永不离开数据中心；协议层仅交换可验证证明。
- 真随机被禁止；轮回不得实现为环；虚幻不得进入执行层。
- 桥只做：语义清洗 / 物理常数核验 / 身份核验。
- 已披露生产加固缺口：`/keys/rotate` 与 `/keys/revoke` 无角色模型、集群 TCP 无 TLS 无节点认证、默认 KMS 为文件后端、API 信任 `X-Forwarded-For` —— 生产部署前须加固。

## 5. 审计与合规

- 第二视角认知审计：合规审查维度按 README/GLOSSARY 为 24 维 + NOMOS 第 25 维二阶因果审计（架构图表述为 19 维，文档间存在差异，规范以 README/GLOSSARY 表述为准，须在实现中消歧）。
- 认证安全维度在隔离内存世界中功能性执行而非探测属性。
- `expert_report.py`：将审计裁定与哈希锚点导出为可重跑报告。

## 6. 一致性声明

符合本规范的实现应满足：

1. 通过 `reality_smoke`（40 项）与 `frames_smoke`（56 项）验证；
2. 入驻强制执行 R1–R5 真实性基准；
3. 账户分层与身份 / 凭据 / 恢复语义与 §3.4 一致；
4. `NOHN_LAW_AXIOMS` 常量唯一权威、不可分叉。

## 7. 版本与变更

- 真实基线标准 V3.0；身份标准含 V2.2 凭据恢复条款；原始框架规范为第五份标准。
- 地理分布式为 horizon-2 子系统。

## 8. 许可与参考

- 非开源双轨授权：个人非商业研究免费；政府 / 企业书面付费授权。
- 参考：README-zh / GLOSSARY / `system/protocol.py` / 五份法律标准。