from django.db import models


class ProfessionalInformation(models.Model):
    profession = models.CharField(max_length=70)
    companyName = models.CharField(max_length=200)
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.profession + " at " + self.companyName

    def to_dict(self):
        professionalinformation = {
            "profession": self.profession,
            "companyName": self.companyName,
            "position": self.position
        }
        return professionalinformation
