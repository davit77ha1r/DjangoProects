from django.urls import path, include
from . import views

urlpatterns = [
    path('home_view/', views.home_view, name="home_view"),
    path('', views.Home),
]