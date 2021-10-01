from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Client, Note


class ModelAdminClientConfig(ModelAdmin):
    readonly_fields = ('client_uuid', 'initial_contact')
    search_fields = ('client_uuid', 'first_name',
                     'last_name', 'phone_number', 'email', 'city', 'success')
    list_filter = ('client_uuid', 'first_name',
                   'last_name', 'phone_number', 'email', 'city', 'success')
    ordering = ('-initial_contact',)
    list_display = ('client_uuid', 'first_name',
                    'last_name', 'phone_number', 'email', 'city', 'success')

    fieldsets = (
        (None, {'fields': ('first_name',
                           'last_name', 'phone_number', 'email', 'city', 'success')
                }
         ),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name',
                       'last_name', 'phone_number', 'email', 'city', 'success')
        }

        ),
    )

    # needed for admin site to work properly
    # original error states it was missing filter_horizontal[0] and [1], which was groups and user_permissions respectively
    filter_horizontal = ()


class ModelAdminNoteConfig(ModelAdmin):
    readonly_fields = ('note_uuid', 'date')
    search_fields = ('note_uuid', 'date',
                     'product', 'content', )
    list_filter = ('note_uuid', 'date',
                   'product', 'price', 'content', )
    ordering = ('-date',)
    list_display = ('note_uuid', 'date',
                    'product', 'price', 'content', )

    fieldsets = (
        (None, {'fields': ('product', 'price', 'content', )
                }
         ),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('product', 'price', 'content', )
        }

        ),
    )

    # needed for admin site to work properly
    # original error states it was missing filter_horizontal[0] and [1], which was groups and user_permissions respectively
    filter_horizontal = ()


admin.site.register(Client, ModelAdminClientConfig)
admin.site.register(Note, ModelAdminNoteConfig)
