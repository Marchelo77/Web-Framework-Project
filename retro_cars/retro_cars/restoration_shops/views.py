from django.shortcuts import render

from retro_cars.restoration_shops.models import RestorationShop, Locations


def restoration_shop(request):
    services = RestorationShop.objects.all()

    context = {
        'services': services,
    }
    return render(request, 'service/restoration-shop.html', context)


def locations_page(request):
    locations = Locations.objects.all()

    context = {
        'locations': locations
    }
    return render(request, 'service/locations.html', context)
