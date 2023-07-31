from django.contrib import admin

from retro_cars.cars.models import RetroCar


# Register your models here.

@admin.register(RetroCar)
class RetroCarAdmin(admin.ModelAdmin):
    pass
