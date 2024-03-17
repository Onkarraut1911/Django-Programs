from django.urls import path
from . views import studentregistration
urlpatterns = [
    path('',studentregistration),
]
