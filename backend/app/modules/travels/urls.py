from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from .views import (
    TravelViewSet #, TravelsAllAPIView,
    
    # TravelsFavoriteAPIView, CommentsListCreateAPIView, CommentsDestroyAPIView, TagListAPIView
)

router = DefaultRouter(trailing_slash=False)
router.register(r'travels', TravelViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),

    # url(r'^travels/feed/?$', TravelsAllAPIView.as_view()),

    # url(r'^travels/(?P<travel_slug>[-\w]+)/favorite/?$',
    #     TravelsFavoriteAPIView.as_view()),

    # url(r'^travels/(?P<travel_slug>[-\w]+)/comments/?$', 
    #     CommentsListCreateAPIView.as_view()),

    # url(r'^travels/(?P<travel_slug>[-\w]+)/comments/(?P<comment_pk>[\d]+)/?$',
    #     CommentsDestroyAPIView.as_view()),

    # url(r'^tags/?$', TagListAPIView.as_view()),
]
