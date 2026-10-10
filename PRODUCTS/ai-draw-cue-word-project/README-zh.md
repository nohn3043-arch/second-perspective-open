# AI 绘画提示词工程

[English](README.md) | 简体中文

> AI 绘画构图细节模板 —— 权重与比例精控版 v2.8（全模型可适配：设定层通用，语法层按模型区分）

本仓库是一份用于单角色与多角色 AI 图像、视频、3D 生成的质量控制工作簿的版本化导出。原始版本为腾讯文档在线表格；本仓库以纯 CSV（每张子表一个文件）保存内容，另附本 README。

## 这是什么

一套跨五大提示词语法体系的实用控制台，用于构建高一致性的角色提示词：

- 自然语言流（Flux / DALL·E 3 / SD3）
- 对话式图像模型（GPT-4o / Gemini）
- Midjourney / Niji
- Stable Diffusion
- 国内 API 模型（即梦 / 可灵 / 豆包 / 通义万相）

v2.8（相对 v2.7）标志着数据标准与交互工作台的分离。21 张 CSV 数据表保持不变。Cloudflare Pages 工作台（www.nohnlins.com/ai-draw/）将漫画模式从静态表格展示升级为全交互生成：拖拽上传 Word/TXT，配合 mammoth.js 解析 .docx，自动切分故事节拍，跨 4 大模型族逐格组装提示词，自动配置气泡，并自动生成 P0 时序一致性检查清单。企业 IP 预设库升级，支持 JSON 导入/导出与 localStorage 持久化。

v2.7（相对 v2.6）新增：漫画模式 —— 三张新表闭环漫画/连环画的生成流程。PanelLayoutRules 覆盖 5 种版式类型（四格网格、六格网格、电影长条、整页大图、竖版条漫/网络漫画），逐一定义分格排布、画幅比例、构图规则、角色位置、背景连续性、提示词组装规则、视觉节奏控制与常见失败。SpeechBubblePositioning 定义 7 种气泡类型（标准对白、内心独白、旁白、拟声词、耳语、呼喊、电子/数字），逐一定义尾部方向、位置规则、尺寸规则、文字量、形状与风格、重叠规则、图层优先级、提示词组装规则与常见失败。TemporalConsistencyChecklist 提供 6 大类共 13 项校验（角色身份、空间连续性、时间连续性、动作连续性、表情连续性、服装与道具），逐项给出严重级 P0/P1/P2、检查时机、校验内容、校验方法、通过标准、失败标准与修复协议。表格总数 18→21。

v2.6（相对 v2.5）新增：StoryboardSkeletonTemplate —— 漫画/连环画分镜骨架，含 10 种分格角色模板（建场、角色登场、A→B 对白、B→A 对白、动作节拍、反应、情绪特写、场景转换、高潮大图、收尾），3 条镜头连续性规则（180 度轴线、30 度规则、视线匹配），4 种页面版式（四格网格、六格网格、电影长条、整页大图）。每行含提示词组装规则、连续性检查与常见失败模式。表格总数 17→18。

v2.5（相对 v2.4）新增：5 张新表，覆盖此前未涉及的生成模态 —— 视频生成（Sora/可灵/Runway/Pika/国内 API，含镜头运动与时间结构）、多角色空间关系（3+ 角色，含景深层级、视线链、交互链）、LoRA 管理（角色/风格/服装/概念/背景类型，含冲突检测与堆叠顺序）、3D 生成矩阵（Meshy/Tripo3D/Rodin/混元3D-2/Stable Fast3D/CRM）、对话式编辑链（GPT-4o/Gemini 的逐轮单点修复协议，含锚点边界规则）。表格总数 12→17。

v2.4（相对 v2.3）新增：姿势–情绪对照表（构图与镜头中的 D 节），将角色气质标签映射到姿势/视线/重心组合。另为双角色场景新增逐角色姿势差异字段。

v2.3（相对 v2.2）新增：国内 API 族语法流、DALL·E 3 弃用说明，以及诚实的"可适配"表述。

## ✦ 系统架构（人话版）

> **一句话：** 这个仓库是一个 **AI 绘画提示词的操控台**——21 张表格，把「祈祷这张脸别崩」变成一份可重复执行的清单。

```mermaid
flowchart TB
    WB["🌐 Cloudflare Pages 在线工作台 · www.nohnlins.com/ai-draw/<br/>拖拽 Word/TXT 上传 · 漫画模式 · 企业 IP 预设库 JSON 导入导出（v2.8 起）"]
    DATA["📚 sheets/*.csv —— 21 张数据表，唯一事实来源<br/>CharacterAnchors · CompositionAndShots · ModelsAndReferences · Checklist · PanelLayoutRules · SpeechBubblePositioning · TemporalConsistencyChecklist · StoryboardSkeletonTemplate · GenerationIterationLog …"]

    S1["① sheets/CharacterAnchors.csv<br/>锚定角色 —— 硬锚权重 ≥ 1.6，永不替换"]
    S2["② sheets/ModelsAndReferences.csv + ReferenceImageCapabilityMatrix.csv<br/>选模型 + 参考图策略"]
    S3["③ sheets/NaturalLanguagePromptTemplate.csv<br/>把角色和场景拼装成一段提示词"]
    S4["④ sheets/Checklist.csv<br/>P0 / P1 / P2 校验 —— P0 是硬闸门"]
    S5["⑤ sheets/GenerationIterationLog.csv<br/>记录每一轮迭代改了什么"]

    M1["🎨 自然语言流<br/>Flux · DALL·E 3 · SD3"]
    M2["💬 对话式<br/>GPT-4o · Gemini"]
    M3["🐇 Midjourney / Niji"]
    M4["🧩 Stable Diffusion"]
    M5["🇨🇳 国内 API<br/>即梦 · 可灵 · 豆包 · 通义万相"]

    EX["📄 examples/nanwang_spring_garden_prompt.md<br/>一份可以直接照抄的完整示例提示词"]
    RESULT["🖼️ 跨图片 / 视频 / 3D 都保持一致的同一个角色"]

    WB --> S1
    DATA --> S1
    S1 --> S2
    S2 --> S3
    S3 --> S4
    S4 --> S5
    S3 --> M1
    S3 --> M2
    S3 --> M3
    S3 --> M4
    S3 --> M5
    M1 --> RESULT
    M2 --> RESULT
    M3 --> RESULT
    M4 --> RESULT
    M5 --> RESULT
    EX --> S3

    classDef cUp fill:#F5F5F5,stroke:#9E9E9E,stroke-width:1px,color:#424242
    classDef cIn fill:#E8F0FE,stroke:#4285F4,stroke-width:1px,color:#173A66
    classDef cCore fill:#FFF8E1,stroke:#C9A96E,stroke-width:1px,color:#5B4614
    classDef cSide fill:#F3E8FD,stroke:#8E44AD,stroke-width:1px,color:#4A235A
    classDef cOut fill:#E6F4EA,stroke:#34A853,stroke-width:1px,color:#14512B
    class WB,DATA cIn
    class S1,S2,S3,S4,S5 cCore
    class M1,M2,M3,M4,M5 cUp
    class EX cSide
    class RESULT cOut
```

**这张图怎么看**

1. **从上往下读：数据进来，同一个角色出去。** 21 张 CSV 表和在线工作台是两个入口；五步工作流消化它们，把一段提示词交给五个模型家族，五个家族应该还回同一个角色。
2. **每个框都写了真实文件或表名。** `CharacterAnchors.csv`、`ModelsAndReferences.csv`、`NaturalLanguagePromptTemplate.csv`、`Checklist.csv`、`GenerationIterationLog.csv`——打开 `sheets/` 目录可以对照着读。
3. **真正要紧的边界。** 表格本身就是产品；第 4 步是硬闸门——P0 失败就等于废图，必须重做，而不是继续碰运气。

📖 每个术语都用一句人话解释 → [术语表 GLOSSARY](./GLOSSARY.md)

## 快速开始

1. **锚定角色** —— 在 `sheets/CharacterAnchors.csv` 中填写角色锚点（硬锚权重 ≥ 1.6，不可替换）。
2. **选择模型与参考策略** —— 在 `sheets/ModelsAndReferences.csv` 与 `ReferenceImageCapabilityMatrix.csv` 中确定目标模型与一致性方法（MJ `--cref` / SD LoRA / Flux Kontext / 对话式参考）。
3. **组装提示词** —— 按 `sheets/NaturalLanguagePromptTemplate.csv` 的优先级构建（硬锚 → 核心特征 → 基线描述 → 氛围）；跨模型语法见"跨模型语法红线"。
4. **校验** —— 用 `sheets/Checklist.csv` 执行 P0/P1/P2 校验；多角色场景补充 `MultiCharacterSpatialRelations.csv`，漫画补充 `PanelLayoutRules.csv` / `SpeechBubblePositioning.csv` / `TemporalConsistencyChecklist.csv`。
5. **记录迭代** —— 每次生成都记录到 `sheets/GenerationIterationLog.csv`；同一类型连续 3 次失败后，切换模型或参数路线。

完整走查示例见 [`examples/nanwang_spring_garden_prompt.md`](examples/nanwang_spring_garden_prompt.md)（同一角色设定在 4 种语法流中的成品提示词）。

## 子表一览（`/sheets` 目录）

> 文件名已统一为英文以便 GitHub 渲染；中文原名在括号内标注。全部 21 张表与早期中文导出逐一对应。

| 文件 | 说明 |
|---|---|
| `Usage.csv`（使用说明） | 工作流、权重语义、权重→叙事映射、P0/P1/P2 校验、跨模型红线 |
| `CharacterAnchors.csv`（角色锚点） | 逐角色锚点；锚权重 ≥ 1.6，永不可替换 |
| `CompositionAndShots.csv`（构图与镜头） | 构图类型、镜头、光、层次、姿势模板；多角色空间字段 |
| `FeatureDetails.csv`（特征细节） | 特征级描述符 |
| `NaturalLanguagePromptTemplate.csv`（自然语言叙述模板） | 各语法族的组装提示词模板 |
| `ModelsAndReferences.csv`（模型与参考） | 各模型的参考图手段与一致性策略 |
| `NegativeWordBank.csv`（负面词库） | 各模型负面提示词（MJ `--no` 4-6 词；SD 用 Negative 框；无负面框模型改用肯定式写作） |
| `Checklist.csv`（校验清单） | P0 硬性 / P1 建议 / P2 可选校验 |
| `AspectRatioBaselines.csv`（比例基准表） | 各画风头身比（Q 版 2-3、萝莉 4-5、少女 6-6.5、青年 6.5-7、成人 7-8、写实 7.5+）；容差 ≤5% |
| `ReferenceImageCapabilityMatrix.csv`（参考图能力矩阵） | 各模型参考图能力（MJ `--cref`、SD LoRA、Flux Kontext/Redux、GPT-4o/Gemini 原生、DALL·E 3 无） |
| `GenerationIterationLog.csv`（生成迭代日志） | 逐次生成的迭代记录 |
| `VideoGenerationPromptTemplate.csv`（视频生成模板） | 各模型视频提示词语法（Sora/可灵/Runway/Pika/国内 API），含镜头运动、时间结构与跨帧锚点一致性 |
| `MultiCharacterSpatialRelations.csv`（多角色空间关系） | 3+ 角色的空间排布、景深层级、视线链、交互链、遮挡规则、比例透视 |
| `LoRAManagement.csv`（LoRA 管理） | LoRA 类型分类（角色/风格/服装/概念/背景）、权重区间、冲突检测、堆叠顺序、跨模型适用性 |
| `ThreeDGenerationMatrix.csv`（3D 生成矩阵） | 各模型 3D 生成能力（Meshy/Tripo3D/Rodin/混元3D-2/Stable Fast3D/CRM）—— 输入格式、输出格式、贴图、拓扑、身份一致性 |
| `ConversationalEditChain.csv`（对话式编辑链） | GPT-4o/Gemini 的逐轮单点修复协议；锚点边界规则；逐轮失败处理 |
| `PanelLayoutRules.csv`（面板排布规则） | 5 种漫画版式（四格 / 六格 / 电影长条 / 整页大图 / 竖版条漫）—— 分格排布、画幅比例、构图规则、角色位置、背景连续性、提示词组装、视觉节奏控制、常见失败 |
| `SpeechBubblePositioning.csv`（对话气泡定位） | 7 种气泡类型（标准对白 / 内心独白 / 旁白 / 拟声词 / 耳语 / 呼喊 / 电子）—— 尾部方向、位置规则、尺寸规则、文字量、形状与风格、重叠规则、图层优先级、提示词组装、常见失败 |
| `TemporalConsistencyChecklist.csv`（时序一致性验收） | 6 大类共 13 项校验（角色身份 / 空间 / 时间 / 动作 / 表情 / 服装道具）—— 严重级 P0/P1/P2、检查时机、校验方法、通过标准、失败标准、修复协议 |
| `StoryboardSkeletonTemplate.csv`（分镜骨架模板） | 漫画/连环画分镜骨架 —— 10 种分格角色、3 条镜头连续性规则、4 种页面版式；每行含提示词组装规则、连续性检查、常见失败 |
| `ChangeLog.csv`（修改日志） | 模板修订历史 |

## 权重语义（SD / MJ 数值体系）

| 区间 | 含义 | 示例 |
|---|---|---|
| 1.6 – 2.0 | 硬锚：绝对不可改 | 左眼下泪痣（1.8） |
| 1.3 – 1.5 | 核心特征：跨所有场景保留 | 浅青色棉裙（1.4） |
| 1.0 – 1.2 | 基线：默认强度 | 温和安静的气质（1.0） |
| 0.7 – 0.9 | 氛围辅助：可按场景调整 | 春日花园（0.8） |
| < 0.7 | 弱提示：易被忽略 | 微风（0.5） |

自然语言模型没有数值权重；将数值映射到叙事位置/精度即可（见"使用说明"表）。

## 跨模型语法红线

- 权重语法 `(word:1.3)` 仅在 SD 有效；MJ 依赖词元位置与重复；
  自然语言模型禁止使用括号权重。
- 负面提示词：MJ 用 `--no` 加 4-6 个短词；SD 用 Negative Prompt 框；
  Flux/DALL·E/GPT-4o/Gemini 无负面框 → 改用肯定式写法，否定式作为兜底；
  国内 API 模型：负面提示词支持情况不一，需查官方文档。
- 参考图：MJ `--cref` 仅 v6 有效（v7 用 `--oref`/`--ow`，v8 用 Edit Model `--edit`）；SD LoRA/IP-Adapter；FLUX.2 多参考图 + Edit；Gemini 3 Pro Image 原生（上限 14 张）；
  DALL·E 3 无（对多图系列已弃用）→ 以描述主导；
  国内 API 模型：能力以官方文档为准（见矩阵表）。
- 锚点复用：自然语言模型必须逐图逐字复用锚点句；
  禁止同义替换（例如"泪痣"不得写成"斑点"或"小痣"）。

## 校验优先级

- **P0** —— 角色核心设定；失败 = 图片作废；必须重生成。
- **P1** —— 画面质量与比例；影响可用性；优先修复，允许重试一次。
- **P2** —— 美观与细节；记录并在下一轮改进。

## 来源

原始腾讯文档：https://docs.qq.com/sheet/DT05rb0tCVmVSSVpR

## 许可

基于 Apache License 2.0 授权。详见 [LICENSE](LICENSE)。
Copyright (c) 2026 NOHN AI TECHNOLOGY PTE LTD. 联系：ai@nohnlins.com。
