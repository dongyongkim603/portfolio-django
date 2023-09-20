from django.db import models
from rest_framework import serializers

from .models import PageDetails

class PageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageDetails
        fields = (
            'get_resume',
            'url',
            'get_slug'
        )