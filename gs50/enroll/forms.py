from django import forms
from .models import User


class StudentRegistration(forms.ModelForm):
    name = forms.CharField(
        max_length=50, required=False
    )  # if you dont write max_length then its use model class you write max_lentgh that
    # This is more priority than modelclass validators

    class Meta:
        model = User
        fields = (
            "name",
            "email",
            "password",
        )  # which model fields you want they write here  , you can change its order according to you

        # model and fields this is attributes

        labels = {
            "name": "Enter Name",
            "email": "Enter Email",
            "password": "Enter Password",
        }  # This labels change the label of key because its get a dictionary

        widgets = {
            "password": forms.PasswordInput,
            "name": forms.TextInput(
                attrs={"class": "myclass", "placeholder": "here Write your name"}
            ),  # change the class name for changes style using this class name in html and placeholder write something in the input filed of the tag
        }


# This error_messages gets dictionary and used to change the error messages occure in the html
