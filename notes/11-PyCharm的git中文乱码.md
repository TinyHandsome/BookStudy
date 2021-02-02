# PyCharm的git中文乱码

## 写在前面

- 做这件事的原因：
  1. 之前一直用的是右键git，然后commit和push，显示还是正常的。
  2. 然后突然发现了pycharm集成的git的快乐，转到pycharm后，发现commit的内容变成了乱码。
- 淌过的坑：
  1. 在git bash右键设置text的编码为zh_cn和utf-8，完全不顶用
  2. 在git bash中输入`git config --global core.quotepath false`还是不行
- 参考链接：
  1. [git乱码解决方案汇总](https://blog.csdn.net/yunnywu/article/details/50553908?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-8.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-8.control)

## 解决方案

1. 设置git gui的界面编码：`git config --global gui.encoding utf-8`

2. 设置 commit log 提交时使用 utf-8 编码，可避免服务器上乱码，同时与linux上的提交保持一致：`git config --global i18n.commitencoding utf-8`

3. 【重要】使得在 $ git log 时将 utf-8 编码转换成 gbk 编码，解决Msys bash中git log 乱码：`git config --global i18n.logoutputencoding gbk`

4. 使得 git log 可以正常显示中文（配合i18n.logoutputencoding = gbk)，在`/etc/profile` 中添加：`export LESSCHARSET=utf-8`

5. 结果展示：

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210202100341270.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)







---

我的CSDN：https://blog.csdn.net/qq_21579045

我的博客园：https://www.cnblogs.com/lyjun/

我的Github：https://github.com/TinyHandsome

纸上得来终觉浅，绝知此事要躬行~

欢迎大家过来OB~

by 李英俊小朋友