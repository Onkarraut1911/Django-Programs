from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.


def STUDENT_LOGIN_1(request):
    FM = StudentRegistration()
    return render(request, "enroll/userregistration.html", {"form": FM})
