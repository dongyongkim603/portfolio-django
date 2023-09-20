from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status

from .models import PageDetails
from .serializers import PageDetailSerializer

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
    
    def post(self, request, format=None):
        serializer = PageDetailSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
