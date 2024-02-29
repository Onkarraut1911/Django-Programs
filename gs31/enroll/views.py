from django.shortcuts import render
from .forms import StudentLogin
# Create your views here.
def Student_Login(request):
    stu_data = StudentLogin()
    return render(request,'enroll/StudentLogin.html',{'form':stu_data})