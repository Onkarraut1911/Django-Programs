from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(
        max_length=50, blank=True
    )  # if you set blank = True then Required error messaage doesnt display in html i.e it make required = False
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)


# makemigrations is convert model class to sql query
# migrate is used to query execution
