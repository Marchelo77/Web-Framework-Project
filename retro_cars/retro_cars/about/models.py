from django.db import models

from retro_cars.about.validators import valid_date_validator


# Create your models here.


class Event(models.Model):
    event_name = models.CharField(max_length=30)

    description = models.TextField(max_length=500)

    event_date = models.DateField()

    event_location = models.CharField(max_length=100)

    image_url = models.URLField()
