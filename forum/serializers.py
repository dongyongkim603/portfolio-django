from django.db import models
from rest_framework import serializers

from .models import Category, Forum, Comment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'slug',
            'get_absolute_url',
        )

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

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'forum',
            'name',
            'content',
            'get_image',
        )