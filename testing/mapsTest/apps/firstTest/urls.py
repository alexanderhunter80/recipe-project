from django.urls import path, include
from . import views #pylint: disable = E0402

urlpatterns = [
    path('embed', views.embed),
    path('', views.index)
]