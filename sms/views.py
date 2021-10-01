from rest_framework import viewsets
from django_filters import rest_framework as filters

from .filters import SMSFilter
from .permissions import IsAuthenticatedOfficeAdmin, IsAuthenticatedOfficeUserToReadOnly, IsSuperuser
from .models import School, Program, Rotation, Student
from .serializers import SchoolSerializer, ProgramSerializer, RotationSerializer, StudentSerializer


class SchoolView(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [IsSuperuser | IsAuthenticatedOfficeUserToReadOnly]


class ProgramView(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [IsSuperuser | IsAuthenticatedOfficeUserToReadOnly]


class RotationView(viewsets.ModelViewSet):
    queryset = Rotation.objects.all()
    serializer_class = RotationSerializer
    permission_classes = [IsAuthenticatedOfficeAdmin |
                          IsAuthenticatedOfficeUserToReadOnly]


class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    permission_classes = [IsAuthenticatedOfficeAdmin |
                          IsAuthenticatedOfficeUserToReadOnly]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SMSFilter
