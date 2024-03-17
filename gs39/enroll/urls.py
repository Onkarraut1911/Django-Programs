from django.urls import path
from .views import ShowFormData

urlpatterns = [
    path("registration/", ShowFormData),
]
