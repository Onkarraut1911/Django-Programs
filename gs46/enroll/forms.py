from django import forms


class StudentRegistration(forms.Form):
    error_css_class = "error"  # This is used to  change the class name of errormessages
    required_css_class = "required"  # This is used to change the class name of errormessage required field
    name = forms.CharField(error_messages={"required": "Enter Your Name"})
    email = forms.EmailField(error_messages={"required": "Enter Your Email"})
    password = forms.CharField(
        widget=forms.PasswordInput, error_messages={"required": "Enter Your Password"}
    )
