from django.shortcuts import render
from .forms import StudentRegistration
from .models import User

# Create your views here.


def studentregistration(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data["name"]
            em = fm.cleaned_data["email"]
            pw = fm.cleaned_data["password"]
            reg = User(
                # id=1   # if you set the id then it update the data of that id , if id is not present in the table then it insert data
                name=nm,
                email=em,
                password=pw,
            )  # This is a object of model class name User , store cleaned data in model fields
            # you want to store this data into database table then you need to create object of modelclass , here User is model class
            reg.save()  # this is word with insert data also they work with update the data , i.e it save update data or insert data

            # reg = User(id=1)  # set id = 1 for delete data from the table of id=1
            # reg.delete() # delete is the delete the data of reg they set id 1

    else:
        fm = StudentRegistration()

    return render(request, "enroll/userregistration.html", {"form": fm})
