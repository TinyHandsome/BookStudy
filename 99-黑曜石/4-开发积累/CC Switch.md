## 问题

### 1. 配置new-api报错400

因为需要在cc-switch中设置OpenAI的路由，不能直接用Anthropic，可能是vLLM做了适配，所以直接配置vLLM的地址没问题？也不用额外修改 new api 里面的配置，透传啊啥的都不用管，直接就能正常调用了，还能配置不同的模型映射，在cc中切换模型。

![image-20261006134307722](CC%20Switch.assets/image-20261006134307722.png)