from .forms import EditAdminProfileForm, EditUserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignupForm

# Create your views here.


def user_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.user.is_superuser:
                fm = EditAdminProfileForm(request.POST, instance=request.user)
                users = User.objects.all()  # Fetch all users
            else:
                fm = EditUserProfileForm(
                    request.POST, instance=request.user
                )  # request.user is an object
                users = None
            if fm.is_valid():
                messages.success(request, "Your Profile Updated ")
                fm.save()
        else:
            if request.user.is_superuser:
                fm = EditAdminProfileForm(instance=request.user)
                users = User.objects.all()
            else:
                fm = EditUserProfileForm(instance=request.user)
                users = None
        return render(
            request,
            "enroll/profile.html",
            {
                "form": fm,
                "name": request.user.username,
                "users": users,
            },  # Use "users" instead of "useres"
        )
    else:
        return HttpResponseRedirect("/login/")


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data["username"]
                upass = fm.cleaned_data["password"]
                user_object = authenticate(username=uname, password=upass)
                if user_object is not None:
                    login(request, user_object)
                    messages.success(request, "User Successfuly Login")
                    return HttpResponseRedirect("/profile/")

        else:
            fm = AuthenticationForm()
        return render(request, "enroll/login.html", {"form": fm})
    else:
        return HttpResponseRedirect("/login/")


def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/login/")


def signup_form(request):
    if request.method == "POST":
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Account created successfully")
    else:
        fm = SignupForm()
    return render(request, "enroll/signup.html", {"form": fm})


def user_details(request, id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk=id)
        fm = EditAdminProfileForm(instance=pi)
        return render(request, "enroll/userdetails.html", {"form": fm})
    else:
        return HttpResponseRedirect("/login/")
