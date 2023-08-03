from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class ProfileViewsTest(TestCase):
    def setUp(self):
        self.test_client = Client()
        self.user = UserModel.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='marchelo123'
        )
        self.profile_url = reverse('profile page', kwargs={'pk': self.user.pk})
        self.login_url = reverse('profile login')
        self.logout_url = reverse('profile logout')
        self.edit_url = reverse('profile edit', kwargs={'pk': self.user.pk})

    def test_profile_details_view(self):
        self.test_client.login(username='testuser', password='marchelo123')
        response = self.test_client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/profile.html')

    def test_profile_delete_view(self):
        self.test_client.login(username='testuser', password='marchelo123')
        response = self.test_client.get(reverse('profile delete', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/profile-delete.html')

    def test_logout_user_view(self):
        response = self.test_client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)

    def test_login_user_view(self):
        response = self.test_client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/profile-login.html')

    def test_register_user_view(self):
        response = self.test_client.get(reverse('profile register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/profile-create.html')

    def test_profile_edit_view(self):
        self.test_client.login(username='testuser', password='marchelo123')
        response = self.test_client.get(self.edit_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/profile-edit.html')

    def test_authenticated_user_redirected_from_register_view(self):
        self.test_client.login(username='testuser', password='marchelo123')
        response = self.test_client.get(reverse('profile register'))
        self.assertRedirects(response, reverse('home_page'))

    def test_authenticated_user_redirected_from_login_view(self):
        self.test_client.login(username='testuser', password='marchelo123')
        response = self.test_client.get(reverse('profile login'))
        self.assertRedirects(response, reverse('home_page'))

    def test_edit_user_profile(self):
        data = {
            'username': 'newuser',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'newuser@example.com',
            'gender': 1,
        }
        self.test_client.login(username='testuser', password='marchelo123')
        response = self.test_client.post(self.edit_url, data=data)
        self.assertRedirects(response, reverse('profile page', kwargs={'pk': self.user.pk}))
        user = UserModel.objects.get(pk=self.user.pk)
        self.assertEqual(user.username, 'newuser')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')
        self.assertEqual(user.email, 'newuser@example.com')
        self.assertEqual(user.gender, 1)

    def test_invalid_edit_user_profile(self):
        data = {
            'username': '',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'invalidemail',
            'gender': 1,
        }
        self.test_client.login(username='testuser', password='marchelo123')
        response = self.test_client.post(self.edit_url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'username', 'This field is required.')
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')

    def test_invalid_login_user(self):
        data = {
            'username': 'testuser',
            'password': 'wrongpassword',
        }
        response = self.test_client.post(reverse('profile login'), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response, 'form', None, 'Please enter a correct username and password. '
                                    'Note that both fields may be case-sensitive.'
        )

    def test_login_user(self):
        data = {
            'username': 'testuser',
            'password': 'marchelo123',
        }
        response = self.test_client.post(reverse('profile login'), data=data)
        self.assertRedirects(response, reverse('home_page'))
        user = response.wsgi_request.user
        self.assertTrue(user.is_authenticated)

    def test_logout_user(self):
        self.test_client.login(username='testuser', password='marchelo123')
        response = self.test_client.get(self.logout_url)
        self.assertRedirects(response, reverse('home_page'))
        user = response.wsgi_request.user
        self.assertFalse(user.is_authenticated)

    def test_register_user(self):
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
        }
        response = self.test_client.post(reverse('profile register'), data=data)
        self.assertRedirects(response, reverse('home_page'))
        user = UserModel.objects.get(username='newuser')
        self.assertTrue(user.is_authenticated)

    def test_register_user_invalid(self):
        data = {
            'username': '',
            'email': 'invalidemail',
            'password1': 'newpassword123',
            'password2': 'wrongpassword',
        }
        response = self.test_client.post(reverse('profile register'), data=data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'username', 'This field is required.')
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')
        self.assertFormError(response, 'form', 'password2', 'The two password fields didn’t match.')

    def test_profile_delete_user(self):
        self.test_client.login(username='testuser', password='marchelo123')
        response = self.test_client.post(reverse('profile delete', kwargs={'pk': self.user.pk}))
        self.assertRedirects(response, reverse('home_page'))
        user_exists = UserModel.objects.filter(username='testuser').exists()
        self.assertFalse(user_exists)
