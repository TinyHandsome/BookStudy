from django.db import models


class UserModel(models.Model):
    u_name = models.CharField(max_length=16, unique=True)
    u_password = models.CharField(max_length=256)

    def __str__(self):
        return self.u_name


class Address(models.Model):
    a_address = models.CharField(max_length=128)
    a_user = models.ForeignKey(UserModel, related_name='address_list', null=True, blank=True)

    def __str__(self):
        return self.a_address
