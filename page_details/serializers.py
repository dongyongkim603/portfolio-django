from django.db import models
from rest_framework import serializers

from .models import PostDetails

class PageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostDetails
        fields = (
            'get_resume',
            'url'
        )