from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Client, Note


class ModelAdminClientConfig(ModelAdmin):
    readonly_fields = ('client_uuid', 'initial_contact')
    search_fields = ('school_name', 'client_uuid', 'first_name',
                     'last_name', 'phone_number', 'email', 'city', 'success')
    list_filter = ('school_name', 'client_uuid', 'first_name',
                   'last_name', 'phone_number', 'email', 'city', 'success')
    ordering = ('-initial_contact',)
    list_display = ('school_name', 'client_uuid', 'first_name',
                    'last_name', 'phone_number', 'email', 'city', 'success')

    fieldsets = (
        (None, {'fields': ('school_name', 'first_name',
                           'last_name', 'phone_number', 'email', 'city', 'recruit_emails', 'success')
                }
         ),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name',
                       'last_name', 'phone_number', 'email', 'city', 'recruit_emails', 'success')
        }

        ),
    )

    # needed for admin site to work properly
    # original error states it was missing filter_horizontal[0] and [1], which was groups and user_permissions respectively
    filter_horizontal = ()


class ModelAdminNoteConfig(ModelAdmin):
    readonly_fields = ('note_uuid', 'date')
    search_fields = ('client', 'note_uuid', 'date',
                     'product', 'content', )
    list_filter = ('client', 'note_uuid', 'date',
                   'product', 'price', 'content', )
    ordering = ('-date',)
    list_display = ('client', 'note_uuid', 'date',
                    'product', 'price', 'content', )

    fieldsets = (
        (None, {'fields': ('client', 'product', 'price', 'content', )
                }
         ),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('client', 'product', 'price', 'content', )
        }

        ),
    )

    # needed for admin site to work properly
    # original error states it was missing filter_horizontal[0] and [1], which was groups and user_permissions respectively
    filter_horizontal = ()


admin.site.register(Client, ModelAdminClientConfig)
admin.site.register(Note, ModelAdminNoteConfig)
