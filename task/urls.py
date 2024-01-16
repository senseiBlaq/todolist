from django.urls import path
from . import views


app_name = 'task'
urlpatterns = [
    path('', views.task_view, name = 'task_view'),
    path('add', views.add_task, name = 'add_task')
]