from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def learn_django(request):
  return render(request, 'learnone.html')

def learn_python(request):
  return render(request,'learntwo.html')
