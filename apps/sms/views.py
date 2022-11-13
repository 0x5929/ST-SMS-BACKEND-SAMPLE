from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters import rest_framework as filters

from .filters import SMSFilterStudent, SMSFilterRotation, SMSFilterProgram
from .permissions import IsAuthenticatedOfficeUserToReadOnly, IsAuthenticatedOfficeUserButCannotDelete, IsAuthenticatedOfficeStaff, IsAuthenticatedOfficeAdmin, IsSuperuser
from .models import School, Program, Rotation, Student
from .serializers import SchoolSerializer, ProgramSerializer, RotationSerializer, StudentSerializer
from .utils import FilterHandler
from .google_sheets import ExportHandler
from .data_operations import StudentDataStatistics


SCHOOL_NAMES = getattr(settings, 'SCHOOL_NAMES')


class SchoolView(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer
    permission_classes = [
        IsSuperuser | IsAuthenticatedOfficeUserToReadOnly]

    def get_queryset(self):
        return School.objects.get_query(self.request)


class ProgramView(viewsets.ModelViewSet):
    serializer_class = ProgramSerializer
    permission_classes = [
        IsSuperuser | IsAuthenticatedOfficeAdmin | IsAuthenticatedOfficeUserToReadOnly]

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SMSFilterProgram

    def get_queryset(self):
        return Program.objects.get_query(self.request)

    # to ensure query parameters are done correctly
    def list(self, request, *args, **kwargs):
        if not FilterHandler.is_valid_query_params(request.query_params, SMSFilterProgram.Meta.fields):
            return Response([])
        return super(ProgramView, self).list(request, *args, **kwargs)

class RotationView(viewsets.ModelViewSet):
    serializer_class = RotationSerializer

    permission_classes = [
        IsSuperuser | IsAuthenticatedOfficeAdmin | IsAuthenticatedOfficeStaff | IsAuthenticatedOfficeUserToReadOnly]

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SMSFilterRotation

    def get_queryset(self):
        return Rotation.objects.get_query(self.request)

    # to ensure query parameters are done correctly
    def list(self, request, *args, **kwargs):
        if not FilterHandler.is_valid_query_params(request.query_params, SMSFilterRotation.Meta.fields):
            return Response([])
        return super(RotationView, self).list(request, *args, **kwargs)


class StudentView(viewsets.ModelViewSet):
    serializer_class = StudentSerializer

    permission_classes = [
        IsSuperuser | IsAuthenticatedOfficeAdmin | IsAuthenticatedOfficeStaff | IsAuthenticatedOfficeUserButCannotDelete]

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SMSFilterStudent

    def get_queryset(self):
        return Student.objects.get_query(self.request)

    # to ensure query parameters are done correctly
    def list(self, request, *args, **kwargs):
        if not FilterHandler.is_valid_query_params(request.query_params, SMSFilterStudent.Meta.fields):
            return Response([])
        return super(StudentView, self).list(request, *args, **kwargs)


class GoogleSheetDataDumpView(APIView):
    """
    GoogleSheetDataDumpView

    Uses the most basic class based view and
    edit only field we need

    """
    permission_classes = [IsSuperuser]

    def get(self, request):
        spreadsheet_id = request.query_params.get('ssid', None)
        sheet_id = request.query_params.get('sid', None)
        school_name = request.query_params.get('school_name', None)

        try:
            if spreadsheet_id and sheet_id and school_name not in SCHOOL_NAMES:

                sheet = ExportHandler.auth_and_get_sheet(
                    spreadsheet_id, sheet_id)

                data_dump = ExportHandler.run(
                    sheet, school_name)

                return Response(data_dump.get_data(), status=status.HTTP_200_OK)
            else:
                err_data = {
                    'error': 'Invalid spreadsheet id (ssid) or sheet id (sid) or school name (school_name) in GET params.'}
                return Response(err_data, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            err_data = {
                'error':  repr(e)}

            return Response(err_data, status=status.HTTP_400_BAD_REQUEST)


class StudentStatisticsView(APIView):
    """
    StudentStatisticsView

    Uses the most basic class based view and
    edit only field we need

    """
    permission_classes = [IsSuperuser | IsAuthenticatedOfficeUserToReadOnly]

    def get(self, request):
        return Response(StudentDataStatistics.fetch_statistics(Student), status=status.HTTP_200_OK)
