
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
                   'last_name', 'makeup_student',)
    ordering = ('-last_name',)
    list_display = ('student_uuid', 'first_name',
                    'last_name', 'makeup_student',)

    fieldsets = (
        (None, {'fields': ('student_uuid', 'first_name',
                           'last_name', 'makeup_student',)
                }
         ),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('student_uuid', 'first_name',
                       'last_name', 'makeup_student',)
        }

        ),
    )

    # needed for admin site to work properly
    # original error states it was missing filter_horizontal[0] and [1], which was groups and user_permissions respectively
    filter_horizontal = ()


class ModelAdminCNATheoryRecordConfig(ModelAdmin):
    readonly_fields = ('cna_theory_record_uuid',)
    search_fields = ('cna_theory_record_uuid', 'date',
                     'hours_spent', 'completed', 'test_score', 'topic')
    list_filter = ('cna_theory_record_uuid', 'date',
                   'hours_spent', 'completed', 'test_score', 'topic')
    ordering = ('-date',)
    list_display = ('cna_theory_record_uuid', 'date',
                    'hours_spent', 'completed', 'test_score', 'topic')

    fieldsets = (
        (None, {'fields': ('cna_theory_record_uuid', 'date',
                           'hours_spent', 'completed', 'test_score', 'topic')
                }
         ),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('cna_theory_record_uuid', 'date',
                       'hours_spent', 'completed', 'test_score', 'topic')
        }

        ),
    )

    # needed for admin site to work properly
    # original error states it was missing filter_horizontal[0] and [1], which was groups and user_permissions respectively
    filter_horizontal = ()


class ModelAdminCNAClinicalRecordConfig(ModelAdmin):
    readonly_fields = ('cna_clinical_record_uuid',)
    search_fields = ('cna_clinical_record_uuid', 'date',
                     'completed', 'performance_satisfied', 'topic')
    list_filter = ('cna_clinical_record_uuid', 'date',
                   'completed', 'performance_satisfied', 'topic')
    ordering = ('-date',)
    list_display = ('cna_clinical_record_uuid', 'date',
                    'completed', 'performance_satisfied', 'comments', 'topic')

    fieldsets = (
        (None, {'fields': ('cna_clinical_record_uuid', 'date',
                           'completed', 'performance_satisfied', 'comments', 'topic')
                }
         ),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('cna_clinical_record_uuid', 'date',
                       'completed', 'performance_satisfied', 'comments', 'topic')
        }

        ),
    )

    # needed for admin site to work properly
    # original error states it was missing filter_horizontal[0] and [1], which was groups and user_permissions respectively
    filter_horizontal = ()
