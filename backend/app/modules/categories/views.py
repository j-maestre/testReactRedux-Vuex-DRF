from django.shortcuts import render
from rest_framework import generics, mixins, status, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import (AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser,)

from .models import Categories
from .serializers import CategoriesSerializer
from .renderers import CategoriesJSONRenderer
import json


class CategoriesViewSet(mixins.CreateModelMixin, 
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    print("*****OLE LOS CANELONES CATEGORIES VIEW SET******")
    lookup_field = 'id'
    queryset = Categories.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = (CategoriesJSONRenderer,)
    serializer_class = CategoriesSerializer
    print(queryset)


    #GET normal
    def get_queryset(self):
        print("**********************************************")
        print("dentro del get categories")
        print("**********************************************")
        queryset = self.queryset
        return queryset.all()  #Todas las categorias


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


    def create(self, request):
        print("**********Create category*******")
        serializer_class = CategoriesSerializer
        serializer_context = {
            'request': request
        }
        serializer_data = request.data.get('category', {})  # Categoria del postman
        serializer = serializer_class(
        #data tiene los valores de postman
        data=serializer_data,
        #context contiene el usuario que está logueado
        context=serializer_context 
        )

        serializer.is_valid(raise_exception=True)#Obligado llamar a .is_valid antes de guardarlo (seguridad++)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)




#Admin
class CategoriesViewSetAdmin(generics.RetrieveUpdateDestroyAPIView): #viewsets.ModelViewSet
    # lookup_field = 'id'
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    lookup_field = 'id'
    permission_classes = (IsAuthenticated,)
    permission_classes = (IsAdminUser,)


    def destroy(self, request, id=None):
        print("*************DESTROY*******************")
        print("USER -> ", self.request.user)
        print(Categories.objects.all())
        try:
            category = Categories.objects.get(id=id)

        except Categories.DoesNotExist:
            raise NotFound('An category with this id does not exist.')
        category.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)




    
