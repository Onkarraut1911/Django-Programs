from django import forms
from .models import User


class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "name",
            "email",
            "password",
        )  # which model fields you want they write here  , you can change its order according to you

        # model and fields this is attributes
