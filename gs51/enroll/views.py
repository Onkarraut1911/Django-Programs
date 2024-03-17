from django.shortcuts import render
from .forms import StudentRegistration
from .models import User

# from .models import User - this is not need to write here for modelform

# Create your views here.


def studentregistration(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data["name"]
            em = fm.cleaned_data["email"]
            pw = fm.cleaned_data["password"]
            # reg = User(name=nm, email=em, password=pw)
            # reg.save()
            # This is used for insert the data into the table

            # reg = User( id=1 ,name=nm, email=em, password=pw)
            # reg.save()
            # This is used for update the exesting data that is id = 1 into the table

            reg = User(id=2)
            reg.delete()
            # This is used for delete the exesting data that is id = 2 from the table
    else:
        fm = StudentRegistration()

    return render(request, "enroll/userregistration.html", {"form": fm})
