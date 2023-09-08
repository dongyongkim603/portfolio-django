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


class AllUserDetails(APIView):
    
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, username, request):
        try:
            user = User.objects.get(username=username)
            user_details = UserDetails.objects.get(user=user)
            return user_details
        except User.DoesNotExist:
            raise Http404

    @login_required
    @transaction.atomic
    def post(self, request, format=None):
        serializer = UserDetailSerializer(data=request.data)
        # user_form = UserForm(request.POST, instance=request.user)
        # user_details_form = UserDetailsForm(request.POST, instance=request.user.userdetails)
        if serializer.is_valid():#user_form.is_valid() and user_details_form.is_valid():
            # user_form.save()
            # user_details_form.save()
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
