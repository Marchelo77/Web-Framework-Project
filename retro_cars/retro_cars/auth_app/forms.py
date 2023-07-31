from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField

UserModel = get_user_model()


class LoginUserForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'placeholder': 'Type your username'}))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Type your password'
        })
    )

    # class Meta(auth_forms.AuthenticationForm.Meta):


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
