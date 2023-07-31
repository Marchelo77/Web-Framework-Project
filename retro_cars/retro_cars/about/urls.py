from django.urls import path

from retro_cars.about.views import about_page, event_page

urlpatterns = [
    path('', about_page, name="about page"),
    path('events/', event_page, name="event page"),
]
