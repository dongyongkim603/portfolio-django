from django.urls import path, include

from user import views

urlpatterns = [
    path('all-users/', views.AllUsersList.as_view()),
]