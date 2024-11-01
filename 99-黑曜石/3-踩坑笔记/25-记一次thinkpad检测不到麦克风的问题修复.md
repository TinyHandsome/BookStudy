---
sticker: emoji//1f624
banner: 3-踩坑笔记/25-记一次thinkpad检测不到麦克风的问题修复.assets/cc64f285459a442b9636412d3b33e87a.png
tags:
  - thinkpad
  - 声音
  - 驱动
  - 麦克风
  - 联想
---
# 记一次thinkpad检测不到麦克风的问题修复

[TOC]

## 写在前面

- 摘要

  新到了一个 thinkpad P16-3SCD，开会没有麦，一直在忍，在考虑要不要买一个带麦的耳机。偶尔的机会看到淘宝上同款thinkpad是支持麦的，这我能忍？开始研究！（设备管理器找不到麦，录音机检测不到麦，声音设置都找不到麦，插带麦的耳机有麦）

- 思路

  - 首先，去了联想官网找到了驱动管理，反正**不好使**，不过这一步让我知道了我的P16其实是**P16 Gen2**，这点很重要，后续的驱动下载操作都是基于型号来的

    ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/02b854b18c6147a59b7d6421eeeb227e.png)

  - 其次，我查啊查，发现很多人提到了**英特尔智音驱动**，好了这个问题的答案呼之欲出了

    > https://www.zhihu.com/question/804497461/answer/4686437230
    >
    > https://blog.csdn.net/weixin_39278265/article/details/125005275
    >
    > https://bbs.thinkpad.com/thread-5980583-1-1.html

    ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/04f64202a7c542e7b27af06fe79d133c.png)

    ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/331c7d22c3614e039945314fabddd078.png)


## 解决方案

1. 百度搜索 **thinkpad 英特尔智音驱动**：手动下载英特尔智音驱动：https://think.lenovo.com.cn/support/driver/driverdetail.aspx?DEditid=127747&driverID=undefined&treeid=15603

   ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/6a46fdf58d3a4326a98ae8c1f9e64a92.png)

   ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/d4a709ea7ea94aa7b31932e5ce464ba5.png)

   好好好，安装了直接显示 fn+f4 的那个麦克风标记了，并且可以用 fn+f4 控制麦的开关，并且通过了腾讯会议的测试，very good。问题来了，扬声器无了，这。。。

2. 下载声卡驱动程序：麦没有了我不好搞，但是声音没有了我还弄不了你吗！这个时候知道自己的型号就很重要了，可以直接去下载对应的声卡驱动。https://newthink.lenovo.com.cn/driveList.html?selname=ThinkPad%20P16%20Gen2

   ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/7b02f983b266407589cde8e0303f1525.png)

   安装，重启，完事儿，测试解决！

3. 最后，测试，确实发现麦克风阵列的输入是 **智音技术** 的驱动，好耶

   ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/cc64f285459a442b9636412d3b33e87a.png)


------


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
