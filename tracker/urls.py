from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('stress-log/', views.stress_log, name='stress_log'),
    path('analytics/', views.analytics, name='analytics'),
    path('resources/', views.resources, name='resources'),
]