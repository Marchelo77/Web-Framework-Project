from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from retro_cars.cars.validators import valid_car_model_validator

UserModel = get_user_model()


class RetroCar(models.Model):
    CAR_MODEL_MAX_LENGTH = 30
    CAR_DESCRIPTION_MAX_LENGTH = 400

    car_image = models.URLField()

    model = models.CharField(max_length=CAR_MODEL_MAX_LENGTH,
                             validators=[
                                 valid_car_model_validator,
                             ])

    description = models.TextField(
        max_length=CAR_DESCRIPTION_MAX_LENGTH,
        validators=[
            MinLengthValidator(10)
        ],
        blank=True,
        null=True
    )

    year = models.IntegerField(
        validators=[
            MinValueValidator(1950),
            MaxValueValidator(2002),
        ],
        blank=True,
        null=True
    )

    date_of_publication = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['-date_of_publication']
