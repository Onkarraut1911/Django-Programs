from django import forms
from .models import StudentRegistration


class student_registration(forms.ModelForm):
    class Meta:
        model = StudentRegistration
        fields = '__all__'