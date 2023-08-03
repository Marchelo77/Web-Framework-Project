from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from retro_cars.cars.models import RetroCar

UserModel = get_user_model()


class CarViewsTestCase(TestCase):
    def setUp(self):
        self.test_client = Client()
        self.user = UserModel.objects.create_user(
            username='testuser',
            email='test@user.com',
            password='testpassword',
        )
        self.car = RetroCar.objects.create(
            model='Test Car Model',
            description='Test Car Description',
            year=2000,
            car_image='https://example.com/test-car-image.jpg',
            user=self.user,
        )

    def test_car_page_view(self):
        response = self.test_client.get(reverse('car page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cars/cars.html')

    def test_detail_car_view(self):
        self.test_client.login(username='testuser', password='testpassword')
        response = self.test_client.get(reverse('car details', kwargs={'pk': self.car.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cars/car-details.html')

    def test_car_create_view_authenticated_user(self):
        self.test_client.login(username='testuser', password='testpassword')
        response = self.test_client.get(reverse('car create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cars/car-create.html')

    def test_car_create_view_anonymous_user(self):
        response = self.test_client.get(reverse('car create'))
        self.assertRedirects(response, reverse('profile login') + '?next=' + reverse('car create'))

    def test_car_create_form_valid(self):
        self.test_client.login(username='testuser', password='testpassword')
        form_data = {
            'model': 'New Car Model',
            'description': 'New Car Description',
            'year': 1960,
            'car_image': 'https://test.com/new-car-image.jpg',
        }
        response = self.test_client.post(reverse('car create'), data=form_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cars/cars.html')

    def test_car_create_form_invalid(self):
        self.test_client.login(username='testuser', password='testpassword')
        form_data = {
            'model': '',
            'description': 'Short',
            'year': 2022,
            'car_image': 'invalid-url',
        }
        response = self.test_client.post(reverse('car create'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cars/car-create.html')

    def test_edit_car_view_authenticated_user(self):
        self.test_client.login(username='testuser', password='testpassword')
        response = self.test_client.get(reverse('car edit', kwargs={'pk': self.car.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cars/car-edit.html')

    def test_edit_car_view_anonymous_user(self):
        response = self.test_client.get(reverse('car edit', kwargs={'pk': self.car.pk}))
        self.assertRedirects(response, reverse('profile login') + '?next=' + reverse('car edit', kwargs={'pk': self.car.pk}))

    def test_edit_car_form_valid(self):
        self.test_client.login(username='testuser', password='testpassword')
        form_data = {
            'model': 'Updated Car Model',
            'description': 'Updated Car Description',
            'year': 2000,
            'car_image': 'https://test.com/updated-car-image.jpg',
        }
        response = self.test_client.post(reverse('car edit', kwargs={'pk': self.car.pk}), data=form_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cars/car-details.html')

    def test_edit_car_form_invalid(self):
        self.test_client.login(username='testuser', password='testpassword')
        form_data = {
            'model': '',
            'description': 'Short',
            'year': 2100,
            'car_image': 'invalid-url',
        }
        response = self.test_client.post(reverse('car edit', kwargs={'pk': self.car.pk}), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cars/car-edit.html')

    def test_delete_car_view(self):
        self.test_client.login(username='testuser', password='testpassword')
        response = self.test_client.delete(reverse('car delete', kwargs={'pk': self.car.pk}))

        self.assertRedirects(response, reverse('car page'))
        car_exists = RetroCar.objects.filter(model='Test Car Model').exists()
        self.assertFalse(car_exists)
