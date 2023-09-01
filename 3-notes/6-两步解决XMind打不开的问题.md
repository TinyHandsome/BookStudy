# 两步解决XMind打不开的问题

## 写在前面

- 做这件事的原因：
  1. 对XMind进行神秘处理之后，发现XMind就打不开了
  2. 然后我研究了半天，发现在XMind.ini中把`-javaagent:D:\XMind\XMindCrack.jar`这行删掉就没问题
- 如果有错别字呢，哪里写错了呢，请在评论区告诉我嗷，同时，可能会有一些奇奇怪怪的符号夹在文字中，这是因为我用的是MarkDown语法，其中一些符号可能在这个平台（比如CSDN）不支持呢。

## 解决方案

1. 把你的`XMindCrack.jar`放到安装目录下，我是新建了一个文件夹`aa\XMindCrack.jar`

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/2020122109232399.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

2. 将`XMind.ini`中的绝对路径改为相对路径：`-javaagent:aa\XMindCrack.jar`

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201221092422524.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

------


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822`
- :avocado: 我的思否：`https://segmentfault.com/u/liyj`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
