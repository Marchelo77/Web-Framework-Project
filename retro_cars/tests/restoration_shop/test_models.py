from django.core.exceptions import ValidationError
from django.test import TestCase
from retro_cars.restoration_shops.models import RestorationShop, Locations


class RestorationShopModelTest(TestCase):
    def test_restoration_shop_model(self):
        shop = RestorationShop.objects.create(
            offer_image_url='https://test.com/offer-image.jpg',
            offer='Car Restoration Services',
            description='We provide top-quality car restoration services.'
        )

        self.assertEqual(shop.offer_image_url, 'https://test.com/offer-image.jpg')
        self.assertEqual(shop.offer, 'Car Restoration Services')
        self.assertEqual(shop.description, 'We provide top-quality car restoration services.')


class LocationsModelTest(TestCase):
    def test_locations_model(self):
        location = Locations.objects.create(
            city='New York',
            address='123 Main Street',
            phone_number='0899122387',
            email='contact@example.com',
            image_url='https://test.com/location-image.jpg'
        )

        self.assertEqual(location.city, 'New York')
        self.assertEqual(location.address, '123 Main Street')
        self.assertEqual(location.phone_number, '0899122387')
        self.assertEqual(location.email, 'contact@example.com')
        self.assertEqual(location.image_url, 'https://test.com/location-image.jpg')

    def test_phone_number_invalid(self):
        location = Locations.objects.create(
            city='New York',
            address='123 Main Street',
            phone_number='1889142386',
            email='contact@example.com',
            image_url='https://test.com/location-image.jpg'
        )
        with self.assertRaises(ValidationError):
            location.full_clean()
