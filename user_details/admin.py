# from John_portfolio.portfolio_django import user_details
from django.contrib import admin

from .models import UserDetails, UserPost
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

class UserDetailsInline(admin.StackedInline):
    model = UserDetails
    can_delete = False

class UserPostInline(admin.StackedInline):
    model = UserPost
    can_delete = True

class AccountsUserAdmin(AuthUserAdmin):
    def add_view(self, *args, **kwargs):
        self.inlines = []
        return super(AccountsUserAdmin, self).add_view(*args, **kwargs)
    
    def change_view(self, *args, **kwargs):
        self.inlines = [
            UserDetailsInline,
            UserPostInline
        ]
        return super(AccountsUserAdmin, self).change_view(*args, **kwargs)

    inlines = [
        UserDetailsInline,
        UserPostInline
    ]

admin.site.unregister(User)
admin.site.register(User, AccountsUserAdmin)