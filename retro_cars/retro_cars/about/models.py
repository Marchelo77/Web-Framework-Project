from django.db import models

from retro_cars.about.validators import valid_date_validator


# Create your models here.


class Event(models.Model):
    EVENT_MAX_LENGTH = 30
    DESCRIPTION_MAX_LENGTH = 500
    EVENT_LOCATION_MAX_LENGTH = 100

    event_name = models.CharField(
        max_length=EVENT_MAX_LENGTH
    )

    description = models.TextField(
        max_length=DESCRIPTION_MAX_LENGTH
    )

    event_date = models.DateField()

    event_location = models.CharField(
        max_length=EVENT_LOCATION_MAX_LENGTH
    )

    image_url = models.URLField()
