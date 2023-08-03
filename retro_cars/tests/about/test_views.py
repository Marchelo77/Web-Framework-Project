from django.test import TestCase
from django.urls import reverse
from retro_cars.about.models import Event
from retro_cars.gallery.models import Gallery


class AboutPageViewTest(TestCase):
    def test_about_page_view(self):
        gallery = Gallery.objects.create(
            image_url='https://test.com/gallery/image1.jpg'
        )
        for i in range(2, 6):
            Gallery.objects.create(image_url=f'https://test.com/gallery/image{i}.jpg')

        response = self.client.get(reverse('about page'))

        self.assertEqual(response.status_code, 200)

        self.assertIn('photos', response.context)
        photos = response.context['photos']

        self.assertEqual(photos.count(), 4)

        self.assertIn(gallery.image_url, [photo.image_url for photo in photos])
        for i in range(1, 4):
            self.assertIn(f'https://test.com/gallery/image{i}.jpg', [photo.image_url for photo in photos])

    def test_about_page_view_with_less_than_4_photos(self):

        gallery = Gallery.objects.create(
            image_url='https://test.com/gallery/image1.jpg'
        )

        response = self.client.get(reverse('about page'))

        self.assertEqual(response.status_code, 200)

        self.assertIn('photos', response.context)
        photos = response.context['photos']

        self.assertEqual(photos.count(), 1)
        self.assertIn(gallery.image_url, [photo.image_url for photo in photos])


class EventPageViewTest(TestCase):
    def test_event_page_view(self):
        event1 = Event.objects.create(
            event_name='Car Show 1',
            description='A classic car show featuring vintage cars.',
            event_date='2023-07-15',
            event_location='Central Park, New York',
            image_url='https://test.com/carshow1-image.jpg'
        )
        event2 = Event.objects.create(
            event_name='Car Show 2',
            description='An event showcasing restored classic cars.',
            event_date='2023-08-20',
            event_location='Downtown Los Angeles',
            image_url='https://test.com/carshow2-image.jpg'
        )

        response = self.client.get(reverse('event page'))

        self.assertEqual(response.status_code, 200)

        self.assertIn('events', response.context)
        events = response.context['events']
        self.assertEqual(events.count(), 2)
        self.assertIn(event1, events)
        self.assertIn(event2, events)