from django.urls import path, include
from django.contrib import admin
from user_details import views

app_name = 'user_details'

urlpatterns = [
  path('profile/', views.AllUserDetails.as_view()),
  path('profile/<str:username>/', views.AllUserDetails.as_view()),
  path('edit-profile/<int:pk>/', views.UserDetailsPatchView.as_view()),
  path('user-posts/', views.AllUserPost.as_view()),
  path('user-posts/<int:pk>/', views.AllUserPost.as_view()),
]
