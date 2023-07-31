from django.urls import path, include

from retro_cars.auth_app.views import ProfileDetailsView, ProfileDeleteView, LogoutUserView, LoginUserView, \
    RegisterUserView, \
    ProfileEditView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name="profile register"),
    path('login/', LoginUserView.as_view(), name="profile login"),
    path('logout/', LogoutUserView.as_view(), name="profile logout"),
    path('profile/<int:pk>/', include([
        path('', ProfileDetailsView.as_view(), name="profile page"),
        path('delete/', ProfileDeleteView.as_view(), name="profile delete"),
        path('edit/', ProfileEditView.as_view(), name="profile edit"),
    ])),
]
