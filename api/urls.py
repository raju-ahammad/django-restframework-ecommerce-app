from django.urls import include, path
from rest_framework import views

from .views import home

urlpatterns = [
    path('', home, name="api-home"),
    
]
