from django.shortcuts import render
from .forms import signupform
from django.contrib import messages
# Create your views here.
def sign_up(request):
  if request.method == "POST":
    fm = signupform(request.POST)
    if fm.is_valid():
      fm.save()
      messages.success(request, ' Your form is successfuly submited')
      fm = signupform()
  else:
    fm = signupform()
  return render(request,'enroll/signup.html',{'form':fm})
