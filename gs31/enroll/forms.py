from django import forms

class StudentLogin(forms.Form):
    name = forms.CharField(initial="Sonam")
    email = forms.EmailField(help_text="is field me only email likhana he")
    last_name = forms.CharField()