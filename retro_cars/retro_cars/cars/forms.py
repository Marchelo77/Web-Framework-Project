from django import forms

from retro_cars.cars.models import RetroCar


class BaseCarForm(forms.ModelForm):
    class Meta:
        model = RetroCar
        fields = ('car_image', 'model', 'description', 'year')
        widgets = {
            'model': forms.TextInput(attrs={'placeholder': 'Enter car model'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter car description'}),
            'car_image': forms.URLInput(attrs={'placeholder': 'Enter car image URL'}),
            'year': forms.NumberInput(attrs={'placeholder': 'Enter manufacturing year'}),
        }

        labels = {
            'model': 'Car Model',
            'description': 'Description',
            'year': 'Year',
        }


class CarCreateForm(BaseCarForm):
    pass


class CarEditForm(BaseCarForm):
    pass
