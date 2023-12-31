# Generated by Django 4.2.3 on 2023-07-29 19:33

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import retro_cars.cars.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RetroCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_image', models.URLField()),
                ('model', models.CharField(max_length=30, validators=[retro_cars.cars.validators.valid_car_model_validator])),
                ('description', models.TextField(blank=True, max_length=400, null=True, validators=[django.core.validators.MinLengthValidator(10)])),
                ('year', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1950), django.core.validators.MaxValueValidator(2002)])),
                ('date_of_publication', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_of_publication'],
            },
        ),
    ]
