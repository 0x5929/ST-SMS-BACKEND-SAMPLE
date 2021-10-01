from .models import Note, Client

import django_filters


class CMSNoteFilter(django_filters.FilterSet):

    class Meta:
        model = Note

        fields = (
            'date',
            'content',
        )

    date = django_filters.DateFilter(field_name='date', lookup_expr='exact')

    content = django_filters.CharFilter(
        field_name='content', lookup_expr='icontains')


class CMSClientFilter(django_filters.FilterSet):
    class Meta:
        model = Client

        fields = (
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'city',
            'success',
            'initial_contact',
        )

    first_name = django_filters.CharFilter(
        field_name='first_name', lookup_expr='iexact')

    cfirst_name = django_filters.CharFilter(
        field_name='first_name', lookup_expr='icontains')

    last_name = django_filters.CharFilter(
        field_name='last_name', lookup_expr='iexact')

    clast_name = django_filters.CharFilter(
        field_name='last_name', lookup_expr='icontains')

    phone_number = django_filters.CharFilter(
        field_name='phone_number', lookup_expr='exact')

    email = django_filters.CharFilter(
        field_name='email', lookup_expr='iexact')

    city = django_filters.CharFilter(
        field_name='city', lookup_expr='iexact')

    success = django_filters.BooleanFilter(field_name='success')

    initial_contact_date = django_filters.DateFilter(
        field_name='initial_contact', lookup_expr='exact')
