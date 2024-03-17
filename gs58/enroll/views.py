from django.shortcuts import render
from .forms import student_registration
from django.contrib import messages

# Create your views here.


def studentRegistration(request):
    if request.method == "POST":
        fm = student_registration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(
                request, messages.SUCCESS, "your account has been created !!!"
            )
            messages.info(request, "Now you can login !!!")
            # print(
            #     messages.get_level(request)
            # )  # get_level method is get the level of messages ,here ex. info level is 20 so this print 20
            # messages.debug(request, "This is debug")
            # messages.set_level(request, messages.DEBUG)
            # messages.debug(request, "This is New debug")
            # print(messages.get_level(request))

        fm = student_registration()
    else:
        fm = student_registration()
    return render(request, "enroll/studentregistration.html", {"form": fm})
