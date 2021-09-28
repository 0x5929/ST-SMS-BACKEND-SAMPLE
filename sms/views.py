from django.shortcuts import render
from rest_framework import viewsets, permissions
from django_filters import rest_framework as filters

from .filters import SMSFilter
from .permissions import IsAuthenticatedToReadOnly, IsSuperuser
from .models import School, Program, Rotation, Student
from .serializers import SchoolSerializer, ProgramSerializer, RotationSerializer, StudentSerializer


# NOTE NOTE NOTE : CHANGE PERMISSIONS, STAFF CAN ONLY ACCESS STUDENTS FULLY, READ ONLY FOR EVERYTHING ELSE, ONLY SUPERUSER CAN DO EVERTHING


class SchoolView(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [IsSuperuser | IsAuthenticatedToReadOnly]


class ProgramView(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [IsSuperuser | IsAuthenticatedToReadOnly]


class RotationView(viewsets.ModelViewSet):
    queryset = Rotation.objects.all()
    serializer_class = RotationSerializer
    permission_classes = [permissions.IsAdminUser | IsAuthenticatedToReadOnly]


class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    permission_classes = [permissions.IsAdminUser | IsAuthenticatedToReadOnly]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SMSFilter
