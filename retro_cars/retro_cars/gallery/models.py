from django.db import models

# Create your models here.


class Gallery(models.Model):
    image_url = models.URLField()
