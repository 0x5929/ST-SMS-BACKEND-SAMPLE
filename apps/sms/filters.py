import django_filters

from django.conf import settings

from .models import Student

PROGRAM_NAMES = getattr(settings, 'PROGRAM_NAMES')


class SMSFilter(django_filters.FilterSet):
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
            'last_name',
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
