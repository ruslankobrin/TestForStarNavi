from django.urls import path, include
from rest_framework import routers

from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'post', views.PostViewSet, basename='post')
router.register(r'like', views.LikeViewSet, basename='like')
router.register(r'unlike', views.LikeViewSet, basename='unlike')

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('signup/', views.SignUp.as_view(), name='signup')
]