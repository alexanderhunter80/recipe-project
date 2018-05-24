from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('recipes/', include('apps.recipes.urls')),
    path('', include('apps.users.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls)
]


