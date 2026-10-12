# Second-Perspective Open — 可信计算公开层

> 规范、校验器与独立认证资产的公开仓库。
> 本仓库是 NOHN AI「第二视角」可信计算体系的 **公开信任层**：任何人无需授权即可核验我们的工作产物 —— 但无法据此获得核心引擎实现。

<p align="center">
  简体中文 | <a href="README.md">English</a>
</p>

## 本仓库是什么 / Why this repository exists

可信计算的信任来自「**可被第三方离线验证**」，而不是「代码全公开」。
本仓库遵循 TPM / Intel SGX / ARM TrustZone 的成熟路径：**规范公开 · 实现保密 · 认证兜底**。

| 层级 | 内容 | 可见性 |
|------|------|--------|
| 公开层（本仓库） | 语言规范、校验器、论文、独立认证报告 | 🔓 公开 |
| 实现层（其他仓库） | 引擎内核、LLM 适配器、硬件 RTL、产品实现 | 🔒 私有 / 授权交付 |

## 目录结构

```
second-perspective-open/
├── PRODUCTS/                   # 🏷️ 全部产品文档门户（README/GLOSSARY/合规/公开规范 SPECIFICATION）
│   ├── Antares/                        # GFSIP v1.0 联邦互操作协议
│   ├── Anthropomorphic-Agent-Engine/   # 拟人心理引擎
│   ├── ai-draw-cue-word-project/       # AI 绘画提示词控制台
│   ├── DMU/                            # 机器人运动平台
│   ├── HuM/                            # 人形系统
│   ├── nomos/                          # 二阶因果决策框架（95/100）
│   ├── PAGES/                          # 官网门户
│   ├── second-perspective/             # GCAE 全局认知审计引擎（即本引擎）
│   ├── second-reality/                 # 虚拟世界基座
│   ├── SPL-G1/                         # 硬件因果审计 TCU
│   └── Story-engine/                   # 长篇小说一致性引擎
├── SPEC/                       # 决策结构语言规范（公开标准）
│   └── language-standard/
│       ├── grammar.md / grammar-zh.md    # 语法规范（中英）
│       ├── decision.ebnf                 # 决策结构文法（EBNF）
│       ├── topology.ebnf                 # 拓扑结构文法（EBNF）
│       ├── dsl.py                        # 参考解释器（规范的可执行定义）
│       └── examples/                     # 合法/非法示例（19 条诊断码演示）
├── VERIFY/                     # 独立校验器与证据链 —— 此处混放两个产品，务必看清归属（见下「如何核验」）
│   ├── verify.py                        # ✅ 第二视角引擎（GCAE）本引擎校验器 —— 零依赖离线（python3，纯标准库）
│   ├── verify_convergence_fix.py        # ✅ 第二视角引擎 —— 收敛逻辑回归（S1–S6）
│   ├── verify-output.log                # ✅ 第二视角引擎 —— v1.0 快照完整验证输出（Zenodo）
│   └── VERIFICATION_GUIDE.md            # ❌ NOMOS 第三方验证指南 —— 另一个产品，不是本引擎的 verify
├── PAPERS/                     # 论文与白皮书（可复现引用）
│   └── paper.pdf / paper.md
└── CERTIFICATIONS/             # 独立认证与合规
    ├── IMDA_AI_Verify_Causal_Audit_Report.pdf   # 新加坡 IMDA AI Verify：95/100
    └── compliance/                          # EU AI Act / ISO 42001 / NIST AI RMF / 上海合规
```

## 如何核验 / How to verify (third-party, offline)

`VERIFY/` 目录中放着**分属两个不同产品的两套验证资产**，请务必先确认你在看哪一套。

### A. 第二视角引擎（GCAE）—— ✅ 这才是本引擎的 verify

`VERIFY/verify.py` **就是第二视角引擎（对外以 GCAE 发布）的独立验证套件**。它加载引擎内核（`Second Perspective Engine.py`，属授权交付物），如实报告 **PASS / FAIL / WARN**，不为了好看而放宽断言 —— `FAIL` 即为产品当前缺陷，须在对外承诺前修复。

| 文件 | 作用 |
|------|------|
| `VERIFY/verify.py` | 零依赖、离线、纯标准库校验器。**共 19 项检查：** V1–V9 覆盖引擎内核，V10–V13 覆盖拓扑层四项能力，V14 覆盖二元事实校验，V15 覆盖唯一插件缝，V16 覆盖 ∞ 极限收敛器，V17 覆盖元因果账本 + 自主进化层，另含 V3b、V7b |
| `VERIFY/verify_convergence_fix.py` | 同一引擎的收敛逻辑回归（S1–S6） |
| `VERIFY/verify-output.log` | v1.0 快照的完整输出，随 Zenodo 存档 |

```bash
# 0 依赖，仅需 Python 3 标准库（在已获授权的引擎部署环境中运行）
python VERIFY/verify.py --root    # 打印链根，与下方固定值比对
python VERIFY/verify.py           # 完整校验：脚本自身在结尾打印 PASS / FAIL / WARN 合计
```

**关于计数（引用数字前请先读这段）。** 脚本每次运行都会在结尾打印本次合计，**以该次运行的合计为准，任何冻结数字都不能替代它**。**v1.0 快照的基线是 11 项检查、`PASS 9 · FAIL 0 · WARN 2`**，其中两条 WARN 是预先登记的披露项（V3b、V9），不是失败。此后套件已扩至 19 项检查，因此**任何出自该基线的计数都必须标注为「v1.0 快照值」**。随库的 `verify-output.log` 记录了该快照，可独立核对链根与 PASS / FAIL 计数。

**运行边界 / Runtime note**：`VERIFY/verify.py` 是**公开可审计的校验器**，其校验逻辑完全可见、零依赖、可离线运行；完整运行需加载引擎内核（私有实现，纳入授权交付物）。

固定链根（v1.0 快照）：
`f5713f49481a80f82356ba1255c0292ddb0d17a235a35348bcff0eef49d6a801`

### B. NOMOS 智能决策中枢 —— ❌ 另一个产品，不是本引擎的 verify

`VERIFY/VERIFICATION_GUIDE.md` 是 **NOMOS**（`Intelligent-Decision-Hub--Nomos` 分支，v0.5.0，2026-10-08）的第三方验证指南。NOMOS 是**另一个产品**，该指南**不验证本引擎**。

- 方法：`pytest` 发布证据（基线 507 个测试、91% 覆盖率）+ 一次可重放的评估运行。
- 其自身链根：`adacff1bd647b7691cf153b5800185b1afbb449de779bebc2847ac1988090a68`。
- 仅在评估 NOMOS 时使用；要评估第二视角引擎，请用上面 §A。

## 许可证 / License

本仓库作品按《软件授权协议》（LICENSE）分级授权：

- **个人非商业研究**：免费（可下载、复制、运行、修改、学术引用，需注明出处）
- **政府 / 企业 / 机构**：必须事先取得书面付费授权

商业授权联系：国际区 <ai@nohnlins.com> ｜ 中国区 <lin@secondai.top>

## 产品介绍 / Product documentation

各产品的 **介绍文档**（README）、**术语表**（GLOSSARY）、**合规与一致性文档**、**协议规范**（如 Antares 的 GFSIP 协议规范）与 **公开规范**（每产品一份 `SPECIFICATION-zh.md`，含定位与边界、接口 / 协议 / 格式、审计与合规、一致性声明）统一收录于 `PRODUCTS/` 目录（索引见 [PRODUCTS/README.md](./PRODUCTS/README.md)），按产品分目录组织，便于检索与引用。每个产品目录仅含介绍性与规范性文档，不含实现源码。

## 相关仓库 / Related

- 论文与元数据：Zenodo（DOI 见论文）
- 核心实现：私有仓库 / 线下授权交付
- 官网门户：https://www.nohnlins.com

---
© 2026 上海霖铭均华科技有限公司 与 NOHN AI TECHNOLOGY PTE. LTD. 保留一切权利。
