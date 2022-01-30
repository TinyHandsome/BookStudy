from django.db import models
from app.mymodels.func2.hana2hive import DMPTbls


class User(models.Model):
    ip = models.CharField(max_length=32, unique=True, verbose_name='ip')
    name = models.CharField(max_length=255, default='未知', verbose_name='姓名')
    count = models.IntegerField(default=0, verbose_name='访问次数')

    class Meta:
        db_table = 'User'

