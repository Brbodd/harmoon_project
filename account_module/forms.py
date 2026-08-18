from django import forms
from django.core import validators


class RegisterForm(forms.Form):
    full_name = forms.CharField(
        label='نام و نام خانوادگی',
        validators=[validators.MaxLengthValidator(200)])
    phone_number = forms.CharField(
        label='شماره تلفن',
        validators=[validators.MaxLengthValidator(11)])