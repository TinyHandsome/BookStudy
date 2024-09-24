# Cmder启动WSL中的Ubuntu出现复制粘贴异常

## 写在前面

- 环境：win10、cmder、wsl（注意不是2，因为我的系统版本不支持2）

- 问题：

  1. cmder启动cmd、dos都正常使用复制粘贴功能，粘贴可以用 `CTRL+V`，也可以用鼠标右键，很舒服
  2. cmder启动cmd后，输入ubuntu（这里我把wsl的ubuntu路径放到系统path中去了），这种方式启动的ubuntu shell中可以正常粘贴
  3. 配置cmder中的 **startup** 和 **tasks** ，无论怎么配置，启动的ubuntu shell都无法实现正常的粘贴功能
  4. 这种异常体现在，无空格的字符串可以正常的粘贴，有空格的字符串粘贴异常，有时候粘贴最后一个单词，有时候啥也粘贴不出来，但是隔壁的【方法2】启动的却可以

- 参考链接：

  - [灵感来源，但是写的也太简单了](https://www.yewen.us/blog/2018/05/paste-drops-characters-in-wsl/)

  - [问题定位](https://github.com/Maximus5/ConEmu/issues/1577)

    ![在这里插入图片描述](https://img-blog.csdnimg.cn/03507367d9884449b7f6e68a85f3e565.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5p2O6Iux5L-K5bCP5pyL5Y-L,size_20,color_FFFFFF,t_70,g_se,x_16)

## 解决方案

1. 没错 ，这个问题就是ConEmu的bug

   - ConEmu是啥？

     你可以理解为Cmder是套了人家ConEmu的壳

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/74c0188b440549c0ba648ee2adac4faf.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5p2O6Iux5L-K5bCP5pyL5Y-L,size_20,color_FFFFFF,t_70,g_se,x_16)

   - 解决方法是啥？

     更新ConEmu

   - 怎么更新？

     下载最新的ConEmu，解压，替换Cmder的ConEmu

2. 能不能直接告诉我怎么做？

   - [打开ConEmu的官网，下载压缩包（点我直接下载）](https://www.fosshub.com/ConEmu.html?dwl=ConEmuPack.210912.7z)

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/616244a086f44441829b91e747449476.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5p2O6Iux5L-K5bCP5pyL5Y-L,size_20,color_FFFFFF,t_70,g_se,x_16)

   - 解压替换 `cmder/vendor/` 目录下的conemu-maximus5，记得重命名为同样的名字哦（下图中，解压的新的和备份的看到了没）

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/eb156719d5ca48b0983fa94bdd5bec6d.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBA5p2O6Iux5L-K5bCP5pyL5Y-L,size_20,color_FFFFFF,t_70,g_se,x_16)

3. 完事儿了，简单吧，爽不爽，你现在有多爽，我当时查的时候就有多绝望好吧，给个机会，留个言点个赞让我知道，不然以后都没有写博客的动力了。有问题留言给我，我回复得很快的~

------


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822`
- :avocado: 我的思否：`https://segmentfault.com/u/liyj`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
