from django.shortcuts import render
def home(request):
  return render(request, 'projectone.html',{'um':'Hello django home page'})