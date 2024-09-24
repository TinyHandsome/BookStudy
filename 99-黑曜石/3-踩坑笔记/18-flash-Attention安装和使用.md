# flash-Attention2安装和使用

[TOC]

标签：flash-attn pytorch llm cuda 大模型

摘要：flash-Attention2从安装到使用一条龙服务。是不是pip安装吃亏了，跑来搜攻略了，哈哈哈哈哈，俺也一样

封面：

![AIGC](18-flash-Attention%E5%AE%89%E8%A3%85%E5%92%8C%E4%BD%BF%E7%94%A8.assets/AIGC.png)

## 写在前面

- **就怕你不知道怎么查 pytorch、cuda 的版本**

  - 配置cuda：`vim ~/.bashrc`

      ```bash
      export CUDA_HOME=/usr/local/cuda/
      export PATH=$PATH:$CUDA_HOME/bin
      export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CUDA_HOME/lib64
      ```

  - 运行配置文件：`source ~/.bashrc`

  - 查看cuda版本：`nvcc --version`

  - 检查pytorch版本和cuda的可用性：`python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())" `

- **问题**

  如题所示，flash-Attention2从安装到使用一条龙服务。是不是pip安装吃亏了，跑来搜攻略了，哈哈哈哈哈，俺也一样 :cry:

- 参考链接

  - https://blog.csdn.net/chongch_wang/article/details/136542877
  - https://blog.csdn.net/lxb206/article/details/130683772


## 解决方案

- 去下载whl：https://github.com/Dao-AILab/flash-attention/releases
  - 我的配置为：
    - cuda：11.6
    - pytorch：1.13
    - python：3.10
  - 那么我要去flash-attn中我能下载的最新版本：2.3.5
  - 下载：flash_attn-2.3.5+cu116torch1.13cxx11abiFalse-cp310-cp310-linux_x86_64.whl，直接点了下就行，命令行为：`wget https://github.com/Dao-AILab/flash-attention/releases/download/v2.3.5/flash_attn-2.3.5+cu116torch1.13cxx11abiFalse-cp310-cp310-linux_x86_64.whl `
  - 安装：`pip install flash_attn-2.3.5+cu116torch1.13cxx11abiFalse-cp310-cp310-linux_x86_64.whl -i  https://mirrors.aliyun.com/pypi/simple/`，加个镜像提速没毛病
  - **注意：**abiTrue的不行，False的可以，就很奇怪，True的会报错：`...-linux-gnu.so: undefined symbol: _ZN3c104cuda9SetDeviceEi...`

- **问题处理**：模型可以启起来，但是模型推理时报错`RuntimeError: CUDA errOr: CUBLAS STATUS INVALID VALUE when calling cublasGemmEx...`

  ![报错截图](https://img-blog.csdnimg.cn/direct/df24283890184dda8a6907cb29a03459.png)

  - 解决：卸载了nvidia-cublas-cu11=11.10.3.66：`pip uninstall nvidia-cublas-cu11`
  - 再启就没问题了，怎么说，给个赞不过分吧~

- **模型推理**

  什么？怎么用你还不知道，就框框下是吧，醉醉的。加载模型的时候，添加一个配置项：`attn_implementation="flash_attention_2"`

  ```python
  AutoModelForCausalLM.from_pretrained(
      model_name_or_path,
      device_map='auto',
      torch_dtype="auto",
      attn_implementation="flash_attention_2"
  )
  ```

记得点赞~ :smile:


------


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822`
- :avocado: 我的思否：`https://segmentfault.com/u/liyj`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友