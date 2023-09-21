import os
from django.http import Http404, HttpResponse
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
    def get(self, request, format=None):
        file_path = os.path.join('/Users/johnhaney/Code/Django/John_portfolio/portfolio_django/media/uploads/resumes/John_William_Meehan_Haney_Resume.docx')
        try:
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/octet-stream")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response
        except PageDetails.DoesNotExist:
            raise Http404 

