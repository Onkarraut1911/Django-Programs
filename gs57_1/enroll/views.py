from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages
# Create your views here.
def Registration(request):
  if request.method == 'POST':
    fm = StudentRegistration(request.POST)
    if fm.is_valid():
      name = fm.cleaned_data['name']
      email = fm.cleaned_data['email']
      password = fm.cleaned_data['password']
      fm.save()
      messages.add_message(request, messages.SUCCESS, 'Form submited successfully...!!!')
      # messages.success(request,'Your account has  been created !!!')
      messages.info(request,'Now you can Login !!!')
  else:
    fm = StudentRegistration()

  return render(request,'enroll/UserRegistration.html',{'form':fm})


