# sendemail/urls.py
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('email/', views.emailView, name='emailView'),
    path('success/', views.successView, name='successView'),
]
