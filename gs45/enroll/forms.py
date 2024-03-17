from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField(
        error_messages={"required": "Enter your name"}
    )  # this field is required default if you want to change error message then write this argument error_message , it gets dictionary
    email = forms.EmailField(error_messages={"required": "Enter your email"})
    password = forms.CharField(
        widget=forms.PasswordInput(), error_messages={"required": "Enter your password"}
    )
