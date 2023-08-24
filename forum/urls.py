from django.urls import path, include

from forum import views

urlpatterns = [
    path('latest-forums/', views.LatestForumsList.as_view()),
]
