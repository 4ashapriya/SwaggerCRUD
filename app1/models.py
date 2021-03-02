from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    owner= models.ForeignKey(to= User, on_delete= models.CASCADE)
    first_name= models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone_no = models.CharField(max_length=25)
