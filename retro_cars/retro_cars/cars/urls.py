from django.urls import path, include

from retro_cars.cars.views import CarPageView, CarCreateView, EditCarView, DeleteCarView, DetailCarView

urlpatterns = [
    path('', CarPageView.as_view(), name="car page"),
    path('add/', CarCreateView.as_view(), name="car create"),
    path('<int:pk>/details/', include([
        path('', DetailCarView.as_view(), name="car details"),
        path('edit/', EditCarView.as_view(), name="car edit"),
        path('delete/', DeleteCarView.as_view(), name="car delete"),
    ])),

]
