from django.db import models


class User(models.Model):
    u_name = models.CharField(max_length=16, unique=True)
    u_password = models.CharField(max_length=256)

class Order(models.Model):
    o_num = models.CharField(max_length=16, unique=True)
    o_time = models.DateTimeField(auto_now_add=True)