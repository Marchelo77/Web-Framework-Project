from django.urls import path

from retro_cars.restoration_shops.views import restoration_shop, locations_page

urlpatterns = [
    path('', restoration_shop, name="restoration shop"),
    path('locations/', locations_page, name="locations page")
]
