from django.contrib import admin
from django.urls import path
from .views import PreferenceCreateView

urlpatterns = [
    
    path('check-out', PreferenceCreateView.as_view(), name='check-out'),
]