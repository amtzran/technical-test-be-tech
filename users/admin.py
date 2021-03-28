"""User admin classes."""

# Django
from django.contrib import admin

# Models
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """User admin."""

    list_display = ('pk', 'username', 'email',)
    list_display_links = ('pk', 'username', 'email',)

    search_fields = (
        'email',
        'username',
        'name',
        'phone',
        'gender',
    )

    list_filter = (
        'is_active',
        'is_staff',
        'created_at',
        'updated_at',
    )

    readonly_fields = ('created_at', 'updated_at',)
