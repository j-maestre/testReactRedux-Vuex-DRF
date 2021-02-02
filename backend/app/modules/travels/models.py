from django.db import models
# from address.models import Address
# from professionalInformation.models import ProfessionalInformation
# from users.validations import validate_rg_length, validate_cpf, validate_cpf_length


class Travels(models.Model):
    Id = models.CharField(max_length=10, unique=True)
    driverId = models.CharField(max_length=10)
    numPassengers = models.CharField(max_length=11) #,  validators=[validate_rg_length]

    date = models.CharField(max_length=200)
    startTime = models.CharField(max_length=200)
    finishTime = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    ubication = models.CharField(max_length=200)
    postalCode = models.CharField(max_length=200)
    # createdAt = models.DateTimeField(auto_now_add=True) ES AQUIII
    # active = models.BooleanField(default=True)

    # @property
    # def description(self):
    #     return "%s - %s" % (self.name, self.professionalInformation.profession)

    def __str__(self):
        return self.Id #Devolvemos el id del travel

    # def to_dict(self):
    #     travel = {
    #         "Id": self.Id,
    #         "driverId": self.driverId,
    #         "numPassengers": self.numPassengers,
    #         "date": self.date,
    #         "startTime": self.starttime,
    #         "finishTime": self.finishTime,
    #         "city": self.city,
    #         "ubication": self.ubication, #.to_dict(),
    #         "postalCode": self.postalCode, #.to_dict(),
    #         # "createdAt": self.createdAt, Aqui no es
    #         #Porque no devolvemos Active ??
    #     }
    #     return travel 
