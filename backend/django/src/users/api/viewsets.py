from rest_framework import generics, mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser,)
from ..api.serializers import UserSerializer
from ..models import User


class UserViewSetAdmin(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


class UserViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
# class UserViewSet(ModelViewSet):
    lookup_field = 'name'
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    # queryset = User.objects.all()
    queryset = User.objects.select_related('address')

    def get_queryset(self):
        queryset = self.queryset
        
        city = self.request.query_params.get('city', None)
        print('*********** city ************')
        print(city)
        if city is not None:
            queryset = queryset.filter(address__city=city)

        print('*********** queryset ************')
        print(queryset)
        return queryset

    def list(self, request):
        serializer_context = {'request': request}
        page = self.paginate_queryset(self.get_queryset())
        serializer = self.serializer_class(
            page,
            context=serializer_context,
            many=True
        )
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, name):
        serializer_context = {'request': request}

        try:
            serializer_instance = self.queryset.get(name=name)
        except User.DoesNotExist:
            return Response('A user with this name does not exist.', status=404)

        serializer = self.serializer_class(
            serializer_instance,
            context=serializer_context
        )
        print('*********** serializer.data ************')
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
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

    def update(self, request, name):
        serializer_context = {'request': request}

        try:
            serializer_instance = self.queryset.get(name=name)
        except User.DoesNotExist:
            return Response('A user with this name does not exist.', status=404)
            
        serializer_data = request.data

        serializer = self.serializer_class(
            serializer_instance, 
            context=serializer_context,
            data=serializer_data, 
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        print('*********** serializer.data ************')
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, name):
        try:
            user = User.objects.get(name=name)
        except User.DoesNotExist:
            return Response('A user with this name does not exist.', status=404)
        user.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
