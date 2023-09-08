from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/uploads/<username>/filename
    return f'uploads/{instance.user.username}/{filename}'

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    thumbnail = models.ImageField(upload_to=user_directory_path, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def get_user_id(self):
        return self.user.id
    
    def get_first_name(self):
        return self.user.first_name
    
    def get_last_name(self):
        return self.user.last_name

    def get_is_superuser(self):
        return self.user.is_superuser
    
    def get_is_active(self):
        return self.user.is_active

    def get_date_joined(self):
        return self.user.date_joined
    
    def get_email(self):
        return self.user.email
    
    def get_profile_image(self):
        if self.profile_image:
            return 'http://127.0.0.1:8000' + self.profile_image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.profile_image:
                self.thumbnail = self.make_thumbnail(self.profile_image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

@receiver(post_save, sender=User)
def create_user_details(sender, instance, created, **kwargs):
    if created:
        UserDetails.objects.create(user=instance)
