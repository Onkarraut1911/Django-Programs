from django.shortcuts import render
from .forms import studentregistration
# Create your views here.
def showformdata(request):
    fm = studentregistration(auto_id=True, label_suffix = '=',
    initial = {'name': 'sonam' , 'email':'ofnaif@gmil.com'})
    return render(request,'enroll\studentregistration.html',{'form':fm})