from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.


def student_registration(request):
    fm = StudentRegistration()  # fm is object of the class StudentRegistration
    return render(request, "enroll/userregistration.html", {"form": fm})
