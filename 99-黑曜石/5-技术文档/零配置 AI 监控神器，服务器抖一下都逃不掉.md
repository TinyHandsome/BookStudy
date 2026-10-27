---
tags:
  - 云原生
link: https://mp.weixin.qq.com/s/QQL2vT3zV8_jJ0niHtgk2A
---

搞过监控的人都知道，从零搭一套 Prometheus 加 Grafana 是什么体验。写采集配置、接数据源、调仪表盘，一个下午就没了，而且每加一台机器还要再改一遍配置。我自己几台服务器上一直跑着 <font color="#ffc000">Netdata</font>，图的就是装完就能看。

- 它答应你的是一秒粒度的现场
- 装完不用配，是因为它自己会扫
- 异常检测是它最像 AI 的部分
- 指标和日志在同一个面板里
- 历史存储是它的短板，也是它和 Prometheus 分工的原因
- 父子节点还是上云，差别在数据出不出网

![CPU 与内存的实时图表，图表上方是异常率标记](%E9%9B%B6%E9%85%8D%E7%BD%AE%20AI%20%E7%9B%91%E6%8E%A7%E7%A5%9E%E5%99%A8%EF%BC%8C%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%8A%96%E4%B8%80%E4%B8%8B%E9%83%BD%E9%80%83%E4%B8%8D%E6%8E%89.assets/image-20261027094006094.png)

![日志页，优先级分布与日志表](%E9%9B%B6%E9%85%8D%E7%BD%AE%20AI%20%E7%9B%91%E6%8E%A7%E7%A5%9E%E5%99%A8%EF%BC%8C%E6%9C%8D%E5%8A%A1%E5%99%A8%E6%8A%96%E4%B8%80%E4%B8%8B%E9%83%BD%E9%80%83%E4%B8%8D%E6%8E%89.assets/image-20261027094104347.png)

## Docker

参考：[Install Netdata with Docker | Installation | Learn Netdata](https://learn.netdata.cloud/docs/netdata-agent/installation/docker)

gpu 支持：Add `--gpus 'all,capabilities=utility'` to your `docker run`.

```bash
docker run -d --name=netdata \
  --pid=host \
  --network=host \
  --gpus 'all,capabilities=utility' \
  -v netdataconfig:/etc/netdata \
  -v netdatalib:/var/lib/netdata \
  -v netdatacache:/var/cache/netdata \
  -v /:/host/root:ro,rslave \
  -v /etc/passwd:/host/etc/passwd:ro \
  -v /etc/group:/host/etc/group:ro \
  -v /etc/localtime:/etc/localtime:ro \
  -v /proc:/host/proc:ro \
  -v /sys:/host/sys:ro \
  -v /etc/os-release:/host/etc/os-release:ro \
  -v /var/log:/host/var/log:ro \
  -v /var/run/docker.sock:/var/run/docker.sock:ro \
  -v /run/dbus:/run/dbus:ro \
  --restart unless-stopped \
  --cap-add SYS_PTRACE \
  --cap-add SYS_ADMIN \
  --security-opt apparmor=unconfined \
  10.4.32.48:5000/netdata:stable
```

- 测试服务器：http://10.5.33.83:19999/ ，齐聚
- docker执行之后要等一下才能进入dashboard
- gpu的没整明白，调了一顿还是不行

