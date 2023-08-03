from django.contrib.auth import get_user_model
from django.test import TestCase
from retro_cars.cars.models import RetroCar
from django.core.exceptions import ValidationError

UserModel = get_user_model()


class RetroCarModelTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            username='testuser',
            email='test@test.com',
            password='testpassword'
        )
        self.car = RetroCar.objects.create(
            model='Car Model',
            car_image='https://test.com/car-image.jpg',
            user=self.user,
        )

    def test_valid_car_model(self):
        valid_models = ['Model123', 'Dodge Camaro', 'BMW']
        for model in valid_models:
            with self.subTest(model=model):
                self.car = RetroCar(
                    model=model,
                    car_image='https://test.com/car-image.jpg',
                    user=self.car.user,
                )
                self.car.full_clean()

    def test_invalid_car_model(self):
        valid_models = ['Car$Model', 'Dodge#Camaro', 'B' * 31]
        for model in valid_models:
            with self.subTest(model=model):
                self.car = RetroCar(
                    model=model,
                    car_image='https://test.com/car-image.jpg',
                    user=self.car.user,
                )
                with self.assertRaises(ValidationError):
                    self.car.full_clean()

    def test_valid_car_year(self):
        valid_year = [1950, 1963, 2000]
        for year in valid_year:
            with self.subTest(year=year):
                car = RetroCar(
                    model='Car Model',
                    car_image='https://test.com/car-image.jpg',
                    year=year,
                    user=self.car.user,
                )
                car.full_clean()

    def test_invalid_car_year(self):
        invalid_years = [1949, 2007, 500]
        for year in invalid_years:
            with self.subTest(year=year):
                car = RetroCar(
                    model='Car Model',
                    car_image='https://test.com/car-image.jpg',
                    year=year,
                    user=self.car.user,
                )
                with self.assertRaises(ValidationError):
                    car.full_clean()

    def test_valid_car_description(self):
        valid_descriptions = ['This is a valid description.', '', 'Hello I am valid']
        for description in valid_descriptions:
            with self.subTest(description=description):
                car = RetroCar(
                    model='Car Model',
                    car_image='https://test.com/car-image.jpg',
                    description=description,
                    user=self.car.user,
                )
                car.full_clean()

    def test_invalid_car_description(self):
        invalid_descriptions = ['Not valid', 1]
        for description in invalid_descriptions:
            with self.subTest(description=description):
                car = RetroCar(
                    model='Car Model',
                    car_image='https://test.com/car-image.jpg',
                    description=description,
                    user=self.car.user,
                )
                with self.assertRaises(ValidationError):
                    car.full_clean()

    def test_valid_car_image(self):
        valid_car_images = ['https://test.com/car-image.jpg', 'https://test.com/dodge-camaro.png']
        for image in valid_car_images:
            with self.subTest(car_image=image):
                car = RetroCar(
                    model='Car Model',
                    car_image=image,
                    user=self.car.user,
                )
                car.full_clean()

    def test_invalid_car_image(self):
        invalid_car_images = ['test.com/image.jpg', 'images/image-car.png']
        for image in invalid_car_images:
            with self.subTest(car_image=image):
                car = RetroCar(
                    model='Car Model',
                    car_image=image,
                    user=self.car.user,
                )
                with self.assertRaises(ValidationError):
                    car.full_clean()

    def test_create_retro_car_with_user(self):

        self.assertIsNotNone(self.car.user)
        self.assertEqual(self.car.user, self.user)
