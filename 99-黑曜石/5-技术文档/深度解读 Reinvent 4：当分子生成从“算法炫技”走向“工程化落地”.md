---
link:
  - https://mp.weixin.qq.com/s/DEN3uxakDDaksedMw4lGCQ
tags:
  - reinvent
  - 分子生成
---

相关论文：REINVENT 4: Modern AI–driven generative molecule design

## 1 分子生成的“热闹”与落地的“冷静”

近几年，分子生成模型几乎成了 AIDD（AI for Drug Development） 领域的显学：VAE、GAN、RNN、Transformer、Diffusion 轮番登场，从 SMILES 到 3D 构象，各种结构精巧的论文接连不断。

站在企业项目的一线视角，会发现几个尴尬的现实：

- 生成结果药化“一眼就不行”
- 工作流割裂
- 工程门槛高
- 评估与现实脱节

REINVENT 系列的特点在于：它从一开始就是 **在真实项目中被“边用边打磨”的工程化工具**

## 2 方法概览

> REINVENT 4 想做的不是“一个模型”，而是一座“分子生成工厂”

1. <font color="#f79646">**从“生成一个好分子”到“重排概率质量”** </font>

   REINVENT 4 把小分子设计明确建模为 **逆向设计 + 概率重排**：

   - **Prior（先验模型）**：在大规模公开库（如 ChEMBL）上无监督训练，学习“化学语法 + 常见药样结构分布”；
   - **Task-specific TL Agent**：用项目相关的小数据（某靶点活性分子、某骨架系列）对 Prior 微调，聚焦到任务相关的局部化学空间；【TL：迁移学习】
   - **RL / Curriculum Agent**：在 TL Agent 基础上叠加多目标打分函数，通过强化学习把概率质量 **从“普通区域”搬到“高分区域”**。

   ![image-20261012154803716](%E6%B7%B1%E5%BA%A6%E8%A7%A3%E8%AF%BB%20Reinvent%204%EF%BC%9A%E5%BD%93%E5%88%86%E5%AD%90%E7%94%9F%E6%88%90%E4%BB%8E%E2%80%9C%E7%AE%97%E6%B3%95%E7%82%AB%E6%8A%80%E2%80%9D%E8%B5%B0%E5%90%91%E2%80%9C%E5%B7%A5%E7%A8%8B%E5%8C%96%E8%90%BD%E5%9C%B0%E2%80%9D.assets/image-20261012154803716.png)

   本质上不是“凭空造分子”，而是：==“在一个合理的化学先验分布上，根据项目目标重排概率质量”。== 这与我们在项目里惯常的思路高度一致：**先学“化学常识” → 再学“本项目历史经验” → 最后围绕当前 TPP 做针对性优化。**

   > TPP（Target Product Profile，目标产品轮廓）：定义候选药物需要达成的药效、理化、ADMET 等属性指标，分为最低可接受标准与理想目标，作为 AIDD 分子生成与候选分子筛选的顶层目标约束。

2. <font color="#f79646">**四类生成模式：覆盖常见 CADD 任务**</font>

   REINVENT 4 把不同设计任务统一封装成四类 agent：

   - **Reinvent（标准 De Novo）**：从零生成分子，适合新靶点 Hit Finding；
   - **LibInvent（库设计/骨架装饰）**：给定 scaffold，自动生长 R-group，适合先导优化、R 位点枚举；
   - **LinkInvent（片段连接/骨架跃迁）**：给定两个“战头”（warheads），生成 linker 连接，适合 FBDD、PROTAC、scaffold hopping；
   - **Mol2Mol（类似物生成）**：条件生成器，输入参考分子，在相似空间内生成更优类似物，用于 Hit Expansion、专利绕开等。

   ![image-20261012155554954](%E6%B7%B1%E5%BA%A6%E8%A7%A3%E8%AF%BB%20Reinvent%204%EF%BC%9A%E5%BD%93%E5%88%86%E5%AD%90%E7%94%9F%E6%88%90%E4%BB%8E%E2%80%9C%E7%AE%97%E6%B3%95%E7%82%AB%E6%8A%80%E2%80%9D%E8%B5%B0%E5%90%91%E2%80%9C%E5%B7%A5%E7%A8%8B%E5%8C%96%E8%90%BD%E5%9C%B0%E2%80%9D.assets/image-20261012155554954.png)

3. <font color="#f79646">**与传统工具/方法的对比**</font>

   - 与 **传统虚筛 / docking** 相比：从“筛库”变成“造库 + 筛库”，可以主动扩展化学空间，而不是局限于已有库；
   - 与 **MMPDB、MEDCHEM Moves 等片段/规则引擎** 相比：前者更“像药化的大规模系统化枚举”，后者则是“从统计意义上学出来的整体生成器”；
   - 与 **新一代 Diffusion / 3D 生成模型** 相比：REINVENT 4 更偏“稳定可用的工程框架”，底层仍以 SMILES RNN/Transformer 为主，但 scoring、RL、工作流对接更成熟。

## 3 方法关键设计

> REINVENT 为什么“经得住项目折腾”？
>
> 这套设计的关键在于：**让 RL 更像是在“微调概率分布”而非“从零学一个黑箱策略”，大幅提升了稳定性和可控性。**

1. <font color="#f79646">**DAP 强化学习：用生成先验给 RL 系上一根“安全绳”**</font>

   REINVENT 的经典 RL 设计有三个要点：

   - Augmented Likelihood 增广似然

     $\log P_{\text{aug}}(T) = \log P_{\text{prior}}(T) + \sigma S(T)$

     其中 Prior 捕捉“合理结构”，S(T) 是多目标打分函数（活性/ADMET/对接/QED 等）归一化后的 reward

     > - $P_{\text{aug}}$：Augmented 增广分布（增广似然对应的概率）
     > - $P_{\text{prior}}$：Prior 预训练先验分布
     > - T：分子（molecule /trajectory，分子序列）
     > - $\sigma$：权重系数，用来控制打分项强度
     > - $S(T)$：**Score 函数**，就是 TPP 对应的分子打分 / 奖励函数（活性、ADMET 等综合评分

   - DAP Loss（Difference between Augmented and Posterior）

     优化目标变成

     $L(T) = \big(\log P_{\text{aug}}(T) - \log P_{\text{agent}}(T)\big)^2$

     即让当前 agent 逼近“先验 + 奖励”定义的目标分布，而不是直接做策略梯度。

     > - $L(T)$：损失函数 Loss，针对分子T
     > - $P_{\text{aug}}(T)$：增广分布（Augmented Likelihood）
     > - $P_{\text{agent}}(T)$：TL Agent 智能体模型输出的分子分布

   - 稳定性与“可回头”

     - Prior 是固定锚点，agent 再怎么经 RL 拉扯，也不会离合理化学空间太远；
     - 实验表明，即便先用 RL 把模型推向“巨无霸分子”，再反向 penalize 分子量，模型也能较快收敛回“小分子区域”——对真实项目很重要：**早期 Reward 配得不完美，后续仍有纠偏空间**。

2. :star: <font color="#f79646">**为什么仍以 RNN 为主？Transformer 是“按需选配”**</font>

   REINVENT 4 虽然支持 Transformer，但在默认配置中仍以 **SMILES RNN** 作为主力生成器，原因很实际：

   - **采样效率**：RL 训练需要大规模在线采样，RNN 对序列是 O(N)，标准 Transformer 则是 O(N²)，在 GPU 利用率和吞吐量上 RNN 仍然更高效；
   - **小数据迁移的鲁棒性**：对几十到几百条 TL 数据，RNN 的 inductive bias 更稳定、不易过拟合；
   - **与旧版工作流兼容**：LDHA 等已跑通项目也是基于 RNN 版本，这条路径被实践证明“够用+稳”。

   从工程角度看，这是在表达能力与易用性之间的一种 **审慎取舍**，而非“技术保守”。

3. <font color="#f79646">**Mol2Mol：一个在 200 亿相似对上训练出来的“局部雷达”**</font>

   - **“给定一个分子，如何在其附近合理游走”**，而不是随便做随机扰动。
   - 与默认 Prior 相比，RL 后的 agent 生成分子 **QED 明显提升、NLL 降低（模型更自信）**，且保持适度相似度；
   - 更适合作为“设计团队已有构想周围的扩展器”，而不是“完全凭空想象”。

3. <font color="#f79646">**工程化细节：Scoring 插件化 + 配置驱动**</font>

   ![image-20261012161242678](%E6%B7%B1%E5%BA%A6%E8%A7%A3%E8%AF%BB%20Reinvent%204%EF%BC%9A%E5%BD%93%E5%88%86%E5%AD%90%E7%94%9F%E6%88%90%E4%BB%8E%E2%80%9C%E7%AE%97%E6%B3%95%E7%82%AB%E6%8A%80%E2%80%9D%E8%B5%B0%E5%90%91%E2%80%9C%E5%B7%A5%E7%A8%8B%E5%8C%96%E8%90%BD%E5%9C%B0%E2%80%9D.assets/image-20261012161242678.png)
   
   框架本身可以长期维护，底层模型和打分器可以随项目演化而替换。

## 4 3 个案例

1. OMG——在质谱注释中做“聚焦生成”：给定 MS/MS 光谱和分子式，当谱图库无匹配时，如何生成一批 **同分子式、结构合理、可能解释谱图** 的候选结构？
2. LDHA——从 RL 生成到 in vivo 的闭环：在严谨的 docking 配置、类药性/合成可行性过滤、MD 与实验验证的多层约束下，**“RNN + RL + docking + 传统药化” 这条路是可以走到 in vivo 的**。
3. TDI 7 个项目中，MMPDB vs REINVENT4 vs 设计团队：MMPDB + REINVENT4 两种方法覆盖的化学空间，都远大于人类设计团队；两者本身也互补：前者像“系统化药化”，后者更适合提出“非直觉”但合理的新点子。

## 5 综合评价

**优势**：

1. 统一范式 + 工程化实现：从 Prior/TL/RL 到 scoring 插件化，REINVENT 提供的是一套 **可持续维护的分子生成工厂**，而不仅是单一模型
2. 与药化团队的互补性得到“第三方背书”：Sun & Huggins 的结果
3. 可与多种下游评价/实验无缝衔接：先用 REINVENT 生成 + docking/QED 预筛，再用 MD、free energy、合成可行性评估、体外体内实验逐层收紧。
4. 支持局部、受约束设计，而不是仅有 De Novo

**劣势**：==【打分导致过拟合reward hacking，1D-smiles局限，药物预训练数据的局限，】==

1. **“Scoring is all you need（也是 All you can break）”**：scoring 的偏差会在 RL 中被放大——如果 docking、QSAR 或合成可行性模型有系统性错误，REINVENT 会非常高效地学会“刷分”
2. **1D 表达和 3D 现实之间的缝隙**：以 SMILES 为主的生成，先天对 3D 构象、多态 pocket 的适配不敏感，需要依赖 docking/MD 做事后筛选。此外，对 GPCR、多态酶等构象复杂靶点，这种“2D 生成 + 3D 修正”的流程可能力不从心。
3. **数据偏倚与化学空间“玻璃天花板”**：Prior 主体来自 ChEMBL、SureChEMBL 等公开/专利库，天然偏向“既有药物化学风格”；对想刻意做“反药物化学”的特定项目（如共价 warhead、分子胶等），需要额外的 Prior/TL 设计来打破这种偏置。
4. **对项目团队文化的依赖**：对AI的信任问题，以及AI之后的流程问题。

## 6 实际项目启示

1. 在 pipeline 中的定位
   - Design 环节的“候选空间放大器”
   - Hit → Lead 阶段的“局部强化 + 创新跳跃”
   - 与 MMPDB 的组合拳
2. 对后续模型设计的启发
   - 先有可靠 scoring，再追求 fancy 生成架构
   - 生成模型要提供“可控的多样性”，而不是极端探索
   - 片段/规则引擎与生成模型可以长期共存

## 7 不足与未来方向

1. 局限
   - REINVENT 4 本身仍然以 1D SMILES 为主，3D 信息主要靠下游 docking/MD 间接引入；
   - 大规模前瞻性实验（prospective）验证少，很多经验来自企业内部未公开项目；
   - Sun & Huggins 的分析集中在 QED、相似度、合成步数、结构警报等“化学空间层面”，没有触及真实项目中的“命中率/TPP 达标率”等更终极指标。
2. 更深一层的思考
   - 评估体系的重构：当前仍停留在“点子层面的覆盖率”，下一步需要往“实验结果层面的增益”走。
   - 数据偏倚与私有数据的价值：Prior 需要更高质量的数据，尤其是大量的 **失败结构**
3. 未来的演化方向
   - **底层生成器 3D 化**：用 3D Diffusion / Equivariant GNN 替换 RNN 部分，同时保留 DAP RL + scoring 插件体系；
   - **与 retrosynthesis / 反应网络做联合优化**：把“是否可在 N 步内合成”直接纳入 Reward，而不是事后过滤；
   - **多模态条件生成**：把蛋白 pocket、MS 谱图、表型 readout 等多模态信息显式作为条件；OMG 已经是一个良好开端。

## 8 QA

> 为什么现在的“显学”是 Transformer，Reinvent 4 却还抱着 RNN 不放？

这其实是**学术界与工业界的错位**。

- **Transformer 的代价：** 在 GPT 这种自回归 Transformer 中，Cache 机制虽然能加速，但在 RL 这种需要不断 Update 权重的场景下，维护成本极高。
- **数据饥渴：** 在药物研发的细分领域（比如设计一个全新的 PROTAC Linker），你可能只有几十个样本做迁移学习。Transformer 这种参数巨兽在这种小数据上几乎必定过拟合（Overfitting），通过死记硬背 Loss 降得很低，但生成能力归零。而 RNN 的参数量少，更适合这种 **Few-shot Learning** 场景。

> Reinvent 4 生成的分子是否会面临“多样性（Diversity）”不足？

在做 R-group Enumeration 时，可能会面临：生成的 100 个分子里，80 个都是甲基、乙基或者氯原子，翻来覆去。这通常由三个原因导致：

- **Exploitation vs. Exploration（利用与探索）：** RL 的本性是贪婪的。一旦发现“甲基”能拿高分，Agent 就会疯狂生成甲基。

- **Sigma ($\sigma$) 参数的陷阱：** Reinvent 的 Loss 中有一个 $\sigma$ 参数，用于控制 Agent 和 Prior 的距离。$\sigma$ 设得太小，Agent 不敢越雷池一步；$\sigma$ 设得太大，Agent 容易坍缩到局部最优。

- **Temperature（采样温度）：** 在 Softmax 采样时，如果 Temperature < 1.0，模型会倾向于选择概率最高的 Token，导致生成的分子千篇一律。

  **对策：** 在 Config 中调高 Temperature（如 1.2），或者强制开启 **Diversity Filter**（Reinvent 4 自带功能，惩罚重复骨架），逼迫模型去“冒险”。

> Reinvent 4 + Docking Score：看起来很美，实则是灾难？

理论上，把 Docking 打分作为 Reward 是最完美的 CADD+AIDD 结合。但在实操中，这往往是噩梦：

- **稀疏奖励与噪声：**Docking 打分对构象极其敏感，噪声巨大。RL 算法极其聪明，它会迅速学会 **Reward Hacking（奖励黑客）**——生成一些奇形怪状、张力极大的分子，刚好卡进蛋白口袋的缝隙骗取高分，但实际上根本合成不出来，或者稍微一动就跑了。

- **计算黑洞：** RL 需要百万次采样。百万次 Docking 计算可能需要数周，直接拖垮项目进度。 

  **对策：** 必须使用 **Curriculum Learning（课程学习）**。先用快速的 2D 描述符或 ML 模型跑前 80% 的 Epoch，把化学空间缩小到靠谱的范围内，最后 20% 再引入 Docking 微调。

> 最大的痛点：手性与立体化学的缺失

Reinvent 4 基于 SMILES，本质上是 1D/2D 模型。虽然它能生成 @ 符号表示手性，但它**不理解 3D 空间**。它可能会生成一个打分极高的分子，但该分子的 3D 构象因为位阻根本无法存在。这是所有基于语言模型（SMILES-based）的通病，目前只能靠后处理（Post-processing）过滤，或者转向基于 Graph/3D 的生成模型（但后者目前在成药性上表现更差）。

> 对于“Reinvent 4 这种需要每次根据任务训练模型”的难度曲线，企业该如何应对？它不能像 AlphaFold 那样训练一次到处用吗？

这是一个根本性的误区。AlphaFold 是**预测模型**（学习物理规律），而 Reinvent 是**优化模型**（寻找特定解）。每个项目的靶点口袋不同、ADMET 需求不同，意味着**目标函数（Reward）完全不同。 企业应对策略： 不要指望药化专家去跑代码。AIDD 团队需要做的是“封装”**。将 Reinvent 4 包装成内部平台，预设好几种标准的 Reward 模板（如“类药性模板”、“穿脑模板”、“高活性模板”）。项目组只需要上传活性预测模型（Oracle）和参考分子，后台自动配置 RL 参数。Reinvent 4 的 TOML 配置文件设计正是为了这种 MLOps 流程准备的。

> Reinvent 4 的发展对于现在构建分子生成模型有哪些启发？

1. **Scoring Is All You Need：** Reinvent 4 证明了生成模型本身其实可以很简单（就是个 RNN），**真正的瓶颈在于 Reward Function 的定义**。AIDD 的下一个突破点不在于发明更好的生成器，而在于开发更准、更快、更通用的 ADMET 和活性预测模型作为 Oracle。
2. **模块化与解耦：** Reinvent 4 将 Prior、Scoring、Learning Strategy 完全解耦的设计，是未来 AIDD 软件架构的标杆。这允许我们随时替换掉底层的 RNN 为 Transformer，或者替换打分函数，而不用重写整个系统。

## 9 小结

> REINVENT 4 带来的，其实是一种“生成式药物设计的组织方式”

- **生成模型本身不是主角**——真正决定价值的是
  - Prior 与 TL 如何定义项目相关的化学空间，
  - scoring 如何刻画 TPP 与风险，
  - 药化/CADD 如何在 DMTA 循环中用好这些候选。Design-Make-Test-Analyze，设计-合成-测试-分析
- MMPDB/REINVENT4 与药化设计团队是互补关系，而不是替代关系
  - 前者系统、全面，后者有直觉与经验；
  - 组合起来，才能既不局限于舒适区，又不被“AI 伪影”带偏。
- 对一线 AIDD/CADD 团队而言，也许更现实的问题不是“要不要上 REINVENT 4”，而是：
  - 我们的 scoring、过滤和实验验证体系，已经准备好承接一台“高通量、可配置的分子生成工厂”了吗？
  - 如果答案是“是”，那么 REINVENT 4 + MMPDB + 好的团队文化，就很可能在未来几年里，悄悄改变许多项目的 ideation 方式。

## 10 Reference

1. Martin, M. R. & Hassoun, S. Optimized De Novo Molecular Generation (OMG) for Mass Spectra Annotation Using Transfer and Reinforcement Learning. Anal. Chem. 97, 20734–20742 (2025).
2. Gong, Q. et al. Machine-Learning-Driven Discovery of N -Phenylbenzenesulfonamides as a Novel Chemotype for Lactate Dehydrogenase A Inhibition with Anti-Pancreatic Cancer Activity. J. Med. Chem. 68, 14384–14404 (2025).
3. Sun, S. & Huggins, D. J. Comparing Molecules Generated by MMPDB and REINVENT4 with Ideas from Drug Discovery Design Teams. *J. Chem. Inf. Model.***65**, 4219–4231 (2025).
