import pytest
from django.db import models

from sms.managers import SchoolManager, ProgramManager, RotationManager, StudentManager

from .sms_constants import (TEST_SCHOOL_NAME, 
                            TEST_SCHOOL_FILTER, 
                            TEST_SCHOOL_ALL, 
                            TEST_PROGRAM_FILTER, 
                            TEST_PROGRAM_ALL, 
                            TEST_ROTATION_FILTER,
                            TEST_ROTATION_ALL, 
                            TEST_STUDENT_FILTER, 
                            TEST_STUDENT_ALL)
class User:
    def __init__(self, superuser=False):
        self.is_superuser = superuser
        self.school_name = TEST_SCHOOL_NAME


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
                return TEST_SCHOOL_FILTER

        def get_school_qs(self):
            return GetSchoolQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset',
                            get_school_qs)

        assert SchoolManager().get_query(get_request_obj) == TEST_SCHOOL_FILTER

    def test_school_get_query_super_user(self, get_request_super_obj, monkeypatch):
        class GetSchoolQuerySet:
            def all(self):
                return TEST_SCHOOL_ALL

        def get_school_qs(self):
            return GetSchoolQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset',
                            get_school_qs)

        assert SchoolManager().get_query(get_request_super_obj) == TEST_SCHOOL_ALL

    def test_prog_get_query_reg_user(self, get_request_obj, monkeypatch):
        class GetProgramQuerySet:
            def filter(self, school__school_name__exact):
                return TEST_PROGRAM_FILTER

        def get_prog_qs(self):
            return GetProgramQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset',
                            get_prog_qs)

        assert ProgramManager().get_query(get_request_obj) == TEST_PROGRAM_FILTER

    def test_prog_get_query_super_user(self, get_request_super_obj, monkeypatch):
        class GetProgramQuerySet:
            def all(self):
                return TEST_PROGRAM_ALL

        def get_prog_qs(self):
            return GetProgramQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset',
                            get_prog_qs)

        assert ProgramManager().get_query(get_request_super_obj) == TEST_PROGRAM_ALL

    def test_rot_get_query_reg_user(self, get_request_obj, monkeypatch):
        class GetRotationQuerySet:
            def filter(self, program__school__school_name__exact):
                return TEST_ROTATION_FILTER

        def get_rot_qs(self):
            return GetRotationQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset',
                            get_rot_qs)

        assert RotationManager().get_query(get_request_obj) == TEST_ROTATION_FILTER

    def test_rot_get_query_super_user(self, get_request_super_obj, monkeypatch):
        class GetRotationQuerySet:
            def all(self):
                return TEST_ROTATION_ALL

        def get_rot_qs(self):
            return GetRotationQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset',
                            get_rot_qs)

        assert RotationManager().get_query(get_request_super_obj) == TEST_ROTATION_ALL

    def test_student_get_query_reg_user(self, get_request_obj, monkeypatch):
        class GetStudentQuerySet:
            def filter(self, rotation__program__school__school_name__exact):
                return TEST_STUDENT_FILTER

        def get_student_qs(self):
            return GetStudentQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset',
                            get_student_qs)

        assert StudentManager().get_query(get_request_obj) == TEST_STUDENT_FILTER

    def test_student_get_query_super_user(self, get_request_super_obj, monkeypatch):
        class GetStudentQuerySet:
            def all(sel):
                return TEST_STUDENT_ALL

        def get_student_qs(self):
            return GetStudentQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset',
                            get_student_qs)

        assert StudentManager().get_query(get_request_super_obj) == TEST_STUDENT_ALL
