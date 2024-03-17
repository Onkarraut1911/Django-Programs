from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.


def student_registration(request):
    if request.method == "POST":
        fm = StudentRegistration(
            request.POST
        )  # fm is object of the class StudentRegistration
        if fm.is_valid():
            print("Form Validate")
            print("Name:", fm.cleaned_data["name"])
            print("email:", fm.cleaned_data["email"])
            print("password:", fm.cleaned_data["password"])

    else:
        fm = StudentRegistration()

    return render(request, "enroll/userregistration.html", {"form": fm})
