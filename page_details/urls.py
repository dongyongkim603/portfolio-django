from django.urls import path, include
from django.contrib import admin
from page_details import views

app_name = 'user_details'

urlpatterns = [
  path('/home', views.HomePageDetails.as_view()),
]
