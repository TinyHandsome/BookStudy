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
docker run -p 3306:3306 --name mysql-test --restart=always --privileged=true -v E:/11-container/mysql-test/log:/var/log/mysql -v E:/11-container/mysql-test/data:/var/lib/mysql -v E:/11-container/mysql-test/conf:/etc/mysql/conf.d -e MYSQL_ROOT_PASSWORD=Qiangmima@666 -d mysql:8.0.29
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

### Mongo

这里给mongo挂载一下本地的盘好了

```bash
docker run -d -p 27017:27017 --restart=always --privileged=true --name mongo-test -v E:/11-container/mongo-test/data:/data/db -v E:/11-container/mongo-test/backup:/data/backup -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=Qiangmima@666 mongo:6.0.20
```

- 如果还想限制资源：`--memory 2g --cpu 1.0`

==备份== mongo的数据备份：

1. 进入容器：`docker exec -it mongo-test bash`

2. 使用 `mongodump` 进行备份，注意这里的备份记得提前挂载哦，不然后面就得 `docker cp` 复制出来了

   ```bash
   mongodump --username root --password Qiangmima@666 --out /data/backup
   ```

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


### GitLab

参考链接：https://blog.csdn.net/weixin_42286658/article/details/144768578

```bash
docker run -d --name mygitlab --restart always --privileged=true -p 8180:80 -p 8122:22 -v /data/gitlab/etc:/etc/gitlab -v /data/gitlab/log:/var/log/gitlab -v /data/gitlab/opt:/var/opt/gitlab gitlab/gitlab-ce:17.8.0-ce.0
```

**修改gitlab的配置**

改 `/data/gitlab/etc/gitlab.rb` 这个文件，在宿主机改就行。一定要改哦，不然后面你push的时候就会很痛苦的。。。

> [!warning] push的时候会报下面的错。。。
>
> ```bash
> # git push --set-upstream origin main
> ssh: Could not resolve hostname 724d10cd38bf: Name or service not known
> fatal: Could not read from remote repository.
> ```

```bash
# 取消external_url注释，地址为宿主机地址，不需要设置端口，别忘了http这些，否则会报错
external_url 'http://你的IP'
# ssh主机ip
gitlab_rails['gitlab_ssh_host'] = '你的IP'
# ssh连接端口
gitlab_rails['gitlab_shell_ssh_port'] =8122
# 时区顺便也改一下吧
gitlab_rails['time_zone'] = 'Asia/Shanghai'
```

改好之后，要重启服务哦

```bash
# 宿主机输入：在容器中执行 gitlab-ctl reconfigure
docker exec -t mygitlab gitlab-ctl reconfigure
# 宿主机输入：在容器中执行 gitlab-ctl restart
docker exec -t mygitlab gitlab-ctl restart
```

**配置root用户**

```
# 进入容器内部
docker exec -it mygitlab /bin/bash
# 进入控制台，要等一会儿哦~
gitlab-rails console -e production
# 查询id为1的用户，id为1的用户是超级管理员
user = User.where(id:1).first
# 修改密码，注意这里密码要求比较严格~
user.password='Qi@ngmima@666'
# 保存
user.save!
# 退出
exit
```

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/91d3c1c3d25a4d04a325c6d878120570.png)

现在就可以去**登录**啦，pia的一下就登录进去了，很快哦

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/9aad2d7fac1b4becad6d20beb2cc3104.png)

**设置关闭自动创建账号功能**：gitlab默认是开放注册账号功能的，在企业里面使用是不允许的，用户的账号是通过管理员创建出来的。**:wink: 去掉勾选哦**

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/5fa11f06620e4e45996310de65a74d2a.png)

**使用说明**

1. 创建项目，一般选私有啦

   ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/aa986f19265d44398c54f9f48b52661f.png)

2. 创建用户、组、项目

   ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/471a0f583b8d48418690837978298c58.png)

3. 添加用户到项目中

   ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/0b652b50fd7a469396f1b808ca3841a5.png)

   邀请用户，设置权限：

   ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/231cda04ae4f4c759260f7ae8b847b50.png)

   > [!info] GitLab用户权限管理
   >
   > GitLab用户在组中有五种权限：Guest、Reporter、Developer、Maintainer、Owner
   >
   > 1.Guest：可以创建issue、发表评论、不能读写版本库
   >
   > 2.Reporter：可以克隆代码，不能提交，QA、PM可以赋予这个权限
   >
   > 3.Developer：可以克隆代码、开发、提交、push、研发人员可以赋予这个权限
   >
   > 4.Maintainer：可以创建项目、添加 tag 、保护分支、添加项目成员、编辑项目、核心研发负责人可以赋予这个权限
   >
   > 5.Owner：可以设置项目的访问权限-Visibility Level、删除项目、迁移项目、管理组成员、项目经理，部门经理可以赋予这个权限

**配置说明**

1. 第一步必然是配置ssh呀，你肯定会git吧，用过吧，不然跑来折腾gitlab干嘛，所以假定你懂啊，不懂自己百度去。以windows举例，在你的 `C:\Users\用户名\.ssh` 文件夹中有你之前生成的公钥和私钥，把公钥填到 **SSH Keys** 中哦

   ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/adf78e045bbb41279b18a658d45f4b6f.png)

2. 项目都只能管理员建啊，多的不说，我自己习惯了先建一个啥没有的空的项目

   ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/0ac83702b90745b5827dfaedb4d68f60.png)

   然后根据下面的提示，直接把本地的目录一顿操作之后push

   ```bash
   git init --initial-branch=main
   git remote add origin ssh://git@10.10.102.111:8122/study/yygh-parent.git
   git add .
   git commit -m "Initial commit"
   git push --set-upstream origin main
   ```

   :tada: 然后就OK啦，刷新就能看到全部推上去咯

   ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/20914faf501c4c1c8f3b399300458b13.png)







------


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822`
- :avocado: 我的思否：`https://segmentfault.com/u/liyj`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
