from rest_framework import viewsets
from django_filters import rest_framework as filters

from ..permissions import IsSuperuser, IsAuthenticatedCNAInstructor
from ..models import CNARotation, CNAStudent, CNATheoryRecord, CNAClinicalRecord
from ..serializers import CNARotationSerializer, CNAStudentSerializer, CNATheoryRecordSerializer, CNAClinicalRecordSerializer
from ..filters import GMSCNARotationFilter, GMSCNAStudentFilter, GMSCNATheoryRecordFilter, GMSCNAClinicalRecordFilter


class CNARotationView(viewsets.ModelViewSet):
    serializers = CNARotationSerializer
    permission_classes = [IsSuperuser | IsAuthenticatedCNAInstructor]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = GMSCNARotationFilter

    def get_queryset(self):
        return CNARotation.objects.get_query(self.request)


class CNAStudentView(viewsets.ModelViewSet):
    serializers = CNAStudentSerializer
    permission_classes = [IsSuperuser | IsAuthenticatedCNAInstructor]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = GMSCNAStudentFilter

    def get_queryset(self):
        return CNAStudent.objects.get_query(self.request)


class CNATheoryRecordView(viewsets.ModelViewSet):
    serializers = CNATheoryRecordSerializer
    permission_classes = [IsSuperuser | IsAuthenticatedCNAInstructor]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = GMSCNATheoryRecordFilter

    def get_queryset(self):
        return CNATheoryRecord.objects.get_query(self.request)


class CNAClinicalRecordView(viewsets.ModelViewSet):
    serializers = CNAClinicalRecordSerializer
    permission_classes = [IsSuperuser | IsAuthenticatedCNAInstructor]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = GMSCNAClinicalRecordFilter

    def get_queryset(self):
        return CNAClinicalRecord.objects.get_query(self.request)
