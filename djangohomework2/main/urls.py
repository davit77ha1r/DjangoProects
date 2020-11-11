from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('json', views.json_read),
    path('check', views.check),
    path('task', views.task),
]
