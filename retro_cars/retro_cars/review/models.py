from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.

UserModel = get_user_model()


class Review(models.Model):
    comment = models.TextField(max_length=300,
                               validators=[
                                   MinLengthValidator(2)
                               ])

    date = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['-date']
