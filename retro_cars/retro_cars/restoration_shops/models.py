from django.db import models

from retro_cars.restoration_shops.validators import valid_phone_number_validator


# Create your models here.


class RestorationShop(models.Model):
    OFFER_MAX_LENGTH = 40
    DESCRIPTION_MAX_LENGTH = 200

    offer_image_url = models.URLField()

    offer = models.CharField(max_length=OFFER_MAX_LENGTH)

    description = models.TextField(max_length=DESCRIPTION_MAX_LENGTH)


class Locations(models.Model):
    CITY_MAX_LENGTH = 20
    ADDRESS_MAX_LENGTH = 100

    city = models.CharField(max_length=CITY_MAX_LENGTH)

    address = models.CharField(max_length=ADDRESS_MAX_LENGTH)

    phone_number = models.CharField(
        validators=[
            valid_phone_number_validator
        ]
    )

    email = models.EmailField()

    image_url = models.URLField()
