from rest_framework import generics, mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser,)
from ..api.serializers import TravelsSerializer
from ..models import Travels


class TravelsViewSetAdmin(ModelViewSet):
    queryset = Travels.objects.all()
    serializer_class = TravelsSerializer
    permission_classes = (IsAdminUser,)


class TravelsViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
# class TravelsViewSet(ModelViewSet):
    lookup_field = 'name'
    serializer_class = TravelsSerializer  #Que es esto?
    permission_classes = (AllowAny,)
    ## permission_classes = (IsAuthenticatedOrReadOnly,)
    ## queryset = Travels.objects.all()
    # queryset = Travels.objects.select_related('address') 

    def get_queryset(self):   #Esto lo dejo igual porque los usuarios buscaran viajes de una ciudad
        queryset = self.queryset
        
        city = self.request.query_params.get('city', None)
        print('*********** city ************')
        print(city)
        if city is not None:
            queryset = queryset.filter(city=city)

        print('*********** queryset ************')
        print(queryset)
        return queryset

    def list(self, request): #Esto tambien se deja igual porque es la paginacion del list, no tiene nada que ver con el modelo
        serializer_context = {'request': request}
        page = self.paginate_queryset(self.get_queryset())
        serializer = self.serializer_class(
            page,
            context=serializer_context,
            many=True
        )
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, name): #El details lo hacemos por el id del Travel
        serializer_context = {'request': request}

        try:
            serializer_instance = self.queryset.get(Id=Id)
        except Travels.DoesNotExist:  #Esto lo busca y si no lo encuentra lanza la excepcion????
            #Lo demás el modelico y no hace falta cambiarlo porque es igual para todos los modelos
            return Response('A TRAVEL with this Id does not exist.', status=404)

        serializer = self.serializer_class(
            serializer_instance,
            context=serializer_context
        )
        print('*********** serializer.data ************')
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

        

    def create(self, request):  #El create es modelico tambien
        serializer_context = {
            'request': request
        }
        serializer_data = request.data

        serializer = self.serializer_class(
        data=serializer_data, context=serializer_context
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        print('*********** serializer.data ************')
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def update(self, request, name): #El update tambien es generico menos el param Id
    #     serializer_context = {'request': request}

    #     try:
    #         serializer_instance = self.queryset.get(Id=Id)
    #     except Travels.DoesNotExist:
    #         return Response('A Travel with this Id does not exist.', status=404)
            
    #     serializer_data = request.data

    #     serializer = self.serializer_class(
    #         serializer_instance, 
    #         context=serializer_context,
    #         data=serializer_data, 
    #         partial=True
    #     )
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()

    #     print('*********** serializer.data ************')
    #     print(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, name):
        try:
            travel = Travels.objects.get(Id=Id)
        except Travels.DoesNotExist:
            return Response('A Travel with this Id does not exist.', status=404)
        travel.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
