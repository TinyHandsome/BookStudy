---
link:
  - https://www.zhihu.com/question/2088428064954901581/answer/2088546122885226932
tags:
  - openai
  - LLM
---

> OpenAI正在把ChatGPT从一个“响应需求”的产品，改造成一套可以长期承担工作的Agent系统。
>
> - Dot是这套系统最明显的入口，或者说，它是Agent的主体。
>
> - OpenAI还在给它补齐整个工作环境。
>
> - 一个Agent最后好不好用、能不能稳定工作，越来越取决于模型之外的东西。
>
>   **Harness、Infra，以及Context。**Harness负责组织Agent的行为，Infra负责提供稳定的执行条件；至于Context，那是另外一层，决定Agent能不能认识“你”。
>
> - ==**AaaS（Agent as a Service）**==：AI看似开辟了新的时代，到头来还是重走了SaaS的老路。

1. **Dot**：这是一个你不用一直盯着、也不用每次重新交代背景的常驻Agent。

2. **ChatGPT Space**：简单来讲就是一个人和Agent的共享工作空间。它取代了原本的Library，“仓库”爆改“办公室”。你可以把文件、页面、演示文稿、表格和项目资料放进同一个Space里，再随时@ChatGPT、Codex或者Dot，让它们基于这些共享内容继续工作。

3. **GPT 6.1 Sol**：6.1 Sol是6 Sol的升级版，根据OpenAI给它的定位，它在复杂编程、电脑操作和专业工作上能做到接近GPT-6 Astra的水平，但价格仍然维持在Sol档（仅为Astra的五分之一）。

4. **Ultrafast**：该模式在Codex里Token生成速度最高可提升到8倍，约300 tokens/s；在API里最高可提升到6倍。

5. **Pro 500**：月费500美元，给你最多的可用额度（Plus的25倍），以及GPT-6 Astra的Ultrafast模式。

6. **Codex更新合集**：
   - **Codex Cloud**：现在Codex的云端开发环境可以直接复用，不用每次重新建一个干净沙箱
   - **Codex CLI**：也升级了，现在可以直接用语音和Codex对话，并且添加了一个新的/agents视图，可以把工作分给多个Agent，同时看不同任务做到哪了。
   - **Codex Security Cloud**：这次也迎来了一次大升级：它现在默认接入Daybreak Blue，可以调用更强的网络安全模型。
   - **Agents API**：这边也补上了computer use。
   
   ![img](%E5%A6%82%E4%BD%95%E8%AF%84%E4%BB%B7%20OpenAI%20%E5%9C%A8%209%20%E6%9C%88%2030%20%E6%97%A5%E5%8F%AC%E5%BC%80%E7%9A%84%20DevDay%202026%20%E4%B8%AD%E5%8F%91%E5%B8%83%E7%9A%84%E5%86%85%E5%AE%B9%EF%BC%9F.assets/v2-a09df800aaf2babee45fef43cfa2bb71_1440w.webp)
   
7. **Plugins**：OpenAI重做了插件的创建、提交和发现流程。插件还新增了基于MCP的事件触发能力。

8. 新的 **==Decisions API==** 可以让Luna在一组预设选项里快速做实时判断，用来做分类、路由，或者决定Agent下一步该做什么。:bulb: [[4-开发积累/Jev.md|这特么不就是抄Jev]]
