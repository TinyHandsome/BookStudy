from django.db import models


class UserModel(models.Model):
    u_name = models.CharField(max_length=32, unique=True)
    u_password = models.CharField(max_length=256)

    is_delete = models.BooleanField(default=False)
    is_super = models.BooleanField(default=False)
