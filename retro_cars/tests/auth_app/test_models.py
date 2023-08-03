from django.test import TestCase
from django.core.validators import ValidationError
from django.contrib.auth import get_user_model
from retro_cars.auth_app.models import Gender

UserModel = get_user_model()


class UserModelTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = UserModel.objects.create_user(
            username='testuser',
            email='testuser@test.com',
            password='testpassword',
            first_name='Test',
            last_name='User',
            gender=Gender.MALE.value,
        )

    def test_user_fields(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@test.com')
        self.assertEqual(self.user.first_name, 'Test')
        self.assertEqual(self.user.last_name, 'User')
        self.assertEqual(self.user.gender, Gender.MALE.value)

    def test_user_profile_picture_default(self):
        self.assertEqual(self.user.profile_picture, None)

    def test_first_name_whenInvalid_expectRaises(self):

        user = UserModel(
            username='testuser3',
            email='testuser3@example.com',
            password='testpassword',
            first_name='Ivan7',
        )
        try:
            user.full_clean()
            user.save()
            self.fail()
        except ValidationError as ex:
            self.assertIsNotNone(ex)

    def test_last_name_whenInvalid_expectRaises(self):

        user = UserModel(
            username='testuser3',
            email='testuser3@example.com',
            password='testpassword',
            last_name='Ivan7',
        )
        try:
            user.full_clean()
            user.save()
            self.fail()
        except ValidationError as ex:
            self.assertIsNotNone(ex)

    def test_first_and_last_name_whenValid(self):

        user = UserModel(
            username='testuser3',
            email='testuser3@example.com',
            password='testpassword',
            first_name='Danail',
            last_name='Ivanov',
        )

        user.full_clean()
        user.save()

        self.assertIsNotNone(user)
