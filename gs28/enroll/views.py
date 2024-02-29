from django.shortcuts import render
from .forms import studentregistration
# Create your views here.
def showformdata(request):
  fm = studentregistration
  return render(request,'enroll/userregistration.html',{'form' : fm })
