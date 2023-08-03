from django.contrib.auth import get_user_model
from django.test import TestCase

from retro_cars.review.forms import ReviewForm

UserModel = get_user_model()


class ReviewFormTest(TestCase):
    def test_review_form_widget_attrs(self):
        form = ReviewForm()
        self.assertIn('placeholder="Add comment..."', str(form['comment']))
