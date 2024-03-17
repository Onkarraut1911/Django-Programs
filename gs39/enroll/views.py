from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration

# Create your views here.


def ShowFormData(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if (
            fm.is_valid()
        ):  # in the form charfield have validation but its need to run and this work obtained by this method 'is_valid()' it gives error in your template ex. This Field is Requierd
            print("Form Validated")
            print("Roll:", fm.cleaned_data["Roll"])
            print(
                "Name:", fm.cleaned_data["name"]
            )  # name of the forms field is here key
            print("Price:", fm.cleaned_data["price"])
            print("Rate:", fm.cleaned_data["rate"])
            print("email:", fm.cleaned_data["email"])
            print("comment:", fm.cleaned_data["comment"])
            print("website:", fm.cleaned_data["website"])
            print("password:", fm.cleaned_data["password"])
            print("discription:", fm.cleaned_data["discription"])
            print("feedback:", fm.cleaned_data["feedback"])
            print("notes:", fm.cleaned_data["notes"])
            print("Agree:", fm.cleaned_data["agree"])
    else:
        fm = StudentRegistration()

    return render(request, "enroll/UserRegistration.html", {"form": fm})


# is_valid() checks if the submitted form data is valid, while cleaned_data contains the cleaned and validated form data after is_valid() has been called and passed. So, is_valid() is used for validation checking, while cleaned_data is used to access the cleaned and validated form data for further processing.
# is_valid() check validation nad cleaned_data is contained validation data i.e cleaned data and for accessing this data using cleaned_data
