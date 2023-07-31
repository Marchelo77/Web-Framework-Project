from django.urls import path

from retro_cars.gallery.views import gallery_page

urlpatterns = [
    path('', gallery_page, name="gallery page")
]
