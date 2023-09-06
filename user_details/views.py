from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from rest_framework.authentication import TokenAuthentication
from rest_framework import status

from .models import UserDetails
from .serializers import UserDetailSerializer

class UserDetailsList(APIView):
    authentication_classes = [] 

    def get(self, request, format=None):
        details = UserDetails.objects.all()[0:100]
        serializer = UserDetailSerializer(details, many=True)
        return Response(serializer.data)
