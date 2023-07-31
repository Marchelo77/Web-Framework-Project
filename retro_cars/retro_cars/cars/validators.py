from django.core.exceptions import ValidationError


def valid_car_model_validator(value):
    for ch in value:
        if not ch.isalnum() and not ch == '-' and not ch == '(' and not ch == ')' and not ch == " ":
            raise ValidationError("Name should contain only letters, digits and the following symbols - '-' '(' ')'")
