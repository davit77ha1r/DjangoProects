from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('messages/', views.message),
    path('home_view/', views.home_view, name="home_view"),
    path('register/', views.user_register),
]
