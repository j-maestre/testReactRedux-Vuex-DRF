from rest_framework import generics, mixins, status, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import (AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser,)
from .models import Travels
from .serializers import TravelSerializer
import json

class ListTravels(generics.ListCreateAPIView):
    print("OLE LOS CANELONES LIST TRAVELSSSSS")
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Travels.objects.all()
    serializer_class = TravelSerializer
    #GET http://0.0.0.0:8000/api/travels/

    def get(self, request):
        serializer_context = {'request': request}
        page = self.paginate_queryset(self.get_queryset())

        serializer = self.serializer_class(
            page,
            context=serializer_context,
            many=True
        )
        return self.get_paginated_response(serializer.data)
