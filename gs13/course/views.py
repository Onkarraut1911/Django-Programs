from django.shortcuts import render

# Create your views here.
def learn_django(request):
  cname = 'django'
  duration = '4 hours'
  seat = 10
  django_details = {'nm':cname , 'du':duration , 'se':seat }
  return render(request, 'course/courseone.html',django_details)