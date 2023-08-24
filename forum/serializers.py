from django.db import models
from rest_framework import serializers

from .models import Category, Forum

class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = (
            'id',
            'name',
            'get_absolute_url',
            'description',
            'get_image',
            'get_thumbnail'
        )