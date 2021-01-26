from django.db import models
from address.models import Address
from professionalInformation.models import ProfessionalInformation
from users.validations import validate_rg_length, validate_cpf, validate_cpf_length


class User(models.Model):
    name = models.CharField(max_length=200)
    RG = models.CharField(max_length=11, unique=True,  validators=[validate_rg_length])
    # CPF = models.CharField(max_length=12, unique=True, validators=[validate_cpf, validate_cpf_length])
    CPF = models.CharField(max_length=12, unique=True)
    phoneNumber = models.CharField(max_length=15)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    professionalInformation = models.ForeignKey(ProfessionalInformation, on_delete=models.CASCADE, null=True, blank=True)
    dateOfBirth = models.DateField()
    createdAt = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    @property
    def description(self):
        return "%s - %s" % (self.name, self.professionalInformation.profession)

    def __str__(self):
        return self.name

    def to_dict(self):
        user = {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "RG": self.RG,
            "CPF": self.CPF,
            "phoneNumber": self.phoneNumber,
            "dateOfBirth": self.dateOfBirth,
            "address": self.address.to_dict(),
            "professionalInformation": self.professionalInformation.to_dict(),
            "createdAt": self.createdAt,
        }
        return user
