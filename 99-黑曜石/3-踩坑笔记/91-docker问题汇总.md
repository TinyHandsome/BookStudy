# docker问题汇总

[TOC]

==docker问题汇总贴，不断学习不断更新。当前更新时间：**20250110**==

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/df9b936058c94cd8a81a9f262a5d9163.png)

## 银河麒麟不删podman无法运行docker

- 报错内容：

  ```
  docker: Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: container_linux.go:318: starting container process caused "permission denied": unknown.
  ```

- 最终解决方案：删掉podman就ok了，`yum remove podman`

- 原因分析：

  - **检查镜像架构是否正确**：查看镜像架构：`docker inspect hello-world`，兄弟，amd64架构你才能跑啊，别搞成arm了

    ![image-20240903092531460](https://i-blog.csdnimg.cn/direct/477137f779924770a297982c6cdcc297.png)

  - [网上有说是版本问题的](https://blog.csdn.net/2401_84926028/article/details/138768767)

    > 这里要安装 docker-ce 19.03 版本，因为我在使用最新版 20.10 启动容器时出现了未知的权限问题，而麒麟服务器操作系统资料相对较少，我未能找到相应的解决方案，只好退而求其次，换到上一个稳定版本。

  - 最后发现删除podman可以解决：[参考1](https://blog.csdn.net/yzlz888/article/details/140043920)、[参考2](https://blog.csdn.net/qq_45547688/article/details/138150469)

    > 找了N多了地方 最后发现是这个podman惹的祸
    >
    > yum remove podman
    >
    > 删掉后docker start *
    >
    > 世界清净了



## 常见容器使用

### MySQL

可以直接启动容器：

```
docker run -p 3306:3306 --name mysql-test --restart=always --privileged=true -v E:/11-container/mysql-test/log:/var/log/mysql -v E:/11-container/mysql-test/data:/var/lib/mysql -v E:/11-container/mysql-test/conf:/etc/mysql/conf.d -e MYSQL_ROOT_PASSWORD=Qiangmima@666 --restart=always -d mysql:8.0.29
```

如果想用配置的话，可以把下面的配置文件复制到配置的路径，然后重启容器：

```
[client]
default-character-set=utf8mb4
 
[mysql]
default-character-set=utf8mb4
 
[mysqld]
lower_case_table_names=1
init_connect='SET collation_connection = utf8mb4_unicode_ci'
init_connect='SET NAMES utf8mb4'
character-set-server=utf8mb4
collation-server=utf8mb4_unicode_ci
skip-character-set-client-handshake
skip-name-resolve
```

### Redis

redis其实也是相似的，比如编辑配置文件

```
mkdir -p E:/11-container/redis-test/conf && vim E:/11-container/redis-test/conf/redis.conf

# 配置示例
appendonly yes
port 6379
bind 0.0.0.0
```

启动容器，跟mysql不同的时候，redis是有启动命令的，在最后

```
docker run -d -p 6379:6379 --restart=always --privileged=true -v E:/11-container/redis-test/conf/redis.conf:/etc/redis/redis.conf -v  E:/11-container/redis-test/data:/data  --name redis-test redis:7.4 redis-server /etc/redis/redis.conf
```

> :bulb: 其实docker在进行-v路径挂载中，路径挂路径，文件挂文件，但是如果宿主机文件的路径写错了/不存在，那么文件就会变成路径的样子，要仔细检查哦~

### vLLM

可恶啊vLLM不能在windows上跑，下好模型，做好路径映射，然后：

```
docker run --runtime nvidia --gpus all --name vllm-test -v /data/vllm/huggingface:/root/.cache/huggingface -v /data/models:/data/models -p 8000:8000 --ipc=host vllm/vllm-openai:latest --model /data/models/qwen-2.5-1.5b
```

其中

- **--ipc=host**: 让容器与主机共享进程间通信（IPC）命名空间。这个选项能提高 GPU 任务的性能，尤其在使用诸如深度学习框架时。
- **--runtime nvidia**: 指定使用 NVIDIA 的运行时环境，以便在容器中启用 GPU 功能。这个需要主机上有 NVIDIA 的驱动和 Docker 的 NVIDIA 插件。
- **--gpus all**: 允许容器访问主机的所有 GPU。这对于需要使用多个 GPU 来加速计算的深度学习任务是必要的。

调用方法：

- python

  > :warning: 注意！model要填真实模型地址，其实就是-v映射的容器内的地址

  ```python
  from openai import OpenAI
  
  openai_api_key = "EMPTY"
  openai_api_base = "http://localhost:8000/v1"
  
  client = OpenAI(
      api_key=openai_api_key,
      base_url=openai_api_base,
  )
  chat_response = client.chat.completions.create(
      model="/data/models/qwen-2.5-1.5b",
      messages=[
          {"role": "system", "content": "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."},
          {"role": "user", "content": "Tell me something about large language models."},
      ],
      temperature=0.7,
      top_p=0.8,
      max_tokens=512,
      extra_body={
          "repetition_penalty": 1.05,
      },
  )
  ```

  输出

  ```bash
  Chat response: ChatCompletion(id='chatcmpl-1daa244c6ca14f5fa8baa9c0d8233f6b', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='Large Language Models (LLMs) are artificial intelligence systems that can generate human-like text based on the input provided to them. These models are designed to understand and respond to natural language queries, such as writing stories, generating poetry, answering questions, and more.\n\nOne of the key features of LLMs is their ability to learn from vast amounts of data. They are trained using massive datasets, which allows them to recognize patterns and relationships in language that humans might not be able to detect on their own. This makes them particularly useful for tasks that require a high level of understanding and interpretation of language, such as machine translation, sentiment analysis, and question-answering systems.\n\nThere are several types of LLMs, including transformer-based models like BERT, GPT, and T5, which have been successful in various applications due to their ability to handle long sequences of text and their capacity for fine-tuning specific tasks.\n\nHowever, LLMs also come with some challenges and limitations. One of the main concerns is bias, as these models can inherit biases present in the training data. Additionally, they can produce inappropriate or offensive responses if they are exposed to inappropriate or offensive inputs. Furthermore, the sheer size and complexity of these models can make them difficult to train and optimize, and they may struggle with certain types of language or complex tasks.\n\nDespite these challenges, large language models continue to advance rapidly, and they are being used in a wide range of applications, from chatbots and virtual assistants to scientific research and language translation. As they become more sophisticated, it will be important to continue developing techniques to address their limitations and ensure they are used responsibly and ethically.', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=[]), stop_reason=None)], created=1736401336, model='/data/models/qwen-2.5-1.5b', object='chat.completion', service_tier=None, system_fingerprint=None, usage=CompletionUsage(completion_tokens=337, prompt_tokens=37, total_tokens=374, completion_tokens_details=None, prompt_tokens_details=None), prompt_logprobs=None)
  ```

- curl

  ```
  curl http://localhost:8000/v1/chat/completions -H "Content-Type: application/json" -d '{
    "model": "/data/models/qwen-2.5-1.5b",
    "messages": [
      {"role": "system", "content": "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."},
      {"role": "user", "content": "Tell me something about large language models."}
    ],
    "temperature": 0.7,
    "top_p": 0.8,
    "repetition_penalty": 1.05,
    "max_tokens": 512
  }'
  ```

  

------


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822`
- :avocado: 我的思否：`https://segmentfault.com/u/liyj`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
