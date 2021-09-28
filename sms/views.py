from django.shortcuts import render
from rest_framework import viewsets, permissions
from django_filters import rest_framework as filters

from .filters import SMSFilter
from .models import School, Program, Rotation, Student
from .serializers import SchoolSerializer, ProgramSerializer, RotationSerializer, StudentSerializer
# Create your views here.

# note allow any is only for dev purpose, remove it after front end is built and we can properly test

# need to customize permissions for each view, only admins can have DEL, POST, PUT, PATCH priv

# NOTE NOTE NOTE : CHANGE PERMISSIONS, STAFF CAN ONLY ACCESS STUDENTS FULLY, READ ONLY FOR EVERYTHING ELSE, ONLY SUPERUSER CAN DO EVERTHING


class SchoolView(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [permissions.IsAdminUser |
                          permissions.IsAuthenticatedOrReadOnly]


class ProgramView(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [permissions.IsAdminUser |
                          permissions.IsAuthenticatedOrReadOnly]


class RotationView(viewsets.ModelViewSet):
    queryset = Rotation.objects.all()
    serializer_class = RotationSerializer
    permission_classes = [permissions.IsAdminUser |
                          permissions.IsAuthenticatedOrReadOnly]


class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SMSFilter
