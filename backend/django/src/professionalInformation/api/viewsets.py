from rest_framework.viewsets import ModelViewSet
from ..models import ProfessionalInformation
from .serializers import ProfessionalInformationSerializer


class ProfessionalInformationViewSet(ModelViewSet):
    queryset = ProfessionalInformation.objects.all()
    serializer_class = ProfessionalInformationSerializer