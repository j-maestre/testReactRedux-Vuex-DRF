from rest_framework.serializers import ModelSerializer
from address.api.serializers import AddressSerializer
from address.models import Address
from professionalInformation.api.serializers import ProfessionalInformationSerializer
from professionalInformation.models import ProfessionalInformation
from django.core.cache import cache
from users.models import User


class UserSerializer(ModelSerializer):
    professionalInformation = ProfessionalInformationSerializer()
    address = AddressSerializer()

    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'description',
            'RG',
            'CPF',
            'phoneNumber',
            'dateOfBirth',
            'address',
            'professionalInformation',
            'createdAt',
        )

    def create(self, validated_data):
        addresstemp = validated_data.pop('address')
        professionalinformationtemp = validated_data.pop('professionalInformation')
        user = User.objects.create(**validated_data)
        address = Address.objects.create(**addresstemp)
        professionalinformation = ProfessionalInformation.objects.create(**professionalinformationtemp)
        user.address = address
        user.professionalInformation = professionalinformation
        user.save()
        
        return user

    def update(self, instance, validated_data):
        addresstemp = validated_data.pop('address')
        address = instance.address
        professionalinformationtemp = validated_data.pop('professionalInformation')
        professionalinformation = instance.professionalInformation

        instance.name = validated_data.get('name', instance.name)
        instance.RG = validated_data.get('RG', instance.RG)
        instance.CPF = validated_data.get('CPF', instance.CPF)
        instance.phoneNumber = validated_data.get('phoneNumber', instance.phoneNumber)
        instance.dateOfBirth = validated_data.get('dateOfBirth', instance.dateOfBirth)
        instance.save()

        professionalinformation.profession = professionalinformationtemp.get('profession', professionalinformation.profession)
        professionalinformation.companyName = professionalinformationtemp.get('companyName', professionalinformation.companyName)
        professionalinformation.position = professionalinformationtemp.get('position', professionalinformation.position)
        professionalinformation.save()

        address.line1 = addresstemp.get('line1', address.line1)
        address.line2 = addresstemp.get('line2', address.line2)
        address.city = addresstemp.get('city', address.city)
        address.state = addresstemp.get('state', address.state)
        address.latitude = addresstemp.get('latitude', address.latitude)
        address.longitude = addresstemp.get('longitude', address.longitude)
        address.save()

        return instance
