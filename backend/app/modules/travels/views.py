from rest_framework import generics, mixins, status, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import (AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser,)
from .models import Travels, Valoration
from .serializers import TravelSerializer, ValorationSerializer
from .renderers import ValorationJSONRenderer
import json

class ListTravels(generics.ListCreateAPIView):
    # print("OLE LOS CANELONES LIST TRAVELSSSSS")
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Travels.objects.all()
    serializer_class = TravelSerializer

    #GET normal
    def get_queryset(self):
        queryset = self.queryset
        #  print(Valoration.objects.get(travel_slug_id="ontinyent-p3jlat"))
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

        #Get Valorations de este travel

        valorations = Valoration.objects.all().filter(travel_slug=travel_slug)
        print("VALORATIONS:")
        print(valorations)


        print("Selializer data")
        print(serializer.data)
        serializer.data.valorations = valorations

        # serializer.data.valorations = valorations

        # serializer = self.serializer_class(
        #     serializer_instance,
        #     valorations=valorations
        # )

        print ("---------------------------")
        print(serializer.data)
        # print(valorations.get(travel_slug=travel_slug))
        
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
        travel.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ValorationsListCreateAPIView(generics.ListCreateAPIView):
    print("DENTRO DE CREATE VALORATION")
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Valoration.objects.select_related(
        'travels', 'travels__driver', 'travels__driver__user',
        'driver', 'driver__user'
    )
    renderer_classes = (ValorationJSONRenderer,)
    serializer_class = ValorationSerializer

    def filter_queryset(self, queryset):
        print("Dentro de filter query")
        # The built-in list function calls `filter_queryset`. Since we only
        # want comments for a specific article, this is a good place to do
        # that filtering.
        filters = {self.lookup_field: self.kwargs[self.lookup_url_kwarg]}

        return queryset.filter(**filters)

    def create(self, request, travel_slug=None):
        print("********CREATE VALORATION**********")
        data = request.data.get('valoration', {}) #La valoration del postman está ok
        context = {'author': request.user.profile} #El author de la valoration ok

        try:
            context['travel'] = Travels.objects.get(slug=travel_slug)
        except Travels.DoesNotExist:
            raise NotFound('An travel with this slug does not exist.')


        serializer = self.serializer_class(data=data, context=context)  #Data tiene la valoration, context tiene el author de la valoration y el travel de la valoration
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

