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
            print("First Name:", fm.cleaned_data["first_name"])
            print("Last Name:", fm.cleaned_data["last_name"])
            print("email:", fm.cleaned_data["email"])

    else:
        fm = StudentRegistration()

    return render(request, "enroll/userregistration.html", {"form": fm})
