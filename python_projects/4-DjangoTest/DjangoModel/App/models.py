from django.db import models


# Create your models here.
class Person(models.Model):
    p_name = models.CharField(max_length=16, unique=True, db_column='name')
    p_age = models.IntegerField(default=18, db_column='age')
    # False代表男孩，True代表女孩
    p_sex = models.BooleanField(default=False, db_column='sex')

    class Meta:
        db_table = 'People'
