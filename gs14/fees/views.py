from django.shortcuts import render
# from django.http import HttpRequest
# Create your views here.
def fees_django(request):
  return render(request, 'fees/feesone.html',{'um':'Hello django fees'})