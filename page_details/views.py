from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status

from .models import PageDetails
from .serializers import PageDetailSerializer, ResumeFileSerializer

class HomePageDetails(APIView):
   
    def get_object(self):
        try:
            page = PageDetails.objects.filter(slug='homepage')
            return page
        except PageDetails.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        page = self.get_object()
        serializer = PageDetailSerializer(page, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DownloadResume(APIView):
   
    def get_object(self):
        try:
            page = PageDetails.objects.filter(slug='homepage')
            return page
        except PageDetails.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        page = self.get_object()
        serializer = ResumeFileSerializer(page, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
