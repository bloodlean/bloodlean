from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]

router = DefaultRouter()
router.register('user', UserViewSet, basename='user')
urlpatterns += router.urls

router = DefaultRouter()
router.register('post', PostViewSet, basename='post')
urlpatterns += router.urls