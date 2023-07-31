from django.db import models

from retro_cars.restoration_shops.validators import valid_phone_number_validator


# Create your models here.


class RestorationShop(models.Model):
    offer_image_url = models.URLField()

    offer = models.CharField(max_length=40)

    description = models.TextField(max_length=200)


class Locations(models.Model):
    city = models.CharField(max_length=20)

    address = models.CharField(max_length=100)

    phone_number = models.CharField(
        validators=[
            valid_phone_number_validator
        ]
    )

    email = models.EmailField()

    image_url = models.URLField()
