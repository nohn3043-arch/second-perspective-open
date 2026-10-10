# AI 绘画构图细节模板 规范（Specification）

> **文档信息**：版本 v2.8 ｜状态：数据标准与工作台分离｜编制：NOHN AI
> **编制依据**：README-zh / GLOSSARY / 21 张 CSV 子表
>
> 本规范描述 **AI 绘画构图细节模板——权重与比例精控版** 的公开规范面：数据表结构、权重语义、五步工作流与跨模型语法红线。21 张 CSV 表为唯一事实来源。

## 1. 范围与定位

### 1.1 定位

跨五大提示词语法体系构建高一致性角色提示词的质量控制工作簿（原为腾讯文档在线表格，现为版本化导出，以纯 CSV 保存）：
自然语言流（Flux / DALL·E 3 / SD3）、对话式（GPT-4o / Gemini）、Midjourney / Niji、Stable Diffusion、国内 API（即梦 / 可灵 / 豆包 / 通义万相）。

### 1.2 设定

- 设定层通用，语法层按模型区分；
- 全模型可适配。

## 2. 术语与定义

| 术语 | 定义 |
|---|---|
| 硬锚点 | 权重 ≥ 1.6 的不可变特征 |
| 核心特征 | 权重 1.3–1.5 |
| 负面词库 | 反向提示词清单 |
| 时序一致性 | 前后两图人物 / 服装 / 光线不变 |
| P0 / P1 / P2 | 校验优先级：P0 硬闸门，P1 可重试一次，P2 记录下轮改进 |
| 迭代日志 | 同类连续失败 3 次 → 换模型或参数路线 |
| 比例基准 | 头身比标准，容差 ≤ 5% |

## 3. 核心规范

### 3.1 数据表（21 张 CSV）

核心子表：`CharacterAnchors.csv`、`NaturalLanguagePromptTemplate.csv`、`Checklist.csv`、`GenerationIterationLog.csv`、`AspectRatioBaselines.csv`、`TemporalConsistencyChecklist.csv`、`PanelLayoutRules.csv`、`SpeechBubblePositioning.csv`、`StoryboardSkeletonTemplate.csv`、`ChangeLog.csv` 等（完整清单见 README"子表一览"）。

### 3.2 权重语义区间（SD / MJ 数值体系）

| 区间 | 语义 |
|---|---|
| 1.6 – 2.0 | 硬锚（不可变特征） |
| 1.3 – 1.5 | 核心特征 |
| 1.0 – 1.2 | 基线 |
| 0.7 – 0.9 | 氛围辅助 |
| < 0.7 | 弱提示 |

### 3.3 比例基准（头身比）

Q 版 2–3；萝莉 4–5；少女 6–6.5；青年 6.5–7；成人 7–8；写实 7.5+。

### 3.4 一致性校验

- `TemporalConsistencyChecklist.csv`：6 大类 13 项校验（含严重级 / 检查时机 / 通过标准 / 修复协议）。
- 镜头连续性：180 度轴线 / 30 度规则 / 视线匹配。

### 3.5 工作流（五步）

锚定角色 → 选模型与参考策略 → 组装提示词 → P0 / P1 / P2 校验 → 记录迭代。

### 3.6 在线工作台

- www.nohnlins.com/ai-draw/；v2.8 起支持拖拽 Word / TXT + mammoth.js 解析 .docx；
- 企业 IP 预设库 JSON 导入 / 导出；localStorage 持久化。

## 4. 边界与禁令（跨模型语法红线）

- 权重语法 `(word:1.3)` 仅 SD 有效；
- MJ `--no` 限 4–6 词；MJ `--cref` 仅 v6；
- DALL·E 3 无参考图，且对多图系列弃用；
- 自然语言模型禁止括号权重；禁止锚点同义替换；
- FLUX.2 与 Gemini 3 Pro Image 完全不支持负面提示词。

## 5. 审计与合规

- `ChangeLog.csv` 记录模板修订历史。
- 许可：Apache License 2.0；Copyright (c) 2026 NOHN AI TECHNOLOGY PTE LTD。

## 6. 一致性声明

符合本规范的模板应满足：

1. 21 张 CSV 表结构与本文档所述语义一致；
2. 权重语义区间与红线规则（§3.2、§4）一致；
3. P0 失败即图片作废 → 必须重生成（硬闸门）。

## 7. 版本与变更

- v2.8（当前）；沿革：v2.3（国内 API 族 / DALL·E 3 弃用说明）→ v2.4（姿势–情绪对照表）→ v2.5（视频 / 多角色 / LoRA / 3D / 对话式编辑，+5 张表）→ v2.6（分镜骨架）→ v2.7（漫画模式，+3 张表）→ v2.8；表数 12 → 17 → 18 → 21。

## 8. 许可与参考

- Apache License 2.0。
- 参考：README-zh / GLOSSARY / 21 张 CSV 子表。