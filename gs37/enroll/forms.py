from django import forms

class STUDENT_REGISTRATION(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_no = forms.IntegerField()
    email = forms.EmailField()