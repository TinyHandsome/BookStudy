# 两步解决JupyterLab添加目录插件的问题

## 写在前面

- 做这件事的原因：
  1. 简简单单：想给`jupyter lab`安装目录
  2. 兄弟，给jupyterlab安装目录，看我就够了，我百度了好久，找的一堆啥啊，我如果用jupyter notebook还跟你比比这么多干嘛鸭？
- [15个好用到爆炸的Jupyter Lab插件](https://www.cnblogs.com/zhuwjwh/p/12325705.html)
- [好用到飞起的12个jupyter lab插件](https://blog.csdn.net/wushijingzuo/article/details/107829081)
- **20201225更新**：
  - kite比lsp好用，用kite的时候，记得要卸载lsp哦，不然会冲突的。
- 如果有错别字呢，哪里写错了呢，请在评论区告诉我嗷，同时，可能会有一些奇奇怪怪的符号夹在文字中，这是因为我用的是MarkDown语法，其中一些符号可能在这个平台（比如CSDN）不支持呢。

## 解决方案

1. 众所周知，安装jupyterlab的插件需要[以下几步](https://blog.csdn.net/zweing/article/details/86768530)

   1. 安装一个插件jupyter_contrib_nbextensions

      ```
      pip install jupyter_contrib_nbextensions
      ```

   2. 配置 nbextension

      ```
      jupyter contrib nbextension install --user
      ```

   3. 安装toc

      ```
      jupyter labextension install @jupyterlab/toc
      ```

2. 好了问题来了，Node.js和npm你没有叭，难受了

   ```
   An error occured.
   ValueError: Please install Node.js and npm before continuing installation. You may be able to install Node.js from your package manager, from conda, or directly from the Node.js website (https://nodejs.org).
   See the log file for details:  C:\Users\LITIAN\AppData\Local\Temp\jupyterlab-debug-amd3fad2.log
   ```

   - 啊，这，这道题我会啊，装不就完事儿了啊：

     所以， **【解决方案的第1步】** ：安装nvm，然后通过这个nvm来安装node和npm，是不是想直到为什么不直接装，你去官网把node都下好了，为什么我给你看这个？

     问的好，看这：[Node.js 安装配置](https://www.runoob.com/nodejs/nodejs-install-setup.html)，下面的凭论会告诉你原因的，[使用 nvm 管理不同版本的 node 与 npm](https://www.runoob.com/w3cnote/nvm-manager-node-versions.html)：

     > nvm是 Nodejs 版本管理器，它让我们方便的对切换Nodejs 版本。

     那，来叭：[nvm安装地址嗷，下这个，解压双击安装就完了](https://github.com/coreybutler/nvm-windows/releases)

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201223194005421.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

   - 安装好了，我们就要开始 **【解决方案的第2步】** ：用nvm安装node和npm

     ```
     nvm install 14.15.3 64-bit
     ```

     欸？这个时候报错了：

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201223194448819.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

     ```
     Could not retrieve https://nodejs.org/dist/latest/SHASUMS256.txt.
     Get https://nodejs.org/dist/latest/SHASUMS256.txt: dial tcp 104.20.23.46:443: connectex: No connection could be made because the target machine actively refused it.
     ```

     这尼玛谁顶得住啊。别担心，解决方案在下面：[**使用nvm-windows安装NodeJs遇到的问题**](https://blog.csdn.net/lisa2017_/article/details/107105016)

     概括呢：

     >  就是说去nvm的安装目录下，找一个settings.txt

     打开之后，在后面加上：

     ```
     node_mirror:npm.taobao.org/mirrors/node/
     npm_mirror:npm.taobao.org/mirrors/npm/
     ```

     然后保存，再开cmd运行`nvm install 14.15.3 64-bit`

     诶~就很舒服。安装完之后记得选择这个使用嗷：`nvm use 14.15.3`

     ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201223194543143.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

   - 好了，真的好了，运行等了很久的语句叭

     ```
     jupyter labextension install @jupyterlab/toc
     ```

     诶 ~ 舒服！

3. 除此之外呢，如果还想安装其他插件呢，看这个链接嗷：[解决 jupyter labextension install 报错](https://www.cnblogs.com/banshaohuan/p/13652143.html)

   > jupyter labextension install @jupyterlab/git 
   >
   > jupyter labextension install @jupyterlab/github 
   >
   > jupyter labextension install @jupyterlab/debugger 
   >
   > jupyter labextension install @lckr/jupyterlab_variableinspector
   >
   > **自动格式化代码**   
   >
   > jupyter labextension install jupyterlab_code_formatter 
   >
   > **ipynb\py\md文件互相转换**
   >
   > jupyter labextension install jupytext         
   >
   > **markdown拼写核对**
   >
   > jupyter labextension install jupyterlab_spellchecker     
   >
   > **自动补全与跳转定义**
   >
   > jupyter labextension install @krassowski/jupyterlab-lsp 

4. 结果展示！

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201223200848174.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

---


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822`
- :avocado: 我的思否：`https://segmentfault.com/u/liyj`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
