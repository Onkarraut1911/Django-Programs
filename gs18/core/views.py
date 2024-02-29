from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'core/coreone.html')

def about(request):
    return render(request,'core/coretwo.html')