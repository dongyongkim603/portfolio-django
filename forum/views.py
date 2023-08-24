from django.http import response
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Forum
from .serializers import ForumSerializer

class LatestForumsList(APIView):
    def get(self, request, format=None):
        forums = Forum.objects.all()[0:4]
        serializer = ForumSerializer(forums, many=True)
        return Response(serializer.data)