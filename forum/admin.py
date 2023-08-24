from django.contrib import admin

from .models import Forum, Category

admin.site.register(Category)
admin.site.register(Forum)
