from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from dashboard.views import data_upload, leaderboard

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('dashboard/', include('dashboard.urls')),
    path('', auth_views.LoginView.as_view(template_name='dashboard/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='dashboard/logout.html'), name='logout'),
    path('settings/', data_upload, name='settings'),
    path('leaderboard/', leaderboard, name='leaderboard'),
]
