from django.shortcuts import render

from retro_cars.about.models import Event
from retro_cars.gallery.models import Gallery


# Create your views here.


def about_page(request):
    photos = Gallery.objects.all()[:4]

    context = {
        'photos': photos
    }
    return render(request, 'about/about.html', context)


def event_page(request):
    events = Event.objects.all()

    context = {
        'events': events
    }

    return render(request, 'about/event.html', context)
