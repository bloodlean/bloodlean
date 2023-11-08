from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('post/', post, name='post'),
    path('post_detail/<pk>/', post_detail, name='post_detail'),
    path('post_detail/<pk>/delete/', post_delete, name='post_delete'),
    path('create/', create, name='create'),
]

