from django.db import models


class Grade(models.Model):
    g_name = models.CharField(max_length=16)
    g_position = models.CharField(max_length=20)


class Student(models.Model):
    s_name = models.CharField(max_length=32)
    s_age = models.IntegerField(default=1)
    s_sex = models.BooleanField(default=False)
    s_height = models.FloatField(default=1)
    s_weight = models.FloatField(default=1)

    s_grade = models.ForeignKey(Grade)


