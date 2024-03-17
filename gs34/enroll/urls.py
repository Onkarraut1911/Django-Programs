from django.urls import path
from .views import student_registration

urlpatterns = [
    path("", student_registration),
]
