from John_portfolio.portfolio_django import user_details
from django.contrib import admin

from user_details.models import UserDetails
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

class UserDetailsInline(admin.StackedInline):
    model = UserDetails