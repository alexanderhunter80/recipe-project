from django.urls import path, include

urlpatterns = [
    path('recipes/', include('apps.recipes.urls')),
]


