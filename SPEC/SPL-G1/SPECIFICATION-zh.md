# SPL-G1 规范（Specification）

> **文档信息**：版本 v1.0（公开规范）｜状态：Phase A 已交付，规范随实现演化｜编制：NOHN AI
> **编制依据**：`SPL-Core.json`（ISA v1.0.0-Commercial：SPL-TCU-G1）、`State_Anchor.pdl`、`Materica-specification`、README-zh、IMPROVEMENT_PLAN v5.1
>
> 本规范描述 SPL-G1 **硬件因果审计可信计算单元（TCU）** 的公开规范面：指令集、数据结构、仲裁协议、审计语义与熔断行为。核心引擎 RTL 与工艺库实现属保密交付物，不在本规范范围内公开。
> 英文版本：[`SPECIFICATION.md`](./SPECIFICATION.md)

## 1. 范围与定位

### 1.1 是什么 / 不是什么

| ✅ 是 | ❌ 不是 |
|---|---|
| 硬件因果审计可信计算单元（TCU） | 运行 Linux / x86 应用的桌面 CPU |
| 具备全生命周期 P→Q 可追溯性的可验证计算原语 | 拥有数千核心与 CUDA 生态的 GPU |
| 三模 PIM 阵列（SCALAR / VECTOR / MATRIX），每次操作皆可审计 | 用于 LLM 推理的数据中心级 NPU 加速器 |
| 面向合规计算、安全攸关审计与证明类负载的嵌入式安全根 | 任何主流微处理器的替代品 |

### 1.2 适用范围

适用于需要硬件级因果审计的安全场景：工业安全审计节点、合规计算、供应链追溯、可证明计算负载。两年内不流片，设计交付物为 M4 综合评估报告及配套工具链。

## 2. 术语与定义

| 术语 | 定义 |
|---|---|
| TCU | Trusted Compute Unit，可信计算单元 |
| PIM | Processing-In-Memory，存内计算 |
| P→Q 因果对 | 每一次操作输出的可审计因果对：前置条件 P 成立、后置 Q 由 P 推出 |
| RA-BUS | 统一寻址总线，四目标：PIM / Audit / Identity / External |
| dep_mask | 56 位依赖掩码，刻画指令间依赖关系 |
| 级联失效 | 依赖链上任何节点审计失败引起下游级联失效 |
| SBC 熔断 | Self-Breaking Circuit，不可逆熔丝；审计失败即熔断、输出永久归零 |
| Materica #4 | 材料因果映射规范第四条：审计失败 → 熔丝熔断 → 输出归零 |
| 身份锚 | 256 位硬件身份，64 周期逐位握手验证 |

## 3. 核心规范

### 3.1 指令集（ISA）

- 权威定义：`SPL-Core.json`，v1.0.0-Commercial，处理器模型 `SPL-TCU-G1`。
- 受限 C 子集经 `splcc` v0.1 编译为微码 CONFIG 字（`int` 变量、`for` / `while` / `if-else`、算术、比较）。
- 序列器 v4：256 项程序存储器；控制流指令 `JMP / JZ / JNZ / CALL / RET / HALT`；8 级返回栈；越界保护。

### 3.2 计算阵列

- 2D PIM 阵列：4×4 网格（规模阶梯 L0），可扩展至 L1（16×16=256 单元）、L3（262144 单元）。
- Cell v2：64 位本地存储 + 32 操作数 ALU；8 位相邻互连；逐列 `vec_sum`；全阵列 `mat_total` 归约。
- 三种执行模式：`SCALAR / VECTOR / MATRIX`。
- 真 FP16（IEEE 754 半精度）：符号 / 5 位指数 / 10 位尾数；次正规数、NaN、±Inf；舍入 `roundTiesToEven`；语义 `FP16_ADD / SUB / MUL / CMP / MAC`。

### 3.3 RA-BUS 仲裁协议

- v1：4 目标地址译码总线（PIM / Audit / Identity / External）。
- 事务类型：`READ / WRITE / EXECUTE / CONFIG`。
- 审计约束掩码 64 位 CONFIG 可编程：bit0 整数 ALU / bit1 FP16 / bit2 VECTOR / bit3 MATRIX；默认全 1（bridge 直通模式，向后兼容）。

### 3.4 身份与熔断

- 身份锚 v1：256 位硬件身份，64 周期逐位握手。
- SBC 熔断：审计失败 → `fuse_blown` 闩锁 → `ra_rdata` 强制清零 → 输出永久归零；仅硬件复位 `rst_n` 可恢复。
- 审计是硬件属性而非软件功能：直通桥接模式下 `constraint_bits` 全 1 → 恒通过。

### 3.5 因果约束校验

- `spl_cim_causal_unit`（v2）硬约束校验：
  `constraint_pass = (constraint_bits == 64'hFFFF_FFFF_FFFF_FFFF)`
- 56 位 `dep_mask` 依赖校验，含级联失败传播。

### 3.6 材料与工艺（PDK）

- PDK 数值为文献校准参考值，流片前须由晶圆厂 PDK 替换。
- 三套 PDK 包：`silicon_cim_v1.json`（28nm CIM，3 变体）、`optical_mzi_photonics_v1.json`（光子，3 变体）、`rram_crossbar_v1.json`（RRAM，3 变体）。

## 4. 边界与禁令

- 不替代通用微处理器；不提供软件堆栈兼容性。
- 两年内不流片；交付物止于 M4 综合评估。
- 熔断后输出不可恢复（除硬件复位），设计方不得提供绕过路径。

## 5. 审计与合规

- 审计失败 → SBC 熔断 → PIM 输出切断；审计通道与身份通道仍可读（如 Test 9 闭环：禁 FP16 → 执行 FP16_ADD → audit reject → `fuse_blown=1`）。
- Attestation：支持远程证明。
- RTL 仿真基线：Icarus Verilog，Phase-A 全套 0 errors，7/7 tests PASS。
- 工具链：EDA（解析 → 映射 → 导出 → RTL 生成，含 SVA 断言与 TCL 综合脚本）。

## 6. 一致性声明

符合本规范的实现应满足：

1. 实现 `SPL-Core.json` 定义的 SPL-TCU-G1 指令集与 `State_Anchor.pdl` 身份锚协议；
2. RA-BUS 四目标寻址与四类事务行为一致；
3. 因果约束校验、级联失效与 SBC 熔断语义与 §3.4/§3.5 一致；
4. 通过 Phase-A 对应测试用例（A1 控制流 / A2 真 FP16 / A3 splcc / A4 数据通道 / A5 因果约束 / A6 SBC 熔断）。

## 7. 版本与变更

- Phase A 能力里程碑全部完成；IMPROVEMENT_PLAN v5.1（2026-08-25）；EDA 工具链 v1.1。
- 里程碑：M1 基线 → M2 splcc → M3 16×16 Tile → M4 Yosys 综合评估（L1 级 16×16=256 单元 32 算子工业审计流水线全 mapped，delay=22.7ns）。

## 8. 许可与参考

- 双轨授权（非开源）：个人非商业研究免费；政府 / 企业须书面付费授权；已申请专利（PCT）。
- 参考：README-zh / GLOSSARY / IMPROVEMENT_PLAN / `SPL-Core.json` / `State_Anchor.pdl` / `Materica-specification`。