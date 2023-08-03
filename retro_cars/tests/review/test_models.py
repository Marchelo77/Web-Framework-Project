from django.contrib.auth import get_user_model
from django.test import TestCase

from retro_cars.review.models import Review

UserModel = get_user_model()


class ReviewModelTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(
            username='testuser',
            password='testpassword',
            email='test@user.com',
        )
        self.review = Review.objects.create(
            comment='I am a comment',
            user=self.user
        )

    def test_comment_when_valid(self):
        valid_comments = ['Hello I am Valid', 'Yes', 123]
        for comment in valid_comments:
            with self.subTest(comment=comment):
                self.review = Review(
                    comment=comment,
                    user=self.review.user
                )
                self.review.full_clean()
