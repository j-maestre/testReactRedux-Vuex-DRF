from rest_framework import generics, mixins, status, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import (AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser,)
from .models import Travels
from .serializers import TravelSerializer
import json

class ListTravels(generics.ListCreateAPIView):
    # print("OLE LOS CANELONES LIST TRAVELSSSSS")
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Travels.objects.all()
    serializer_class = TravelSerializer

    #GET normal
    def get_queryset(self):
        queryset = self.queryset
        return queryset.all()  #Devuelve todos los travels, en un futuro aqui podemos aplicar filtros


    # PAGINATE
    def list(self, request):
        serializer_context = {'request': request}
        page = self.paginate_queryset(self.get_queryset())

        serializer = self.serializer_class(
            page,
            context=serializer_context,
            many=True
        )
        return self.get_paginated_response(serializer.data)

    

class PostTravels(generics.ListCreateAPIView):
    #POST http://0.0.0.0:8000/api/travels/

    def create(self, request):
        serializer_class = TravelSerializer
        serializer_context = {
            'driver': request.user.profile,
            'request': request
        }
        serializer_data = request.data.get('travel', {})  # Aqui está el travel de postman. Pilla el json travel, y si no hay, devuelve un json vacio
        serializer = serializer_class(
        #data tiene los valores de postman
        data=serializer_data,
        #context contiene el usuario que está logueado
        context=serializer_context 
        )

        serializer.is_valid(raise_exception=True)#Obligado llamar a .is_valid antes de guardarlo (seguridad++)
        serializer.save() #Antes de hacer el save, signals lo pilla y le añade el slug

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class RetrieveTravel(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Travels.objects.all()
    serializer_class = TravelSerializer

    # print("*************dentro del retrieve*************")
    # print("queryseet-> ",queryset.filter(slug="ontinyent-3vbudf"))    

    def retrieve(self, request, travel_slug):
        serializer_context = {'request': request}
        try:
            serializer_instance = self.queryset.get(
                slug=travel_slug,
            )

        except Travels.DoesNotExist:
            raise NotFound('A travel with this slug does not exist.')

        serializer = self.serializer_class(
            serializer_instance,
            context=serializer_context
        )
        return Response(serializer.data, status=status.HTTP_200_OK)

    #Eliminar el travel estando logueado y poniendo el slug del travel
    def destroy(self, request, travel_slug=None):
        print("*************DESTROY*******************")
        print("USER -> ", self.request.user)
        print(Travels.objects.all())
        try:
            travel = Travels.objects.get(
                slug=travel_slug, 
                driver=self.request.user)
        except Travels.DoesNotExist:
            raise NotFound('An travel with this slug does not exist.')
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
