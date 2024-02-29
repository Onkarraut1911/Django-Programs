from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('Home Page')


def learn_django(request):
    return HttpResponse('<h1><b>Hello World</b></h1>')


def learn_python(request):
    a = '<h2> Hello Python </h2>'
    return HttpResponse(a)


def learn_var(request):
    a = 'Hello Varibale'
    return HttpResponse(a)


def learn_math(request):
    a = 10+10
    return HttpResponse(a)


def learn_format(request):
    a = 'Geekyshows'
    return HttpResponse(f'Hello how are you (a)')
