from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('messages', views.messages),
]