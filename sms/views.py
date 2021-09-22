from django.shortcuts import render
from rest_framework import viewsets, permissions

from .permissions import IsSuperuserOrAuthenticatedReadOnly
from .models import School, Program, Rotation, Student
from .serializers import SchoolSerializer, ProgramSerializer, RotationSerializer, StudentSerializer
# Create your views here.

# note allow any is only for dev purpose, remove it after front end is built and we can properly test

# need to customize permissions for each view, only admins can have DEL, POST, PUT, PATCH priv


class SchoolView(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [permissions.AllowAny |
                          IsSuperuserOrAuthenticatedReadOnly]


class ProgramView(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [permissions.AllowAny |
                          IsSuperuserOrAuthenticatedReadOnly]


class RotationView(viewsets.ModelViewSet):
    queryset = Rotation.objects.all()
    serializer_class = RotationSerializer
    permission_classes = [permissions.AllowAny |
                          IsSuperuserOrAuthenticatedReadOnly]


class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny |
                          IsSuperuserOrAuthenticatedReadOnly]
