from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm #this is a built in form and import here for the using this form
from django.contrib import messages
# Create your views here.

def sign_up(request):
  if request.method == "POST":  # this is see the request method is get or post if it is post then go to the next in the if statement
    fm = UserCreationForm(request.POST)  #this line give the filled form data i.e. POST store in fm 
    if fm.is_valid():  #This is a validation statement if data is valid the is_valid function returns true and run the if statement
      Username = fm.cleaned_data['Username']
      Password = fm.cleaned_data['Password']
      Password_again = fm.cleaned_data['Password_confirmation']
      # if Password == Password_again :
      #   fm.save() # this line save the data from gives the post method in the template file
      # else:
      #   messages.success(request,"Password doesn't match")
      fm.save()

  else: # this else run if the request method is get (this is the defaulet method )
    fm = UserCreationForm()  # this line create a object of form (form object) when call the views()(this is a blank form because request is the get )
  return render(request,'enroll/signup.html',{'form':fm})
