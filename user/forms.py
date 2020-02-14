from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField
from .models import Account


class SingupForm(UserCreationForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = 'username', 'email', 'password1', 'password2'


class AccountForm(forms.ModelForm):
    address = forms.CharField(max_length=250)
    phone = PhoneNumberField()

    class Meta:
        model = Account
        fields = 'address', 'phone'


class SinginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
