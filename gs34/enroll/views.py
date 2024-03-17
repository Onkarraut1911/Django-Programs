from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.


def student_registration(request):
    fm = StudentRegistration(
        initial={
            "name": "Rahul"
        }  # you can pass the initial here , name is the field of form  , it is replaced default value
    )  # fm is object of the class StudentRegistration
    return render(request, "enroll/userregistration.html", {"form": fm})
