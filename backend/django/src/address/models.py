from django.db import models

from address.choices import UF_CHOICES


class Address(models.Model):
    line1 = models.CharField(max_length=100)
    line2 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=80)
    state = models.CharField(max_length=50, choices=UF_CHOICES)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.line1 + " " + self.city + " " + self.state + " "

    def to_dict(self):
        address = {
            "line1": self.line1,
            "line2": self.line2,
            "city": self.city,
            "state": self.state,
            "latitude": self.latitude,
            "longitude": self.longitude
        }
        return address
