from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAdminConfig(UserAdmin):
    search_fields = ('email', 'username', 'first_name',
                     'last_name')
    list_filter = ('email', 'username', 'first_name',
                   'last_name')
    ordering = ('-date_joined',)

    list_display = ('email', 'username', 'first_name', 'last_name',
                    'phone_number', 'is_active', 'is_office', 'is_recruit', 'is_instructor', 'is_staff', 'is_admin', 'is_superuser')

    fieldsets = (
        (None, {'fields': ('username', 'first_name', 'last_name', 'password',)}),
        ('Permissions', {
         'fields': ('programs', 'is_active', 'is_office', 'is_recruit', 'is_instructor', 'is_staff',  'is_admin', 'is_superuser')}),
        ('Personal', {'fields': ('phone_number', 'email',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'last_name', 'password1', 'password2', 'programs', 'is_office', 'is_recruit', 'is_instructor', 'is_staff', 'is_admin', 'is_superuser', )
        }

        ),
    )

    # needed for admin site to work properly
    # original error states it was missing filter_horizontal[0] and [1], which was groups and user_permissions respectively
    filter_horizontal = ()


admin.site.register(Account, AccountAdminConfig)
