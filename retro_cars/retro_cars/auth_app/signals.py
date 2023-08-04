from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(instance, created, **kwargs):
    if created:
        send_successful_registration_email(instance)


def send_successful_registration_email(user):
    send_mail(
        subject='Hello',
        message='You were registered successfully! Enjoy our site!',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=(user.email,),
    )
