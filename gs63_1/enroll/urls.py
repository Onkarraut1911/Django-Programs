from django.urls import path
from enroll.views import *
urlpatterns = [
    path('signup/',sign_up , name='signup'),
    path('login/',user_login , name='login'),
    path('profile/',user_profile , name='profile'),
]
