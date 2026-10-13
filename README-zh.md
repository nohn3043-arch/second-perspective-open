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
├── PRODUCTS/                   # 🏷️ 一产品一目录：介绍与说明在根，公开规范在 spec/
│   ├── Antares/                        # GFSIP v1.0 联邦互操作协议
│   ├── ai-draw-cue-word-project/       # AI 绘画提示词控制台
│   ├── second-perspective/             # GCAE 全局认知审计引擎（即本引擎）
│   └── second-reality/                 # 虚拟世界基座
├── STANDARD/                   # 📐 决策结构语言规范（EBNF 文法 + 参照解释器）
│   ├── grammar.md / grammar-zh.md    # 语法规范（中英）
│   ├── decision.ebnf                 # 决策结构文法（EBNF）
│   ├── topology.ebnf                 # 拓扑结构文法（EBNF）
│   ├── dsl.py                        # 参考解释器（规范的可执行定义）
│   ├── 2026.md                       # 标准年度版本说明（2026）
│   └── examples/                     # 合法/非法示例（4 份 .spd 样例）
├── second-perspective-verify/  # ✅ 第二视角引擎（GCAE）校验器 —— 见下 §A
│   ├── verify.py                        # 零依赖离线（python3，纯标准库）
│   ├── verify_convergence_fix.py        # 收敛逻辑回归（S1–S6）
│   ├── verify-output.log                # v1.0 快照完整验证输出（Zenodo）
│   └── evidence/                        # ✅ 冻结审计链 + 免引擎重算 —— 无需引擎、无需许可
├── nomos-verify/               # ❌ NOMOS 第三方验证指南 —— 另一个产品，见下 §B
│   └── VERIFICATION_GUIDE.md            # 验证 NOMOS，不验证本引擎
├── PAPERS/                     # 论文与白皮书（可复现引用）
│   └── paper.pdf / paper.md
└── CERTIFICATIONS/             # 独立认证与合规
    ├── IMDA_AI_Verify_Causal_Audit_Report.pdf   # 新加坡 IMDA AI Verify：95/100
    └── compliance/                          # EU AI Act / ISO 42001 / NIST AI RMF / 上海合规
```

## 如何核验 / How to verify (third-party, offline)

验证资产按产品分开放置，一个产品一个目录：`second-perspective-verify/` 与 `nomos-verify/`。动手前请先确认你在看哪一套。

### A. 第二视角引擎（GCAE）—— ✅ 本引擎的 verify，位于 `second-perspective-verify/`

`second-perspective-verify/verify.py` **就是第二视角引擎（对外以 GCAE 发布）的独立验证套件**。它加载引擎内核（`Second Perspective Engine.py`，属授权交付物），如实报告 **PASS / FAIL / WARN**，不为了好看而放宽断言 —— `FAIL` 即为产品当前缺陷，须在对外承诺前修复。

| 文件 | 作用 |
|------|------|
| `second-perspective-verify/verify.py` | 零依赖、离线、纯标准库校验器。**共 19 项检查：** V1–V9 覆盖引擎内核，V10–V13 覆盖拓扑层四项能力，V14 覆盖二元事实校验，V15 覆盖唯一插件缝，V16 覆盖 ∞ 极限收敛器，V17 覆盖元因果账本 + 自主进化层，另含 V3b、V7b |
| `second-perspective-verify/verify_convergence_fix.py` | 同一引擎的收敛逻辑回归（S1–S6） |
| `second-perspective-verify/verify-output.log` | v1.0 快照的完整输出，随 Zenodo 存档 |

```bash
# 0 依赖，仅需 Python 3 标准库（在已获授权的引擎部署环境中运行）
python second-perspective-verify/verify.py --root    # 打印链根，与下方固定值比对
python second-perspective-verify/verify.py           # 完整校验：脚本自身在结尾打印 PASS / FAIL / WARN 合计
```

**关于计数（引用数字前请先读这段）。** 脚本每次运行都会在结尾打印本次合计，**以该次运行的合计为准，任何冻结数字都不能替代它**。**v1.0 快照的基线是 11 项检查、`PASS 9 · FAIL 0 · WARN 2`**，其中两条 WARN 是预先登记的披露项（V3b、V9），不是失败。此后套件已扩至 19 项检查，因此**任何出自该基线的计数都必须标注为「v1.0 快照值」**。随库的 `verify-output.log` 记录了该快照，可独立核对链根与 PASS / FAIL 计数。

**运行边界 / Runtime note**：`second-perspective-verify/verify.py` 是**公开可审计的校验器**，其校验逻辑完全可见、零依赖、可离线运行；完整运行需加载引擎内核（私有实现，纳入授权交付物）。

固定链根（v1.0 快照）：
`f5713f49481a80f82356ba1255c0292ddb0d17a235a35348bcff0eef49d6a801`

**免引擎证据包 —— 建议从这里开始。** `second-perspective-verify/evidence/` 内含冻结的审计链、期望链根，以及一个零依赖的重算脚本。它**不需要引擎、不需要许可**即可运行：

```bash
python second-perspective-verify/evidence/recompute.py --tamper
```

这是本仓库中唯一一处，外部读者今天就能执行「不必信任供应商」这句话的地方。它跑六项检查，把公开的输入、公开的报告视图与冻结的链相互绑定、并绑定到公开的链根 —— 输入摘要 → 报告哈希 → 链根 —— 并演示三者任一被改动都会被检出。

### B. NOMOS 智能决策中枢 —— ❌ 另一个产品，位于 `nomos-verify/`，不是本引擎的 verify

`nomos-verify/VERIFICATION_GUIDE.md` 是 **NOMOS**（[nohn3043-arch/NOMOS](https://github.com/nohn3043-arch/NOMOS)，v0.5.0，2026-10-08）的第三方验证指南。NOMOS 是**另一个产品**，该指南**不验证本引擎**。

- 方法：`pytest` 发布证据（基线 507 个测试、91% 覆盖率）+ 一次可重放的评估运行。
- 其自身链根：`adacff1bd647b7691cf153b5800185b1afbb449de779bebc2847ac1988090a68`。
- 仅在评估 NOMOS 时使用；要评估第二视角引擎，请用上面 §A。

## 许可证 / License

本仓库作品按《软件授权协议》（LICENSE）分级授权：

- **个人非商业研究**：免费（可下载、复制、运行、修改、学术引用，需注明出处）
- **政府 / 企业 / 机构**：必须事先取得书面付费授权

商业授权联系：国际区 <ai@nohnlins.com> ｜ 中国区 <lin@secondai.top>

## 产品介绍 / Product documentation

每个产品在 `PRODUCTS/` 下占一个目录（索引见 [PRODUCTS/README.md](./PRODUCTS/README.md)）：根下放介绍文档、术语表、变更记录与架构 / 测试说明，**公开规范**放在该目录的 `spec/` 子目录——定位与边界、接口 / 协议 / 格式、审计与合规、一致性声明。唯一不属于产品文档的规范是决策结构语言（连同其参照解释器 `dsl.py`），收纳于 [`STANDARD/`](./STANDARD/)。本仓库任何目录均不含实现源码。

## 相关仓库 / Related

- 论文与元数据：Zenodo（DOI 见论文）
- 核心实现：私有仓库 / 线下授权交付
- 官网门户：https://www.nohnlins.com

---
© 2026 上海霖铭均华科技有限公司 与 NOHN AI TECHNOLOGY PTE. LTD. 保留一切权利。
