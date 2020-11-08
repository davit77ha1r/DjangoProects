from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('greeting/', views.greeting),
    path('introduction/', views.introduction),
    path('datetime/', views.datetime1),
    path('task/', views.task),
]