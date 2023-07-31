from django.contrib import admin

from retro_cars.about.models import Event


# Register your models here.


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass
