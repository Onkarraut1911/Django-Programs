from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class signupform(
    UserCreationForm
):  # This defines a custom form that inherits from the UserCreationForm
    password2 = forms.CharField(
        label="Confirm Password(Again)",
        widget=forms.PasswordInput,  # override the field of the usercreationform , we write here for changing this field
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
        labels = {"email": "Email"}


# When you set the model attribute inside the class Meta, you are essentially saying "this form is based on this model." Django uses this information to automatically generate form fields corresponding to the fields of the specified model.
#  In object-oriented programming, methods (functions) and variables (data) associated with a class or an instance of a class are both considered attributes.
