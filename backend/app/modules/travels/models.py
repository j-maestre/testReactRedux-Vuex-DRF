from django.db import models

class Travels(models.Model):
    driverId = models.CharField(max_length=10)
