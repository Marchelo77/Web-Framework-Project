from django.contrib.auth import get_user_model
from django.test import TestCase
from retro_cars.cars.forms import CarCreateForm, CarEditForm
from retro_cars.cars.models import RetroCar

UserModel = get_user_model()


class CarFormsTestCase(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='testpassword'
        )

    def test_car_create_form_valid(self):
        form_data = {
            'model': 'Test Car Model',
            'description': 'Test Car Description',
            'year': 2000,
            'car_image': 'https://test.com/test-car-image.jpg',
        }
        form = CarCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_car_create_form_invalid(self):
        form_data = {
            'model': '',
            'description': 'Short',
            'year': 2100,
            'car_image': 'invalid-url',
        }
        form = CarCreateForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)

    def test_car_create_form_widget_attrs(self):
        form = CarCreateForm()
        self.assertIn('placeholder="Enter car model"', str(form['model']))
        self.assertIn('placeholder="Enter car description"', str(form['description']))
        self.assertIn('placeholder="Enter manufacturing year"', str(form['year']))
        self.assertIn('placeholder="Enter car image URL"', str(form['car_image']))

    def test_car_edit_form_valid(self):
        car_instance = RetroCar.objects.create(
            model='Test Car Model',
            description='Test Car Description',
            year=2000,
            car_image='https://test.com/test-car-image.jpg',
            user=self.user,
        )

        form_data = {
            'model': 'Updated Car Model',
            'description': 'Updated Car Description',
            'year': 1999,
            'car_image': 'https://test.com/updated-car-image.jpg',
        }
        form = CarEditForm(instance=car_instance, data=form_data)
        self.assertTrue(form.is_valid())

    def test_car_edit_form_invalid(self):
        car_instance = RetroCar.objects.create(
            model='Test Car Model',
            description='Test Car Description',
            year=2000,
            car_image='https://test.com/test-car-image.jpg',
            user=self.user,
        )

        form_data = {
            'model': '',
            'description': 'Short',
            'year': 2100,
            'car_image': 'invalid-url',
        }
        form = CarEditForm(instance=car_instance, data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)

    def test_car_edit_form_widget_attrs(self):
        car_instance = RetroCar.objects.create(
            model='Test Car Model',
            description='Test Car Description',
            year=2000,
            car_image='https://test.com/test-car-image.jpg',
            user=self.user,
        )

        form = CarEditForm(instance=car_instance)
        self.assertIn('placeholder="Enter car model"', str(form['model']))
        self.assertIn('placeholder="Enter car description"', str(form['description']))
        self.assertIn('placeholder="Enter manufacturing year"', str(form['year']))
        self.assertIn('placeholder="Enter car image URL"', str(form['car_image']))