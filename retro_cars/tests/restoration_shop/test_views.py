from django.test import TestCase
from django.urls import reverse
from retro_cars.restoration_shops.models import RestorationShop, Locations


class RestorationShopViewTest(TestCase):
    def test_restoration_shop_view(self):
        shop1 = RestorationShop.objects.create(
            offer_image_url='https://test.com/offer1-image.jpg',
            offer='Car Restoration Services 1',
            description='We provide top-quality car restoration services 1.'
        )
        shop2 = RestorationShop.objects.create(
            offer_image_url='https://test.com/offer2-image.jpg',
            offer='Car Restoration Services 2',
            description='We provide top-quality car restoration services 2.'
        )

        response = self.client.get(reverse('restoration shop'))

        self.assertEqual(response.status_code, 200)

        self.assertIn('services', response.context)
        services = response.context['services']
        self.assertEqual(services.count(), 2)
        self.assertIn(shop1, services)
        self.assertIn(shop2, services)


class LocationsPageViewTest(TestCase):
    def test_locations_page_view(self):
        location1 = Locations.objects.create(
            city='New York',
            address='123 Main Street',
            phone_number='0899142485',
            email='contact@example.com',
            image_url='https://test.com/location1-image.jpg'
        )
        location2 = Locations.objects.create(
            city='Los Angeles',
            address='456 Elm Street',
            phone_number='0899142485',
            email='info@example.com',
            image_url='https://test.com/location2-image.jpg'
        )

        response = self.client.get(reverse('locations page'))

        self.assertEqual(response.status_code, 200)

        self.assertIn('locations', response.context)
        locations = response.context['locations']
        self.assertEqual(locations.count(), 2)
        self.assertIn(location1, locations)
        self.assertIn(location2, locations)
