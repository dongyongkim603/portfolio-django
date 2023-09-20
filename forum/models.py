from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
from django.utils.text import slugify
from user_details.models import UserDetails

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return f'/{self.slug}/'
    
class Forum(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    creator_details = models.ForeignKey(UserDetails, on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
          ordering = ('-date_added',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        super().save(*args, **kwargs)
    
    def get_creator_id(self):
        return self.creator.id

    def get_creator_name(self):
        return self.creator.username

    def get_category_id(self):
        return self.category.id

    def get_category_name(self):
        return self.category.name
    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
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

class Comment(models.Model):
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    creator_details = models.ForeignKey(UserDetails, on_delete=models.CASCADE, default=1)
    forum = models.ForeignKey(Forum, related_name='forums', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True, max_length=255)
    content = models.TextField()
    image_url = models.ImageField(upload_to='uploads/', blank=True, null=True)
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

            while Comment.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{num}"
                num += 1

            self.slug = unique_slug

        super().save(*args, **kwargs)

    def get_creator(self):
        return self.creator.username

    def get_forum_name(self):
        return f'/{self.forum.name}/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''