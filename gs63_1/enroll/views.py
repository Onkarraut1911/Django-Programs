from django.shortcuts import render , HttpResponseRedirect
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages 
from django.contrib.auth import authenticate , login , logout
# Create your views here.

#Sign up View
def sign_up(request):
  if request.method=='POST':
    fm = UserCreationForm(request.POST)
    if fm.is_valid():
      fm.save()
      messages.success(request,'Your form succesfuly submited')
      # return HttpResponseRedirect('')
    fm = UserCreationForm()

  else:
    fm = UserCreationForm()
  return render(request,'enroll/signup.html',{'form':fm})

#Login View Function
def user_login(request):
  fm = AuthenticationForm(request=request , data=request.POST)
  if fm.is_valid():
    uname = fm.cleaned_data['username']
    upass = fm.cleaned_data['password']
    user = authenticate(username=uname , password=upass)
    if user is not None:
      login(request, user)
      return HttpResponseRedirect('/profile/')
  else:
    fm = AuthenticationForm
  return render(request,'enroll/login.html',{'form':fm})
    
#profile

def user_profile(request):
  return render(request , 'enroll/profile.html')
