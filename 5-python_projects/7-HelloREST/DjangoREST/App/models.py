from django.db import models


# Create your models here.
class Game(models.Model):
    g_name = models.CharField(max_length=32)
    g_price = models.FloatField(default=0)
