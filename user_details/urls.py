from django.urls import path, include
from django.contrib import admin
from user_details import views

app_name = 'user_details'

urlpatterns = [
  path('profile/<str:username>', views.UserDetails.as_view())
]
