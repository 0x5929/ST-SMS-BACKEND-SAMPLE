
from django.contrib.admin import ModelAdmin

# Register your models here.


class ModelAdminCNARotationConfig(ModelAdmin):
    readonly_fields = ('rotation_uuid',)
    search_fields = ('rotation_uuid', 'school_name',
                     'start_date', 'end_date', 'instructor_email',)
    list_filter = ('rotation_uuid', 'school_name',
                   'start_date', 'end_date', 'instructor_email',)
    ordering = ('-start_date',)
    list_display = ('rotation_uuid', 'school_name',
                    'start_date', 'end_date', 'instructor_email', 'rotation_num', 'instructor_title', 'clinical_site')

    fieldsets = (
        (None, {'fields': ('rotation_uuid', 'school_name',
                           'start_date', 'end_date', 'instructor_email', 'rotation_num', 'instructor_title', 'clinical_site')
                }
         ),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('rotation_uuid', 'school_name',
                       'start_date', 'end_date', 'instructor_email', 'rotation_num', 'instructor_title', 'clinical_site')
        }

        ),
    )

    # needed for admin site to work properly
    # original error states it was missing filter_horizontal[0] and [1], which was groups and user_permissions respectively
    filter_horizontal = ()


class ModelAdminCNAStudentConfig(ModelAdmin):
    readonly_fields = ('student_uuid',)
    search_fields = ('student_uuid', 'first_name',
                     'last_name', 'makeup_student',)
    list_filter = ('student_uuid', 'first_name',
                   'last_name', 'rotation', 'makeup_student',)
    ordering = ('-last_name',)
    list_display = ('student_uuid', 'first_name',
                    'last_name', 'rotation', 'makeup_student',)

    fieldsets = (
        (None, {'fields': ('student_uuid', 'first_name',
                           'last_name', 'rotation', 'makeup_student',)
                }
         ),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('student_uuid', 'first_name',
                       'last_name', 'rotation', 'makeup_student',)
        }

        ),
    )

    # needed for admin site to work properly
    # original error states it was missing filter_horizontal[0] and [1], which was groups and user_permissions respectively
    filter_horizontal = ()


class ModelAdminCNATheoryRecordConfig(ModelAdmin):
    readonly_fields = ('record_uuid',)
    search_fields = ('record_uuid', 'date',
                     'hours_spent', 'completed', 'test_score', 'topic', 'student')
    list_filter = ('record_uuid', 'date',
                   'hours_spent', 'completed', 'test_score', 'topic', 'student')
    ordering = ('-date',)
    list_display = ('record_uuid', 'date',
                    'hours_spent', 'completed', 'test_score', 'topic', 'student')

    fieldsets = (
        (None, {'fields': ('record_uuid', 'date',
                           'hours_spent', 'completed', 'test_score', 'topic', 'student')
                }
         ),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('record_uuid', 'date',
                       'hours_spent', 'completed', 'test_score', 'topic', 'student')
        }

        ),
    )

    # needed for admin site to work properly
    # original error states it was missing filter_horizontal[0] and [1], which was groups and user_permissions respectively
    filter_horizontal = ()


class ModelAdminCNAClinicalRecordConfig(ModelAdmin):
    readonly_fields = ('record_uuid',)
    search_fields = ('cna_clinical_record_uuid', 'date',
                     'completed', 'performance_satisfied', 'topic', 'student')
    list_filter = ('record_uuid', 'date',
                   'completed', 'performance_satisfied', 'topic', 'student')
    ordering = ('-date',)
    list_display = ('record_uuid', 'date',
                    'completed', 'performance_satisfied', 'comments', 'topic', 'student')

    fieldsets = (
        (None, {'fields': ('record_uuid', 'date',
                           'completed', 'performance_satisfied', 'comments', 'topic', 'student')
                }
         ),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('record_uuid', 'date',
                       'completed', 'performance_satisfied', 'comments', 'topic', 'student')
        }

        ),
    )

    # needed for admin site to work properly
    # original error states it was missing filter_horizontal[0] and [1], which was groups and user_permissions respectively
    filter_horizontal = ()
