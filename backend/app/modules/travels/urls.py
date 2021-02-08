from django.shortcuts import render
from django.urls import reverse
from rest_framework.routers import DefaultRouter
from django.conf.urls import include, url

from .views import (
    ListTravels,
    PostTravels,
)



urlpatterns = [
    # url('travels/',ListTravels.as_view()),
    url(r'^travels/?$', ListTravels.as_view()),
    url(r'^travels/create/?$', PostTravels.as_view()),
    # url(r'^travels/(?P<pk>\d+)/$', DetailsTravel.as_view()),
]
