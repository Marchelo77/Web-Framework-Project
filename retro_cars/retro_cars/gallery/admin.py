from django.contrib import admin

from retro_cars.gallery.models import Gallery


# Register your models here.


@admin.register(Gallery)
class AdminGallery(admin.ModelAdmin):
    pass
