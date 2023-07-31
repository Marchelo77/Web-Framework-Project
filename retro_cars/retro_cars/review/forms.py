from django import forms

from retro_cars.review.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('comment',)
        widgets = {
            'comment': forms.TextInput(attrs={'placeholder': 'Add comment...'})
        }
