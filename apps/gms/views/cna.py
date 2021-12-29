from rest_framework import viewsets, response
from django_filters import rest_framework as filters

from ..permissions import IsSuperuser, IsAuthenticatedCNAInstructor, IsAuthenticatedAdminInstructor, IsAuthenticatedCNAStaffInstructor
from ..models import CNARotation, CNAStudent, CNATheoryRecord, CNAClinicalRecord
from ..serializers import CNARotationSerializer, CNAStudentSerializer, CNATheoryRecordSerializer, CNAClinicalRecordSerializer
from ..filters import GMSCNARotationFilter, GMSCNAStudentFilter, GMSCNATheoryRecordFilter, GMSCNAClinicalRecordFilter
from ..utils import FilterHandler


class CNARotationView(viewsets.ModelViewSet):
    serializer_class = CNARotationSerializer
    permission_classes = [
        IsSuperuser |
        IsAuthenticatedAdminInstructor |
        IsAuthenticatedCNAStaffInstructor |
        IsAuthenticatedCNAInstructor
    ]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = GMSCNARotationFilter

    def get_queryset(self):
        return CNARotation.objects.get_query(self.request)

    # to ensure query parameters are done correctly
    def list(self, request, *args, **kwargs):
        if not FilterHandler.is_valid_query_params(request.query_params, GMSCNARotationFilter.Meta.fields):
            return response.Response([])
        return super(CNARotationView, self).list(request, *args, **kwargs)


class CNAStudentView(viewsets.ModelViewSet):
    serializer_class = CNAStudentSerializer
    permission_classes = [
        IsSuperuser |
        IsAuthenticatedAdminInstructor |
        IsAuthenticatedCNAStaffInstructor |
        IsAuthenticatedCNAInstructor
    ]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = GMSCNAStudentFilter

    def get_queryset(self):
        return CNAStudent.objects.get_query(self.request)

    # to ensure query parameters are done correctly
    def list(self, request, *args, **kwargs):
        if not FilterHandler.is_valid_query_params(request.query_params, GMSCNAStudentFilter.Meta.fields):
            return response.Response([])
        return super(CNAStudentView, self).list(request, *args, **kwargs)


class CNATheoryRecordView(viewsets.ModelViewSet):
    serializer_class = CNATheoryRecordSerializer
    permission_classes = [
        IsSuperuser |
        IsAuthenticatedAdminInstructor |
        IsAuthenticatedCNAStaffInstructor |
        IsAuthenticatedCNAInstructor
    ]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = GMSCNATheoryRecordFilter

    def get_queryset(self):
        return CNATheoryRecord.objects.get_query(self.request)

    # to ensure query parameters are done correctly
    def list(self, request, *args, **kwargs):
        if not FilterHandler.is_valid_query_params(request.query_params, GMSCNATheoryRecordFilter.Meta.fields):
            return response.Response([])
        return super(CNATheoryRecordView, self).list(request, *args, **kwargs)


class CNAClinicalRecordView(viewsets.ModelViewSet):
    serializer_class = CNAClinicalRecordSerializer
    permission_classes = [
        IsSuperuser |
        IsAuthenticatedAdminInstructor |
        IsAuthenticatedCNAStaffInstructor |
        IsAuthenticatedCNAInstructor
    ]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = GMSCNAClinicalRecordFilter

    def get_queryset(self):
        return CNAClinicalRecord.objects.get_query(self.request)

    # to ensure query parameters are done correctly
    def list(self, request, *args, **kwargs):
        if not FilterHandler.is_valid_query_params(request.query_params, GMSCNAClinicalRecordFilter.Meta.fields):
            return response.Response([])
        return super(CNAClinicalRecordView, self).list(request, *args, **kwargs)
