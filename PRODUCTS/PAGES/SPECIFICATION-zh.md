# PAGES 规范（Specification）

> **文档信息**：版本 1.x ｜状态：静态站点，无构建步骤｜编制：NOHN AI
> **编制依据**：README.md
>
> 本规范描述 **NOHN AI 技术生态官方落地页** 的公开规范面：站点架构、视觉语言、部署与导航约定。

## 1. 范围与定位

### 1.1 定位

NOHN AI 技术生态统一入口，以极简白奢（minimalist white-luxury）视觉语言呈现生态核心项目，提供零成本、高可读性的项目导航门户。

### 1.2 生态卡片（六张）

SPL Virtual-World Base（在线演示 `/second-reality/`）、SPL-G1 处理器（硬件因果审计 TCU，`/spl-g1/`）、Anthropomorphic Agent Engine（`/your-soulmate/` 演示）、NOMOS（IMDA AI Verify 95/100）、Story Engine、Antares · GFSIP（v1.0，implementation-ready）。

### 1.3 特色区

- SPL 认知审计引擎：中性、离线、决策无关，100% 客户端运行于浏览器（`/audit/`），"no data leaves the machine"；
- AI 绘画构图模板（`/ai-draw/`）。

## 2. 术语与定义

| 术语 | 定义 |
|---|---|
| 白奢 | white-luxury，极简白 + 金色强调的视觉语言 |
| Deep Mode | 深度模式：切换为专业第二视角因果术语（确定性执行内核 / 不可变不变量集 / 只追加账本 / SHA-256 溯源），强调色变紫 |
| 第二视角因果术语 | 生态通用的确定性 / 审计术语集 |

## 3. 核心规范

### 3.1 技术栈与部署

- 纯静态 HTML + CSS；无构建步骤、无框架。
- 本地运行：`python serve.py [PORT]`（默认 8000），或任意静态服务器。
- 部署目标：GitHub Pages / SourceForge Pages（含 CNAME）。

### 3.2 主题与样式

- 字体：Cormorant Garamond / Noto Serif SC（serif）；Manrope / Noto Sans SC（sans）。
- 强调色：`--gold: #b8954a`（定义于 `:root`）。

### 3.3 交互约定

- 双语 EN / ZH 页内切换并持久化；
- Deep Mode 开关（切换为专业术语与紫色强调）。

### 3.4 站点结构（Cloudflare Pages）

- `functions/`：Cloudflare Pages Functions（API + OAuth）；
- `worker/`：后台 worker；
- `schema/`：数据 schema；`seed/`：种子数据；
- `wrangler.toml`：Cloudflare Pages 配置。

### 3.5 信息架构

子项目目录：`ai-draw/`、`audit/`、`nomos/`、`second-reality/`、`spl-g1/`、`story-engine/`、`your-soulmate/`、`docs/`、`forum/`、`login/`、`contact/`、`tax-audit/`、`agents.html`。
隐私配套页：`character-studio-privacy.html`、`story-engine-privacy.html`。

## 4. 边界与禁令

- 静态站点：无构建步骤、无框架；
- 认知审计引擎决策无关、完全客户端运行（离线，数据不出机器）。

## 5. 审计与合规

- 站点内容与设计语言为原创作品；
- 底层项目遵循双轨授权模式（个人免费研究 / 付费商业），详见各项目 LICENSE；
- 授权渠道：国际 / 全球 `ai@nohnlins.com`；中国 `lin@secondai.top`。

## 6. 一致性声明

符合本规范的页面应满足：

1. 基于白奢视觉语言，强调色与字体符合 §3.2；
2. 展示生态卡片与特色区（§1.2 / §1.3）；
3. 支持双语切换与持久化、Deep Mode；
4. 无构建步骤、可被任意静态服务器托管。

## 7. 版本与变更

- 生态成员状态随上游项目更新（Second-Perspective GCAE 五算子、NOMOS、Antares GFSIP v1.0、Anthropomorphic-Agent-Engine SPL Pure Core V8.0）。

## 8. 许可与参考

- 站点原创内容遵循双轨授权；各底层项目许可见各自 LICENSE。
- 参考：README.md / 站点目录结构。