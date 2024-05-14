from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('send_log/', views.send_log, name='send_log'),
    path('filter_logs/', views.filter_logs, name='filter_logs'),
]