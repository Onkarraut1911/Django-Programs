from django import forms
from .models import User

class Student_Registration(forms.ModelForm):
  class Meta:
    model = User
    fields = ['student_name','email','password']

# class Teacher_Registration(Student_Registration):
#   class Meta(Student_Registration.Meta):
#     fields = ['teacher_name','email','password']

class Teacher_Registration(Student_Registration):
  class Meta(Student_Registration.Meta):
    fields = ['teacher_name', 'email', 'password']
