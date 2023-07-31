from django.contrib import admin

from retro_cars.restoration_shops.models import RestorationShop, Locations


# Register your models here.


@admin.register(RestorationShop)
class RestorationShopAdmin(admin.ModelAdmin):
    pass


@admin.register(Locations)
class LocationsAdmin(admin.ModelAdmin):
    pass
