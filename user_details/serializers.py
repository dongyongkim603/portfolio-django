from django.db import models
from rest_framework import serializers

from .models import UserDetails, UserPost

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = (
            'user',
            'get_user_id',
            'birthday',
            'bio',
            'profile_image',
            'thumbnail',
            'get_profile_image',
            'get_thumbnail',
            'get_first_name',
            'get_last_name',
            'get_is_superuser',
            'get_is_active',
            'get_date_joined',
            'get_email',
        )

class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPost
        fields = (
            'get_creator_thumbnail',
            'get_creator',
            'creator_details',
            'description',
            'image_url',
            'get_date_added'
        )