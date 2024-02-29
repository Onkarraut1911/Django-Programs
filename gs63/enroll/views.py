from django.shortcuts import render ,HttpResponseRedirect
from django.contrib import messages
from .forms import signupform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login , logout
# from django.contrib.auth.models import User


# Create your views here.
def sign_up(request):
  if request.method == 'POST':
    fm = signupform(request.POST)
    if fm.is_valid():
      fm.save()
      messages.success(request,'Your form is successfuly submited')

  else:
    fm = signupform()
  return render(request,'enroll/signup.html',{'form':fm})


#When a user submits a form on a website (for example, a login form), the data from that form is sent to the server. In Django, this data is received in the request object.


def user_login(request):
  if request.method == "POST":   #if your request comes from post
    fm = AuthenticationForm(request=request , data=request.POST) # This part specifically takes the data that the user sent (like username and password from a login form) and gives it to the form
    if fm.is_valid():       #When you see request=request in a Django context, it means you are passing the request object from the current view to another function or method,
      uname = fm.cleaned_data['username']
      upass = fm.cleaned_data['password']
      user = authenticate(username=uname , password = upass) #Django provides an authenticate() function as part of its authentication system. This function checks the given username and password against the user model specified in your Django project and returns a user object if the credentials are correct, or None if the credentials are invalid.
      if user is not None:    
        login(request, user)  #function attaches the user object to the request object, indicating that the user is authenticated for the current session.
        return HttpResponseRedirect('/profile/')   ##This means the user is now considered logged in
  else:
    fm = AuthenticationForm()
  return render(request,'enroll/userlogin.html',{'form':fm})


def profile(request):
  # users = User.objects.all()
  return render(request,'enroll/profile.html',{'name':request.user})

def user_logout(request ):
  logout(request)
  return HttpResponseRedirect('/login/')


