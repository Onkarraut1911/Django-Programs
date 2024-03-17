from django.shortcuts import render
from .forms import student_registration
from django.contrib import messages

# Create your views here.


def studentRegistration(request):

    messages.success(request, "Your form submited successfuly")
    messages.info(request, "This is info ")
    messages.warning(request, "This is warning")
    messages.error(request, "This is error")

    fm = student_registration()
    return render(request, "enroll/studentregistration.html", {"form": fm})
