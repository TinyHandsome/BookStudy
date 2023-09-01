from django.db import models

# Create your models here.
from tinymce.models import HTMLField


class Blog(models.Model):
    b_content = HTMLField()
