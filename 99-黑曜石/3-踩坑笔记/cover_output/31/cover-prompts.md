# 《玩转 jupyterhub》公众号封面 · 设计方案 + AI 生成 Prompts

> 用途：为踩坑笔记《玩转 jupyterhub》生成公众号封面。
> 风格：**科技感 · 深空底色 + emerald 霓虹**（与正文「摸鱼绿」主题一致）。
> 本文档 = 设计说明 + 可直接粘贴的生成提示词（分「纯背景」和「带文字」两类）。

---

## 1. 设计思路（Concept）

- **主体意象**：一个**发光的 emerald 立方体容器**悬浮在深空中央（= docker 容器 / JupyterHub 的多用户容器），立方体由细线框 + 霓虹描边构成，表面有微光电路板纹理。容器右侧/后方**漂浮着几个半透明小容器碎片**（= 被 spawn 出来的单用户 notebook 容器），呈"母体派生子容器"的放射关系，呼应"一个 hub 隔离出 N 个用户容器"的核心。
- **背景**：深空黑蓝（`#05070F` → `#0A1120` 径向渐变），带**透视网格地平线 / 点阵**（tech dashboard 感），四角有淡淡的 HUD 括号与刻度线。
- **光效**：emerald 霓虹辉光（glow / bloom），冷蓝（`#38BDF8`）作次级点缀光；少量漂浮的微光粒子。整体**留白克制**，主体偏左，右侧留作文字区。
- **气质**：干净、高级、工程感强，不堆砌；暗色底 + 绿光，一眼"部署/容器/后端"。
- **文字**：封面主标题建议 `踩了无数个坑，`（上）`只推荐一个 Docker 最佳实践`（下，emerald 高亮）。**优先用"纯背景图 + 后期叠字"**（见第 5 节），文字最可控、最清晰。

---

## 2. 规格（Spec）

| 项 | 值 |
|---|---|
| 头条封面比例 | **900 × 383**（约 2.35 : 1，横长条） |
| 次条封面比例 | 200 × 200（1 : 1，小方图，建议同套背景裁中央） |
| 安全区 | 主体与高光**集中在画面中左 2/3**，右侧 1/3 保持较暗、较空（放文字） |
| 主色 | emerald `#059669` / 亮 emerald `#34D399` / 极亮霓虹 `#6EE7B7` |
| 次色 | 深空蓝黑 `#05070F`、`#0A1120`；冷蓝点缀 `#38BDF8` |
| 字体（叠字用） | 中文思源黑体 / 苹方 / 鸿蒙黑体 粗体；英文标题可用无衬线（Inter / SF） |
| 风格关键词 | 3D、octane、cinematic lighting、dark tech、neon emerald、minimal、high detail |

---

## 3. Prompt A —— 纯背景图（**推荐**，无文字，后期叠标题）

适配：Midjourney / Stable Diffusion / DALL·E / 即梦 / 可图。出图后在右侧/留白处叠标题，文字最清晰可控。

### A1 · 英文（Midjourney / SD / DALL·E 通用）

> A clean futuristic tech banner, a single glowing emerald glass cube container floating in deep dark space at center-left, the cube made of neon wireframe edges and faint circuit-board texture, several translucent smaller cube shards floating around it as if spawned from the main container, dark deep-navy to black radial gradient background, subtle perspective grid horizon and fine dot matrix, soft emerald neon glow and bloom, a few cool cyan accent light streaks, faint HUD corner brackets and scale marks in the corners, minimal composition with generous negative space on the right third for text, 3D render, octane render, cinematic lighting, dark tech aesthetic, high detail, no text, no letters, no watermark

**Midjourney 参数（可选）：** `--ar 2.35:1 --style raw --v 6`（要更强景深/氛围可加 `--stylize 120`）

### A2 · 中文（即梦 / 可图 / 文心一言 等国产模型）

> 科技感 banner 横幅：深空黑色与深蓝径向渐变背景，画面中左侧悬浮一个发光的祖母绿（emerald）半透明玻璃立方体容器，立方体是霓虹线框结构，表面带淡淡的电路板纹理，主容器周围漂浮着几个更小的半透明立方体碎片，像从主容器里派生出来的子容器；背景有透视网格地平线和细点阵，四角有淡淡的 HUD 括号和刻度线；祖母绿霓虹辉光、光晕，少量冷蓝色光带点缀，画面右侧三分之一保持暗、留白（用于放文字）；3D 渲染、电影级打光、干净高级的工程科技感，无文字、无水印

> ⚠️ 国产模型容易自作主张加字，务必保留句末「**无文字**」，并在设置里关掉/降低"文字"权重。

---

## 4. Prompt B —— 带文字的整图（一步出图，文字由 AI 渲染）

适配：GPT-image / 即梦（支持中文文字）/ 可图。适合"直接要一张成品封面"。

### B1 · 中文整图（即梦 / 可图 / 文心）

> 一张科技感的公众号封面横幅（横版，比例约 2.35:1）。深空黑蓝渐变背景，左侧一个发光的祖母绿玻璃立方体容器悬浮，霓虹线框 + 电路纹理，周围漂浮几个半透明小容器碎片，背景有透视网格、点阵和淡淡的 HUD 刻度。右侧留白处用**粗体白色中文大字**写主标题：
> 第一行：`踩了无数个坑，`
> 第二行：`只推荐一个 Docker 最佳实践`（"Docker 最佳实践"用亮祖母绿色 #34D399 强调）
> 顶部左上角放一条极小的浅色英文小标签：`TUTORIAL · JUPYTERHUB 部署实战`。
> 字体为无衬线黑体、清晰锐利，整体干净高级、暗色霓虹风格，文字无错字、无多余水印。

### B2 · 英文整图（DALL·E / GPT-image）

> A dark tech newsletter cover banner (wide, ~2.35:1). Deep navy-to-black radial gradient background; on the left, a glowing emerald glass cube container with neon wireframe edges and faint circuit texture, with a few translucent smaller cube shards floating around it; subtle perspective grid, dot matrix and faint HUD ticks. On the right, large bold clean sans-serif headline in white: first line "踩了无数个坑，", second line "只推荐一个 Docker 最佳实践" with "Docker 最佳实践" highlighted in bright emerald (#34D939). A tiny light-gray micro-label top-left reads "TUTORIAL · JUPYTERHUB". Minimal, premium, neon-glow, sharp legible Chinese text, no typos, no watermark.

> ⚠️ 大多数模型**画中文易出错字**。若文字渲染不理想，改回"方案 A：纯背景 + 后期叠字"，最稳。

---

## 5. 使用建议

1. **首选流程**：用 **Prompt A**（纯背景）出图 → 导入 **Figma / 即时设计 / PS / 美图秀秀** → 在**右侧留白区**叠标题文字（白 + emerald 高亮），字号大、字重粗。文字清晰度和中文正确率 100% 可控。
2. **想一步到位**：用 **Prompt B**，选**即梦 / GPT-image**（中文支持较好）；出图后**务必逐字检查**主标题是否有错字/缺笔。
3. **比例**：所有 prompt 都按 **900×383 / 2.35:1** 设计。做次条小方图时，从中央裁 1:1 即可（主体在中间，裁切安全）。
4. **微调方向**（按需替换词）：
   - 想要更"云/K8s"：把"cube container"换成 `a cluster of interconnected glowing cube nodes`（节点网络感）。
   - 想要更"终端/代码"：加入 `faint lines of green code in the background`。
   - 想要更极简：删掉"HUD 刻度 / 网格"，只留主体 + 大留白。

---

## 6. 负面提示词（Negative Prompt，SD/即梦支持时填）

> text, words, letters, watermark, logo, signature, lowres, blurry, jpeg artifacts, extra fingers, deformed, cluttered, overexposed, flat, cartoonish, busy background, white background
