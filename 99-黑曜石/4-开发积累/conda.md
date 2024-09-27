# conda

## 环境管理

- 首先需要安装打包的工具 pack [^1]：`conda install -c conda-forge conda-pack`

- 创建和激活环境[^3]：

  ```
  # 创建环境
  conda create -n 名字 python=版本
  # 激活环境
  conda activate 名字
  # 退出环境
  conda deactivate
  ```

- 如果启动的时候遭遇问题，需要先初始化：`conda init --all`

  



## 代理管理

- 配置镜像 [^2]

  ```
  # 显示所有镜像
  conda config --show-sources
  
  # 添加清华镜像
  conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
  conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
  conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/linux-64/
  conda config --set show_channel_urls yes
  
  # 删除镜像
  conda config --remove channels 源名称或链接
  # 删除所有镜像
  conda config --remove-key channels
  ```

  



















---

[^1]: https://blog.csdn.net/weixin_43038346/article/details/113621332 "Conda环境迁移--离线版本"
[^2]: https://zhuanlan.zhihu.com/p/628870519 "conda配置镜像"
[^3]: https://blog.csdn.net/miracleoa/article/details/106115730 "conda创建、查看、删除虚拟环境"