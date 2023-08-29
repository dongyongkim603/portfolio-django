from django.http import Http404

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

class ForumDetail(APIView):
    def get_object(self, category_slug, forum_slug):
        try:
            return Forum.objects.filter(category__slug=category_slug).get(slug=forum_slug)
        except Forum.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, forum_slug, format=None):
        forum = self.get_object(category_slug, forum_slug)
        serializer = ForumSerializer(forum)
        return Response(serializer.data)

class LatestCommentsList(APIView):
    def get(self, request, format=None):
        comments = Comment.objects.all()[0:40]
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)