from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('newuser', views.newuser),
    path('login', views.login),
    path('username', views.create_username),
]