from django.contrib import admin
from django.urls import path, include
from tracker import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('stress-log/', views.stress_log, name='stress_log'),
    path('analytics/', views.analytics, name='analytics'),
    path('resources/', views.resources, name='resources'),
]