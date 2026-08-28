from django import forms
from django.core import validators


class RegisterForm(forms.Form):

    full_name = forms.CharField(
        label='نام و نام خانوادگی',
        validators=[
            validators.MaxLengthValidator(200)
        ])
    
    phone_number = forms.CharField(
        label='شماره تلفن',
        validators=[
            validators.MaxLengthValidator(11),
            validators.MinLengthValidator(11)
        ],
        error_messages={
            'max_length':'شماره تلفن باید ۱۱ رقمی باشد.',
            'min_length':'شماره تلفن باید ۱۱ رقمی باشد.'
        }
    )

class LoginForm(forms.Form):

    phone_number = forms.CharField(
        label='شماره تلفن',
        validators=[
            validators.MaxLengthValidator(11),
            validators.MinLengthValidator(11)
        ],
        error_messages={
            'max_length':'شماره تلفن باید ۱۱ رقمی باشد.',
            'min_length':'شماره تلفن باید ۱۱ رقمی باشد.'
        }
    )



class PhoneNumberVerificationForm(forms.Form):

    code_input_1 = forms.CharField(
        max_length=1,
        min_length=1
    )

    code_input_2 = forms.CharField(
        max_length=1,
        min_length=1
    )

    code_input_3 = forms.CharField(
        max_length=1,
        min_length=1
    )

    code_input_4 = forms.CharField(
        max_length=1,
        min_length=1
    )

    code_input_5 = forms.CharField(
        max_length=1,
        min_length=1
    )