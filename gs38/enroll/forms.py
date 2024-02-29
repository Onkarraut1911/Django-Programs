from django import forms

class student_login(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    phone_no = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)