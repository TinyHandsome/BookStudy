# 最简洁的Mysql修改密码，不会你打我

## 写在前面

1. 先说mysql版本：mysql-8.0.21-winx64（就是从官网上下载了之后解压缩的那种）
2. 再说问题出现的原因：下了之后第一次登录不需要修改密码嘛，然后进去了嘛，百度怎么修改密码嘛，修改成功，退出，一气呵成。但是再登录的时候，发现用修改的密码登录不上去了。我人傻了。
3. 然后是过程：百度一堆花里胡哨的修改密码的教程基本没有能解决问题的，然后就是mysql的版本，很多教程都是针对老版本的mysql，我是202010下的最新的mysql，所以基本没啥帮助。
4. 希望能帮到你。

## 不多比比，直接上手

1. 关闭mysql服务：`net stop mysql`

2. 用管理员打开cmd，进入mysql的bin目录

3. 特殊启动mysql服务：`mysqld --shared-memory --skip-grant-tables`

4. 新打开一个cmd（管理员），进入mysql的bin目录，运行mysql：`mysql -u root -p`，这里不需要输入密码，直接回车就行，然后发现进去了是吧。

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20201003111327635.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70#pic_center)

5. 刷新特权：`flush privileges;`（这里一定要刷新哦，你看上图，下面一堆error就是因为没刷新）

6. 修改密码：`ALTER USER 'root'@'localhost' IDENTIFIED WITH MYSQL_NATIVE_PASSWORD BY 'password';`

7. 修改好了别忘了开启MySQL服务哦：`net start mysql`

8. **这你成功了不给我点个赞，我觉得很过分了好吧！**

## 参考链接

1. [忘记密码了怎么进mysql呢](https://blog.csdn.net/xl_1803/article/details/82503781)
2. [修改密码语句](https://blog.csdn.net/weixin_41463971/article/details/88010770)
3. [The MySQL server is running with the --skip-grant-tables option so it cannot execute解决方案](https://blog.csdn.net/appleyuchi/article/details/104265671)

------

- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822`
- :avocado: 我的思否：`https://segmentfault.com/u/liyj`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友