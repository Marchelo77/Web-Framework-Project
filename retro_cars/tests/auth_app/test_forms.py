from django.contrib.auth import get_user_model
from django.forms import TextInput, PasswordInput
from django.test import TestCase, Client
from django.core.exceptions import ValidationError

from retro_cars.auth_app.forms import LoginUserForm, RegisterUserForm, AppUserEditForm, GroupAdminForm

UserModel = get_user_model()


class LoginUserFormTest(TestCase):
    def test_login_form_valid(self):
        user = UserModel.objects.create_user(username='testuser', password='testpassword')
        form_data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        form = LoginUserForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_login_form_invalidUsernameOrPassword(self):
        form_data = {
            'username': 'test',
            'password': 'test123',
        }

        form = LoginUserForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_login_form_invalid(self):
        form_data = {
            'username': '',
            'password': '',
        }

        form = LoginUserForm(data=form_data)

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)

    def test_login_form_widgets(self):
        form = LoginUserForm()
        self.assertIsInstance(form.fields['username'].widget, TextInput)
        self.assertIsInstance(form.fields['password'].widget, PasswordInput)

    def test_login_form_attrs(self):
        form = LoginUserForm()
        self.assertEqual(form.fields['username'].widget.attrs['placeholder'], 'Type your username')
        self.assertEqual(form.fields['password'].widget.attrs['placeholder'], 'Type your password')
        self.assertEqual(form.fields['password'].strip, False)


class RegisterUserFormTest(TestCase):
    def test_register_form_valid(self):
        form = RegisterUserForm(
            data={
                'username': 'testuser',
                'email': 'test@test.com',
                'password1': 'testpass123',
                'password2': 'testpass123'
            }
        )
        self.assertTrue(form.is_valid())

    def test_register_form_invalid(self):
        form = RegisterUserForm(
            data={
                'username': 'testuser',
                'email': '',
                'password1': '',
                'password2': ''
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)

    def test_form_widgets_and_attrs(self):
        form = RegisterUserForm()

        self.assertEqual(form.fields['username'].widget.attrs['placeholder'], 'Enter an username')
        self.assertEqual(form.fields['email'].widget.attrs['placeholder'], 'Enter an email')
        self.assertEqual(form.fields['password1'].widget.attrs['placeholder'], 'Enter a password')
        self.assertEqual(form.fields['password2'].widget.attrs['placeholder'], 'Confirm your password')

        self.assertEqual(form.Meta.model, UserModel)
        self.assertListEqual(list(form.Meta.fields), ['username', 'email', 'password1', 'password2'])


class AppUserEditFormTest(TestCase):
    def test_app_user_edit_form_valid(self):
        user = UserModel.objects.create(username='testuser', email='test@test.com')
        form = AppUserEditForm(instance=user, data={
            'username': 'newuser',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'newuser@test.com',
            'gender': 1,
            'profile_picture': 'https://example.com/profile.jpg',
        })
        self.assertTrue(form.is_valid())

    def test_app_user_edit_form_whenUsernameExists_expectRaises(self):
        user1 = UserModel.objects.create(username='Tom', email='tom@test.com')
        user2 = UserModel.objects.create(username='testuser', email='test@test.com')
        form = AppUserEditForm(instance=user2, data={
            'username': 'Tom',
            'first_name': '',
            'last_name': '',
            'email': 'newuser@test.com',
            'gender': '',
            'profile_picture': '',
        })
        self.assertFalse(form.is_valid())

    def test_app_user_edit_form_whenEmailExists_expectRaises(self):
        user1 = UserModel.objects.create(username='Tom', email='test@test.com')
        user2 = UserModel.objects.create(username='testuser', email='testuser@test.com')
        form = AppUserEditForm(instance=user2, data={
            'username': 'testuser',
            'first_name': '',
            'last_name': '',
            'email': 'test@test.com',
            'gender': '',
            'profile_picture': '',
        })
        self.assertFalse(form.is_valid())

    def test_app_user_edit_form_invalid(self):
        user = UserModel.objects.create(username='testuser', email='test@test.com')
        form = AppUserEditForm(instance=user, data={
            'username': 'testuser',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'invalidemail',
            'gender': 1,
            'profile_picture': 'not-a-picture',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)
        self.assertEqual(form.errors['email'], ['Enter a valid email address.'])
        self.assertEqual(form.errors['profile_picture'], ['Please enter a valid URL for the profile picture.'])

    def test_app_user_edit_form_labels(self):
        form = AppUserEditForm()
        self.assertEqual(form.fields['username'].label, 'Username')
        self.assertEqual(form.fields['first_name'].label, 'First Name')
        self.assertEqual(form.fields['last_name'].label, 'Last Name')
        self.assertEqual(form.fields['email'].label, 'Email')
        self.assertEqual(form.fields['gender'].label, 'Gender')
        self.assertEqual(form.fields['profile_picture'].label, 'Profile Picture')

    def test_app_user_edit_form_exclude(self):
        form = AppUserEditForm()
        self.assertNotIn('password', form.fields)
