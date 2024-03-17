from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    fields = [
        "username",
        "first_name",
        "last_name",
        "email",
    ]
    labels = {"email": "Email"}


class EditUserProfileForm(UserCreationForm):
    password = None

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "date_joined",
            "last_login",
            "is_active",
        ]


class EditAdminProfileForm(UserCreationForm):
    password = None

    class Meta:
        model = User
        fields = "__all__"
