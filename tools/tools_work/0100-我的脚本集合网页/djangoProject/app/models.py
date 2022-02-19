from django.db import models
from app.mymodels.func2.hana2hive import DMPTbls


class MyRole(models.Model):
    """我的角色，不同的角色能看到的功能不同"""
    name = models.CharField(max_length=128, unique=True, verbose_name='规则名称')
    alias = models.CharField(max_length=32, unique=True, verbose_name='规则别名')


class User(models.Model):
    ip = models.CharField(max_length=32, unique=True, verbose_name='ip')
    name = models.CharField(max_length=255, default='未知', verbose_name='姓名')
    count = models.IntegerField(default=0, verbose_name='访问次数')
    is_admin = models.BooleanField(default=False, verbose_name='是否是管理员')
    rule = models.ForeignKey(MyRole, default='', on_delete=models.SET_DEFAULT)

    class Meta:
        db_table = 'User'
