from django.db import models


class Student(models.Model):
    s_name = models.CharField(max_length=16, unique=True)
    s_password = models.CharField(max_length=128)

    s_token = models.CharField(max_length=256)