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

from .models import UserDetails
from .serializers import UserDetailSerializer

class UserDetailsPatchView(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def patch(self, request, pk, format=None):
        try:
            user_details = UserDetails.objects.get(pk=pk)
        except UserDetails.DoesNotExist:
            return Response({"detail": "UserDetails not found."}, status=status.HTTP_404_NOT_FOUND)
        if 'age' in request.data:
            user_details.age = request.data['age']
        if 'bio' in request.data:
            user_details.bio = request.data['bio']
        if 'profile_image' in request.data:
            user_details.profile_image = request.data['profile_image']
        if 'thumbnail' in request.data:
            user_details.thumbnail = request.data['thumbnail']
        serializer = UserDetailSerializer(user_details)
        user_details.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class AllUserDetails(APIView):
    
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, username, request):
        try:
            user = User.objects.get(username=username)
            user_details = UserDetails.objects.get(user=user)
            return user_details
        except User.DoesNotExist:
            raise Http404

    @transaction.atomic
    def post(self, request, format=None):
        serializer = UserDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, username, format=None):
        details = self.get_object(username, request)
        try:
            serializer = UserDetailSerializer(details)
            print(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
