# 尚硅谷韩顺平Linux教程学习笔记

[TOC]

## 写在前面

学习链接：[尚硅谷韩顺平Linux教程](https://www.bilibili.com/video/av21303002)

## 虚拟机

- 虚拟机的网络连接三种形式说明
  - 桥连接：Linux可以和其他的系统通信。但是可能造成IP冲突。
  - NAT：网络地址转换方式：Linux可以访问外网，不会造成IP冲突。
  - 主机模式：你的Linux是一个独立的主机，不能访问外网。
- vmtools:
  - 共享文件夹
  - 共享剪贴板

## Linux目录结构

**Linux世界里，一切皆文件。**

- /bin：是Binary的缩写，这个目录存放着最经常使用的命令。
- /sbin：s就是Super User的意思，这里存放的是系统管理员使用的系统管理程序。
- /home：存放普通用户的主目录，在Linux中每个用户都有一个自己的目录，一般该目录名是以用户的账号命名的。
- /root：该目录为系统管理员，也称作超级权限者的用户主目录。
- /lib：系统开机所需要最基本的动态连接共享库，其作用类似于Windows里的DLL文件。几乎所有的应用程序都需要用到这些共享库。
- /lost+found：这个目录一般情况下是空的，当系统非法关机后，这里就存放了一些文件。
- /etc：所有的系统管理所需要的配置文件和子目录my.conf。
- /usr：这是一个非常重要的目录，用户的很多应用程序和文件都放在这个目录下，类似与windows下的program files目录。
- /boot：存放的是启动Linux时使用的一些核心文件，包括一些连接文件以及镜像文件。
- /proc：这个目录是一个虚拟的目录，它是系统内存的映射，访问这个目录来获取系统信息。
- /srv：service的缩写，该目录存放一些服务启动之后需要提供的数据。
- /sys：这是linux2.6内核的一个很大的变化。该目录下安装了2.6内核中新出现的一个文件系统sysfs。
- /tmp：这个目录是用来存放一些临时文件的。
- /dev：类似windows的设备管理器，把所有的硬件用文件的形式存储。
- /media：linux系统会自动识别一些设备，例如U盘光驱等等，当识别后，linux会把识别的设备挂载到这个目录下。
- /mnt：系统提供该目录是为了让用户临时挂载别的文件系统的，我们可以将外部的存储挂载在/mnt/上，然后进入该目录就可以查看里面的内容了。
- /opt：这是给主机额外安装软件所摆放的目录，如安装ORACLE数据库就可放到该目录下。默认为空。
- /usr/local：这是另一个给主机额外安装软件所安装的目录，一般是通过编译源码的方式安装的程序。
- /var：这个目录中存放着在不断扩充着的东西，习惯将经常被修改的目录放在这个目录下，包括各种日志文件。
- /selinux：SELinux是一种安全子系统，它能控制程序只能访问特定文件。

总结：

1. Linux的目录中有且只有一个根目录。
2. Linux的各个目录存放的内容是规划好，不用乱放文件。
3. Linux是以文件的形式管理我们的设备，因此linux系统，一切皆为文件。
4. Linux的各个文件目录下存放什么内容，必须有一个认识。

## 远程登录Linux系统

- 远程登录：XShell5
- 远程上传下载文件：Xftp5

## vi和vim编辑器

- 三种常见模式：

  - 正常模式

    在正常模式下，我们可以使用快捷键。

  - 插入模式/编辑模式

    在这个模式下，程序猿可以输入内容。

  - 命令行模式

    在这个模式中，可以提供相关指令。

- 快捷键使用练习：

  - yy：拷贝当前行
  - 5yy：拷贝当前5行
  - dd：删除当前行
  - 5dd：删除当前行向下的5行
  - 在文件中查找某个单词：命令行输入 /（查找内容），按n查找下一个
  - 设置文件行号：set nu，取消文件行号：set nonu
  - 编辑文件，正常模式下使用快捷键到达文档最末行：G，最首行：gg
  - 撤销输入：在正常模式下输入u
  - 编辑文件，光标移动到某行：shift+g
    - 显示行号：set nu
    - 输入行号这个数
    - 输入shift+g

## 关机、重启和用户登录注销

- shutdown -h now：表示立即关机
- shutdown -h 1：表示1分钟后关机
- shutdown -r now：立即重启
- halt：直接使用，关机
- reboot：重启
- sync：把内存的数据同步到磁盘上，**当我们关机或者重启时，都应该先执行一下sync，防止数据丢失**。
- logout：注销用户，**在图形运行级别无效，在运行级别3有效**。

## 用户管理

用户，组，家目录。

1. Linux系统是一个多用户多任务的操作系统，任何一个要使用系统资源的用户，都必须首先向系统管理员申请一个账号，然后以这个账号的身份进入系统。
2. Linux的用户需要至少要属于一个组。

- 添加用户：useradd [选项] 用户名。
- cd：表示change directory，切换目录。
- 当创建用户成功后，会自动的创建和用户同名的家目录。
- 也可以通过useradd -d 指定目录 新的用户名。
- 指定/修改密码：passwd 用户名
- 删除用户，保留家目录：userdel 用户名，**一般保留家目录，因为干过的活要留着**。
- 删除用户以及家目录：userdel -r 用户名
- 查询用户信息：id 用户名
- 切换用户：su - 切换用户名，**从权限高切换到权限低的用户不需要输密码**。
- 返回切换前的用户：exit
- 查看当前用户/登录用户：who am i
- 用户组：类似于角色，系统可以对有共性的多个用户进行统一的管理。
- 增加组：groupadd 组名
- 删除组：groupdel 组名
- 增加用户时直接加上组：useradd -g 用户组 用户名
- 修改用户组：usermod -g 用户组 用户名

3. /etc/passwd 文件

- 用户（user）的配置文件，记录用户的各种信息。
- 每行的含义：用户名：口令：用户标识号：注释性描述：主目录：登录shell

4. /etc/shadow 文件

- 口令配置文件
- 每行的含义：登录名：加密口令：最后一次修改时间：最小时间间隔：最大时间间隔：警告时间：不活动时间：失效时间：标志

5. /etc/group 文件

- 组（group）的配置文件，记录Linux包含的组的信息。
- 每行含义：组名：口令：组标识号：组内用户列表

## 实用指令

- 指定运行级别（7个级别）
  0. 关机
  1. 单用户【找回丢失密码】
  2. 多用户状态没有网络服务
  3. 多用户状态有网络服务
  4. 系统未使用保留给用户
  5. 图形界面
  6. 系统重启

- 系统的运行级别配置文件：/etc/inittab

- 切换到指定运行级别的指令：init [012356]

- **面试题：<u>如何找回丢失的root密码？</u>**：进入到单用户模式，然后修改root密码。因为进入单用户模式，root不需要密码就可以登录。【开机->在引导时输入 回车键->看到一个界面输入 e->看到一个新的界面，选中第二行（编辑内核），再输入 e->在这行最后输入 1，再输入 回车键->再输入b，这时就会进入到单用户模式，使用passed来修改root密码。】

- 帮助指令：

  - man [命令或配置文件]
  - help

- 文件目录类

  - pwd：Print Working Directory，显示当前工作目录的绝对路径。

  - ls：-a：显示当前目录所有的文件和目录，包括隐藏的；-l：以列表的方式显示信息。

  - cd：cd ~：回到自己的家目录；cd ..：回到当前目录的上一级目录。

  - mkdir：创建目录；-p：创建多级目录。

  - rmdir：删除空目录。<u>rmdir不能删除非空的目录。如果需要删除非空的目录，需要使用rm -rf。</u>

  - touch：创建空文件。<u>可以一次性创建多个文件</u>

  - cp：拷贝文件到指定目录；-r：递归复制整个文件夹。<u>强制覆盖不提示的方法：cp命令改为\cp</u>

  - rm：移除文件或目录；-r：递归删除整个文件夹；-f：强制删除不提示。

  - mv：<u>移动文件与目录</u>或<u>重命名</u>，两种功能！

  - cat：查看文件内容。<u>只能浏览文件，而不能修改文件。</u>-n：显示行号。<u>结尾加上 | more：分页显示，不会全部一下显示完。</u>

  - more：是一个基于VI编辑器的文本过滤器，它以全屏幕的方式按页显示文本文件的内容。more还内置了很多快捷键：

    | 操作            | 功能说明                         |
    | --------------- | -------------------------------- |
    | 空白键（Space） | 向下翻一页                       |
    | Enter           | 向下翻一行                       |
    | q               | 立刻离开more，不再显示该文件内容 |
    | Ctrl + F        | 向下滚动一屏                     |
    | Ctrl + B        | 返回上一屏                       |
    | =               | 输出当前行的行号                 |
    | ：f             | 输出文件名和当前行的行号         |

  - less：用来分屏查看文件内容，与more相似，但是更强大，支持各种显示终端。<u>less指令在显示文件内容时，并不是一次将整个文件加载之后才显示，而是根据显示需要加载内容。</u>**对于显示大型文件具有较高的效率。**

  - `>`指令：输出重定向。如果不存在会创建文件，否则会将原来的文件内容覆盖。
  
  - `>>`指令：追加。如果不存在会创建文件，否则不会覆盖原来的文件内容，而是追加到文件的尾部。
  
  - cat是查看，echo是写入，echo （内容） >> 文件
  
  - cal：显示当前月日历。
  
  - echo：输出内容到控制台。
  
  - head：显示文件的开头部分。<u>-n 5：看前面5行内容。</u>
  
  - tail：输出文件中尾部的内容。<u>-n 5：看后面5行内容。-f：时事追踪该文档的所有更新</u>
  
- 时间日期类

  - date：显示当前日期和时间
  - date “+%Y”：显示当前年份
  - date “+%d”：显示当前月份
  - date “+%Y-%m-%d %H:%M:%S”：显示年-月-日 时：分：秒
  - 设置日期：date -s 字符串时间
  - cal：查看日历指令；cal 年份：显示某一年一整年的日历

- 搜索查找类

  - find：从指定目录向下递归的遍历其各个子目录，将满足条件的文件或者目录显示在终端。
    - find (搜索范围) -name (文件名)：按照指定的文件名查找模式查找文件。
    - find (搜索范围) -user (用户名)：按照指定的用户名查找模式查找文件。
    - find (搜索范围) -size (+多少/-多少/多少)：按照指定的文件大小查找模式查找文件（大于多少/小于多少/等于多少）
    - **查询 /目录下所有.txt的文件**：find / -name *.txt
  - locate：locate (搜索文件)
    - 可以快速定位文件路径。locate指令利用事先建立的系统中所有文件名称及路径的locate数据库实现快速定位给定的文件。locate指令无需遍历整个文件系统，查询速度较快。为了保证查询结果的准确度，管理员必须定期更新locate时刻。
    - 在第一次运行之前，必须使用updatedb指令创建locate数据库。
  - grep：过滤查找，表示将前一个命令的处理结果输出传递给后面的命令处理。经常跟管道一起使用。
    - grep [选项] 查找内容 源文件
    - -n：显示匹配行及行号。
    - -i：忽略大小写字母。
    - `cat hello.txt | grep yes`

- 压缩和解压类

  - gzip/gunzip：压缩文件/解压
    - gzip (文件)：压缩为.gz文件，<u>原来文件不保留</u>。
    - gunzip (文件)：解压缩，<u>同样也不保留源文件</u>。
  - zip/unzip：压缩文件/解压
    - zip [选项] (压缩后文件xxx.zip) (将要压缩的文件)
    - unzip [选项] (要解压的文件xxx.zip)
    - zip -r：递归压缩，即压缩目录
    - unzip -d (目录)：指定解压后的文件的存放目录
  - tar：打包指令，最后打包后的文件是.tar.gz的文件
    - tar [选项] xxx.tar.gz (打包的内容)
    - -c：产生.tar打包文件
    - -v：显示详细信息
    - -f：指定压缩后的文件名
    - -z：打包同时压缩
    - -x：解压.tar文件
    - 压缩：tar -zcvf (压缩后文件名) (要压缩的文件)
    - 解压：tar -zxvf (要解压的文件)
    - 解压到指定目录：tar -zxvf (要解压的文件) -C (指定目录)，<u>指定解压到的目录要存在。</u>

## 组管理和权限管理

- 文件：
  1. 所有者
  2. 所在组
  3. 其他组
  4. 改变用户所在组

- 文件/目录所有者：

  - 一般为文件的创建者，谁创建了该文件，就自然的称为该文件的所有者。 
  - 查看文件所有者：ls -ahl
  - 修改文件所有者：chown (用户名) (文件名)
  - <u>文件所在组不一定是文件所有者。</u>

- 组的创建

  - groupadd (组名)

- 文件/目录所在组

  - 修改文件所在组：chgrp (组名) (文件名)

- 其他组

  - 除文件的所有者和所在组的用户外，系统的其他用户都是文件的其他组

- 改变用户所在组

  - 在添加用户时，可以指定将该用户添加到哪个组中，同样的用root的管理权限可以改变某个用户所在的组
  - 改变用户所在组：usermod -g 组名 用户名
  - 改变用户登录的初始目录：usermod -d 目录名 用户名

- 权限的基本介绍

  - 文件类型：

    - -：普通类型
    - d：目录
    - l：软连接
    - c：字符设备【键盘、鼠标等】
    - b：块文件【硬盘】

  - ls -l 显示内容说明：

    - rw-：表示文件所有者权限（rw，读写）
    - r--：表示文件所在组的用户的权限（r，只有读的权限）
    - r--：表示文件其他组的用户的权限（r，只有读的权限）
    - 1：如果是文件，表示硬连接的数；如果是目录则表示该目录的子目录个数
    - tom：文件所有者
    - bandit：文件所在组
    - 0：文件的大小，0个字节；如果是目录，则统一为4096
    - July 1 13：40：文件最后的修改时间
    - ok.txt：文件名

    ![img](https://img-blog.csdnimg.cn/20190701154715856.png)

- rwx权限详解
  - rwx作用到文件：
    - r：read，可读。读取查看。
    - w：write，可以修改。但不代表可以删除该文件。<u>删除一个文件的前提条件是对该文件所在的目录有写权限，才能删除该文件。</u>
    - x：execute，可执行。可以被执行。
  - rwx作用到目录：
    - r：可以读取，ls查看目录内容。
    - w：可以修改，目录内创建+删除+重命名目录。
    - x：可执行，可以进入该目录。
- 修改权限 chmod
  - 修改文件或者目录的权限
  - u：所有者；g：所在组；o：其他人；a：所有人（u、g、o的总和）
  - chmod u=rwx，g=rx，o=x 文件目录名：分别权限
  - chmod o+w 文件目录名：给其他人都增加写的权限
  - chmod a-x 文件目录名：给所有的用户都减掉执行权限
- 通过数字变更权限
  - 规则：r=4 w=2 x=1 rwx=4+2+1=7
  - chmod u=rwx，g=rx，o=x 文件目录名 **等价于** chmod 751 文件目录名
- 修改文件所有者 chown
  - chown newowner file：改变文件的所有者
  - chown newowner：newgroup file：改变用户的所有者和所在组
  - -R：如果是目录，则使其下所有子文件或目录递归生效
- 修改文件所在组 chgrp
  - chgrp newgroup file：改变文件的所有组
  - -R：如果是目录，则使其下所有子文件或目录递归生效

## 定时任务调度

- crond任务调度：crontab进行定时任务调度

  - crontab [选项]
  - -e：编辑crontab定时任务
  - -i：查询crontab任务
  - -r：删除当前用户所有的crontab任务
  - -l：列出当前有哪些任务调度
  - service crond restart：重启任务调度
  - 当保存退出后就生效了
  - 参数细节说明

  | 项目      | 含义                 | 范围                    |
  | --------- | -------------------- | ----------------------- |
  | 第一个“*” | 一小时当中的第几分钟 | 0-59                    |
  | 第二个“*” | 一天当中的第几小时   | 0-23                    |
  | 第三个“*” | 一个月当中的第几天   | 1-31                    |
  | 第四个“*” | 一年当中的第几月     | 1-12                    |
  | 第五个“*” | 一周当中的星期几     | 0-7（0和7都代表星期日） |

- 特殊符号说明
  - `*`：代表任何时间。比如第一个`*`就代表一小时中每分钟都执行一次的意思。
  - `,`：代表不连续的时间。比如“0 8,12,16 * * *命令”，就代表在每天的8点0分，12点0分，16点0分都执行一次命令。
  - `-`：代表连续的时间范围。比如“0 5 * * 1-6命令”，代表在周一到周六的凌晨5点0分执行命令。
  - `/n`：代表每隔多久执行一次。比如“*/10 * * * * 命令”，代表每隔10分钟就执行一遍命令。

## Linux磁盘分区、挂载

- 分区的方式
  - mbr分区
    - 最多支持四个主分区
    - 系统只能安装在主分区
    - 扩展分区要占一个主分区
    - MBR最大只支持2TB，但拥有最好的兼容性
  - gpt分区
    - 支持无限多个主分区（但操作系统可能限制，比如windows下最多128个分区）
    - 最大支持18EB的大容量（1EB=1024PB，PB=1024TB）
    - windows7 64位以后支持gpt
- Linux分区
  - Linux来说无论有几个分区，分给哪一个目录使用，它归根结底就只有一个根目录，一个独立且唯一的文件结构，Linux中每个分区都是用来组成整个文件系统的一部分。
  - Linux采用了一种叫做“载入”的处理方法，它的整个文件系统中包含了一整套的文件和目录，且将一个分区和一个目录联系起来。这时要载入的一个分区将使它的存储空间在一个目录下获得。
- 硬盘说明
  - Linux硬盘分IDE硬盘和SCSI硬盘，目前基本上是SCSI硬盘
  - lsblk -f：查看当前系统的分区和挂载情况。（list block）

- 挂载的经典案例

  - 需求是给我们的Linux系统增加一个新的硬盘，并且挂载到/home/newdisk

  1. 虚拟机添加硬盘
  2. 分区：fdsk /dev/sdb
  3. 格式化：mkfs -t ext4 /dev/sdb1
  4. 挂载：新建目录：mkdir /home/newdisk；挂载：mount /dev/sdb1 /home/newdisk
  5. 设置可以自动挂载（永久挂载）：重启系统后，仍然可以挂载。vim etc/fstab 增加挂载信息。mount -a：生效

  - 取消挂载：unmount /dev/sdb1

- 磁盘情况查询：df -h / df -l

- 查询指定目录的磁盘占用情况：du -h /目录，默认为当前目录

  - -s：指定目录占用大小汇总
  - -h：带计量单位
  - -a：含文件
  - --max-depth=1：子目录深度
  - -c：列出明细的同时，增加汇总值

- 磁盘情况-工作实用指令

  1. 统计/home文件夹下文件的个数：`ls -l /home | grep "^-" | wc -l`
  2. 统计/home文件夹下目录的个数：`ls -l /home | grep "^d" | wc -l`
  3. 统计/home文件夹下文件的个数，包括子文件夹里的：`ls -lR /home | grep "^-" | wc -l`
  4. 统计文件夹下目录的个数，包括子文件夹里的：`ls -lR /home | grep "^d" | wc -l`
  5. 以树状显示目录结构：<u>首先安装tree指令：yum install tree</u>，tree

## 网络配置

- 指定固定IP：直接修改配置文件来指定IP，并可以连接到外网，编辑：vim  /etc/sysconfig/network-scripts/ifcfg-eth0
- 重启网络服务：service network restart

## 进程管理

- 在Linux中，每个执行的**程序（代码）**都称为一个进程。每个进程都分配一个ID号
- 每一个进程，都会对应一个父进程，而这个父进程可以复制多个子进程。例如www服务器。
- 每个进程都可能以两种方式存在。**前台和后台**。
  - 前台进程：用户目前的屏幕上可以进行操作的。
  - 后台进程：实际在操作，但由于屏幕上无法看到的进程，通常使用后台方式执行。
- 一般系统的服务都是以后台进程的方式存在，而且都会常驻在系统中，直到关机才结束。
- 显示系统执行的进程
  - ps：查看目前系统中，有哪些正在执行，以及它们执行的状况。可以不加任何参数。<u>PID：进程识别号；TTY：终端机号；TIME：此进程所消耗的CPU时间；CMD：正在执行的命令或进程名</u>
  - ps -a：显示当前终端的所有进程信息。
  - ps -u：以用户的格式显示进程信息。
  - ps -x：显示后台进程运行的参数。
  - ps -axu | grep xxx：过滤得到xxx的信息。
  - ps -ef：以全格式显示当前所有的进程，查看进程的父进程。
  - -e：显示所有进程。
  - -f：全格式。
- 终止进程
  - kill [选项] 进程号：通过进程号杀死进程
  - killall 进程名称：通过进程名称杀死进程，也支持通配符，<u>这在系统因负载过大而变得很慢时很有用</u>
  - -9：表示强迫进程立刻停止
  - 案例1：踢掉非法用户：kill 进程号
  - 案例2：终止远程登录服务sshd，在适当时候再次重启sshd服务
  - 案例3：终止多个gedit编辑器：killall 进程名称
  - 案例4：强制杀掉一个终端：kill -9 进程号
- 查看进程树：pstree [选项]
  - -p：显示进程的PID
  - -u：显示进程的所属用户
- 服务（service）管理
  - service管理指令：service 服务名 [start | stop | restart | reload | status]
  - 在CentOS7.0之后，不再使用service，而是systemctl
  - 查看防火墙情况：
    - service iptables status
    - systemctl status firewalld（7.0之后的版本）
  - 测试某个端口是否在监听：telnet
  - 查看服务名：
    - 方式1：使用setup->系统服务就可以看到
    - 方式2：/etc/init.d/服务名称
  - 服务的运行级别（runlevel）：
    - 查看或修改默认级别：vim /etc/inittab
    - 每个服务对应的每个运行级别都可以设置
  - 如果不小心将默认的运行级别设置成0或者6，怎么处理？
    - 进入单用户模式，修改成正常的即可。
  - chkconfig：可以给每个服务的各个运行级别设置自启动/关闭
  - 查看xxx服务：chkconfig –list | grep xxx
  - 查看服务的状态：chkconfig 服务名 --list
  - 给服务的运行级别设置自启动：chkconfig –level 5 服务名 on/off
  - 要所有运行级别关闭或开启：chkconfig 服务名 on/off
- 动态监控进程
  - top [选项]
  - top和ps命令很相似。它们都用来显示正在执行的进程。top和ps最大的不同之处在于top在执行一段时间可以更新正在运行的进程。
  - -d 秒数：指定top命令每隔几秒更新。默认是3秒。
  - -i：使top不显示任何闲置或者僵死进程。
  - -p：通过指定监控进程ID来仅仅监控某个进程的状态。
  - 案例1：监控特定用户：top查看进程；u输入用户名。
  - 案例2：终止指定的进程：top查看进程；k输入要结束的进程。
  - 案例3：指定系统状态更新的时间（每隔10秒自动更新，默认是3秒）：top -d 10
  - 交互操作说明：
    - P：以CPU使用率排序，默认就是此项
    - M：以内存的使用率排序
    - N：以PID排序
    - q：退出top
- 监控网络状态
  - netstat [选项]
  - -an：按一定顺序排列输出
  - -p：显示哪个进程在调用

## RPM

- RPM：RedHat Package Manager，红帽软件包管理工具。
- RPM查询已安装的rpm列表：rpm -qa | grep xx
- rpm包的其它查询指令：
  - rpm -qa：查询所安装的所有rpm软件包
  - rpm -qa | more
  - rpm -qa | grep xx
  - rpm -q xx：查询xx软件包是否安装
  - rpm -qi xx：查询软件包信息
  - rpm -ql xx：查询软件包中的文件
  - rpm -qf 文件全路径名：查询文件所属的软件包
- 卸载rpm包：rpm -e 软件包名称
- 删除时可能会发生依赖错误，忽视依赖强制删除的方法：rpm -e --nodeps 软件包名称
- 安装rpm包：rpm -ivh 软件包全路径名称
  - i=install：安装
  - v=verbose：提示
  - h=hash：进度条

## YUM

- YUM：是一个shell前端软件包管理器。基于RPM包管理，能够从指定的服务器自动下载RPM包并安装，可以**自动处理依赖性关系**，并且一次安装所有依赖的软件包。使用yum的前提是联网。
- yum list | grep xx：查询yum服务器是否有需要安装的软件
- yum install xx：安装指定的yum包
- yum -y remove xx：卸载指定的yum包

## 搭建JAVAEE环境

1. 将软件上传到/opt下
2. 解压缩
3. 配置环境变量的配置文件vim /etc/profile
   - JAVA_HOME=/opt/jdk1.7.0_79
   - PATH=/opt/jdk1.7.0_79/bin:$PATH
   - export JAVA_HOME PATH
   - 保存然后source /etc/profile生效

## 安装Tomcat

1. 解压缩到/opt：tar -zxvf apache-tomcat-7.0.70.tar.gz
2. 进入tomcat的bin目录，启动tomcat  ./startup.sh：./startup.sh
3. 开放端口  vim /etc/sysconfig/iptables
   - firewall-cmd --zone=public --add-port=8080/tcp --permanent（Centos7）
   - systemctl restart firewalld.service
   - firewall-cmd --reload
   - 重启防火墙生效
4. 测试是否安装成功：在windows和Linux下访问http://linuxip:8080

## 安装Eclipse

1. 解压缩到/opt：tar -zxvf eclipse-jee-mars-2-linux-gtk-x86_64.tar.gz
2. 启动eclipse，配置jre和server：./eclipse
3. 编写Hello world程序并测试成功
4. 编写jsp页面，并测试成功

## 安装mysql

1. 查看是否有mysql：rpm -qa | grep mysql

2. 删除旧mysql：rpm -e –nopdeps mysql（强制删除）

3. 安装环境：yum -y install make gcc-c++ cmake bison-devel ncurses-devel

4. 解压mysql：tar -zxvf mysql-5.6.14.tar.gz

5. 进入mysql目录

6. 编译安装：

   cmake -DCMAKE_INSTALL_PREFIX=/usr/local/mysql
   -DMYSQL_DATADIR=/usr/local/mysql/data -DSYSCONFDIR=/etc
   -DWITH_MYISAM_STORAGE_ENGINE=1 -DWITH_INNOBASE_STORAGE_ENGINE=1
   -DWITH_MEMORY_STORAGE_ENGINE=1 -DWITH_READLINE=1
   -DMYSQL_UNIX_ADDR=/var/lib/mysql/mysql.sock -DMYSQL_TCP_PORT=3306
   -DENABLED_LOCAL_INFILE=1 -DWITH_PARTITION_STORAGE_ENHINE=1
   -DEXTRA_CHARSETS=all -DDEFAULT_CHARSET=utf8
   -DDEFAULT_COLLATION=utf8_general_ci
   
7. 编译并安装：make && make install

8. 配置mysql，设置权限

   - 查看是否有mysql用户和组：cat /etc/passwd，cat /etc/group

   - 添加mysql组：groupadd mysql

   - 添加mysql用户并放在mysql组中：useradd -g mysql mysql

   - 修改/usr/local/mysql权限：chown -R mysql:mysql /usr/local/mysql/

   - 初始化mysql：

     scripts/mysql_install_db --basedir=/usr/local/mysql --datadir=/usr/local/mysql/data
     --user=mysql

     如果报错：`Can't locate Data/Dumper.pm`，则运行：`yum install 'perl(Data::Dumper)'`，参考链接：https://www.cnblogs.com/yanghongfei/p/7118072.html

   - 删除之前mysql的配置文件：mv /etc/my.cnf /etc/my.cnf.bak

9. 启动MySQL

   - 添加服务，拷贝服务脚本到init.d目录，并设置开机启动

   - [注意在 /usr/local/mysql 下执行]

     cp support-files/mysql.server /etc/init.d/mysql

     chkconfig mysql on

     service mysql start

   - 执行下面的命令修改root密码

     cd /usr/local/mysql/bin

     ./mysql -u root -p

     set password = password('root');（quit退出mysql）

## Shell编程

- Shell是一个命令行解释器，它为用户提供了一个向Linux内核发送请求以便裕兴程序的界面系统级程序，用户可以用Shell来启动、挂起、停止甚至是编写一些程序。

- Shell脚本的执行方式：
  - 脚本格式要求：
    - 脚本以#!/bin/bash 开头
    - 脚本需要有可执行权限
  - 脚本的常用执行方式：
    - 方式1（输入脚本的绝对路径或相对路径）
      - 首先要赋予xx.sh脚本的+x权限：chmod 744 myShell.sh
      - 执行脚本：./myShell.sh
    - 方式2（sh+脚本）：
      - 说明：不用赋予+x权限，直接执行即可
      - sh ./myShell.sh

- shell的变量

  - shell变量的介绍

    - Linux Shell的变量分为，系统变量和用户自定义变量
    - 系统变量：`$HOME`、`$PWD`、`$SHELL`、`$USER`等等
    - 显示当前shell中所有变量：set

  - shell变量的定义

    - 基本语法

      定义变量：变量=值，**=两边不能有空格**

      撤销变量：unset 变量

      声明静态变量：readonly 变量，注意：不能unset

  - 定义变量的规则

    - 变量名称可以由字母、数字和下划线组成，但是不能以数字开头
    - 等号两侧不能有空格
    - 变量名称一般习惯为大写

  - 将命令的返回值赋给变量

    - A=`ls -la`这里有反引号（ESC下面），运行里面的命令，并把结果返回给变量A
    - A=$(ls -la)等价于上面
  
- 设置环境变量

  - 基本语法

    - export 变量名=变量值：将shell变量输出为环境变量

    - source 配置文件：让修改后的配置文件信息立即生效

    - echo $变量名：查询环境变量的值

    - 多行注释：

      :<<!

      需要注释的内容

      !

- 位置参数变量

  - 当我们执行一个shell脚本时，如果希望获取到命令行的参数信息就可以使用到位置参数变量。比如： ./myshell.sh 100 200，这个就是一个执行shell的命令行，可以在myshell脚本中传参100，200。
  - 基本语法：
    - `$n`：n为数字，`$0`代表命令本身，`$1-$9`代表第一到第九个参数，10以上的参数需要用大括号包含，如`${10}`
    - `$*`：这个变量代表命令行中所有的参数，`$*`把所有的参数看成一个整体
    - `$@`：这个变量也代表命令行中所有的参数，不过`$@`把每个参数区分对待
    - `$#`：这个变量代表命令行中所有参数的个数

- 预定义变量

  - shell设计者事先已经定义好的变量，可以直接在shell脚本中使用
  - 基本语法：
    - `$$`：当前进程的进程号（PID）
    - `$!`：后台运行的最后一个进程的进程号（PID）
    - `$?`：最后一次执行的命令的返回状态。如果这个变量的值为0，证明上一个命令正确执行；如果这个变量的值为非0（具体是哪个数，由命令自己来决定），则证明上一个命令执行不正确。
    - 后台运行：./myShell.sh &

- 运算符

  - 在Shell中进行各种运算操作
  - “`$`((运算式))”或“`$`[运算时]”
  - expr m + n，注意expr运算符间要有空格
  - expr m - n
  - expr `\*` / %，乘，除，取余
  
- 条件判断

  - 基本语法：[ condition ]，注意condition前后有空格！
  - 非空返回true，可使用$?验证（0为true，>1为false）
  - 两个整数比较
    - =：字符串比较
    - -lt：小于
    - -le：小于等于
    - -eq：等于
    - -gt：大于
    - -ge：大于等于
    - -ne：不等于
  - 按照文件权限进行判断
    - -r：有读的权限
    - -w：有写的权限
    - -x：有执行的权限
  - 按照文件类型进行判断
    - -f：文件存在并且是一个常规的文件
    -  -e：文件存在
    - -d：文件存在并且是一个目录

- 流程控制if语句

  - if判断基本语法：

    if [ 条件判断式 ];then

    程序

    fi

  - 或者：

    if [ 条件判断式 ]

    ​	then

    ​		程序

    elif [ 条件判断式 ]

    ​	then

    ​		程序

    fi

- 流程控制case语句

  - case语句基本语法：

    case $变量名 in

    “值1”)

    如果变量的值等于值1，则执行程序1

    ;;

    “值2”)

    如果变量的值等于值2，则执行程序2

    ;;

    …省略其他分支…

    *)

    如果变量的值都不是以上的值，则执行此程序

    ;;

    esac

- 流程控制for循环

  - for循环基本语法1：

    for 变量 in 值1 值2 值3…

    ​	do

    ​		程序

    ​	done

  - for循环基本语法2

    for ((初始值;循环控制条件;变量变化))

    ​	do

    ​		程序

    ​	done

- 流程控制while循环

  - while循环基本语法1：

    while [ 条件判断式 ]

    ​	do

    ​		程序

    ​	done

- read读取控制台的输入

  - read [选项] (参数)
  - -p：指定读取值时的提示符
  - -t：指定读取值时等待的时间（秒），如果没有在指定的时间内输入，就不再等待了。
  - 参数：变量：指定读取值的变量名

- 函数

  - 系统函数

    - basename：返回完整路径最后/的部分，常用于获取文件名
      - basename [pathname] [suffix]
      - basename [string] [suffix]
      - basename命令会删掉所有的前缀包括最后一个/
      - 选项：suffix为后缀，如果suffix被指定了，basename会将pathname或string中的suffix去掉
    - dirname：返回完整路径最后/的前面的部分，常用于返回路径部分
      - dirname 文件绝对路径：从给定的包含绝对路径的文件名中出去文件名（非目录部分），然后返回剩下的路径（目录部分）
    - **反正两个系统函数都不要最后一个/**

  - 自定义函数

    - 基本语法：

      function funname()

      {

      ​	Action;

      ​	[return int;]

      }

    - 调用直接写函数名：funname（不用写括号），然后在后面写参数

## Shell编程综合案例

- 需求分析
  1. 每天凌晨2：10备份数据库atguiguDB到/data/backup/db
  2. 备份开始和备份结束能够给出相应的提示信息
  3. 备份后的文件要求以备份时间为文件名，并打包成.tar.gz的形式，比如：2018-03-12_230201.tar.gz
  4. 在备份的同时，检查是否有10天前备份的数据库文件，如果有就将其删除。

- 如果报错：mysqldump: command not found

  解决方案：

  1. 先找到mysqldump的位置：find  / -name mysqldump -print
  2. 然后建立一个链接：ln -fs /usr/local/mysql/bin/mysql /usr/bin

- crontab -e
- 10 2 * * * /usr/sbin/mysql_backup_db.sh

## Python定制篇 开发平台Ubuntu

- 设置Ubuntu支持中文

- su root显示认证失败：是因为我们还没有对root用户设置密码

- 给root用户设密码：sudo passwd

- 如果ubuntu没有vim：apt install vim

- apt软件管理和远程登录

  - apt：Advanced Packaging Tool，是一款安装包管理工具。在Ubuntu下，我们可以使用apt命令进行软件包的安装、删除、清理等。

  - 常用命令：

    sudo apt-get update
    更新源
    sudo apt-get install package 安装包
    sudo apt-get remove package 删除包
    sudo apt-cache search package 搜索软件包
    sudo apt-cache show package
    获取包的相关信息,如说明、大小、版本等
    sudo apt-get install package --reinstall
    重新安装包

    sudo apt-get -f install
    修复安装
    sudo apt-get remove package --purge 删除包,包括配置文件等
    sudo apt-get build-dep package 安装相关的编译环境

    sudo apt-get upgrade 更新已安装的包
    sudo apt-get dist-upgrade 升级系统
    sudo apt-cache depends package 了解使用该包依赖那些包
    sudo apt-cache rdepends package 查看该包被哪些包依赖
    sudo apt-get source package
    下载该包的源代码

  - 更新Ubuntu软件下载地址

    - 查看Ubuntu版本：cat /proc/version
    - 需要修改的文件位置：/etc/apt/source.list

- Windows使用SSH远程登录Ubuntu

  - 安装SSH：sudo apt-get install openssh-server
  - 启用SSH：service sshd start

- Linux使用SSH远程登录Ubuntu

  - 同上
  - 基本语法：ssh 用户名@IP
  - 例如：ssh atguigu@192.168.188.130
  - 使用shh访问，如访问出现错误。可查看是否有该文件 ~/.ssh/known_ssh，尝试删除该文件解决。
  - 登出：exit或者logout

------

我的CSDN：https://blog.csdn.net/qq_21579045

我的博客园：https://www.cnblogs.com/lyjun/

我的Github：https://github.com/TinyHandsome

纸上得来终觉浅，绝知此事要躬行~

欢迎大家过来OB~

by 李英俊小朋友