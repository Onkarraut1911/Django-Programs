from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def Showformdata(request):
    fm = StudentRegistration
    return render(request,'enroll/studentregistration.html',{'form':fm})