from django.db import models
from rest_framework import serializers

from .models import UserDetails

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = (
            'id',
            'name',
            'slug',
            'get_absolute_url',
        )