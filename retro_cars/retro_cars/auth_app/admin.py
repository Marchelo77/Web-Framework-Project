from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db.models.functions import Upper, Lower

from retro_cars.auth_app.forms import GroupAdminForm

from django.db import models

# from django.contrib.auth.admin import UserAdmin, GroupAdmin
#
# from retro_cars.auth_app.models import AppUser, CustomGroup

UserModel = get_user_model()


@admin.register(UserModel)
class ProfileAdmin(admin.ModelAdmin):
    pass


admin.site.unregister(Group)


class GroupAdmin(admin.ModelAdmin):
    form = GroupAdminForm

    filter_horizontal = ['permissions']

    list_display = ('name', 'custom_field1', 'custom_field2', 'custom_field3')
    search_fields = ('name',)
    ordering = ('id',)

    readonly_fields = ('id',)

    def custom_field1(self, obj):
        return obj.id

    custom_field1.short_description = 'Group ID'

    def custom_field2(self, obj):
        return ', '.join([user.username for user in obj.user_set.all()])

    custom_field2.short_description = 'Users in the Group'

    def custom_field3(self, obj):
        return [user.id for user in obj.user_set.all()]

    custom_field3.short_description = 'User ID'


admin.site.register(Group, GroupAdmin)
