---
tags:
  - docker
  - 容器
  - 镜像
  - 离线
  - 银河麒麟
banner: 3-踩坑笔记/docker问题汇总.assets/df9b936058c94cd8a81a9f262a5d9163.png
sticker: emoji//1f6a2
---
# docker问题汇总

[TOC]

> 我不会设置仅粉丝可见，不需要你关注我，仅仅希望我的踩坑经验能帮到你。如果有帮助，麻烦点个 :+1: 吧，这会让我创作动力+1 :grin:
>
> **docker问题汇总贴，不断学习不断更新。当前更新时间：** ==20250923==

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/df9b936058c94cd8a81a9f262a5d9163.png)

## Django+Vue项目的docker打包

> https://www.cnblogs.com/tytbook/p/19011411

- django打包

  ```dockerfile
  FROM python:3.12-slim
  
  WORKDIR /app
  COPY . /app
  RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
  
  # 暴露容器内的端口（通常是8000）
  EXPOSE 8000
  ENV PYTHONDONTWRITEBYTECODE=1
  ENV PYTHONUNBUFFERED=1
  
  CMD ["uvicorn", "ZHIN.asgi:application", "--host", "0.0.0.0", "--port", "8000"]
  ```

- vue打包

  - 构建项目：`npm run build`

  - 在项目根目录下，创建 `nginx.conf`

    ```
    server {
        listen 80;
        server_name _;
        root /usr/share/nginx/html;
        index index.html index.htm;
    
        location / {
            try_files $uri $uri/ /index.html;
        }
    
        location ~* \.(js|css|png|jpg|jpeg|gif|svg|ico|json)$ {
            try_files $uri =404;
        }
    }
    ```

  - 在项目根目录下，创建Dockerfile文件

    ```dockerfile
    FROM nginx:alpine
    COPY dist/ /usr/share/nginx/html/
    COPY nginx.conf /etc/nginx/conf.d/default.conf
    EXPOSE 80
    CMD ["nginx", "-g", "daemon off;"]
    ```

  - 打包：`docker build -t 镜像名 .`

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

## docker镜像盘迁移

参考链接1：https://blog.csdn.net/qq_15607445/article/details/142753636

参考链接2：https://www.cnblogs.com/FatSheepKiller/p/17884682.html

1. 先把应用停一停：`docker ps | awk '{print $1}' |xargs docker stop`

2. 停止docker先啦：`systemctl stop docker`

3. 复制原来docker的内容到新建的文件夹里：`cp -pr /var/lib/docker/ /data/`

   > [!warning] 路径警告
   >
   > 路径这里需要注意的是你把 `/var/lib/docker/*` 复制到 `/data/docker/*` 中，直接跑代码就行了。**不需要**额外的 `mkdir /data/docker`
   >
   > :sweat_smile: 可能是复制的时候我没加 \* ？

4. docker原来的的文件改名：`mv /var/lib/docker /var/lib/docker2`

5. 配置 `/etc/docker/daemon.json`，再重启docker即可 `systemctl start docker`

   ```json
   {
   	"data-root": "/data/docker/"
   }
   ```

   > [!tag] 方法2，建立软连接（懒得试了）
   >
   > `ln -s /data/docker/ /var/lib/docker`

## docker怎么用gpu

在用vllm的时候，发现使用 `docker run --runtime nvidia --gpus all`，增加了一些运行的命令，其中 `--gpus all` 就是用宿主机的gpu驱动，不过要想起作用还得装 **NVIDIA Container Toolkit**，[在线安装很简单](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)，我必然要搞离线安装的~

先看清楚依赖，四个rpm，问题不大~

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/7cf344aa2da54a6e90417417d46a0c52.png)

这四个可以从github上找到：https://github.com/NVIDIA/libnvidia-container/tree/gh-pages/stable/rpm/x86_64

> [!warning] 问题来了，怎么从github中下载单个文件
>
> 从 `raw.githubusercontent.com` 中下载：比如 `wget https://raw.githubusercontent.com/NVIDIA/libnvidia-container/refs/heads/gh-pages/stable/rpm/x86_64/libnvidia-container1-1.17.4-1.x86_64.rpm`
>
> 包括下面4个，改一下url就行：
>
> - `nvidia-container-toolkit-base-1.17.4-1.x86_64.rpm`
> - `nvidia-container-toolkit-1.17.4-1.x86_64.rpm`
> - `libnvidia-container1-1.17.4-1.x86_64.rpm`
> - `libnvidia-container-tools-1.17.4-1.x86_64.rpm`

下载完了之后传到没网的服务器，再安装：`rpm -ivh *`

## unknown or invalid runtime name: nvidia

参考链接：https://developer.baidu.com/article/details/2805250

配置 `/etc/docker/daemon.json`，既然没有这个runtime name，那我自己建一个

```json
{
    ...
	"runtimes": {
    	"nvidia": {
      		"path": "/usr/bin/nvidia-container-runtime",
      		"runtimeArgs": []
    		}
  	}
  	...
}
```

然后重启 `systemctl restart docker` 完事儿~

## Docker进阶命令

1. 清除没有up的容器：`docker container prune`

1. 以follow的形式查看日志：`docker logs -f xxx`

1. 更新容器设置：
   - 先stop容器：`docker stop xxx`
   
   - 再update，以restart举例：`docker update --restart=no xxx `
   
     > [!info] restart的区别
     >
     > `--restart=always`:
     >
     > - 容器将始终尝试重启，无论它是如何停止的。
     > - 如果容器崩溃，它会自动重启。
     > - 如果Docker守护进程重启，容器也会自动启动。
     > - 即使容器被手动停止（如使用 `docker stop` 命令），当Docker守护进程重启时，它也会重新启动。
     >
     > `--restart=unless-stopped`:
     >
     > - 容器会在崩溃时自动重启。
     > - 如果Docker守护进程重启，容器也会自动启动。
     > - 关键区别：如果容器被手动停止（如使用 `docker stop` 命令），它不会在Docker守护进程重启时自动启动。
   
1. 获取某个镜像的tags有哪些，用sglang举例：`curl -s https://registry.hub.docker.com/v2/repositories/lmsysorg/sglang/tags/`



## 常见容器使用

### OneAPI

```bash
docker run --name one-api --privileged=true -d -p 3282:3000 -e TZ=Asia/Shanghai -v ${PWD}:/data 10.4.32.48:5000/justsong/one-api
```

### Higress

参考文档：https://higress.cn/en/docs/latest/user/quickstart

```bash
# 先创建目录
mkdir higress; cd higress
# 启动
docker run -d --name higress-ai -v ${PWD}:/data -e O11Y=on -p 3281:8001 -p 3280:8080 -p 3283:8443 -p 32820:15020 -p 32821:15021 10.4.32.48:5000/higress/all-in-one:latest
```

其中：

- 8001：Higress的UI，进入这个就行
- 8080：HTTP网关
- 8443：HTTPS网关
- 15020：Prometheus需要的metrics端口
- 15021：*还没搞明白*
- `-e O11Y=on`：打开自带的监控功能，Prometheus 和 Granfana，如果省事儿可以开，否则可以自己对接。

:warning: 感觉问题很大，我整了一个yaml，这个好使了，解决了prometheus的问题，毕竟上面的端口少暴露了 15020，害我搞了半天，醉醉的。哎，把redis整上是因为在github上看到说mcp相关的需要redis，弄上吧，完一后面需要呢，我真服了。。。

```yaml
name: higress

services:
  redis:
    image: 10.4.32.48:5000/redis:6-alpine
    restart: always
    container_name: redis
    environment:
      REDIS_PASSWORD: ""
    volumes:
      - ./redis_db:/data
  higress-ai:
    image: 10.4.32.48:5000/higress/all-in-one:latest
    container_name: higress
    ports:
      - "3281:8001"
      - "3280:8080"
      - "3283:8443"
      - "32820:15020"
      - "32821:15021"
    volumes:
      - ./data:/data
      - ./config/grafana:/etc/grafana
      - ./logs:/var/log/higress
    restart: unless-stopped
```

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/7c5ef07c8d3d45d88016740afae40935.png)

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/3b7d278bdabe4813a9f2e5c459a008ac.png)

来做 AI 网关管理真的不错：

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/906719f065d747c0b982fb5dde51b3c3.png)

### n8n

[Flexible AI workflow automation
for technical teams](https://n8n.io/)

```bash
docker run -d --name n8n-test --privileged=true -p 5678:5678 -v /data/projects/n8n-data:/home/node/.n8n -e N8N_SECURE_COOKIE=false -e GENERIC_TIMEZONE="Asia/Shanghai" -e TZ="Asia/Shanghai" 10.4.32.48:5000/n8nio/n8n:1.92.0
```

- 如果启不起来：`message: EACCES: permission denied, open '/home/node/.n8n/config'`

  [考虑放数据的文件夹是否有权限](https://github.com/n8n-io/n8n/issues/12007)，使用：`chown -R 1000:1000 文件夹`

- 如果报错建议你用https：`Your n8n server is configured to use a secure cookie`

  设置启动时的环境变量：`-e N8N_SECURE_COOKIE=false`

### 银河麒麟

我用的是V10SP3版本，启动：

```bash
docker run -it --name huazhi --privileged=true --network host -v E:\1-Work\4-Project\1-万华智享平台\HuaZhi-Backend:/data/HuaZhi ubuntu:18.04
```

### Ubuntu

```
docker run -it --name ubuntu-test --runtime nvidia --gpus all --privileged=true --network host -v E:/11-container/ubuntu-test:/data/ ubuntu:22.04
```

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

### Minio

直接启动！直接启动！

```bash
docker run -d -p 9000:9000 -p 9001:9001 --restart=always --privileged=true --name minio-test -v E:/11-container/minio-test/data:/data -v E:/11-container/minio-test/config:/root/.minio -e MINIO_ACCESS_KEY=root -e MINIO_SECRET_KEY=Qiangmima@666 quay.io/minio/minio:RELEASE.2023-12-20T01-00-02Z server /data --console-address ":9001"
```

要注意版本问题，之前我跑2019的版本，反正就各种出错，上面的可以跑通。

- `--console-address`：这里一定要制定管理端口，默认的可不是9001

[**Kubesphere配置**](https://blog.csdn.net/cqnaqjy/article/details/136853852)，注意事项：

1. 有状态副本集，所以需要先配置pvc，绑定的路径要记住了，比如 `/minio/data`

2. 用户名和密码记得配置环境变量：`MINIO_ROOT_USER`、`MINIO_ROOT_PASSWORD`

3. 启动命令一定要配置，`server /minio/data --console-address ":9001"`

   *因为前面 PVC 配置的 `/minio/data`，所以这里的启动命令也要一致*
   
   ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/fa4c195c4ca84863a1621fecf7cf82b8.png)

---

> [!tag] SGLang和vLLM有哪些区别？
>
> 参考：https://www.zhihu.com/question/666943660/answer/77360338901
>
> - vLLM（Virtual Large Language Model）的核心技术是**PagedAttention**。
>   - PagedAttention是一种新颖的注意力算法，其设计灵感来源于操作系统中的虚拟内存分页管理技术。通过将LLM（大型语言模型）服务状态分页管理，PagedAttention算法能够高效地处理大规模数据，从而实现高吞吐量的服务性能。
>   - 具体来说，PagedAttention算法将注意力机制中的缓存（如KV缓存）划分为多个小块（pages），根据用户输入token的数量动态分配这些小块的空间。这种非连续的内存管理方式避免了显存的浪费，提高了内存的利用率。同时，PagedAttention算法能够高效地管理注意力键和值，减少了重复计算，从而显著提高了推理速度。
>   - 相较于传统的注意力算法，PagedAttention算法在保持模型精度的同时，大幅提升了推理性能。实验表明，vLLM凭借PagedAttention算法，其吞吐量比HuggingFace Transformers高14-24倍，为自然语言处理领域的高效推理提供了新的解决方案。

### SGLang

怎么大厂都在说 SGLang 比vLLM更好啊，奶奶滴，做了fp8优化吗？

**ds-32b 蒸馏模型**

```bash
docker run -d --privileged=true --runtime nvidia --gpus all --shm-size 32g --name sglang-test -v /data/models:/data/models -p 8000:8000 10.4.32.48:5000/lmsysorg/sglang:v0.4.3.post2-cu124 python3 -m sglang.launch_server --model /data/models/DeepSeek-R1-Distill-Qwen-32B --host 0.0.0.0 --port 8000 --allow-auto-truncate --enable-dp-attention
```

**qwen3-30b moe模型**

```bash
docker run -d --privileged=true --runtime nvidia --gpus all --shm-size 32g --name qwen3  -v /data/models:/data/models -p 8000:8000 10.4.32.48:5000/lmsysorg/sglang:v0.4.6.post1-cu124 python3 -m sglang.launch_server --model /data/models/Qwen3-30B-A3B --host 0.0.0.0 --port 8000 --allow-auto-truncate
```

```bash
# 最新命令，更新时间 20250721，解决了docker指定gpu不好使的问题，不再需要docker-compose了，直接用docker也能指定gpu啦~
docker run -d \
  --name=qwen3-2 \
  --runtime=nvidia \
  --ipc=host \
  --shm-size=128g \
  -p 32802:8000 \
  -v /data2/litian/models:/data/models \
  --gpus '"device=2"' \
  10.4.32.48:5000/lmsysorg/sglang:v0.4.6.post1-cu124 \
  python3 -m sglang.launch_server \
  --model-path /data/models/Qwen3-30B-A3B \
  --host 0.0.0.0 \
  --port 8000 \
  --allow-auto-truncate
```

**qwen3.5-35b-a3b 模型**

```bash
docker run -d \
  --name=qwen3.5 \
  --runtime=nvidia \
  --ipc=host \
  --shm-size=128g \
  -p 32808:8000 \
  -v /data2/litian/models:/data/models \
  --gpus '"device=7"' \
  10.4.32.48:5000/lmsysorg/sglang:v0.5.9 \
  python3 -m sglang.launch_server \
  --model-path /data/models/Qwen3.5-35B-A3B \
  --host 0.0.0.0 \
  --port 8000 \
  --mem-fraction-static 0.95 \
  --context-length 262144 \
  --reasoning-parser qwen3 \
  --allow-auto-truncate
```

- `--gpus`：一般为 `all`，就是都可以用，如果指定gpu可以把 `all` 换成 `'"device=2"'`

- `--shm-size`：用来设置容器内一个特殊区域的大小，这个区域叫做“共享内存”（Shared Memory）。你可以把它想象成一个超级快的临时存储空间，它位于内存中，比普通硬盘快得多。

- `--enable-dp-attention`：Data Parallelism Attention optimization can be enabled for DeepSeek Series Models.

- `--enable-torch-compile`：启用 Torch Compile 优化，虽然会增加服务启动时间，但能显著提升推理性能。

- `--allow-auto-truncate`: 自动截断超过最大输入长度的请求。

- `--watchdog-timeout`: 调整看门狗线程的超时时间，在批处理生成花费过长时间时终止服务器。

- `--reasoning-parser`：解析思考内容，响应消息除了包含 `content` 字段外，还会有一个名为 `reasoning_content` 的字段，其中包含模型生成的思考内容。

  > 请注意，此功能与 OpenAI API 规范不一致。
  >
  > `enable_thinking=False` 可能与思考内容解析不兼容。如果需要向 API 传递 `enable_thinking=False`，请考虑禁用该功能。

> :warning: 如果跑起来报错啊啥的，服务启不起来，有可能是sglang的bug。比如：v0.4.3-cu124，就各种报错，切换了v0.4.3.post2-cu124就没事了

:bulb: 我发现我怎么搞都没办法直接指定gpu启动，每次都是用的0，无奈使用下面的docker-compose编排了一个解决

```yaml
services:
  sglang:
    runtime: nvidia
    ipc: host
    shm_size: 128g
    image: 10.4.32.48:5000/lmsysorg/sglang:v0.4.6.post1-cu124
    entrypoint: python3 -m sglang.launch_server
    command: >
      --model-path /data/models/Qwen3-30B-A3B
      --host 0.0.0.0
      --port 8000
      --allow-auto-truncate	
    ports:
      - "32801:8000"
    volumes:
      - /data2/litian/models:/data/models
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              device_ids: ["1"]
              capabilities: [gpu]
```

测试参数：`http://xxx/v1/chat/completions`

```json
// qwen3
{
    "model": "qwen3",
    "messages": [
        {
            "role": "user",
            "content": "你好。/no_think"
        }
    ]
}
```

```json
// qwen3.5 语言和视觉统一模型
{
    "model": "qwen3.5",
    // 可以通过配置关闭思考
    "chat_template_kwargs": {
        "enable_thinking": false
    },
    // 流输出控制
    "stream": false,
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "你是谁开发的，是什么版本"
                }
            ]
        }
    ]
}
```

### vLLM

> [vLLM中enforce_eager模式为何影响推理性能？_编程语言-CSDN问答](https://ask.csdn.net/questions/8861852)
>
> vLLM通过两大核心技术显著提升大模型推理效率：
>
> 1. **PagedAttention**：借鉴操作系统虚拟内存分页思想，将KV缓存切分为固定大小的“页面”，实现跨请求的内存块复用，避免连续内存分配导致的碎片化问题。
> 2. **CUDA Graph Optimization**：将整个前向计算流程捕获为静态CUDA图，减少GPU Kernel启动开销和CPU-GPU同步延迟，提升批处理吞吐量。
>
> :warning: 总结：不要使用 **enforce_eager=True**，不然没有高并发服务

可恶啊vLLM不能在windows上跑，下好模型，做好路径映射，然后：

比如qwen

```bash
docker run -d --privileged=true --runtime nvidia --gpus all --name vllm-test -v /data/vllm/huggingface:/root/.cache/huggingface -v /data/models:/data/models -p 8000:8000 --ipc=host vllm/vllm-openai:latest --model /data/models/qwen-2.5-1.5b
```

比如deepseek，注意，这里我80g A100也无法完美运行 `--max-model-len 32768`，因此修改为 `--max-model-len 10000`

> [!warning] deepseek推理要用新版vllm
>
> 除此之外还要用推理模式：`--enable-reasoning --reasoning-parser deepseek_r1`

```bash
docker run -d --runtime nvidia --gpus all --name vllm-test --ipc=host -v /data/models:/data/models -p 8000:8000  10.4.32.48:5000/vllm/vllm-openai:latest --model /data/models/DeepSeek-R1-Distill-Qwen-32B --max-model-len 10000 --gpu-memory-utilization 0.9
```

其中，参考[vLLM相关配置参数](https://zhuanlan.zhihu.com/p/3722264996)，docker相关参数解释如下：

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

> [!tag] 在vllm后面加个ollama的备注不过分吧
>
> 部署参考官网：https://github.com/ollama/ollama/blob/main/docs/linux.md
>
> 量化bge reranker参考hf：https://huggingface.co/gpustack/bge-reranker-v2-m3-GGUF
>
> 注意：怎么导入hf上下的模型，先编写一个 `Modelfile`，里面 `FROM /data/models/bge-reranker-v2-m3-GGUF`，后面的文件夹就是你的模型路径，然后用ollama导入，`ollama create bge-reranker-v2-m3-GGUF -f Modelfile`，:tada: 然后你就能在 `ollama list` 中看到你导入的模型了~

**Qwen3.6-35B-A3B**

参考1：[vLLM部署Qwen3.6-27B教程_vllm qwen3.6-CSDN博客](https://blog.csdn.net/hbslsdfdf/article/details/161081137)

参考2：[Qwen3.5 & Qwen3.6 使用指南 - vLLM 方案 - vLLM 文档](https://docs.vllm.com.cn/projects/recipes/en/latest/Qwen/Qwen3.5.html#installing-vllm)

```bash
docker run -d \
  --name=qwen3.6 \
  --runtime=nvidia \
  --ipc=host \
  --shm-size=128g \ 
  -p 6601:8000 \
  -v /data2/litian/models:/data/models \
  --gpus '"device=1,2"' \
  10.4.32.48:5000/vllm/vllm-openai:v0.22.1 \
  --tensor-parallel-size 2 \
  --gpu_memory_utilization 0.8 \
  --max_model_len 262144 \
  --reasoning-parser auto \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_coder \
  --enable-prefix-caching \
  --enable-chunked-prefill \
  --async-scheduling \
  --speculative-config '{"method": "mtp", "num_speculative_tokens": 1}' \
  --mm-encoder-tp-mode data \
  --mm-processor-cache-type shm \
  --model /data/models/Qwen3.6-35B-A3B  \
  --served-model-name qwen3 \
  --host 0.0.0.0 \
  --port 8000
```

**Qwen2.5-VL 7b** ==视觉模型==

```bash
docker run -d \
  --name=qwen2.5-vl \
  --runtime=nvidia \
  --ipc=host \
  --shm-size=128g \
  -p 32803:8000 \
  -v /data2/litian/models:/data/models \
  --gpus '"device=3"' \
  10.4.32.48:5000/vllm/vllm-openai:v0.10.0 \
  --model /data/models/Qwen2.5-VL-7B-Instruct \
  --served-model-name qwen2.5-vl \
  --host 0.0.0.0 \
  --port 8000
```

- `--served-model-name`：记得设置，这个就是访问的时候 `model` 参数要填入的值

- `--task`

  > https://docs.vllm.ai/en/latest/configuration/engine_args.html?h=task#modelconfig
  >
  > **--task**
  >
  > Possible choices: auto, classify, draft, embed, embedding, generate, reward, score, transcription, None
  >
  > [DEPRECATED] The task to use the model for. If the model supports more than one model runner, this is used to select which model runner to run.
  >
  > Note that the model may support other tasks using the same model runner.
  >
  > Default: None

测试参数：`http://xxx/v1/chat/completions`

```json
{
    "model": "qwen2.5-vl",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What's in this image?"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "data:image/png;base64,xxxxxxx"
                    }
                }
            ]
        }
    ]
}
```

**Qwen3-VL 30b a3b** ==视觉模型==

- Qwen3-VL-30B-A3B-Instruct，其实跟上面运行是一样的，修改一下名称啊、路径啊之类的就行，只需要注意，v**llm镜像的版本，v0.10.0不行，v0.11.0行了**

  ```bash
  docker run -d \
    --name=qwen3-vl \
    --runtime=nvidia \
    --ipc=host \
    --shm-size=128g \
    -p 32806:8000 \
    -v /data2/litian/models:/data/models \
    --gpus '"device=6"' \
    10.4.32.48:5000/vllm/vllm-openai:v0.11.0 \
    --gpu_memory_utilization 0.9 \
    --max_model_len 81920 \
    --model /data/models/Qwen3-VL-30B-A3B-Instruct \
    --served-model-name qwen3-vl \
    --host 0.0.0.0 \
    --port 8000
  ```

- 其次是一张 A100 80G 是无法运行满血的模型的，报错如下：

  ```
  (EngineCore_DP0 pid=268) ERROR 10-21 00:35:03 [core.py:708] ValueError: To serve at least one request with the models's max seq len (262144), (24.00 GiB KV cache is needed, which is larger than the available KV cache memory (8.04 GiB). Based on the available memory, the estimated maximum model length is 87840. Try increasing `gpu_memory_utilization` or decreasing `max_model_len` when initializing the engine.
  ```

  根据报错内容推断，还需要24G显存才行，剩下8.04G不够，因此满血模型默认参数部署需要 **96G** 的样子，由于 `gpu_memory_utilization` 参数的默认值是 0.9，因此我们做两个改动：

  1. 增加 `gpu_memory_utilization = 0.95`，少省一点
  2. 降低 `max_model_len = 100000`，到不了最大长度了 `262144（256k）`

- 但即使这样，还是会有显存超了的报错，只能把上面再缩一缩了，还是只能0.9啊，长度也再缩一缩

  ```
  torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 266.00 MiB. GPU 0 has a total capacity of 79.10 GiB of which 17.88 MiB is free. Process 3941857 has 79.07 GiB memory in use. Of the allocated memory 75.46 GiB is allocated by PyTorch, with 314.00 MiB allocated in private pools (e.g., CUDA Graphs), and 1.04 GiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation. 
  ```

**Qwen3 Embedding 8b** ==向量模型==

```bash
docker run -d \
  --name=qwen3-embedding \
  --runtime=nvidia \
  --ipc=host \
  --shm-size=128g \
  -p 32805:8000 \
  -v /data2/litian/models:/data/models \
  --gpus '"device=5"' \
  10.4.32.48:5000/vllm/vllm-openai:v0.10.0 \
  --model /data/models/Qwen3-Embedding-8B \
  --served-model-name qwen3-embedding \
  --task embedding \
  --host 0.0.0.0 \
  --port 8000
```

测试参数：`http://xxx/v1/embedding`

```json
{
    "model": "qwen3-embedding",
    "input": [
        "The capital of China is Beijing.",
        "Gravity is a force that attracts two bodies towards each other. It gives weight to physical objects and is responsible for the movement of planets around the sun."
    ]
}
```

**Qwen3 Reranker 8b** ==排序模型==

```bash
docker run -d \
  --name=qwen3-reranker \
  --runtime=nvidia \
  --ipc=host \
  --shm-size=128g \
  -p 32804:8000 \
  -v /data2/litian/models:/data/models \
  --gpus '"device=4"' \
  10.4.32.48:5000/vllm/vllm-openai:v0.10.0 \
  --model /data/models/Qwen3-Reranker-8B \
  --served-model-name qwen3-reranker \
  --task score \
  --host 0.0.0.0 \
  --port 8000
```

测试参数：`http://xxx/v1/rerank`

```json
{
    "model": "qwen3-reranker",
    "query": "What is the capital of China?",
    "documents": [
        "The capital of China is Beijing.",
        "Gravity is a force that attracts two bodies towards each other. It gives weight to physical objects and is responsible for the movement of planets around the sun."
    ]
}
```

### Text Embedding Interface

参考链接：https://huggingface.co/docs/text-embeddings-inference/quick_tour

以embedding举例：

```bash
docker run -d --runtime nvidia --gpus all --name embedding-test  -v /data/models:/data/models -p 8001:8001 --ipc=host  text-embeddings-inference --model-id /data/models/bge-m3 --port 8001
```

调用：如果是dify，直接配置到端口就行

```bash
curl 127.0.0.1:8080/embed \
    -X POST \
    -d '{"inputs":"What is Deep Learning?"}' \
    -H 'Content-Type: application/json'
```

以rerank举例：

```bash
docker run -d --runtime nvidia --gpus all --name rerank-test  -v /data/models:/data/models -p 8002:8002 --ipc=host  text-embeddings-inference --model-id /data/models/bge-reranker-v2-m3 --port 8002
```

调用：如果是dify，直接配置到端口就行，垃圾RAGFlow，TEI部署的rerank竟然不支持，ollama部署的也不支持，我真服了 :smile:

```bash
curl 127.0.0.1:8080/rerank \
    -X POST \
    -d '{"query":"What is Deep Learning?", "texts": ["Deep Learning is not...", "Deep learning is..."], "raw_scores": false}' \
    -H 'Content-Type: application/json'
```

### GitLab

参考链接：https://blog.csdn.net/weixin_42286658/article/details/144768578

```bash
docker run -d --name gitlab --restart always --privileged=true --log-opt max-size=10m --log-opt max-file=3 -p 80:80 -p 8022:22 -v /data/gitlab/etc:/etc/gitlab -v /data/gitlab/log:/var/log/gitlab -v /data/gitlab/opt:/var/opt/gitlab gitlab/gitlab-ce:17.8.0-ce.0
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
gitlab_rails['gitlab_shell_ssh_port'] =8022
# 时区顺便也改一下吧
gitlab_rails['time_zone'] = 'Asia/Shanghai'
```

:bulb: 后续我发现日志超多，直接给磁盘都占满了，所以可以 [关闭一下Prometheus啊gitlab_kas 等等的配置](https://cloud.tencent.com/developer/article/2146262)

```bash
prometheus['enable'] = false
gitlab_kas['enable'] = false
```

- `gitlab-ctl stop`
- `gitlab-ctl reconfigure`
- `gitlab-ctl start`

改好之后，生成配置文件：

```bash
# 宿主机输入：在容器中执行 gitlab-ctl reconfigure
docker exec -t mygitlab gitlab-ctl reconfigure
```

配置文件中，还要改个web server的端口，不然http的请求就不显示啦：`/opt/gitlab/embedded/service/gitlab-rails/config/gitlab.yml`，修改这个端口哦~

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/7f8a7682f0f64bf882da69123898e7c3.png)

修改之后，这里的http才正常显示端口

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/8a6953608f9f482ab4bf15efe9e152c6.png)

最后，要重启服务哦~

```bash
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

### Prometheus

1. 先去找个路径创建一下配置文件 `E:\11-container\prometheus-test\prometheus.yml `

   :bulb: *我是让大模型帮忙生成的*

   ```yaml
   # 全局配置
   global:
     scrape_interval: 15s
     evaluation_interval: 15s
     external_labels:
       monitor: 'my-monitor'
   
   # 告警规则
   # rule-files:
   # - 'rules/*.yml'
   
   # 监控目标
   scrape_configs:
     - job_name: 'prometheus'
       static_configs:
         - targets: ['localhost:9090']
   ```

2. 运行：`docker run -d --name prometheus-test --privileged=true --net=host -v E:/11-container/prometheus-test:/etc/prometheus prom/prometheus`

3. 查看ui界面：`http://localhost:9090/`

   ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/d1fea172ec014d87aaf79ac807a8f83c.png)

### Grafana

官网就有安装手册啦拜托：https://grafana.com/docs/grafana/latest/setup-grafana/installation/docker/

```bash
docker run -d -p 3000:3000 --name=grafana -e "GF_SECURITY_COOKIE_SECURE=true" -e "GF_SECURITY_COOKIE_SAMESITE=none" -e "GF_SECURITY_ALLOW_EMBEDDING=true" --volume "E:\11-container\grafana-test:/var/lib/grafana" grafana/grafana-enterprise
```

- 这里加环境变量是为了让外部可以集成 grafana 的报表

- 进去之后要输入的是管理员密码：admin/admin，成功了要修改密码哦

> :warning: 报错：mkdir: can't create directory '/var/lib/grafana/plugins': Permission denied
>
> 其实就是说你挂载的路径没有权限，直接 `chmod 777 当前路径` 即可

**那么如何连接prometheus呢**

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/e8db3affecc5445b926574847aef047c.png)

**那么如何配置higress呢**

- grafana 配置好了 prometheus 后，我们可以在路径上拿到一串 id。*当然了，根据 higress 的文档指导是一样的。*

- 然后填入到对应的位置，就能获得好的配置文件啦

  ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/d52baf4db6064adb87f9c91abfff1cd4.png)

- grafana 中的 dashboard 可以导入前面获得的 json 配置文件

  ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/8fa5710ac5eb4451af41bb8dcfb242fd.png)

- 这就弄好啦，家人们

  ![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/33819aff706742f5aec6ea3f82fc676d.png)

- higress集成，直接把dashboard的url粘过去就行。

  > :warning: 注意，不要用什么内部、外部分享链接，直接拿url就行。
  >
  > :warning: 虽然我是成功了，但是又出现了频繁跳转登录页的问题。。。哎。

### ChemGraph

- 阿贡实验室Nature子刊【AI4C】让AI帮你跑量化化学：ChemGraph如何用大语言模型驯服复杂分子模拟流程

- https://mp.weixin.qq.com/s/A_ebnX0dfY7m7ll3n92p1g?scene=1&click_id=4

- 需要注意的是，看源码，如果要用vllm部署的本地模型，需要自己给环境里写好这些变量

  ```bash
  docker run --rm -itd --name chemgraph -e VLLM_BASE_URL="http://xxxxxx/v1" -e OPENAI_API_KEY="aa" -p 8501:8501 ghcr.io/argonne-lcf/chemgraph:latest  streamlit run src/ui/app.py --server.address=0.0.0.0 --server.port=8501
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
