from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework import status

from django.shortcuts import redirect, render
from django import forms
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib.auth.decorators import login_required

from .models import UserDetails, UserPost
from .serializers import UserDetailSerializer, UserPostSerializer

class HomePageDetails(APIView):
  
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, username, request):
        try:
            creator = User.objects.get(username=username)
            user_posts = UserPost.objects.filter(creator=creator)
            return user_posts
        except UserPost.DoesNotExist:
            raise Http404

    def get(self, request, username, format=None):
        user = self.get_object(username, request)
        user_post = UserPost.objects.all()[0:40]
        serializer = UserPostSerializer(user_post, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = UserPostSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
