# PRODUCTS — 引擎目录

> 一引擎一个目录：`spec/` 放**公开规范**，`verify/` 放**验证资产**。
> 两个子目录在三个引擎间保持对称，第三方可用同一套姿势核验任意一款。
>
> **实现源码不在本仓库。** 各引擎内核属授权交付物。

## 目录索引

| 引擎 | 定位 | 公开规范 | 验证资产 |
|---|---|---|---|
| [Anthropomorphic-Agent-Engine](Anthropomorphic-Agent-Engine/) | AAE 拟人心理引擎 —— 为 AI 角色提供连续、确定、可回放的内心状态层 | [spec/](Anthropomorphic-Agent-Engine/spec/) | [verify/](Anthropomorphic-Agent-Engine/verify/) |
| [nomos](nomos/) | NOMOS 智能决策中枢 | spec/ | [verify/](nomos/verify/) |
| [second-perspective](second-perspective/) | 第二视角引擎（SPE）—— AI 的刹车系统（面向大模型厂商 / 政府 / 对 AI 有控制权的企业；AI Verify 自评 95/100） | [spec/](second-perspective/spec/) | [verify/](second-perspective/verify/) |

另有一项不属任何引擎：决策结构语言规范在其专属目录 [`../STANDARD/`](../STANDARD/)，
是唯一把参照解释器（`dsl.py`）一并公开的规范。

## 规范面包含什么

每份规范描述对应引擎的**公开接口契约面**：定位与边界、输入契约、状态契约、引擎入口、审计契约、确定性前提。
规范面向第三方离线核验，不涉及实现源码、动力学系数或调参依据。

## 未收录的产品

| 产品 | 原因 |
|---|---|
| second-reality、Antares（GFSIP）、ai-draw 等 | 各有独立公开仓库，不在此公开层收录 |

## 许可

各引擎遵循双轨授权（个人非商业研究免费；政府 / 企业须书面付费授权）。
**规范文本可自由引用，须注明出处；本层不授予任何实现对的使用许可。**
具体见各目录 LICENSE。
