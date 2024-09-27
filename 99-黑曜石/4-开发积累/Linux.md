# Linux

## 常用命令

### 文件操作

- 移动文件：`mv file1.txt file2.txt file3.txt /tmp` 
- 改名：`mv /tmp/a.txt aaa.txt`
- 显示当前目录所有文件大小的命令：`ls -lht`
- 列出当前文件以及文件夹的大小：`du -sh *`
- 查看单独文件的大小：`du -s ，du -sh，ls -lh 文件名`
- 服务器之间移动文件：`scp -r -P 10022 Qwen-VL-Chat/  root@10.5.32.169:/data/newDisk/`



## 一些工具

### Screen

- 使用-R创建，如果之前有创建唯一一个同名的screen，则直接进入之前创建的screen[^1]
- 使用-S创建和直接输入screen创建的虚拟终端，不会检录之前创建的screen（也就是会创建同名的screen)

    ```
    # 查询screen提示
    screen -help
    
    # 查看已经存在的screen终端
    screen -ls
    
    # 创建一个叫Hello的虚拟终端flash_attn
    screen -S Hello
    
    # 使用-R创建Hello
    screen -R Hello
    
    # 使用screen -r命令回到终端
    screen -r [pid/name]
    
    # 退出终端
    exit
    
    # 暂离终端
    ctrl+a d
    
    # 在主终端内，使用命令释放，使用-R/-r/-S均可
    screen -R [pid/Name] -X quit
    
    # 删除某个screen
    screen -X -S "名称" quit
    ```







---

[^1]: https://zhuanlan.zhihu.com/p/405968623 "Screen常用命令"
