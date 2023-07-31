from django.core.exceptions import ValidationError


def valid_name_validator(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError("Your name must contain only letters!")
