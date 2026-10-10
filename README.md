# Second-Perspective Open — 可信计算公开层

> 规范、校验器与独立认证资产的公开仓库。
> 本仓库是 NOHN AI「第二视角」可信计算体系的 **公开信任层**：任何人无需授权即可核验我们的工作产物 —— 但无法据此获得核心引擎实现。

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
├── PRODUCTS/                   # 🏷️ 全部产品介绍文档门户（README/GLOSSARY/合规/规范）
│   ├── Antares/                        # GFSIP v1.0 联邦互操作协议
│   ├── Anthropomorphic-Agent-Engine/   # 拟人心理引擎
│   ├── ai-draw-cue-word-project/       # AI 绘画提示词控制台
│   ├── DMU/                            # 机器人运动平台
│   ├── HuM/                            # 人形系统
│   ├── nomos/                          # 二阶因果决策框架（95/100）
│   ├── PAGES/                          # 官网门户
│   ├── second-perspective/             # GCAE 全局认知审计引擎
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
├── VERIFY/                     # 独立校验器与证据链
│   ├── verify.py                        # 零依赖离线校验器（python3，纯标准库）
│   ├── verify_convergence_fix.py        # 收敛验证辅助
│   ├── verify-output.log                # Zenodo 快照时的完整验证输出
│   └── VERIFICATION_GUIDE.md            # 第三方验证指南
├── PAPERS/                     # 论文与白皮书（可复现引用）
│   └── paper.pdf / paper.md
└── CERTIFICATIONS/             # 独立认证与合规
    ├── IMDA_AI_Verify_Causal_Audit_Report.pdf   # 新加坡 IMDA AI Verify：95/100
    └── compliance/                          # EU AI Act / ISO 42001 / NIST AI RMF / 上海合规
```

## 如何核验 / How to verify (third-party, offline)

```bash
# 0 依赖，仅需 Python 3 标准库（在已获授权的引擎部署环境中运行）
python VERIFY/verify.py --root    # 打印链根，与下方固定值比对
python VERIFY/verify.py           # 完整校验：预期 PASS 9 · FAIL 0 · WARN 2
```

**运行边界 / Runtime note**：`VERIFY/verify.py` 是**公开可审计的校验器**，其校验逻辑完全可见、零依赖、可离线运行；完整运行需加载引擎内核（私有实现，纳入授权交付物）。本仓库附带的 `verify-output.log` 为 v1.0 快照时刻的完整输出，可独立核对链根与 PASS/FAIL 计数。

固定链根（v1.0 快照）：
`f5713f49481a80f82356ba1255c0292ddb0d17a235a35348bcff0eef49d6a801`

## 许可证 / License

本仓库作品按《软件授权协议》（LICENSE）分级授权：

- **个人非商业研究**：免费（可下载、复制、运行、修改、学术引用，需注明出处）
- **政府 / 企业 / 机构**：必须事先取得书面付费授权

商业授权联系：国际区 <ai@nohnlins.com> ｜ 中国区 <lin@secondai.top>

## 产品介绍 / Product documentation

各产品的 **介绍文档**（README、术语表 GLOSSARY、合规与一致性文档、协议规范）统一收录于 `PRODUCTS/` 目录，按产品分目录组织，便于检索与引用。每个产品目录仅含介绍性文档，不含实现源码。

## 相关仓库 / Related

- 论文与元数据：Zenodo（DOI 见论文）
- 核心实现：私有仓库 / 线下授权交付
- 官网门户：https://www.nohnlins.com

---
© 2026 上海霖铭均华科技有限公司 与 NOHN AI TECHNOLOGY PTE. LTD. 保留一切权利。