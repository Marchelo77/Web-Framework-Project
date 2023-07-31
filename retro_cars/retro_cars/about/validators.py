from django.core.exceptions import ValidationError


def valid_date_validator(value):
    for ch in value:
        if not ch.isnumeric() and not ch == '.':
            raise ValidationError("Please write a valid date for example - 20.06.2023")
