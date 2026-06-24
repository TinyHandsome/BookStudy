---
tags:
  - django
  - djongo
  - python
  - daphne
  - gunicorn
banner: 3-踩坑笔记/92-django问题汇总.assets/f64ec0c37861422bbcc83215b39843b4.png
sticker: emoji//1f40d
---
# django问题汇总

[TOC]

> 我不会设置仅粉丝可见，不需要你关注我，仅仅希望我的踩坑经验能帮到你。如果有帮助，麻烦点个 :+1: 吧，这会让我创作动力+1 :grin:。我发现有的时候会自动要求会员才能看，可以留言告诉我，不是我干的！😠
>
> **django问题汇总贴，不断学习不断更新。当前更新时间：** ==20250618==

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/f64ec0c37861422bbcc83215b39843b4.png)

## 静态文件处理

静态文件有两个东西：

:one: admin的静态文件，先 `python manage.py collectstatic` 把东西都收集到文件夹中，一般是 `static` 文件夹的 `admin` 下；

:two: `favicon.ico`，放在 `static/icon/` 路径下，主要是为了不跟 `static/` 重复。

解决：查了全网半天整不明白，最终还是自己看源码慢慢摸明白了

- 首先是 `settings.py`，注意这里 `STATICFILES_DIRS` 的路径不要跟 `STATIC_ROOT` 收集静态文件的路径重复了（为了防止重复收集静态文件）

  ```python
  STATIC_URL = "static/"
  
  # ----- 下面是新加的内容 -----
  # 配置才能在生产环境收集静态文件  `python manage.py collectstatic`
  # 这是 Django 收集所有静态文件的最终目标目录（通过 collectstatic 命令生成）。
  STATIC_ROOT = os.path.join(BASE_DIR, "static")
  # 配置了才能让admin的图表 favicon.ico 正常工作
  # 这是 Django 在收集静态文件时，额外搜索的源目录（除了应用内部的 static/ 目录）。
  STATICFILES_DIRS = [
      os.path.join(BASE_DIR, 'static/icon/'),
  ]
  ```

- 其次是总路由 `urls.py`

  favicon路由的逻辑就是：从静态路径 `static/ilovebasketball.svg` 中找这个文件当做 `favicon.ico`，而 `static` 的路径前面定好了，一个是默认的 `static/`，还一个是 `STATICFILES_DIRS` 定义的 `static/icon/`，所以就能找到了，缺一不可
  
  ```python
  from django.urls import re_path
  from django.contrib.staticfiles.views import serve
  from django.views.generic.base import RedirectView
  
  urlpatterns = [
      ...
      # 配置生产环境静态文件服务，先收集静态文件，然后配置路由
      re_path(r'static/(?P<path>.*)$', lambda request, path, insecure=True, **kwargs: serve(request, path, insecure, **kwargs), name='static'),
      # 配置favicon.ico的重定向，同时需要配置 STATICFILES_DIRS 
      re_path(r'^favicon\.ico$', RedirectView.as_view(url=r'static/ilovebasketball.svg')),
      ...
  ]
  ```

最后，我是用 `daphne` 启动的服务，总之没问题~

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/a5f8a2f1a7644f08874c1610731e5e99.png)

------


- :cloud: 我的CSDN：`https://blog.csdn.net/qq_21579045`
- :snowflake: 我的博客园：`https://www.cnblogs.com/lyjun/`
- :sunny: 我的Github：`https://github.com/TinyHandsome`
- :rainbow: 我的bilibili：`https://space.bilibili.com/8182822`
- :avocado: 我的思否：`https://segmentfault.com/u/liyj`
- :tomato: 我的知乎：`https://www.zhihu.com/people/lyjun_`
- :penguin: 粉丝交流群：1060163543，神秘暗号：为干饭而来

碌碌谋生，谋其所爱。:ocean:              @李英俊小朋友
