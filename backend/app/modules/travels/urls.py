from django.shortcuts import render
from django.urls import reverse
from rest_framework.routers import DefaultRouter
from django.conf.urls import include, url

from .views import (
    ListTravels,
    PostTravels,
    RetrieveTravel,
    ValorationsListCreateAPIView
)



urlpatterns = [
    # url('travels/',ListTravels.as_view()),
    url(r'^travels/?$', ListTravels.as_view()),
    url(r'^travels/create/?$', PostTravels.as_view()),
    url(r'^travel/(?P<travel_slug>[-\w]+)/?$',RetrieveTravel.as_view()),  #Retrieve and destroy
    url(r'^travel/(?P<travel_slug>[-\w]+)/valoration/?$',ValorationsListCreateAPIView.as_view()),
    # url(r'^travels/(?P<pk>\d+)/$', DetailsTravel.as_view()),
]
