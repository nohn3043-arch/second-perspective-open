<div align="center">

# 📖 术语表 · Glossary

**SPL-G1 · Trusted Compute Unit**

*每个词都用一句人话解释 · Every term explained in one plain sentence*

</div>

---

> 英文术语保留原样，方便你对照 README、RTL 代码与文档。
> The English term is kept as-is so you can match it against the README, the RTL source and the docs.

| 术语 Term | 中文 | 一句话人话 · Plain meaning |
|---|---|---|
| **TCU (Trusted Compute Unit)** | 可信计算单元 | 一颗专门做「可验证计算」的安全芯片——不是通用 CPU / GPU / NPU。 |
| **PIM (processing-in-memory)** | 存算一体 | 把计算直接做在存储阵列里，数据不必来回搬运，快且省电。 |
| **RA-BUS** | 统一寻址总线 | 芯片内部的一条总线，用同一个地址空间同时管计算、审计、身份与外部内存。 |
| **SCALAR / VECTOR / MATRIX** | 三种执行模式 | 标量、向量、矩阵三种粒度的计算模式。 |
| **Causal pair (P→Q)** | 因果对 | 每一步计算同时产出「前提 P」和「结论 Q」，事后可核验。 |
| **Causal constraint unit** | 因果约束单元 | 硬件层负责校验因果是否成立的模块。 |
| **dep_mask** | 依赖掩码 | 56 位，用来标记当前这次计算依赖了哪些上游结果。 |
| **Cascading failure** | 级联失效 | 上游一旦出错，下游全部连带判为失败。 |
| **SBC fuse** | 熔丝 | 审计失败即熔断，输出被永久清零——只有硬件复位能恢复。 |
| **Materica #4** | 材料因果映射第四条 | 规定「审计失败 → 熔丝熔断 → 输出归零」这条硬规则。 |
| **Identity anchor** | 身份锚 | 256 位硬件身份，握手时逐位核验。 |
| **FP16 (IEEE 754 half)** | 半精度浮点 | 真·16 位浮点：支持次正规数、NaN、±Inf，采用「四舍六入五成双」。 |
| **Sequencer** | 定序器 | 芯片里的「指令指针」：256 条程序存储 + 跳转 / 调用 / 返回。 |
| **splcc** | C 子集编译器 | 把一个受限的 C 语言子集，编译成芯片的微码 CONFIG 字。 |
| **RTL** | 寄存器传输级 | 芯片电路的 Verilog / SystemVerilog 描述，可以直接仿真验证。 |
| **Testbench** | 测试台 | 跑 RTL 仿真的验证程序（本例为 `tb_G1_Integrated.sv`）。 |
| **PDK** | 工艺设计套件 | 描述目标工艺的参数包：28nm CIM · 光子 · RRAM 三种。 |
| **EDA toolchain** | EDA 工具链 | 从因果设计 JSON → 网表 → 自动生成 RTL 的纯 Python 流水线。 |
| **Phase A** | A 阶段 | 芯片核心能力闭环完成的里程碑（A1 控制流 … A6 熔丝）。 |
| **Attestation** | 远程证明 | 让远端相信「这台设备确实运行在未被篡改的硬件之上」。 |

---

## ✦ English Glossary

*Every term explained in one plain sentence.*

| Term | Plain meaning |
|---|---|
| **TCU (Trusted Compute Unit)** | A security chip built for verifiable computation — not a general-purpose CPU, GPU or NPU. |
| **PIM (processing-in-memory)** | Compute happens inside the memory array, so data isn't shuttled back and forth — fast and power-efficient. |
| **RA-BUS** | One on-chip bus managing compute, audit, identity and external memory through a single address space. |
| **SCALAR / VECTOR / MATRIX** | The three execution granularities: scalar, vector and matrix. |
| **Causal pair (P→Q)** | Every computation emits both its premise P and its conclusion Q, so it can be checked afterwards. |
| **Causal constraint unit** | The hardware module that verifies whether causality actually holds. |
| **dep_mask** | A 56-bit mask marking which upstream results a computation depends on. |
| **Cascading failure** | If an upstream step fails, everything downstream is marked failed too. |
| **SBC fuse** | Audit failure blows the fuse and output is permanently zeroed — only a hardware reset recovers it. |
| **Materica #4** | The material-causality rule that hard-codes "audit failure → fuse blows → output zeroed". |
| **Identity anchor** | A 256-bit hardware identity, verified bit by bit during the handshake. |
| **FP16 (IEEE 754 half)** | True 16-bit floating point: supports subnormals, NaN and ±Inf, with round-half-to-even. |
| **Sequencer** | The chip's instruction pointer: 256 words of program storage plus jump, call and return. |
| **splcc** | A compiler for a restricted C subset that emits the chip's microcode CONFIG words. |
| **RTL** | The Verilog / SystemVerilog description of the circuit, ready for direct simulation. |
| **Testbench** | The verification program that drives RTL simulation (here `tb_G1_Integrated.sv`). |
| **PDK** | The parameter package describing a target process: 28nm CIM, photonic, or RRAM. |
| **EDA toolchain** | A pure-Python pipeline from causal-design JSON → netlist → auto-generated RTL. |
| **Phase A** | The milestone where the chip's core capability loop closed (A1 control flow … A6 fuse). |
| **Attestation** | Convincing a remote party that this device really runs on untampered hardware. |

---

<div align="center">

[← 返回 README](./README.md) &nbsp;·&nbsp; [中文说明](./README-zh.md)

<sub>NOHN AI · SPL-G1</sub>

</div>
