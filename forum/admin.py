from django.contrib import admin

from .models import Forum, Category, Comment

admin.site.register(Category)
admin.site.register(Forum)
admin.site.register(Comment)
