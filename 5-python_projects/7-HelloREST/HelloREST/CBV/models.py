from django.db import models


class Book(models.Model):
    b_name = models.CharField(max_length=32)
    b_price = models.FloatField(default=10)

    def to_dict(self):
        return {'id': self.id, 'b_name': self.b_name, 'b_price': self.b_price}
