from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'post', views.PostViewSet, basename='post')
router.register(r'like', views.LikeViewSet, basename='like')
router.register(r'unlike', views.LikeViewSet, basename='unlike')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]