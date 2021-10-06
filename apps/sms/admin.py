from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import School, Program, Rotation, Student


class ModelAdminSchoolConfig(ModelAdmin):

    readonly_fields = ('school_uuid',)
    search_fields = ('school_uuid', 'school_name',
                     'school_code', 'year_founded',)
    list_filter = ('school_uuid', 'school_name',
                   'school_code', 'year_founded',)
    ordering = ('-year_founded',)
    list_display = ('school_uuid', 'school_name',
                    'school_code', 'school_address', 'year_founded',)

    fieldsets = (
        (None, {'fields': ('school_uuid', 'school_name',
                           'school_code', 'school_address', 'year_founded',)
                }
         ),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('school_uuid', 'school_name',
                       'school_code', 'school_address', 'year_founded',)
        }

        ),
    )

    # needed for admin site to work properly
    # original error states it was missing filter_horizontal[0] and [1], which was groups and user_permissions respectively
    filter_horizontal = ()


class ModelAdminProgramConfig(ModelAdmin):

    readonly_fields = ('program_uuid',)
    search_fields = ('program_uuid', 'program_name',)
    list_filter = ('program_uuid', 'program_name',)
    ordering = ()
    list_display = ('school', 'program_uuid', 'program_name',
                    'approval_entities',)

    fieldsets = (
        (None, {'fields': ('school', 'program_uuid', 'program_name',
                           'approval_entities',)
                }
         ),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('school', 'program_uuid', 'program_name',
                       'approval_entities',)
        }

        ),
    )

    # needed for admin site to work properly
    # original error states it was missing filter_horizontal[0] and [1], which was groups and user_permissions respectively
    filter_horizontal = ()


class ModelAdminRotationConfig(ModelAdmin):
    readonly_fields = ('rotation_uuid',)
    search_fields = ('rotation_uuid', 'rotation_number',)
    list_filter = ('program', 'rotation_uuid', 'rotation_number',)
    ordering = ('-rotation_number',)
    list_display = ('rotation_uuid', 'rotation_number',)

    fieldsets = (
        (None, {'fields': ('program', 'rotation_uuid', 'rotation_number',)
                }
         ),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('program', 'rotation_uuid', 'rotation_number',)
        }

        ),
    )

    # needed for admin site to work properly
    # original error states it was missing filter_horizontal[0] and [1], which was groups and user_permissions respectively
    filter_horizontal = ()


class ModelAdminStudentConfig(ModelAdmin):
    all_fields = ('rotation', 'student_uuid', 'student_id', 'first_name', 'last_name', 'phone_number',
                  'email', 'mailing_address', 'course', 'start_date', 'completion_date',
                  'date_enrollment_agreement_signed', 'third_party_payer_info', 'course_cost',
                  'total_charges_charged', 'total_charges_paid', 'graduated', 'passed_first_exam',
                  'passed_second_or_third_exam', 'employed', 'place_of_employment', 'employment_address',
                  'position', 'starting_wage', 'hours_worked_weekly', 'description_of_attempts_to_contact_student', 'paid',)

    readonly_fields = ('student_uuid', 'paid',)
    search_fields = ('student_uuid', 'student_id', 'first_name', 'last_name', 'phone_number',
                     'email', 'course', 'start_date', 'completion_date', 'third_party_payer_info',
                     'graduated', 'passed_first_exam', 'passed_second_or_third_exam', 'employed',)
    list_filter = ('rotation', 'student_uuid', 'student_id', 'first_name', 'last_name', 'phone_number',
                   'email', 'course', 'start_date', 'completion_date', 'third_party_payer_info',
                   'graduated', 'passed_first_exam', 'passed_second_or_third_exam', 'employed', 'paid',)
    ordering = ('-start_date',)
    list_display = all_fields
    fieldsets = (
        (None, {'fields': all_fields
                }
         ),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': all_fields
        }

        ),
    )

    # needed for admin site to work properly
    # original error states it was missing filter_horizontal[0] and [1], which was groups and user_permissions respectively
    filter_horizontal = ()


admin.site.register(School, ModelAdminSchoolConfig)
admin.site.register(Program, ModelAdminProgramConfig)
admin.site.register(Rotation, ModelAdminRotationConfig)
admin.site.register(Student, ModelAdminStudentConfig)
