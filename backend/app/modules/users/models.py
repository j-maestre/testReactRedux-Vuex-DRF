from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=200, default="")
    surname = models.CharField(max_length=200, default="")
    tlf = models.CharField(max_length=20,default=0)
    address = models.CharField(max_length=200, default="")

def __str__(self):
    return self.id