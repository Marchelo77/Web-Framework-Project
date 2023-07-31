from django.core.exceptions import ValidationError


def valid_phone_number_validator(value):
    for ch in value:
        if not ch.isdigit():
            raise ValidationError("Phone Number must contain only digits!")
