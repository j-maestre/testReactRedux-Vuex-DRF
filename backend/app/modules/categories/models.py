from django.db import models

class Categories(models.Model):
    type = models.CharField(max_length=100)