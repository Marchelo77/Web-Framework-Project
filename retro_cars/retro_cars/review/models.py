from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.

UserModel = get_user_model()


class Review(models.Model):
    COMMENT_MAX_LENGTH = 300

    comment = models.TextField(max_length=COMMENT_MAX_LENGTH,
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
