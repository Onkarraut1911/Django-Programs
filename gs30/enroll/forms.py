from django import forms
class student_login(forms.Form):

    # Define your form fields here

    name = forms.CharField()
    email = forms.EmailField()
    first_name = forms.CharField()