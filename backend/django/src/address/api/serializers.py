from rest_framework.serializers import ModelSerializer
from ..models import Address


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'line1',
            'line2',
            'city',
            'state',
            'latitude',
            'longitude'
        )