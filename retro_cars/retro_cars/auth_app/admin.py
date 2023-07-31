from django.contrib import admin
from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin, GroupAdmin
#
# from retro_cars.auth_app.models import AppUser, CustomGroup

UserModel = get_user_model()


@admin.register(UserModel)
class ProfileAdmin(admin.ModelAdmin):
    pass


# admin.site.register(AppUser, UserAdmin)
# admin.site.register(CustomGroup, GroupAdmin)
