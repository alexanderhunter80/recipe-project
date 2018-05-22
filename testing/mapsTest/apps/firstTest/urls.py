from django.urls import path, include
from . import views #pylint: disable = E0402

urlpatterns = [
    path('embed', views.embed),
    path('embed/addLoc', views.addLoc),
    path('jsonReceiver', views.jsonReceiver),
    path('populateMap', views.populateMap),
    path('', views.index)
]