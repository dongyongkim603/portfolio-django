from django.urls import path, include
from django.contrib import admin
from page_details import views

app_name = 'page_details'

urlpatterns = [
  path('homepage-detail/', views.HomePageDetails.as_view()),
]
