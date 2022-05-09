from django.db import models
from app.mymodels.func2.hana2hive import DMPTbls
from supports.password_management import encode_password


class Role(models.Model):
    """我的角色，不同的角色能看到的功能不同"""
    name = models.CharField(max_length=128, unique=True, verbose_name='规则名称')
    alias = models.CharField(max_length=32, unique=True, verbose_name='规则别名')

    list_display = ('name', 'alias')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'my_table_role'
        verbose_name = verbose_name_plural = '我的角色'


class IP(models.Model):
    """IP"""
    ip = models.CharField(max_length=32, unique=True, verbose_name='ip')
    name = models.CharField(max_length=255, default='未知', verbose_name='姓名')
    count = models.IntegerField(default=0, verbose_name='访问次数')
    is_admin = models.BooleanField(default=False, verbose_name='是否是管理员')
    rule = models.ForeignKey(Role, on_delete=models.SET_DEFAULT, null=True, blank=True, default=2)

    class Meta:
        db_table = 'my_table_ip'
        verbose_name = verbose_name_plural = '我的IP'

    def __str__(self):
        return self.name


class User(models.Model):
    """用户"""
    username = models.CharField(max_length=255, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=255, verbose_name='密码')

    class Meta:
        db_table = 'my_table_user'
        verbose_name = verbose_name_plural = '我的用户'

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.password = encode_password(self.password)
        super().save(*args, **kwargs)


class FuncType(models.Model):
    """模型类型"""
    func_type_name = models.CharField(max_length=64, verbose_name='功能类型')
    func_type_des = models.CharField(max_length=255, default=None, verbose_name='功能类型描述')
    shown_index = models.BooleanField(default=True, verbose_name='是否展示在主页')

    class Meta:
        db_table = 'my_table_functype'
        verbose_name = verbose_name_plural = '我的功能'

    def __str__(self):
        return self.func_type_name


class Url(models.Model):
    """地址管理模型"""

    labels = (
        (1, '正常使用'),
        (2, '开发中'),
        (3, '开发者使用'),
        (4, '特定用户使用'),
    )

    func_name = models.CharField(max_length=255, unique=True, verbose_name='功能')
    func_url = models.CharField(max_length=64, unique=True, verbose_name='地址')
    func_url_name = models.CharField(max_length=64, default='', verbose_name='地址别名')
    func_type = models.ForeignKey(FuncType, default=0, on_delete=models.SET_DEFAULT, verbose_name='功能类型')
    func_des = models.CharField(max_length=255, default=None, verbose_name='功能描述')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    func_label = models.IntegerField(default=1, choices=labels, verbose_name='状态')
    auth_role = models.ForeignKey(Role, default=2, verbose_name='访问角色权限', on_delete=models.PROTECT)

    class Meta:
        db_table = 'my_table_url'
        verbose_name = verbose_name_plural = '我的地址'

    def __str__(self):
        return self.func_name
