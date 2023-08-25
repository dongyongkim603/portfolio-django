from django.http import response
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Forum, Comment, Category
from .serializers import ForumSerializer, CommentSerializer, CategorySerializer

class AllCategroiesList(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()[0:100]
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class LatestForumsList(APIView):
    def get(self, request, format=None):
        forums = Forum.objects.all()[0:4]
        serializer = ForumSerializer(forums, many=True)
        return Response(serializer.data)

class LatestCommentsList(APIView):
    def get(self, request, format=None):
        comments = Comment.objects.all()[0:40]
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)