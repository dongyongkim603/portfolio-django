# from John_portfolio.portfolio_django import user_details
from django.contrib import admin

from .models import UserDetails
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

class UserDetailsInline(admin.StackedInline):
    model = UserDetails
    can_delete = False

class AccountsUserAdmin(AuthUserAdmin):
    inlines = [UserDetailsInline]

admin.site.unregister(User)
admin.site.register(User, AccountsUserAdmin)