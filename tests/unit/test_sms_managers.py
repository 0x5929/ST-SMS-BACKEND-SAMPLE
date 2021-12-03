import pytest
from django.db import models

from sms.managers import SchoolManager, ProgramManager, RotationManager, StudentManager


class User:
    def __init__(self, superuser=False):
        self.is_superuser = superuser
        self.school_name = 'STI'


class Request:
    def __init__(self, superuser=False):
        self.user = User(superuser=superuser)


@pytest.mark.sms
class TestSMSManagers:

    @pytest.fixture
    def get_request_obj(self):
        return Request(superuser=False)

    @pytest.fixture
    def get_request_super_obj(self):
        return Request(superuser=True)

    def test_school_get_query_reg_user(self, get_request_obj, monkeypatch):
        class GetSchoolQuerySet:
            def filter(self, school_name__exact):
                return '__SCHOOL_FILTER__'

        def get_school_qs(self):
            return GetSchoolQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset',
                            get_school_qs)

        assert SchoolManager().get_query(get_request_obj) == '__SCHOOL_FILTER__'

    def test_school_get_query_super_user(self, get_request_super_obj, monkeypatch):
        class GetSchoolQuerySet:
            def all(self):
                return '__SCHOOL_ALL__'

        def get_school_qs(self):
            return GetSchoolQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset',
                            get_school_qs)

        assert SchoolManager().get_query(get_request_super_obj) == '__SCHOOL_ALL__'

    def test_prog_get_query_reg_user(self, get_request_obj, monkeypatch):
        class GetProgramQuerySet:
            def filter(self, school__school_name__exact):
                return '__PROGRAM_FILTER__'

        def get_prog_qs(self):
            return GetProgramQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset',
                            get_prog_qs)

        assert ProgramManager().get_query(get_request_obj) == '__PROGRAM_FILTER__'

    def test_prog_get_query_super_user(self, get_request_super_obj, monkeypatch):
        class GetProgramQuerySet:
            def all(self):
                return '__PROGRAM_ALL__'

        def get_prog_qs(self):
            return GetProgramQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset',
                            get_prog_qs)

        assert ProgramManager().get_query(get_request_super_obj) == '__PROGRAM_ALL__'

    def test_rot_get_query_reg_user(self, get_request_obj, monkeypatch):
        class GetRotationQuerySet:
            def filter(self, program__school__school_name__exact):
                return '__ROTATION_FILTER__'

        def get_rot_qs(self):
            return GetRotationQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset',
                            get_rot_qs)

        assert RotationManager().get_query(get_request_obj) == '__ROTATION_FILTER__'

    def test_rot_get_query_super_user(self, get_request_super_obj, monkeypatch):
        class GetRotationQuerySet:
            def all(self):
                return '__ROTATION_ALL__'

        def get_rot_qs(self):
            return GetRotationQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset',
                            get_rot_qs)

        assert RotationManager().get_query(get_request_super_obj) == '__ROTATION_ALL__'

    def test_student_get_query_reg_user(self, get_request_obj, monkeypatch):
        class GetStudentQuerySet:
            def filter(self, rotation__program__school__school_name__exact):
                return '__STUDENT_FILTER__'

        def get_student_qs(self):
            return GetStudentQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset',
                            get_student_qs)

        assert StudentManager().get_query(get_request_obj) == '__STUDENT_FILTER__'

    def test_student_get_query_super_user(self, get_request_super_obj, monkeypatch):
        class GetStudentQuerySet:
            def all(sel):
                return '__STUDENT_ALL__'

        def get_student_qs(self):
            return GetStudentQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset',
                            get_student_qs)

        assert StudentManager().get_query(get_request_super_obj) == '__STUDENT_ALL__'
