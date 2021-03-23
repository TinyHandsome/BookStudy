from django.db import models


class Person(models.Model):
    p_name = models.CharField(max_length=16)
    p_sex = models.BooleanField(default=False)


class IDCard(models.Model):
    id_num = models.CharField(max_length=18, unique=True, null=True, blank=True)
    id_person = models.OneToOneField(Person, null=True, blank=True, on_delete=models.SET_NULL)

