from django.urls import path
from . import views

urlpatterns = [
    path("profile/", views.user_profile, name="profile"),
    path("signup/", views.signup_form, name="signup"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("userdetails/<int:id>", views.user_details, name="userdetails"),
]
