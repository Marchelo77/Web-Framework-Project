from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.contrib.auth.models import Group

UserModel = get_user_model()


class LoginUserForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Type your username'
            }
        )
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Type your password'
        })
    )


class RegisterUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Enter an username'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter an email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter a password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm your password'

    def save(self, commit=True):
        result = super().save(commit)
        return result


class AppUserEditForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('username', 'first_name', 'last_name', 'email', 'gender', 'profile_picture',)
        exclude = ('password',)
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'gender': 'Gender',
            'profile_picture': 'Profile Picture',
        }
        error_messages = {
            'profile_picture': {
                'invalid': 'Please enter a valid URL for the profile picture.',
            },
        }


class GroupAdminForm(forms.ModelForm):
    class Meta:
        model = Group
        exclude = []

    users = forms.ModelMultipleChoiceField(
         queryset=UserModel.objects.all(),
         required=False,

         widget=FilteredSelectMultiple('users', False)
    )

    def __init__(self, *args, **kwargs):
        super(GroupAdminForm, self).__init__(*args, **kwargs)

        if self.instance.pk:
            self.fields['users'].initial = self.instance.user_set.all()

    def save_m2m(self):
        self.instance.user_set.set(self.cleaned_data['users'])

    def save(self, *args, **kwargs):
        instance = super(GroupAdminForm, self).save()
        self.save_m2m()
        return instance

