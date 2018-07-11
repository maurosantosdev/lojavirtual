# coding=utf-8

from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('registro/', views.register, name='register'),
]