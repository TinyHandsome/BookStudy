from django.db import models


class Student(models.Model):
    s_name = models.CharField(max_length=16)

    def get_name(self):
        return self.s_name
