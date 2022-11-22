import django_filters

from django.conf import settings

from .models import Program, Rotation, Student

PROGRAM_NAMES = getattr(settings, 'PROGRAM_NAMES')
SCHOOL_NAMES = getattr(settings, 'SCHOOL_NAMES')

class SMSFilterStudent(django_filters.FilterSet):
    strict = True
    # for any new filters, please add within fields and declare explicit below as well

    class Meta:
        model = Student
        fields = (
            'rotation__program__school__school_name',
            'rotation__program__program_name',
            'rotation__rotation_number',
            'student_id',
            'first_name',
            'cfirst_name',
            'last_name',
            'clast_name',
            'phone_number',
            'email',
            'start_date',
            'completion_date',
            'date_enrollment_agreement_signed',
            'paid',
            'employed',
            'graduated',
            'passed_first_exam',
            'passed_second_or_third_exam',
            'google_sheet_migrated'
        )

    school = django_filters.CharFilter(
        field_name='rotation__program__school__school_name',
        lookup_expr='exact')

    program = django_filters.ChoiceFilter(
        field_name='rotation__program__program_name',
        lookup_expr='exact',
        choices=PROGRAM_NAMES)

    rotation = django_filters.NumberFilter(
        field_name='rotation__rotation_number',
        lookup_expr='exact')

    student_id = django_filters.CharFilter(
        field_name='student_id',
        lookup_expr='iexact')

    first_name = django_filters.CharFilter(
        field_name='first_name',
        lookup_expr='iexact')

    cfirst_name = django_filters.CharFilter(
        field_name='first_name', lookup_expr='icontains'
    )

    last_name = django_filters.CharFilter(
        field_name='last_name',
        lookup_expr='iexact')

    clast_name = django_filters.CharFilter(
        field_name='last_name', lookup_expr='icontains'
    )

    phone_number = django_filters.CharFilter(
        field_name='phone_number',
        lookup_expr='exact')

    email = django_filters.CharFilter(
        field_name='email',
        lookup_expr='iexact')

    start_date = django_filters.DateFilter(
        field_name='start_date',
        lookup_expr='exact')

    completion_date = django_filters.DateFilter(
        field_name='completion_date',
        lookup_expr='exact')

    date_enrollment_agreement_signed = django_filters.DateFilter(
        field_name='date_enrollment_agreement_signed',
        lookup_expr='exact')

    paid = django_filters.BooleanFilter(field_name='paid')

    employed = django_filters.BooleanFilter(field_name='employed')

    graduated = django_filters.BooleanFilter(field_name='graduated')

    passed_first_exam = django_filters.BooleanFilter(
        field_name='passed_first_exam')

    passed_second_or_third_exam = django_filters.BooleanFilter(
        field_name='passed_second_or_third_exam')

    google_sheet_migrated = django_filters.BooleanFilter(
        field_name='google_sheet_migrated')


# this was added later, we could change SMSFIlter to SMSFilterStudent, but not super important atm.
class SMSFilterRotation(django_filters.FilterSet):
    strict = True
    # for any new filters, please add within fields and declare explicit below as well

    class Meta:
        model = Rotation
        fields = (
            'rotation_number',
            'program__program_name',
            'program__school__school_name'
        )

    rotation = django_filters.CharFilter(
        field_name='rotation_number',
        lookup_expr='exact')

    program = django_filters.ChoiceFilter(
        field_name='program__program_name',
        lookup_expr='exact',
        choices=PROGRAM_NAMES)
    
    school = django_filters.ChoiceFilter(
        field_name='program__school__school_name',
        lookup_expr='exact',
        choices=SCHOOL_NAMES)


class SMSFilterProgram(django_filters.FilterSet):
    strict = True

    # for any new filters, please add within fields and declare explicit below as well
    class Meta: 
        model = Program
        fields = (
            'school__school_name',
        )

    
    school = django_filters.ChoiceFilter(
        field_name='school__school_name',
        lookup_expr='exact',
        choices=SCHOOL_NAMES)