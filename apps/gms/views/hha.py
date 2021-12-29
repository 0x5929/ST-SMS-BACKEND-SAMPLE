from rest_framework import viewsets, response
from django_filters import rest_framework as filters

from ..permissions import IsSuperuser, IsAuthenticatedHHAInstructor, IsAuthenticatedAdminInstructor, IsAuthenticatedHHAStaffInstructor
from ..models import HHARotation, HHAStudent, HHATheoryRecord, HHAClinicalRecord
from ..serializers import HHARotationSerializer, HHAStudentSerializer, HHATheoryRecordSerializer, HHAClinicalRecordSerializer
from ..filters import GMSHHARotationFilter, GMSHHAStudentFilter, GMSHHATheoryRecordFilter, GMSHHAClinicalRecordFilter
from ..utils import FilterHandler


class HHARotationView(viewsets.ModelViewSet):
    serializer_class = HHARotationSerializer
    permission_classes = [
        IsSuperuser |
        IsAuthenticatedAdminInstructor |
        IsAuthenticatedHHAStaffInstructor |
        IsAuthenticatedHHAInstructor
    ]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = GMSHHARotationFilter

    def get_queryset(self):
        return HHARotation.objects.get_query(self.request)

    # to ensure query parameters are done correctly
    def list(self, request, *args, **kwargs):
        if not FilterHandler.is_valid_query_params(request.query_params, GMSHHARotationFilter.Meta.fields):
            return response.Response([])
        return super(HHARotationView, self).list(request, *args, **kwargs)


class HHAStudentView(viewsets.ModelViewSet):
    serializer_class = HHAStudentSerializer
    permission_classes = [
        IsSuperuser |
        IsAuthenticatedAdminInstructor |
        IsAuthenticatedHHAStaffInstructor |
        IsAuthenticatedHHAInstructor
    ]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = GMSHHAStudentFilter

    def get_queryset(self):
        return HHAStudent.objects.get_query(self.request)

    # to ensure query parameters are done correctly
    def list(self, request, *args, **kwargs):
        if not FilterHandler.is_valid_query_params(request.query_params, GMSHHAStudentFilter.Meta.fields):
            return response.Response([])
        return super(HHAStudentView, self).list(request, *args, **kwargs)


class HHATheoryRecordView(viewsets.ModelViewSet):
    serializer_class = HHATheoryRecordSerializer
    permission_classes = [
        IsSuperuser |
        IsAuthenticatedAdminInstructor |
        IsAuthenticatedHHAStaffInstructor |
        IsAuthenticatedHHAInstructor
    ]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = GMSHHATheoryRecordFilter

    def get_queryset(self):
        return HHATheoryRecord.objects.get_query(self.request)

    # to ensure query parameters are done correctly
    def list(self, request, *args, **kwargs):
        if not FilterHandler.is_valid_query_params(request.query_params, GMSHHATheoryRecordFilter.Meta.fields):
            return response.Response([])
        return super(HHATheoryRecordView, self).list(request, *args, **kwargs)


class HHAClinicalRecordView(viewsets.ModelViewSet):
    serializer_class = HHAClinicalRecordSerializer
    permission_classes = [
        IsSuperuser |
        IsAuthenticatedAdminInstructor |
        IsAuthenticatedHHAStaffInstructor |
        IsAuthenticatedHHAInstructor
    ]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = GMSHHAClinicalRecordFilter

    def get_queryset(self):
        return HHAClinicalRecord.objects.get_query(self.request)

    # to ensure query parameters are done correctly
    def list(self, request, *args, **kwargs):
        if not FilterHandler.is_valid_query_params(request.query_params, GMSHHAClinicalRecordFilter.Meta.fields):
            return response.Response([])
        return super(HHAClinicalRecordView, self).list(request, *args, **kwargs)
