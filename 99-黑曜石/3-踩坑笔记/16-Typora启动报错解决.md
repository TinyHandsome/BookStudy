# 【Typora启动报错】This beta version of Typora is expired, please download and install a newer version.

> 问题描述：This beta version of Typora is expired, please download and install a newer version.
>
> 参考链接：https://blog.csdn.net/no_say_you_know/article/details/125806545

1. 下载一个大佬的项目：https://github.com/fossabot/typoraCracker

2. 安装这个项目需要的python包

   - **注意**：如果报错找不到这个库：`Crypto`，去python的lib中找到这个库的文件夹，修改这个文件夹的首字母大写
   - `\Lib\site-packages\crypto`改为`\Lib\site-packages\Crypto`

3. 输入命令：`python typora.py "C:\Program Files\Typora\resources\app.asar" .`

4. 命令会在当前文件夹下生成一个`dec_app`文件夹，找到`License.js`，搜索：`This beta version of Typora is expired, please download and install a newer version.`

5. 接下来，你要找到这句话周围的时间，类似这样
   ![在这里插入图片描述](https://img-blog.csdnimg.cn/5a18b848a5c54cd691a484d0947ad1d5.png)

6. 将这个数字改为较大的数字哦~（比如我的话，将这个数字改为：4102329600000 ，即2099-12-31）

7. 搞完之后退出去，用命令把这个文件打包一下：` python typora.py -u dec_app/ .`

8. 这样你就会在根目录下找到打包好的文件：`app.asar`

9. 把这个文件复制到Typora的安装目录下的`resources`文件夹中哦，替换原文件。

10. 完事儿起飞~

------


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822`
- :avocado: 我的思否：`https://segmentfault.com/u/liyj`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
