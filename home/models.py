
from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()


class flavour(models.Model):
    name = models.TextField(primary_key= True)
    avail = models.TextField()
    price = models.TextField()

class type(models.Model):
    name = models.TextField()
    avail= models.TextField()


    
    