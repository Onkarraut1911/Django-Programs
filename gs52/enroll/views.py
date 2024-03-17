from django.shortcuts import render
from .forms import StudentRegistration
from .models import User

# from .models import User - this is not need to write here for modelform

# Create your views here.


def studentregistration(request):
    if request.method == "POST":
        # Steps of the update the data from the table using instance
        pi = User.boject.get(pk=1)  # get the data from the table of primary key(id) = 1
        fm = StudentRegistration(
            request.POST, instance=pi
        )  # send the data into the instance
        if fm.is_valid():
            # This is not need to cleaned_data
            fm.save()  # update the data of id = 1 in the table

    else:
        fm = StudentRegistration()

    return render(request, "enroll/userregistration.html", {"form": fm})
