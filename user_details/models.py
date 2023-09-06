from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import post_save

class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_details(sender, instance, created, **kwargs):
    if created:
        UserDetails.objects.create(user=instance)
