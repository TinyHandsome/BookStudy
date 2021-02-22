# 自动化LeapHD文档

[TOC]

## 1. 写在前面

- 还没想好写啥

## 2. 实现思路

### 2.1 自动重跑

1. searchProcess.do | 查询目标实例列表

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210222110941602.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

2. getProcessRuns.do | 查询所有运行实例列表

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/2021022209404275.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

3. checkRerunProcess.do | 点击重跑按钮

   此时会弹出需要确认的框

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210222094156720.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

4. rerunProcesses.do | 实施重跑

   此时还会调用getProcessRuns.do

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/2021022209451629.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

   ![在这里插入图片描述](https://img-blog.csdnimg.cn/20210222094603354.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)