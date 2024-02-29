from django.shortcuts import render
from .forms import student_login
# Create your views here.

def STUDENT_LOGIN_1(request):
    FM = student_login()
    return render(request,"enroll/studentlogin.html",{"form":FM})