# Python数据科学手册Seaborn马拉松可视化里时分秒转化为秒数的问题

## 问题描述：

我实在是太懒了，问题描述抄的网上的哈哈哈：<https://www.jianshu.com/p/6ab7afa059d1>

> 在做Python Data Science Handbook的实例学习，4.16.3 案例：探索马拉松比赛成绩里，有提示将时分秒的时间化为秒的总数，以方便画图。书里给出的指令是：
>
> **data['split_sec']=data['split'].astype(int)/1E9**
>
> **data['final_sec']=data['final'].astype(int)/1E9**
>
> 我用这种方式会出现以下错误：
>
> **TypeError: cannot astype a timedelta from [timedelta64[ns]] to [int32]**

## 解决办法：

问题描述的连接里面给出了一种解决办法，可是这种解决办法太复杂了，我想了一个更简单的。

先写一个将Timedelta格式的时间数据转化为总秒数的函数：

```python
def transfor_time(tt):
    return tt.total_seconds()
```

然后对我们需要的列广播这个函数：

```python
data['split_sec'] = data['split'].apply(transfor_time)
data['final_sec'] = data['final'].apply(transfor_time)
```

查看结果：

```python
data.head()
```

![img](https://img-blog.csdnimg.cn/20190530100318792.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIxNTc5MDQ1,size_16,color_FFFFFF,t_70)

OK！完美解决。。。



------

我的CSDN：https://blog.csdn.net/qq_21579045

我的博客园：https://www.cnblogs.com/lyjun/

我的Github：https://github.com/TinyHandsome

纸上得来终觉浅，绝知此事要躬行~

欢迎大家过来OB~

by 李英俊小朋友