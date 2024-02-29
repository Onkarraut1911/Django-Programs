from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from enroll.forms import signupform
# Create your views here
def sign_up(request):
  if request.method == "POST":
    fm = signupform(request.POST)
    if fm.is_valid():
      fm.save()
      messages.success(request,'form is successfully submited')
  else:
    fm = signupform()
  return render(request,'enroll/signup.html', {'form':fm})
