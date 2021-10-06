
from django.contrib.admin import ModelAdmin


class ModelAdminHHARotationConfig(ModelAdmin):
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


class ModelAdminHHAStudentConfig(ModelAdmin):
    readonly_fields = ('student_uuid',)
    search_fields = ('student_uuid', 'first_name',
                     'last_name', 'makeup_student',)
    list_filter = ('student_uuid', 'first_name',
                   'last_name', 'makeup_student',)
    ordering = ('-last_name',)
    list_display = ('student_uuid', 'first_name',
                    'last_name', 'rotation',  'makeup_student',)

    fieldsets = (
        (None, {'fields': ('student_uuid', 'first_name',
                           'last_name', 'rotation',  'makeup_student',)
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


class ModelAdminHHATheoryRecordConfig(ModelAdmin):
    readonly_fields = ('hha_theory_record_uuid',)
    search_fields = ('hha_theory_record_uuid', 'date',
                     'completed', 'test_score', 'topic', 'student')
    list_filter = ('hha_theory_record_uuid', 'date',
                   'completed', 'test_score', 'topic', 'student')
    ordering = ('-date',)
    list_display = ('hha_theory_record_uuid', 'date',
                    'completed', 'hours_spent', 'start_time', 'end_time', 'test_score', 'topic', 'student')

    fieldsets = (
        (None, {'fields': ('hha_theory_record_uuid', 'date',
                           'completed', 'hours_spent', 'start_time', 'end_time', 'test_score', 'topic', 'student')
                }
         ),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('hha_theory_record_uuid', 'date',
                       'completed',  'hours_spent', 'start_time', 'end_time', 'test_score', 'topic', 'student')
        }

        ),
    )

    # needed for admin site to work properly
    # original error states it was missing filter_horizontal[0] and [1], which was groups and user_permissions respectively
    filter_horizontal = ()


class ModelAdminHHAClinicalRecordConfig(ModelAdmin):
    readonly_fields = ('hha_clinical_record_uuid',)
    search_fields = ('hha_clinical_record_uuid', 'date',
                     'completed', 'performance_satisfied', 'topic', 'student')
    list_filter = ('hha_clinical_record_uuid', 'date',
                   'completed', 'performance_satisfied', 'topic', 'student')
    ordering = ('-date',)
    list_display = ('hha_clinical_record_uuid', 'date',
                    'completed', 'hours_spent', 'comments', 'performance_satisfied', 'start_time', 'end_time', 'start_date', 'end_date', 'topic', 'student')

    fieldsets = (
        (None, {'fields': ('hha_clinical_record_uuid', 'date',
                           'completed', 'hours_spent', 'comments', 'performance_satisfied', 'start_time', 'end_time', 'start_date', 'end_date', 'topic', 'student')
                }
         ),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('hha_clinical_record_uuid', 'date',
                       'completed', 'hours_spent', 'comments', 'performance_satisfied', 'start_time', 'end_time', 'start_date', 'end_date', 'topic', 'student')
        }

        ),
    )

    # needed for admin site to work properly
    # original error states it was missing filter_horizontal[0] and [1], which was groups and user_permissions respectively
    filter_horizontal = ()
