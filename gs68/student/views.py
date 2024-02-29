from django.shortcuts import render
from datetime import timedelta , datetime
# Create your views here.
def setcookie(request):
    reponse = render(request,'student/setcookie.html')
    reponse.set_cookie('name','sonam' , max_age=2000)  # max age is cookie deletion time in seconds
    reponse.set_cookie('name','sonam' , expires=datetime.utcnow()+timedelta(days=2))  # expires is cookie deletion expires time to set 2 days
    
    return reponse


def getcookie(request):
    # name = request.COOKIES['name']
    name = request.COOKIES.get('name',"Guest") # if cookie is not available in browser then its show None, now  its return default value Guest
    return render(request,'student/getcookie.html',{'name':name})


def delcookie(request):
    reponse =  render(request,'student/delcookie.html')
    reponse.delete_cookie('name')
    return reponse