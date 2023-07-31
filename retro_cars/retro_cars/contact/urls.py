from django.urls import path

from retro_cars.contact.views import contact_page

urlpatterns = [
    path('', contact_page, name="contact page")
]
