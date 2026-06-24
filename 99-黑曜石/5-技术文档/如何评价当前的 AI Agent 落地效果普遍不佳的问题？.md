---
tags:
  - agent
reference:
  - https://www.zhihu.com/question/13476251758/answer/1898359865941931619
  - https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-llm-agents
sticker: emoji//1f916
banner: 5-技术文档/如何评价当前的 AI Agent 落地效果普遍不佳的问题？.assets/v2-1bf53514a6db8a0bdb909c0d67cc3c2c_1440w-17458047799131.webp
---

# 如何评价当前的 AI Agent 落地效果普遍不佳的问题？

## 1 什么是AI Agent？

### AI Agent 概念的澄清

AI Agent也叫AI代理，AI智能体，经常会听到三个词：**Agent，AI Agent和Agentic AI。**用来形容智能体达到的级别。

**Agent：**家里的热水器恒温器就是个典型Agent。它感知温度（环境感知），开关加热系统（采取行动），保持设定温度（实现目标）。它只是按照预设规则工作，不需要任何AI能力。

> **Agent**是任何可以被视为通过**传感器**感知其环境并通过**执行器**作用于该环境的事物。
>
> —— Russell & Norvig，《人工智能：现代方法》（2016）

**AI Agent：**它是由AI驱动Agents，它们不再只是遵循简单规则，而是能利用机器学习、自然语言处理等AI技术做决策，它能从数据中学习，适应新情况，随时间变得更聪明。例如Siri、小爱同学这类虚拟助手就是AI Agents。它们能理解你的语音指令，学习改进回答质量，执行设置闹钟、播放音乐等任务。

**Agentic AI：**Agentic AI把AI agents带到了一个全新境界，让它们更加自主、适应性强且主动。与被动等待指令的普通AI agents不同，Agentic AI能自主规划、决策，**无需人类指示**就能行动。一个管理智能家居的Agentic AI系统不仅能调节温度，还能在食物快用完时自动下单，安排家电维护，优化能源使用——全程无需你动手。

这个Agentic AI在笔者看来就是AI Agent的一个另一个阶段而已，只是创造了一个名词，也有人将AI Agent的特点做了总结，即有下面的10个特点：

![AI Agent的10个特点](%E5%A6%82%E4%BD%95%E8%AF%84%E4%BB%B7%E5%BD%93%E5%89%8D%E7%9A%84%20AI%20Agent%20%E8%90%BD%E5%9C%B0%E6%95%88%E6%9E%9C%E6%99%AE%E9%81%8D%E4%B8%8D%E4%BD%B3%E7%9A%84%E9%97%AE%E9%A2%98%EF%BC%9F.assets/v2-1bf53514a6db8a0bdb909c0d67cc3c2c_1440w-17458047799131.webp)

### AI Agent和传统的Chaining/RPA的区别

刚开始接触AI Agent肯定觉得和传统的RPA很像，和流程自动化差不多。其实还有区别的，毕竟传统的流程自动化根本不需要大模型，只要if/else的条件判断即可。

![AI Agent和Chain的区别](%E5%A6%82%E4%BD%95%E8%AF%84%E4%BB%B7%E5%BD%93%E5%89%8D%E7%9A%84%20AI%20Agent%20%E8%90%BD%E5%9C%B0%E6%95%88%E6%9E%9C%E6%99%AE%E9%81%8D%E4%B8%8D%E4%BD%B3%E7%9A%84%E9%97%AE%E9%A2%98%EF%BC%9F.assets/v2-feb36ca0b6c40ad3575d0efb7e681aca_1440w.webp)

### AI Agent的不同阶段

就和前面将的AI Agent和Agentic AI一样，人类的想象力是无限的，即便没有实现，人类依然依靠想想力将AI Agent的能力做了描述，分为5个层次，我们目前达到的还是Level 2或者level 3，我们所说的Agentic AI就是AI Agent的4、5层面的问题。

![img](%E5%A6%82%E4%BD%95%E8%AF%84%E4%BB%B7%E5%BD%93%E5%89%8D%E7%9A%84%20AI%20Agent%20%E8%90%BD%E5%9C%B0%E6%95%88%E6%9E%9C%E6%99%AE%E9%81%8D%E4%B8%8D%E4%BD%B3%E7%9A%84%E9%97%AE%E9%A2%98%EF%BC%9F.assets/v2-13818c76f0f2046bc43fca92cad2a4cb_1440w.webp)

### AI Agent的基本构成

AI Agent的构成还是要看它需要做什么，我们讲 Agents 与环境交互，通常由几个重要组件组成：

- **环境（Environment）** — Agent交互的世界
- **传感器（Sensors）** — 用于观察环境，Agent可以通过文本输入观察环境（因为LLM通常是文本模型）
- **执行器（Actuators）** — 用于与环境交互的工具，通过使用工具（如网络搜索）执行特定操作
- **效应器（Effectors）** — 决定如何从观察转化为行动的"大脑"或规则，即通过工具和记忆增强的大模型做思考决策

![img](%E5%A6%82%E4%BD%95%E8%AF%84%E4%BB%B7%E5%BD%93%E5%89%8D%E7%9A%84%20AI%20Agent%20%E8%90%BD%E5%9C%B0%E6%95%88%E6%9E%9C%E6%99%AE%E9%81%8D%E4%B8%8D%E4%BD%B3%E7%9A%84%E9%97%AE%E9%A2%98%EF%BC%9F.assets/https%253A%252F%252Fsubstack-post-media.s3.amazonaws.com%252Fpublic%252Fimages%252Fc3177e12-432e-4e41-814f-6febf7a35f68_1360x972.png)

**选择要采取的行动，AI Agent有一个重要组件：规划能力，规划能力的本质就是思考能力。**即面对感知到的环境，和执行器的反馈，基于你的目的该如何做判断决策，你想的对——这个就是LLM的**提示词工程（[Prompt Engineering](https://zhida.zhihu.com/search?content_id=724216113&content_type=Answer&match_order=1&q=Prompt+Engineering&zhida_source=entity)）**，AI Agent里的规划能力，本质就是提示词工程的升级，达到了自主行动的程度就是规划。

规划能力，根据实际的需求，根据自主能力的级别也可以有不同的Agent，具体如下图。

![img](%E5%A6%82%E4%BD%95%E8%AF%84%E4%BB%B7%E5%BD%93%E5%89%8D%E7%9A%84%20AI%20Agent%20%E8%90%BD%E5%9C%B0%E6%95%88%E6%9E%9C%E6%99%AE%E9%81%8D%E4%B8%8D%E4%BD%B3%E7%9A%84%E9%97%AE%E9%A2%98%EF%BC%9F.assets/https%253A%252F%252Fsubstack-post-media.s3.amazonaws.com%252Fpublic%252Fimages%252F98d5ce2c-e9ba-4f67-bc11-e62983f890a1_1736x1140.png)

一个系统越是由LLM决定其行为方式，就越具有"自主性"，接下来的部分，我们将通过AI Agent的三个主要组成部分——**记忆**、**工具**和**规划**——探讨各种自主行为方法。

## 2 AI Agent——记忆 Memory

大模型就像熊瞎子掰苞米，每次推理都是独立的，如果什么都不做，每问一个问题，对于LLM来讲就是一次单独的推理，它是不知道上次推理的内容和结果的，即它根本不会执行任何记忆行为。

![img](%E5%A6%82%E4%BD%95%E8%AF%84%E4%BB%B7%E5%BD%93%E5%89%8D%E7%9A%84%20AI%20Agent%20%E8%90%BD%E5%9C%B0%E6%95%88%E6%9E%9C%E6%99%AE%E9%81%8D%E4%B8%8D%E4%BD%B3%E7%9A%84%E9%97%AE%E9%A2%98%EF%BC%9F.assets/v2-2283d873a31bf1de673300033a3de689_1440w.webp)

那该怎么办呢，对标人类的记忆习惯，AI Agent的记忆也分为短期和长期，而且实现的方法并不相同，我们来分别研究下为啥是这样的。

![img](%E5%A6%82%E4%BD%95%E8%AF%84%E4%BB%B7%E5%BD%93%E5%89%8D%E7%9A%84%20AI%20Agent%20%E8%90%BD%E5%9C%B0%E6%95%88%E6%9E%9C%E6%99%AE%E9%81%8D%E4%B8%8D%E4%BD%B3%E7%9A%84%E9%97%AE%E9%A2%98%EF%BC%9F.assets/https%253A%252F%252Fsubstack-post-media.s3.amazonaws.com%252Fpublic%252Fimages%252F81dfc42c-2cbd-4a1d-9430-4ac2518d4490_936x696.png)

### 短期记忆（Short-term memory）

前面说大模型是没有记忆力的，这时候你可能就好奇了，为啥我用大模型的时候没有这个问题，它明明记得我以前说的话，这个原理就是大模型的**短期记忆。**本质就是每次会话的时候，同时通过prompt将以往的问题和答案提前输入，并加上本次的问题一起给大模型做推理，所以在会话场景下**一个大模型的真正上下文长度是：以往的问题和答案的长度+本次问题的长度。**可以用下面的图像形象的理解。

![img](%E5%A6%82%E4%BD%95%E8%AF%84%E4%BB%B7%E5%BD%93%E5%89%8D%E7%9A%84%20AI%20Agent%20%E8%90%BD%E5%9C%B0%E6%95%88%E6%9E%9C%E6%99%AE%E9%81%8D%E4%B8%8D%E4%BD%B3%E7%9A%84%E9%97%AE%E9%A2%98%EF%BC%9F.assets/https%253A%252F%252Fsubstack-post-media.s3.amazonaws.com%252Fpublic%252Fimages%252F66e6afca-afc6-4a3f-a4b0-4d11e050c558_1204x616.png)

我们可以看到，**短期记忆的实现方式就是使用提示词工程（Prompt Engineering），限制就是大模型的上下文长度。**

### 长期记忆（Long-term memory）

前面我们讲了，短期记忆是有限制是大模型的上下文长度，但是有些信息是不能被忘记的，需要在会话中一直生效，或者数据量特别大，那该怎么办呢？有办法，那就是通过 **向量数据（Vector Database）** 来实现，每次会话，查询问题并将得到匹配的结果作为上下文补充进去，同时也可以同时支持多个会话。

![img](%E5%A6%82%E4%BD%95%E8%AF%84%E4%BB%B7%E5%BD%93%E5%89%8D%E7%9A%84%20AI%20Agent%20%E8%90%BD%E5%9C%B0%E6%95%88%E6%9E%9C%E6%99%AE%E9%81%8D%E4%B8%8D%E4%BD%B3%E7%9A%84%E9%97%AE%E9%A2%98%EF%BC%9F.assets/https%253A%252F%252Fsubstack-post-media.s3.amazonaws.com%252Fpublic%252Fimages%252F47304195-33bd-4637-b18e-ad7c57c8aa2c_1028x756.png)

## 3 AI Agent——工具 Tools

### 工具的研究情况和工具选择

工具允许LLM与外部环境（如数据库）交互或使用外部应用程序，这部分研究也很多，这部分包括2个话题，一个是工具本身，另一个就是怎么选择工具。

![img](%E5%A6%82%E4%BD%95%E8%AF%84%E4%BB%B7%E5%BD%93%E5%89%8D%E7%9A%84%20AI%20Agent%20%E8%90%BD%E5%9C%B0%E6%95%88%E6%9E%9C%E6%99%AE%E9%81%8D%E4%B8%8D%E4%BD%B3%E7%9A%84%E9%97%AE%E9%A2%98%EF%BC%9F.assets/https%253A%252F%252Fsubstack-post-media.s3.amazonaws.com%252Fpublic%252Fimages%252F0f533a89-9af8-482c-aac6-f1806801b725_1284x820.png)

工具选择方式常见的有两种，一种是框架固定后按照固定顺序执行，另一种是由一个模型先判断选择什么工具来执行。

![img](%E5%A6%82%E4%BD%95%E8%AF%84%E4%BB%B7%E5%BD%93%E5%89%8D%E7%9A%84%20AI%20Agent%20%E8%90%BD%E5%9C%B0%E6%95%88%E6%9E%9C%E6%99%AE%E9%81%8D%E4%B8%8D%E4%BD%B3%E7%9A%84%E9%97%AE%E9%A2%98%EF%BC%9F.assets/v2-5738b88f26ad6711bd1f38ceac74845a_1440w.webp)

**例1：固定顺序——框架固定的情况下**

固定的议题搜索，首先将问题导入LLM1，由它按照固定工具输入格式输出搜索内容；然后按照计划执行（顺序并行均可），最后通过LLM2导出交给LLM3总结出答案。

**例2：模型做工作选择**

对于非固定需求的输入，首先将问题导入训练好的工具选择模型LLM1，由它决策使用什么工具，并根据工具的反馈决策下一步行动，是换工具继续执行还是结束工具使用；然后由LLM2总结出答案。

以上那种方案更佳，取决于具体的使用场景。

### Toolformer

这就要引入Meta的一个论文了：[Toolformer: Language Models Can Teach Themselves to Use Tools](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/2302.04761)，Toolformer也是一个模型，它是一种训练用于决定调用哪些API以及如何调用的模型。下面是一个例子，通过一个推理活动判断这个活动需要什么样的工具执行这个行动。

![img](%E5%A6%82%E4%BD%95%E8%AF%84%E4%BB%B7%E5%BD%93%E5%89%8D%E7%9A%84%20AI%20Agent%20%E8%90%BD%E5%9C%B0%E6%95%88%E6%9E%9C%E6%99%AE%E9%81%8D%E4%B8%8D%E4%BD%B3%E7%9A%84%E9%97%AE%E9%A2%98%EF%BC%9F.assets/v2-938c911b40450896e0c07eb5fbfbd01f_1440w.webp)

### MCP

工具是主体框架的重要组成部分，允许LLM与世界交互并扩展其能力。然而，当你有许多不同的API时，启用工具使用变得麻烦，因为任何工具都需要：

- 手动**跟踪**并提供给LLM
- 手动**描述**（包括其预期的JSON模式）
- 当其API变更时手动**更新**

为了使工具更容易在任何给定的主体框架中实现，Anthropic开发了模型上下文协议（MCP），标准化了对github服务的API访问。它由三个组件组成：

- MCP **Host** — 管理连接的LLM应用程序（如Cursor）
- MCP **Client** — 与MCP Host保持1:1连接
- MCP **Server** — 向LLM提供上下文、工具和功能

![动图](%E5%A6%82%E4%BD%95%E8%AF%84%E4%BB%B7%E5%BD%93%E5%89%8D%E7%9A%84%20AI%20Agent%20%E8%90%BD%E5%9C%B0%E6%95%88%E6%9E%9C%E6%99%AE%E9%81%8D%E4%B8%8D%E4%BD%B3%E7%9A%84%E9%97%AE%E9%A2%98%EF%BC%9F.assets/v2-aa52cdbb57a9ba58140bce491c430274_720w.webp)

这个框架通过连接到任何大模型的应用程序都可以使用的MCP服务器，使创建工具变得更容易。因此，当你创建一个与GitHub交互的MCP服务器时，任何支持MCP的LLM应用程序都可以直接使用它，这也给了其他厂家思路，可以拓展到自己的业务场景中。

## 4 AI Agent——规划 Planning

### 规划能力需要什么

前面讲到了模型的记忆力、工具的使用，但是什么时候开始调用工具，取决于对于这个业务场景的设计规划，这个能力就是所谓的规划能力。AI Agents中的规划涉及将给定任务分解为可执行的步骤。

**规划：一项复杂任务通常包括多个子步骤，AI Agent 需要提前将一项任务分解为多个子任务。**

1. **子目标与分解（Subgoal and decomposition）**：将复杂任务分解为更小、更易于处理的子目标，从而实现对复杂任务的高效处理。
2. **反思与完善（Reflection and refinement）**：对历史的动作进行自我批评和自我反思，从错误中吸取教训，并为未来的步骤进行改进，从而提高最终结果的质量。

想做到上面的要求需要有两个能力：

**推理：**指的是一步一步思考，即思考过程即是任务分解的过程

**行动：**需要观察环境收集反馈，这个是一个动态的交互过程

根据需求可能单独需要推理或者行动，也可能同时需要，甚至完成后还需要反思行动的结果，所以也就有了后来规划的常见的方案，我们后面逐一讲解。

![img](%E5%A6%82%E4%BD%95%E8%AF%84%E4%BB%B7%E5%BD%93%E5%89%8D%E7%9A%84%20AI%20Agent%20%E8%90%BD%E5%9C%B0%E6%95%88%E6%9E%9C%E6%99%AE%E9%81%8D%E4%B8%8D%E4%BD%B3%E7%9A%84%E9%97%AE%E9%A2%98%EF%BC%9F.assets/v2-787d2dc07f0651cb96ed82a535a8ea1f_1440w.webp)

### 推理（Reasoning）

推理常见的方式是思维链或者思维树，在训练LLM时，我们可以给它提供足够数量的包含类似思考例子的数据集，或者LLM可以发现自己的思考过程。这种推理行为大致可以通过两种选择：对大模型进行**微调**或特定的**提示工程**。

![img](%E5%A6%82%E4%BD%95%E8%AF%84%E4%BB%B7%E5%BD%93%E5%89%8D%E7%9A%84%20AI%20Agent%20%E8%90%BD%E5%9C%B0%E6%95%88%E6%9E%9C%E6%99%AE%E9%81%8D%E4%B8%8D%E4%BD%B3%E7%9A%84%E9%97%AE%E9%A2%98%EF%BC%9F.assets/v2-4c94028352b3f1d1d0ec98a344e0d882_1440w.webp)

### 推理和行动（ReAct）

思维链仅专注于推理，但是和环境并没有交互（行动），结合这两个过程的首批技术之一被称为ReAct（推理和行动），ReAct通过精心设计的提示词工程来实现这一点。ReAct提示描述了三个步骤：

- **思考** - 关于当前情况的推理步骤
- **行动** - 要执行的一组行动（例如，工具）
- **观察** - 关于行动结果的推理步骤

![img](%E5%A6%82%E4%BD%95%E8%AF%84%E4%BB%B7%E5%BD%93%E5%89%8D%E7%9A%84%20AI%20Agent%20%E8%90%BD%E5%9C%B0%E6%95%88%E6%9E%9C%E6%99%AE%E9%81%8D%E4%B8%8D%E4%BD%B3%E7%9A%84%E9%97%AE%E9%A2%98%EF%BC%9F.assets/v2-ea702b3ac2596343a4b0f86c0589c59b_1440w.webp)

可以看到，这样的方案与具有预定义固定步骤的Agents相比，这个框架使LLM能够展示更多自主的自主行为。

### 反思（Reflexion）

没有人（甚至使用ReAct的LLM）能完美执行每项任务。只要你能对过程进行反思，失败就是过程的一部分，但是这个过程在ReAct中缺失，而Reflexion正是解决这一问题的技术，它是一种帮助agents从先前失败中学习的技术。

![img](%E5%A6%82%E4%BD%95%E8%AF%84%E4%BB%B7%E5%BD%93%E5%89%8D%E7%9A%84%20AI%20Agent%20%E8%90%BD%E5%9C%B0%E6%95%88%E6%9E%9C%E6%99%AE%E9%81%8D%E4%B8%8D%E4%BD%B3%E7%9A%84%E9%97%AE%E9%A2%98%EF%BC%9F.assets/https%253A%252F%252Fsubstack-post-media.s3.amazonaws.com%252Fpublic%252Fimages%252Fb22cf4df-37b1-4359-8417-084a77248232_1176x588.png)

## 5 AI Agent的落地方案

### 多Agents方案

我们一直聊的都是单Agent，它存在几个问题：工具过多可能使选择复杂化，实际任务可能需要专业化的工具，所以我们可以转向多Agent框架，其中多个agents（每个都有访问工具、记忆和规划的能力）相互交互并与其环境交互。

![img](%E5%A6%82%E4%BD%95%E8%AF%84%E4%BB%B7%E5%BD%93%E5%89%8D%E7%9A%84%20AI%20Agent%20%E8%90%BD%E5%9C%B0%E6%95%88%E6%9E%9C%E6%99%AE%E9%81%8D%E4%B8%8D%E4%BD%B3%E7%9A%84%E9%97%AE%E9%A2%98%EF%BC%9F.assets/v2-c68100b2626b3f325ad48123af27d6f5_1440w.webp)

### AI Agents几种常见的类型

- Simulations Agent：模拟智能体，在模拟器中包括一个 and/or 多个 Agent 相互作用。
- Automatic Agent：自动化智能体，给定一个 and/or 多个长期目标，独立执行这些目标。
- Multimodal Agent：多模态智能体，除 NLP 信息外还可以拓展到图像，语音，视频的交互。

简单举个stanford论文里（[Generative Agents: Interactive Simulacra of Human Behavior](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/2304.03442)）的例子，这个就是多Agents的部署，它们都可以自主行为。

![img](%E5%A6%82%E4%BD%95%E8%AF%84%E4%BB%B7%E5%BD%93%E5%89%8D%E7%9A%84%20AI%20Agent%20%E8%90%BD%E5%9C%B0%E6%95%88%E6%9E%9C%E6%99%AE%E9%81%8D%E4%B8%8D%E4%BD%B3%E7%9A%84%E9%97%AE%E9%A2%98%EF%BC%9F.assets/v2-b4eab3e269afff07c391cf4f3bc6a502_1440w.webp)

### AI Agents的模块化组件

多Agent系统，无论选择什么框架它们通常由几个部分组成，包括其档案、环境感知、记忆、规划和可用行动。

![img](%E5%A6%82%E4%BD%95%E8%AF%84%E4%BB%B7%E5%BD%93%E5%89%8D%E7%9A%84%20AI%20Agent%20%E8%90%BD%E5%9C%B0%E6%95%88%E6%9E%9C%E6%99%AE%E9%81%8D%E4%B8%8D%E4%BD%B3%E7%9A%84%E9%97%AE%E9%A2%98%EF%BC%9F.assets/https%253A%252F%252Fsubstack-post-media.s3.amazonaws.com%252Fpublic%252Fimages%252F16d08b46-3c57-434e-aa73-7a1e516305c7_1232x656.png)

## 6 思考

### 为什么AI Agent都雷声大雨点小

AI Agent Demo表现都是非常惊艳，但是后面就没动静了，其实就是因为给出的很多例子都都是经过精挑细算的。然而实际应用则会前面一些步骤出现偏差，后续的执行步骤逐渐越跑越远。

其实说白了只有一个问题，就是**大模型本身能力很重要**，不管是规划还是执行，都依赖模型本身的能力，为啥能用的只有很窄的范围呢，其实可能是名字的问题：如果将AI Agent换成个名字，叫AI Workflow就好一些了吧，Workflow本身就是个很好用的应用，补上AI能力依然好用。

### AI Agent落地效果要看场景

想回答AI Agent适合什么有点难，但是不适合什么场景相对简单。

**监督学习：**对于 Classification、Regression 的监督 Supervised Learning 任务，AI Agent生成一步即决定能否完成任务，因为与规划 Planning 无关，并不适用我们说的Agent。

**多步序列决策 Sequential decision making ：**这个有点说不大上来，咨询过专家讲说这个问题需要通盘考虑，因此需要结合 Planning、RL 等算法，制定 or 学习最优策略，但是目前大部分的大模型没有专门训练多步决策，错误累积并不好解决。

其实这个就很像大模型下围棋了，大模型下围棋确实不如基于深度学习的AlphaGo，主要原因可能就是因为大模型本身是自回归，每次都是做了**一次预测**，但是AlphaGo每次落子的背后其实是有过多次模拟的，可大模型的资源消耗能让它做到每步都多次模拟吗？

*继续期待学术上的突破。*



































