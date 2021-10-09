from rest_framework import viewsets
from django_filters import rest_framework as filters

from ..permissions import IsSuperuser, IsAuthenticatedHHAInstructor
from ..models import HHARotation, HHAStudent, HHATheoryRecord, HHAClinicalRecord
from ..serializers import HHARotationSerializer, HHAStudentSerializer, HHATheoryRecordSerializer, HHAClinicalRecordSerializer
from ..filters import GMSHHARotationFilter, GMSHHAStudentFilter, GMSHHATheoryRecordFilter, GMSHHAClinicalRecordFilter


class HHARotationView(viewsets.ModelViewSet):
    serializer_class = HHARotationSerializer
    permission_classes = [IsSuperuser | IsAuthenticatedHHAInstructor]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = GMSHHARotationFilter

    def get_queryset(self):
        return HHARotation.objects.get_query(self.request)


class HHAStudentView(viewsets.ModelViewSet):
    serializer_class = HHAStudentSerializer
    permission_classes = [IsSuperuser | IsAuthenticatedHHAInstructor]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = GMSHHAStudentFilter

    def get_queryset(self):
        return HHAStudent.objects.get_query(self.request)


class HHATheoryRecordView(viewsets.ModelViewSet):
    serializer_class = HHATheoryRecordSerializer
    permission_classes = [IsSuperuser | IsAuthenticatedHHAInstructor]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = GMSHHATheoryRecordFilter

    def get_queryset(self):
        return HHATheoryRecord.objects.get_query(self.request)


class HHAClinicalRecordView(viewsets.ModelViewSet):
    serializer_class = HHAClinicalRecordSerializer
    permission_classes = [IsSuperuser | IsAuthenticatedHHAInstructor]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = GMSHHAClinicalRecordFilter

    def get_queryset(self):
        return HHAClinicalRecord.objects.get_query(self.request)
