from django.db import models
from rest_framework import serializers

from .models import UserDetails

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = (
            'user_id',
            'age',
            'get_image',
            'get_thumbnail'
        )