# coding=utf-8

from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.index, name='index'),
    path('alterar-dados/', views.update_user, name='update_user'),
    path('alterar-senha/', views.update_password, name='update_password'),
    path('registro/', views.register, name='register'),
    path('endereco/', views.update_address, name='update_endereco'),
]