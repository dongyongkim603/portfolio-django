from django.db import models
from rest_framework import serializers

from .models import PageDetails

class PageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageDetails
        fields = (
            'get_resume_html',
            'get_resume_url',
            'url',
            'get_slug'
        )

class ResumeFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageDetails
        fields = (
            'get_resume_file',
            'url',
            'get_slug'
        )        