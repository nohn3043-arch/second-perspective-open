# PRODUCTS — 产品目录

> 一产品一个目录。根下放**介绍与说明**，`spec/` 子目录放该产品的**公开规范**。
>
> **实现源码不在本仓库。** 各产品的引擎内核属授权交付物。

## 目录索引

| 产品 | 定位 | 根下文档 | 公开规范 |
|---|---|---|---|
| [Antares](Antares/) | GFSIP v1.0 — 带因果审计的联邦稳定互操作协议（开放标准） | README / README-zh / GLOSSARY / NOTICE / CHANGELOG | [spec/](Antares/spec/) |
| [DMU](DMU/) | 直驱运动统一驱动系统（动力学仿真原型） | README / README-zh | [spec/](DMU/spec/) |
| [HuM](HuM/) | 人形驱动系统（含空气动力学，动力学仿真原型） | README / README-zh | [spec/](HuM/spec/) |
| [nomos](nomos/) | 二阶因果决策支持框架（IMDA AI Verify 自评 95/100） | README / README-zh / GLOSSARY / CHANGELOG / LICENSE | [spec/](nomos/spec/) |
| [PAGES](PAGES/) | NOHN AI 生态官方落地页（白奢视觉语言） | README | [spec/](PAGES/spec/) |
| [second-perspective](second-perspective/) | GCAE 全局认知审计引擎（IMDA 自评 95/100） | GLOSSARY / TESTING / TESTING-zh / LICENSE | [spec/](second-perspective/spec/) |
| [second-reality](second-reality/) | 虚拟世界基础设施基座（宪法—法律—桥） | README / README-zh / GLOSSARY / LICENSE | [spec/](second-reality/spec/) |
| [SPL-G1](SPL-G1/) | 硬件因果审计可信计算单元 TCU（Phase A 完成） | README / README-zh / GLOSSARY / IMPROVEMENT_PLAN / LICENSE | [spec/](SPL-G1/spec/) |
| [Story-engine](Story-engine/) | 长篇叙事一致性引擎 + 离线文档合规复核引擎 | README / README-zh / GLOSSARY / LICENSE | [spec/](Story-engine/spec/) |
| [ai-draw-cue-word-project](ai-draw-cue-word-project/) | AI 绘画构图细节模板 v2.8（21 张 CSV 数据表） | README / README-zh / GLOSSARY / LICENSE | [spec/](ai-draw-cue-word-project/spec/) |

另有一项不属任何产品：决策结构语言规范在其专属目录 [`../STANDARD/`](../STANDARD/)，
是唯一把参照解释器（`dsl.py`）一并公开的规范。

## 说明

每份规范描述对应产品的**公开规范面**：定位与边界、接口 / 协议 / 格式、参数与配置、审计与合规、一致性声明、版本与变更。规范面向第三方离线核验，不涉及实现源码。

> ⚠️ 部分文档存在表述差异（如 second-reality 的审计维度数、second-perspective 的验证检查项数量），规范文档已标注消歧说明，最终以规范正文 / 权威源为准。

## 未收录的产品

| 产品 | 原因 |
|---|---|
| Anthropomorphic-Agent-Engine | 核心设计与实现参数不予公开，故本仓库不提供其规范面；评估需求请按 LICENSE 联系授权。 |

## 许可

各产品遵循双轨授权（个人非商业研究免费；政府 / 企业书面付费授权），**Antares（GFSIP）除外**——其规范文档为 CC BY 4.0、代码为 Apache-2.0，属开放标准。具体见各目录 LICENSE。
