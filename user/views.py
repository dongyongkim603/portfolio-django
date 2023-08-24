from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User
from .serializers import ForumSerializer

class LatestForumsList(APIView):
    def get(self, request, format=None):
        users = User.objects.all()[0:4]
        serializer = ForumSerializer(User, many=True)
        return Response(serializer.data)