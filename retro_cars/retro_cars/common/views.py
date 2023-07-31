from django.shortcuts import render

from retro_cars.restoration_shops.models import RestorationShop
from retro_cars.review.models import Review


# Create your views here.


def home_page(request):
    reviews = Review.objects.all()[:2]
    services = RestorationShop.objects.all()[:4]

    context = {
        'reviews': reviews,
        'services': services
    }
    return render(request, 'index.html', context)
