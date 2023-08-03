from enum import Enum

from django.contrib.auth.models import AbstractUser, Group
from django.core.validators import MinLengthValidator
from django.db import models

from retro_cars.auth_app.validators import valid_name_validator


class ChoicesMixin:
    @classmethod
    def choices(cls):
        return [(choices.value, choices.name) for choices in cls]


class Gender(ChoicesMixin, Enum):
    MALE = 1
    FEMALE = 2
    NONE_GIVEN = 3


class AppUser(AbstractUser):
    FIRST_AND_LAST_NAME_MAX_LENGTH = 50
    email = models.EmailField(
        unique=True
    )

    first_name = models.CharField(
        max_length=FIRST_AND_LAST_NAME_MAX_LENGTH,
        blank=True,
        null=True,
        validators=[
            MinLengthValidator(2),
            valid_name_validator,
        ]
    )

    last_name = models.CharField(
        max_length=FIRST_AND_LAST_NAME_MAX_LENGTH,
        blank=True,
        null=True,
        validators=[
            MinLengthValidator(2),
            valid_name_validator,
        ]
    )

    profile_picture = models.URLField(
        blank=True,
        null=True
    )

    gender = models.IntegerField(
        choices=Gender.choices(),
        default=Gender.NONE_GIVEN.value,
    )

    def save(self, *args, **kwargs):
        result = super().save(*args, **kwargs)

        return result


