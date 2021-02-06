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

    print(queryset)
    #GET normal
    def get_queryset(self):
        queryset = self.queryset

        # author = self.request.query_params.get('author', None)
        # if author is not None:
        #     queryset = queryset.filter(author__user__username=author)

        # hashtag = self.request.query_params.get('hashtags', None)
        # if hashtag is not None:
        #     queryset = queryset.filter(hashtags__hashtag=hashtag)

        return queryset.all()  #Devuelve todos los travels, en un futuro aqui podemos aplicar filtros


    # PAGINATE
    # def get(self, request):
    #     serializer_context = {'request': request}
    #     page = self.paginate_queryset(self.get_queryset())

    #     serializer = self.serializer_class(
    #         page,
    #         context=serializer_context,
    #         many=True
    #     )
    #     return self.get_paginated_response(serializer.data)

    #POST http://0.0.0.0:8000/api/travels/    Tienes que estar logueado
    def create(self, request):
        print("POST TRAVELLL")
        serializer_context = {
            'driverId': 1 #Esto es el id del usuario logueado, que es quien publica el viaje que es el conductor #request.user.profile,
        }
        print('************** create post view *******************')
        print(request.data.get('post', {}))


        serializer_data = request.data.get('post', {})

        print("SERIALIZER data: ",serializer_data)
        
        serializer = self.serializer_class(
            data=serializer_data, context=serializer_context
        )
        serializer.is_valid(raise_exception=True)
        print('*********** validated_data ************')
        print(serializer.validated_data)

        serializer.save()
        
        print('*********** data ************')
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
