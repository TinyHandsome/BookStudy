# PyCharm的git和git bash中文乱码解决方案汇总

## 写在前面

- 做这件事的原因：
  1. pycharm中的git和teminal、git bash三个地方会出现各种各样的中文乱码
  2. 我的理解：pycharm中的teminal相当于cmd
- 淌过的坑：
  1. 在git bash右键设置text的编码为zh_cn和utf-8，完全不顶用
  2. 在git bash中输入`git config --global core.quotepath false`还是不行
- 参考链接：
  1. [git乱码解决方案汇总](https://blog.csdn.net/yunnywu/article/details/50553908?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-8.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-8.control)
  2. [git status 显示中文和解决中文乱码](https://blog.csdn.net/u012145252/article/details/81775362?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_baidulandingword-2&spm=1001.2101.3001.4242)

## 解决方案

### 1. pycharm-git-commit

1. 问题描述：

   1. 之前一直用的是右键git，然后commit和push，显示还是正常的。
   2. 然后突然发现了pycharm集成的git的快乐，转到pycharm后，发现commit的内容变成了乱码。

2. 设置git gui的界面编码：`git config --global gui.encoding utf-8`

3. 设置 commit log 提交时使用 utf-8 编码，可避免服务器上乱码，同时与linux上的提交保持一致：`git config --global i18n.commitencoding utf-8`

4. 【重要】~~使得在 $ git log 时将 utf-8 编码转换成 gbk 编码，解决Msys bash中git log 乱码~~：

   这里跟参考链接的处理不一样，直接设置为utf-8，而不是gbk

   `git config --global i18n.logoutputencoding utf-8`

5. 使得 git log 可以正常显示中文（配合i18n.logoutputencoding = gbk)，在`/etc/profile` 中添加：`export LESSCHARSET=utf-8`

6. 结果展示：

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210202100341270.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

### 2. pycharm-terminal-git log

1. 问题描述：

   pycharm中的terminal输入`git log`发现中文乱码，可是在git bash中是正常的

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210202102032378.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210202102225405.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

2. 设置环境变量后，可以解决问题

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210202102531365.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

### 3. git bush-git status

1. 问题描述：

   在git bash中输入git status显示中文乱码，但是在pycharm的terminal中没问题，我吐了

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210202103151730.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210202103139623.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

2. 查了各种资料后发现，如果在文件profile末尾添加`export LESSHARESET=utf-8`没有作用的话，那么就是你windows安装git bash的时候框选了字体，然后你系统中没有那个字体导致。这种情况下只能先卸载git bash，重装不要选字体。

3. 上述检验的方法很简单，如果你用ls看目录没问题，git status有问题，那就重装git吧。（我懒得重装了）

---

我的CSDN：https://blog.csdn.net/qq_21579045

我的博客园：https://www.cnblogs.com/lyjun/

我的Github：https://github.com/TinyHandsome

纸上得来终觉浅，绝知此事要躬行~

欢迎大家过来OB~

by 李英俊小朋友