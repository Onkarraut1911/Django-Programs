from django import forms
from django.core import validators


def starts_wth_s(value):  # you can write this function name as you wish
    if value[0] != "s":
        raise forms.ValidationError("Name should start with s")


class StudentRegistration(forms.Form):
    first_name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
    last_name = forms.CharField(validators=[starts_wth_s])
    email = forms.EmailField()
