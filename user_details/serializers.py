from django.db import models
from rest_framework import serializers

from .models import UserDetails

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = (
            'get_user_id',
            'age',
            'bio',
            'get_profile_image',
            'get_thumbnail',
            'get_first_name',
            'get_last_name',
            'get_is_superuser',
            'get_is_active',
            'get_date_joined',
            'get_email'
        )