from django.urls import path
from . import views #pylint: disable = E0402

urlpatterns = [
    path('new', views.new),
    path('create', views.create)
]