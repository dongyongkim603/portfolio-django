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
            'get_category_id',
            'get_category_name',
            'get_creator_id',
            'get_creator_name',
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
            'slug',
            'forum',
            'get_creator',
            'content',
            'get_image',
            'get_creator_thumbnail',
            'date_added'
        )