from django.db import models


class UserModel(models.Model):
    u_name = models.CharField(max_length=16, unique=True)
    u_password = models.CharField(max_length=256)


class Address(models.Model):
    a_address = models.CharField(max_length=128)
    a_user = models.ForeignKey(UserModel, related_name='address_list', null=True, blank=True)
