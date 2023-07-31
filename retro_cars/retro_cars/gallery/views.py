from django.shortcuts import render


from retro_cars.gallery.models import Gallery


def gallery_page(request):
    gallery = Gallery.objects.all()

    context = {
        'gallery': gallery,
    }
    return render(request, 'gallery/gallery.html', context)
