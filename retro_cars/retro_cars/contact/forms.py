from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Full Name', 'class': 'contactus'})
    )
    phone_number = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'Phone', 'class': 'contactus'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'contactus'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Message', 'class': 'contactus'})
    )
