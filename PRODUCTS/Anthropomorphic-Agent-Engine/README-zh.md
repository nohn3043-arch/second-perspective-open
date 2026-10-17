# Anthropomorphic Agent Engine（AAE）· 公开层

> 简体中文 | [English](./README.md)

## 本目录是什么

AAE 是**拟人心理引擎**——为 AI 角色提供连续、确定、可回放的内心状态层。

本目录是它的**公开规范层**：任何人无需授权即可阅读契约、自行实现、离线核验。引擎内核（`SPL-anthropic-engine.py`）属授权交付物，**不在**本仓库。

| 层级 | 内容 | 可见性 |
|---|---|---|
| 公开层（本目录） | 接口契约、机器可读 schema、第三方验证指南 | 🔓 公开 |
| 实现层（私有仓库） | 引擎内核、动力学系数与调参依据、测试套件 | 🔒 授权交付 |

## 开放边界

**开放** —— 接口的"形状"：

- 输入契约：内感受向量字段与区间、叙事事件词汇表
- 状态契约：快照顶层键集（主 23 / 未成年 15）、`fluid` 8 键、`mood` 3 键、标量区间
- 引擎入口：9 个方法的签名与行为
- 审计契约：JSONL 信封、事件类型、`delta` 归因算法
- 确定性前提：确定性条件、心境动力学形式、时钟注入前提

**不开放** —— 实现的"手感"：

- 动力学系数、权重与阈值
- 调参依据与标定方法
- 源码级模块划分与标识符

> 规范回答"必须做到什么"，不回答"我们怎么调的"。

## 目录结构

```
Anthropomorphic-Agent-Engine/
├── spec/
│   ├── SPECIFICATION-zh.md          # 规范性契约（中文）
│   ├── SPECIFICATION.md             # Normative contract (EN)
│   └── schema/
│       ├── snapshot.schema.json     # 状态契约
│       ├── vector.schema.json       # 输入契约
│       └── audit-record.schema.json # 审计契约
├── verify/
│   ├── TESTING-zh.md                # 第三方验证指南（中文）
│   └── TESTING.md                   # Third-party verification guide (EN)
├── GLOSSARY.md                      # 术语表
└── LICENSE                          # 许可范围
```

## 如何核验

1. 读 [`spec/SPECIFICATION-zh.md`](./spec/SPECIFICATION-zh.md) 取契约；
2. 用 [`spec/schema/`](./spec/schema/) 校验你的实现输出；
3. 按 [`verify/TESTING-zh.md`](./verify/TESTING-zh.md) 设计你自己的测试并出具你自己的报告。

**契约一致性（A 区）无需引擎即可验证。内核行为（B 区）需授权。**

## 一致性级别

| 级别 | 要求 | 可声称 |
|---|---|---|
| **L0 — 接口一致** | 满足输入契约与引擎入口 | "AAE interface compatible" |
| **L1 — 状态一致** | L0 + 快照键集与区间 | "AAE state compatible" |
| **L2 — 审计一致** | L1 + delta 算法，审计链可跨机复算 | "AAE conformant" |

> 一致性不包含正确性。一致性套件是变更检测器，不是心理学正确性的判据。

## 许可

规范文本可自由引用，须注明出处。本目录**不授予**对任何实现的许可。商用 / 政府用途需书面付费授权，见 [`LICENSE`](./LICENSE)。

**联系**：国际 / 全球 — [ai@nohnlins.com](mailto:ai@nohnlins.com)　·　中国 — [lin@secondai.top](mailto:lin@secondai.top)

*Copyright © NOHN AI TECHNOLOGY PTE. LTD.*
