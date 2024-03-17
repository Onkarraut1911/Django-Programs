from django.db import models

# Create your models here.


class StudentRegistration(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=104)
    password = models.CharField(max_length=50)
