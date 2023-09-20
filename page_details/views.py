from django.http import Http404, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status

from .models import PageDetails
from .serializers import PageDetailSerializer, ResumeFileSerializer

def get_object(self):
    try:
        page = PageDetails.objects.filter(slug='homepage')
        return page
    except PageDetails.DoesNotExist:
        raise Http404

class HomePageDetails(APIView):
   

    def get(self, request, format=None):
        page = self.get_object()
        serializer = PageDetailSerializer(page, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DownloadResume(APIView):
    def get(self, request, format=None):
        page_details = PageDetails.objects.first()

        try:
            binary_content = page_details.get_resume_file()

            response = HttpResponse(binary_content, content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{page_details.resume.name}"'

            return response
        except PageDetails.DoesNotExist:
            raise Http404 

