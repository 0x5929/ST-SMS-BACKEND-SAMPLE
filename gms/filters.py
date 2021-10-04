from django.db.models import fields
from .models import CNARotation, CNAStudent, CNATheoryRecord, CNAClinicalRecord

import django_filters


class GMSCNARotationFilter(django_filters.FilterSet):

    class Meta:
        model = CNARotation

        fields = (
            'start_date',
            'end_date',
            'rotation_num',
        )

    start_date = django_filters.DateFilter(
        field_name='start_date', lookup_expr='exact')

    end_date = django_filters.DateFilter(
        field_name='end_date', lookup_expr='exact')

    rotation_num = django_filters.NumberFilter(
        field_name='rotation_num', lookup_expr='exact')


class GMSCNAStudentFilter(django_filters.FilterSet):

    class Meta:
        model = CNAStudent

        fields = (
            'first_name',
            'last_name',
            'makeup_student',

        )

    first_name = django_filters.CharFilter(
        field_name='first_name', lookup_expr='iexact')

    last_name = django_filters.CharFilter(
        field_name='last_name', lookup_expr='iexact')

    makeup_student = django_filters.BooleanFilter(field_name='makeup_student')


class GMSCNATheoryRecordFilter(django_filters.FilterSet):

    class Meta:
        model = CNATheoryRecord

        fields = (
            'date',
            'completed',
            'topic'
        )

    date = django_filters.DateFilter(field_name='date', lookup_expr='exact')
    completed = django_filters.BooleanFilter(field_name='completed')
    topic = django_filters.CharFilter(
        field_name='topic', lookup_expr='icontains')


class GMSCNAClinicalRecordFilter(django_filters.FilterSet):

    class Meta:
        model = CNAClinicalRecord

        fields = (
            'date',
            'completed',
            'topic'
        )

    date = django_filters.DateFilter(field_name='date', lookup_expr='exact')
    completed = django_filters.BooleanFilter(field_name='completed')
    topic = django_filters.CharFilter(
        field_name='topic', lookup_expr='icontains')
