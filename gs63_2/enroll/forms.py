from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class SignupForm(forms.Form):


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        # fields = "__all__"
        fields = [
            "username",
            "email",
        ]


# password1 and password2 are not included in the fields list, but they will still be rendered in the form because they are automatically added by UserCreationForm


# if we need to change the error messages in authenticationform

# class CustomAuthenticationForm(AuthenticationForm):
#     error_messages = {
#         'invalid_login': "Custom error message here.",
#         'inactive': "Custom inactive account message here.",
#     }
