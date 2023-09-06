from django.urls import path, include
from django.contrib import admin
from user_details import views

app_name = 'user_details'

urlpatterns = [
  path('profile/', views.update_profile, name='profile')
]
