from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.


def ShowFormData(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print("Form Validated")
            print("Name:", fm.cleaned_data["name"])
            print("Email:", fm.cleaned_data["email"])
            print("Password:", fm.cleaned_data["password"])

    else:
        fm = StudentRegistration()

    return render(request, "enroll/UserRegistration.html", {"form": fm})
