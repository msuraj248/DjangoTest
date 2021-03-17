from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=20)
    mail = models.CharField(max_length=20)
    contact = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    date = models.DateField()