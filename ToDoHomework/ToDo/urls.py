from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('new_task', views.new_task,name="new_task"),
    path('task_update/<str:pk>', views.task_update, name="task_update"),
    path('see_task/<str:pk>', views.see_task, name="see_task"),
    path('delete_task/<str:pk>', views.delete_task, name="delete_task"),
]