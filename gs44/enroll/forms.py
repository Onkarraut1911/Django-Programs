from django import forms
from django.core import validators


class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    rpassword = forms.CharField(widget=forms.PasswordInput(), label="Password(again)")

    def clean(self):
        cleaned_data = super().clean()
        valpwd = self.cleaned_data.get(
            "password"
        )  #    valpwd = self.cleaned_data['password']  , this is a same method
        valrpwd = self.cleaned_data.get("rpassword")

        if valpwd != valrpwd:
            raise forms.ValidationError("Password does not match")
