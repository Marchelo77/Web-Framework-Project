from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from retro_cars.review.models import Review

UserModel = get_user_model()


class ReviewViewTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            username='testuser',
            password='testpassword',
        )
        self.client.login(
            username='testuser',
            password='testpassword',
        )
        self.review_url = reverse('review page')

        self.review = Review.objects.create(
            comment='Hello there!',
            user=self.user,
        )

    def test_review_view_get(self):
        response = self.client.get(self.review_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/reviews.html')

    def test_review_view_post(self):
        form_data = {
            'comment': 'This is a test review.'
        }
        response = self.client.post(self.review_url, data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('review page'))

        self.assertTrue(Review.objects.filter(
            user=self.user,
            comment='This is a test review.',
        ).exists())


class DeleteReviewViewTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            username='testuser',
            password='testpassword',
        )
        self.client.login(
            username='testuser',
            password='testpassword',
        )
        self.review = Review.objects.create(
            user=self.user,
            comment='Test review.',
        )

    def test_delete_review_view(self):
        delete_url = reverse('review delete', kwargs={'pk': self.review.pk})
        response = self.client.post(delete_url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('review page'))

        self.assertFalse(Review.objects.filter(pk=self.review.pk).exists())
