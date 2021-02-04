from django.db import models

class Passengers(models.Model):
    travel_id = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)

def __str__(self):
    return self.id
