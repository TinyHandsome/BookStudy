---
sticker: lucide//webhook
tags:
  - requests
  - aiohttp
  - httpx
  - 中文乱码
  - upload
  - postman
banner: 3-踩坑笔记/29-调用aiohttp上传文件中文名出现乱码.assets/74262f3c2c2e4f8496a3074eb5f78472.png
---
# 调用aiohttp上传文件中文名出现乱码

> 我不会设置仅粉丝可见，不需要你关注我，仅仅希望我的踩坑经验能帮到你。如果有帮助，麻烦点个 :+1: 吧，这会让我创作动力+1 :grin:

- 摘要

  老老实实用aiohttp、用FormData，用 `data.add_field` 给文件加名字，然后用发post异步请求，发现服务器上收到的文件名是类似 `%E4%BD%A0%E5%A5%BD` 的URL编码，给我急的啊。**关键是，postman调用没问题啊！**

- 结论

  老样子先说结论：用 **httpx**，别用垃圾 **aiohttp**，迎刃而解，真的，信我。

- 思路

  - 为了解决这个问题，我卡卡狂搜，包括且不限于
    - `urllib.parse.quote` 给文件名保护住
    - 手动构建 **Content-Disposition** 头 `content_disposition = f'form-data; name="file"; filename="{quote(filename)}"; filename*="UTF-8\'\'{quote(filename)}"'`
    - 疯狂改 `content_type`
    - **等等，但就是不好使**
    
  - 当然百度、bing、google、github、stackflow我直接狂搜，就是搜不到，怎么回事，这个世界没人能解决了吗。发现了以下两个方案：
    1. `requests` 曾经出现过同样的问题，但是新版解决了，[参考链接](https://blog.csdn.net/lluozh2015/article/details/122414571)
    
       ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/74262f3c2c2e4f8496a3074eb5f78472.png)
    
    2. 还有一个说请求侧解决不了，要去服务器解决的，有点搞笑。。。
    
  - 当然aiohttp文档狂看，依然解决不了
  
  - 总的来说，问题的核心是：`Non-ASCll filename uploads don't comply with RFC 7578`，类似这样的问题。
  
  - 然后我突发奇想，试试 `httpx`，好使了好使了！:tada:，可恶啊，笨比 `aiohttp`，狗都不用，气死我了！:angry:


------


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
