from rest_framework.serializers import ModelSerializer
from ..models import ProfessionalInformation


class ProfessionalInformationSerializer(ModelSerializer):
    class Meta:
        model = ProfessionalInformation
        fields = (
            'profession',
            'companyName',
            'position'
        )