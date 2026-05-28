from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
class CustomUserAdmin(UserAdmin):

    list_display = ('email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')

    # Custom Config
    ordering = ('email',)
    fieldsets =(
        (None,{'fields':('email', 'password')}),
        ('Permissions', {'fields':('role', 'is_active', 'is_staff', 'is_superuser')}),
    )

    add_fields = (
        (None, {
            'classes': ('toggle',),
            'fields': ('email', 'role', 'password'),
        }),
    )
    search_fields = ('email',)

# Connecting to interfaces
admin.site.register(User, CustomUserAdmin)