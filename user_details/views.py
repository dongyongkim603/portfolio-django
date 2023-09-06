from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from rest_framework.authentication import TokenAuthentication
from rest_framework import status

from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib.auth.decorators import login_required

from .models import UserDetails
from .serializers import UserDetailSerializer


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ('age', 'profile_image')

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == "POST":
        pass
    else:
        user_form = UserForm(instance=request.user)
        user_details_form = UserDetailsForm(instance=request.user.userdetails)
    return render(request, 'profile.html', {"u_form":user_form, "p_form": user_details_form})

class UserDetailsList(APIView):
    authentication_classes = [] 

    def get(self, request, format=None):
        details = UserDetails.objects.all()[0:100]
        serializer = UserDetailSerializer(details, many=True)
        return Response(serializer.data)
