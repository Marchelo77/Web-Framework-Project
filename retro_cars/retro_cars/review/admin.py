from django.contrib import admin

from retro_cars.review.models import Review


# Register your models here.

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
