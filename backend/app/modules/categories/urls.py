from django.shortcuts import render
from django.conf.urls import include, url
from django.urls import reverse
from rest_framework.routers import DefaultRouter
from .views import (
    CategoriesViewSet,
    CategoriesViewSetAdmin

)

app_name = 'categories'

router = DefaultRouter()
router.register(r'categories', CategoriesViewSet)
 
#Admin
# router.register(r'^categories_Admin/(?P<category_id>\d+)/$', CategoriesViewSetAdmin)  #Las categorias solo las puede borrar un admin  xema@gmail.com
# r'^categories_Admin/(?P<id>\d+)/$'
# r'^categories_Admin/(?P<id>\d+)/$'
# router.register(r'comments_Admin', CommentViewSetAdmin)   
# router.register(r'tags_Admin', TagViewSetAdmin)  


urlpatterns = [
    url(r'^categories_Admin/(?P<id>\d+)/$', CategoriesViewSetAdmin.as_view()),  #Retrieve and destroy
    # url(r'^categories/?$', CategoriesViewSet)
    # url(r'^posts_slug/(?P<post_slug>[-\w]+)/?$', DetailsPost_slug.as_view()),
]

urlpatterns += router.urls
