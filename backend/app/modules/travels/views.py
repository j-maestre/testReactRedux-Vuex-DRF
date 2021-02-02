# from django.shortcuts import render

from rest_framework import generics, mixins, status, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.permissions import (
    AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
)
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Travels #, Comment, Tag
#from .renderers import TravelJSONRenderer #, CommentJSONRenderer
from .serializers import TravelSerializer #, CommentSerializer, TagSerializer

# Create your views here.



class TravelViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                   ):

    print("OLE LOS CANELONES")
    queryset = list(Travels.objects.all())
    def list(self, request):
        print("OLE LOS CANELONES LIST ALL TRAVELS")
        serializer_context = {'request': request}
        page = self.paginate_queryset(self.get_queryset())

        serializer = self.serializer_class(
            page,
            context=serializer_context,
            many=True
        )
        return self.get_paginated_response(serializer.data)


    # queryset = Travel.objects.select_related('author', 'author__user')
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    # renderer_classes = (TravelJSONRenderer,)
    # serializer_class = TravelSerializer

    # def get_queryset(self):
        

        # queryset = self.queryset

        # author = self.request.query_params.get('author', None)
        # if author is not None:
        #     queryset = queryset.filter(author__user__username=author)

        # tag = self.request.query_params.get('tag', None)
        # if tag is not None:
        #     queryset = queryset.filter(tags__tag=tag)

        # favorited_by = self.request.query_params.get('favorited', None)
        # if favorited_by is not None:
        #     queryset = queryset.filter(
        #         favorited_by__user__username=favorited_by
        #     )

        # return queryset

    # def create(self, request):
    #     serializer_context = {
    #         'driverId': request.user.profile,
    #         'request': request
    #     }
    #     serializer_data = request.data.get('travel', {})

    #     serializer = self.serializer_class(
    #     data=serializer_data, context=serializer_context
    #     )
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()

    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    # def retrieve(self, request, slug):
    #     serializer_context = {'request': request}

    #     try:
    #         serializer_instance = self.queryset.get(slug=slug)
    #     except Travel.DoesNotExist:
    #         raise NotFound('An travel with this slug does not exist.')

    #     serializer = self.serializer_class(
    #         serializer_instance,
    #         context=serializer_context
    #     )

    #     return Response(serializer.data, status=status.HTTP_200_OK)