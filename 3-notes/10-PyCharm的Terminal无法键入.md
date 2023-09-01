# PyCharm的Terminal无法键入

## 写在前面

- 做这件事的原因：
  1. 打开pycharm中的terminal界面只显示一个光标
  2. 输入什么都没用，没有任何反应
- 问题原因：
  1. 百度了之后才知道原来是我们的windows的用户名是中文，必须用英文才行
- 参考链接：[pycharm的terminal无法呼出](https://blog.csdn.net/qq_44111565/article/details/106605705)

## 解决方案

1. 打开注册表（`windows+R`打开运行，然后输入`regedit`）：

   `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Profilelist`

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210117220938456.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

2. 然后你就能看到你的用户名了，如上图，我的叫<u>李英俊小朋友</u>

3. 双击这个值，修改为**新的值**（英文嗷），然后重启。

   重启后会发现跟以前的界面不同了，这是新建了一个临时用户，以前的用户改名之后找不到了。会弹出一个告诉你现在做啥都不会保存的界面，点确定就好了。

4. 然后再去`C:/User`或者`C:/用户`中，找你的名字，我这就是<u>李英俊小朋友</u>，改为刚才**重命名的值**，再重启就好了。

5. 再打开pycharm的terminal，就显示正常了，嘿嘿

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210117221429311.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

---


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822`
- :avocado: 我的思否：`https://segmentfault.com/u/liyj`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
