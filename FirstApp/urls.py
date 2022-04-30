from django import views
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'FirstApp'

urlpatterns = [
    path('hallo', views.index, name='index'),

    path('add/<int:num1>/<int:num2>', views.add, name='add'),
    path('minus/<str:num1>/<str:num2>', views.minus, name='minus'),
    path('div/<str:num1>/<str:num2>', views.div, name='div'),
]