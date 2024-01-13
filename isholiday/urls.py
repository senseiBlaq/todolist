from django.urls import path
from . import views


urlpatterns = [
    path('', views.isChristmas, name = 'index'),
    path('time', views.time_day, name = 'time')
]