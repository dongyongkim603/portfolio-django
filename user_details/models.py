from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.text import Truncator
from django.utils.text import slugify

def user_directory_path(instance, filename):
    return f'uploads/{instance.user.username}/{filename}'

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    birthday = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, unique=False, null=True,)
    profile_image = models.URLField(blank=True, unique=False, null=True, max_length=2000)
    thumbnail = models.URLField(blank=True, unique=False, null=True, max_length=2000)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

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
            return self.profile_image
        return ''

    def get_thumbnail(self):
        return self.thumbnail
        # if self.thumbnail:
        #     return 'http://127.0.0.1:8000' + self.thumbnail.url
        # else:
        #     if self.profile_image:
        #         self.thumbnail = self.make_thumbnail(self.profile_image)
        #         self.save()

        #         return 'http://127.0.0.1:8000' + self.thumbnail.url
        #     else:
        #         return ''
    
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

class UserPost(models.Model):
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    creator_details = models.ForeignKey(UserDetails, on_delete=models.CASCADE, default=1)
    slug = models.SlugField(unique=True, blank=True, max_length=255)
    description = models.TextField(blank=True, unique=False, null=True,)
    image_url = models.URLField(blank=True, unique=False, null=True, max_length=2000)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
          ordering = ('-date_added',)

    def get_creator_thumbnail(self):
        return self.creator_details.get_thumbnail()
    
    def generate_slug(self):
        truncated_content = Truncator(self.content).chars(20)
        slug_text = f"{self.id}-{self.creator.username}-{slugify(truncated_content)}"
        return slug_text

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.creator.username)
            unique_slug = base_slug
            num = 1

            while UserPost.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{num}"
                num += 1

            self.slug = unique_slug

        super().save(*args, **kwargs)

    def get_creator(self):
        return self.creator.username