from django.db import models

class Travels(models.Model):
    # driver = models.CharField(max_length=10)
    numPassengers = models.CharField(max_length=11, default="2") #,  validators=[validate_rg_length]
    date = models.CharField(max_length=200) # default timezone.now()
    startTime = models.CharField(max_length=200) # default timezone.now()
    finishTime = models.CharField(max_length=200) # default timezone.now()
    city = models.CharField(max_length=200, default="no where")
    ubication = models.CharField(max_length=200, default="no where")
    postalCode = models.CharField(max_length=200, default="0000")
    createdAt = models.DateTimeField(auto_now_add=True) #default timezone.now()
    active = models.BooleanField(default=True)

    driver = models.ForeignKey(
        'profiles.Profile', on_delete=models.CASCADE, related_name='travels'
    )

def __str__(self):
    return self.id
#     # @property
#     # def description(self):
#     #     return "%s - %s" % (self.name, self.professionalInformation.profession)


# def to_dict(self):
#     travel = {
#         "driver": self.driver,
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