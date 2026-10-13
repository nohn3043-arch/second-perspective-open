# SPEC — 公开规范索引

> 本目录按**产品**分目录收纳公开规范：每个产品一个目录，一份 `SPECIFICATION.md`（英）与一份 `SPECIFICATION-zh.md`（中），两份内容一致。
>
> 规范描述的是**公开规范面**：定位与边界、接口 / 协议 / 格式、参数与配置、审计与合规、一致性声明、版本与变更。
>
> **实现源码不在本仓库。** 各产品的引擎内核属授权交付物，见下表「实现位置」一列。

## 一、索引

| 目录 | 产品 | 规范覆盖 | 实现位置 |
|---|---|---|---|
| [`language-standard/`](language-standard/) | 决策结构语言（Standard 2026.2） | EBNF 文法（`decision.ebnf` / `topology.ebnf`）、语法规范、示例 | 参照解释器 `dsl.py` **已在公开层**（规范的可执行定义） |
| [`second-perspective/`](second-perspective/) | 第二视角引擎（GCAE） | 十算子流水线、状态与信号、不变式、收敛语义 | 私有 · 授权交付 |
| [`nomos/`](nomos/) | NOMOS 智能决策中枢 | REST 接口、二阶因果语义、不变式 I‑1…I‑4、人类闸门、哈希链报告 | 私有 · 授权交付 |
| [`SPL-G1/`](SPL-G1/) | 硬件因果审计可信计算单元（TCU） | 指令集、数据结构、仲裁协议、审计语义、熔断行为 | 私有 · RTL 与工艺库不公开 |
| [`Antares/`](Antares/) | GFSIP v1.0 联邦稳定互操作协议 | 协议规范、一致性文档、规范层许可 | 协议规范公开 · 实现私有 |
| [`second-reality/`](second-reality/) | 虚拟世界基础设施基座 | 宪法 / 法律 / 桥三层结构 | 私有 · 授权交付 |
| [`Story-engine/`](Story-engine/) | 长篇叙事一致性引擎 | 一致性校验与文档合规复核的公开面 | 私有 · 授权交付 |
| [`Anthropomorphic-Agent-Engine/`](Anthropomorphic-Agent-Engine/) | 确定性拟人心理引擎 | SPL Pure Core V8.0 的公开面 | 私有 · 授权交付 |
| [`DMU/`](DMU/) | 直驱运动统一驱动系统 | 动力学仿真原型的公开面 | 私有 · 授权交付 |
| [`HuM/`](HuM/) | 人形驱动系统 | 含空气动力学的仿真原型公开面 | 私有 · 授权交付 |
| [`PAGES/`](PAGES/) | 生态官方落地页 | 视觉语言与页面结构规范 | 私有 · 授权交付 |
| [`ai-draw-cue-word-project/`](ai-draw-cue-word-project/) | AI 绘画构图细节模板 | 数据表格式与字段规范 | 私有 · 授权交付 |

## 二、核验入口

- **免引擎独立验证**：`second-perspective-verify/evidence/` —— 不需要引擎、不需要许可、不需要联网，用标准库即可复算输入摘要 → 报告哈希 → 链根。
- **产品介绍与术语表**：`PRODUCTS/`。
- **规范文本与实现不一致时，以规范正文为准**；规范未覆盖的行为不视为已承诺。

## 三、许可

除 `Antares/`（GFSIP，规范层 CC BY 4.0）外，本目录作品均适用仓库根目录的《软件授权协议》双轨授权：个人非商业研究免费，政府 / 企业需书面付费授权。详见 [../LICENSE](../LICENSE)。
