from django.urls import path

from retro_cars.review.views import ReviewView, DeleteReviewView
urlpatterns = [
    path('', ReviewView.as_view(), name="review page"),
    path('<int:pk>/delete/', DeleteReviewView.as_view(), name="review delete"),
]
