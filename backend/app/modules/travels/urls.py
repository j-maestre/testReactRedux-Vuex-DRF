from django.shortcuts import render
from django.urls import reverse
from rest_framework.routers import DefaultRouter


urlpatterns = [
    url('travels/',ListTravels.as_view()),
    # url(r'^travels/?$', ListTravels.as_view()),
    # url(r'^travels/(?P<pk>\d+)/$', DetailsTravel.as_view()),
]
