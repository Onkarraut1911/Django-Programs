from django.shortcuts import render
from .forms import student_login
# Create your views here.

def student_registration(request):
    SF  = student_login()
    SF.order_fields(field_order = [ 'email','name','first_name'])
    return render(request,'enroll\studentlogin.html',{'form':SF})