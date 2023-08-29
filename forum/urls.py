from django.urls import path, include

from forum import views

urlpatterns = [
    path('latest-forums/', views.LatestForumsList.as_view()),
    path('forums/<slug:category_slug>/<slug:forum_slug>/', views.ForumDetail.as_view()),
    path('categories/', views.AllCategroiesList.as_view()),
]
