from . import views
from django.urls import path
urlpatterns = [
    path('',views.student_registration),
    path('success/',views.thankyou),
]