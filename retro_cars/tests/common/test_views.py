from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from retro_cars.review.models import Review
from retro_cars.restoration_shops.models import RestorationShop

UserModel = get_user_model()


class HomePageViewTest(TestCase):
    def setUp(self):

        self.user = UserModel.objects.create_user(username='testuser', password='testpassword')

    def test_home_page_view_with_less_than_2_comments_and_less_than_4_restoration_shops(self):

        Review.objects.create(user=self.user, comment='Hello there I am comment')
        RestorationShop.objects.create(offer='Service 1', description='Description 1', offer_image_url='https://test.com/1.jpg')
        RestorationShop.objects.create(offer='Service 2', description='Description 2', offer_image_url='https://test.com/2.jpg')
        RestorationShop.objects.create(offer='Service 3', description='Description 3', offer_image_url='https://test.com/3.jpg')

        response = self.client.get(reverse('home_page'))

        self.assertEqual(response.status_code, 200)

        self.assertIn('reviews', response.context)
        self.assertIn('services', response.context)

        reviews = response.context['reviews']
        self.assertEqual(reviews.count(), 1)
        self.assertIn('Hello there I am comment', [review.comment for review in reviews])

        services = response.context['services']
        self.assertEqual(services.count(), 3)
        self.assertIn('Service 1', [service.offer for service in services])

    def test_home_page_view_with_more_than_2_comments_and_more_than_4_restoration_shops(self):
        for i in range(1, 4):
            Review.objects.create(user=self.user, comment=f'Hello there I am comment {i}')
        for i in range(1, 6):
            RestorationShop.objects.create(offer=f'Service {i}', description=f'Description {i}', offer_image_url=f'https://test.com/{i}.jpg')

        response = self.client.get(reverse('home_page'))

        self.assertEqual(response.status_code, 200)

        self.assertIn('reviews', response.context)
        self.assertIn('services', response.context)

        reviews = response.context['reviews']
        self.assertEqual(reviews.count(), 2)
        self.assertIn('Hello there I am comment 2', [review.comment for review in reviews])
        self.assertIn('Hello there I am comment 3', [review.comment for review in reviews])

        services = response.context['services']
        self.assertEqual(services.count(), 4)
        self.assertIn('Service 1', [service.offer for service in services])
        self.assertIn('Service 2', [service.offer for service in services])
        self.assertIn('Service 3', [service.offer for service in services])
        self.assertIn('Service 4', [service.offer for service in services])