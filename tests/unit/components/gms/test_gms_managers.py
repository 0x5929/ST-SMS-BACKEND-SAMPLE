import pytest
from django.db import models

from gms.managers import (CNARotationManager, 
                            CNAStudentManager, 
                            CNATheoryRecordManager, 
                            CNAClinicalRecordManager,
                            HHARotationManager,
                            HHAStudentManager,
                            HHATheoryRecordManager,
                            HHAClinicalRecordManager)


from .gms_constants import (TEST_CNA_ROTATION, 
                            TEST_CNA_STUDENT, 
                            TEST_CNA_THEORY_RECORD, 
                            TEST_CNA_CLINICAL_RECORD , 
                            TEST_HHA_ROTATION,
                            TEST_HHA_STUDENT,
                            TEST_HHA_THEORY_RECORD,
                            TEST_HHA_CLINICAL_RECORD)

from tests.common_constants import TEST_SCHOOL_NAME


class User:
    def __init__(self, superuser=False, admin=False, staff=False):
        self.is_superuser = superuser
        self.is_admin = admin
        self.is_staff = staff
        self.school_name = TEST_SCHOOL_NAME
        self.email = '__TEST_EMAIL__'


class Request:
    def __init__(self, superuser=False, admin=False, staff=False):
        self.user = User(superuser=superuser, admin=admin, staff=staff)


@pytest.mark.gms
class TestGMSManagers:
    
    @pytest.fixture
    def get_request_obj(self):
        return Request()
    
    @pytest.fixture
    def get_request_super_obj(self):
        return Request(superuser=True)

    @pytest.fixture
    def get_request_admin_obj(self):
        return Request(admin=True)

    @pytest.fixture
    def get_request_staff_obj(self):
        return Request(staff=True)


    def test_cnaRotation_get_superuser(self, get_request_super_obj, monkeypatch):
        class GetCNARotationQuerySet:
            def all(self):
                return TEST_CNA_ROTATION

        def get_cnaRotation_qs(self):
            return GetCNARotationQuerySet()
        
        monkeypatch.setattr(models.Manager, 'get_queryset', get_cnaRotation_qs)

        assert CNARotationManager().get_query(get_request_super_obj) == TEST_CNA_ROTATION

    def test_cnaRotation_get_adminuser(self, get_request_admin_obj, monkeypatch):
        class GetCNARotationQuerySet:
            def filter(self, school_name__exact):
                return TEST_CNA_ROTATION

        def get_cnaRotation_qs(self):
            return GetCNARotationQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset', get_cnaRotation_qs)

        assert CNARotationManager().get_query(get_request_admin_obj) == TEST_CNA_ROTATION


    def test_cnaRotation_get_staffuser(self, get_request_staff_obj, monkeypatch):
        class GetCNARotationQuerySet:
            def filter(self, school_name__exact):
                return TEST_CNA_ROTATION

        def get_cnaRotation_qs(self):
            return GetCNARotationQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset', get_cnaRotation_qs)

        assert CNARotationManager().get_query(get_request_staff_obj) == TEST_CNA_ROTATION


    def test_cnaRotation_get_reguser(self, get_request_obj, monkeypatch):
        class GetCNARotationQuerySet:
            def filter(self, school_name__exact, instructor_email__contains):
                return TEST_CNA_ROTATION

        def get_cnaRotation_qs(self):
            return GetCNARotationQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset', get_cnaRotation_qs)

        assert CNARotationManager().get_query(get_request_obj) == TEST_CNA_ROTATION




    def test_cnaStudent_get_superuser(self, get_request_super_obj, monkeypatch):
        class GetCNAStudentQuerySet:
            def all(self):
                return TEST_CNA_STUDENT

        def get_cnaStudent_qs(self):
            return GetCNAStudentQuerySet()
        
        monkeypatch.setattr(models.Manager, 'get_queryset', get_cnaStudent_qs)

        assert CNAStudentManager().get_query(get_request_super_obj) == TEST_CNA_STUDENT

    def test_cnaStudent_get_adminuser(self, get_request_admin_obj, monkeypatch):
        class GetCNAStudentQuerySet:
            def filter(self, rotation__school_name__exact):
                return TEST_CNA_STUDENT

        def get_cnaStudent_qs(self):
            return GetCNAStudentQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset', get_cnaStudent_qs)

        assert CNAStudentManager().get_query(get_request_admin_obj) == TEST_CNA_STUDENT


    def test_cnaStudent_get_staffuser(self, get_request_staff_obj, monkeypatch):
        class GetCNAStudentQuerySet:
            def filter(self, rotation__school_name__exact):
                return TEST_CNA_STUDENT

        def get_cnaStudent_qs(self):
            return GetCNAStudentQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset', get_cnaStudent_qs)

        assert CNAStudentManager().get_query(get_request_staff_obj) == TEST_CNA_STUDENT


    def test_cnaStudent_get_reguser(self, get_request_obj, monkeypatch):
        class GetCNAStudentQuerySet:
            def filter(self, rotation__school_name__exact, rotation__instructor_email__contains):
                return TEST_CNA_STUDENT

        def get_cnaStudent_qs(self):
            return GetCNAStudentQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset', get_cnaStudent_qs)

        assert CNAStudentManager().get_query(get_request_obj) == TEST_CNA_STUDENT



    def test_cnaTheoryRecord_get_superuser(self, get_request_super_obj, monkeypatch):
        class GetCNATheoryRecordQuerySet:
            def all(self):
                return TEST_CNA_THEORY_RECORD

        def get_cnaTheoryRecord_qs(self):
            return GetCNATheoryRecordQuerySet()
        
        monkeypatch.setattr(models.Manager, 'get_queryset', get_cnaTheoryRecord_qs)

        assert CNATheoryRecordManager().get_query(get_request_super_obj) == TEST_CNA_THEORY_RECORD

    def test_cnaTheoryRecord_get_adminuser(self, get_request_admin_obj, monkeypatch):
        class GetCNATheoryRecordQuerySet:
            def filter(self, student__rotation__school_name__exact):
                return TEST_CNA_THEORY_RECORD

        def get_cnaTheoryRecord_qs(self):
            return GetCNATheoryRecordQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset', get_cnaTheoryRecord_qs)

        assert CNATheoryRecordManager().get_query(get_request_admin_obj) == TEST_CNA_THEORY_RECORD


    def test_cnaTheoryRecord_get_staffuser(self, get_request_staff_obj, monkeypatch):
        class GetCNATheoryRecordQuerySet:
            def filter(self, student__rotation__school_name__exact):
                return TEST_CNA_THEORY_RECORD

        def get_cnaTheoryRecord_qs(self):
            return GetCNATheoryRecordQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset', get_cnaTheoryRecord_qs)

        assert CNATheoryRecordManager().get_query(get_request_staff_obj) == TEST_CNA_THEORY_RECORD


    def test_cnaTheoryRecord_get_reguser(self, get_request_obj, monkeypatch):
        class GetCNATheoryRecordQuerySet:
            def filter(self, student__rotation__school_name__exact, student__rotation__instructor_email__contains):
                return TEST_CNA_THEORY_RECORD

        def get_cnaTheoryRecord_qs(self):
            return GetCNATheoryRecordQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset', get_cnaTheoryRecord_qs)

        assert CNATheoryRecordManager().get_query(get_request_obj) == TEST_CNA_THEORY_RECORD



    def test_cnaClinicalRecord_get_superuser(self, get_request_super_obj, monkeypatch):
        class GetCNAClinicalRecordQuerySet:
            def all(self):
                return TEST_CNA_CLINICAL_RECORD

        def get_cnaClinicalRecord_qs(self):
            return GetCNAClinicalRecordQuerySet()
        
        monkeypatch.setattr(models.Manager, 'get_queryset', get_cnaClinicalRecord_qs)

        assert CNAClinicalRecordManager().get_query(get_request_super_obj) == TEST_CNA_CLINICAL_RECORD

    def test_cnaClinicalRecord_get_adminuser(self, get_request_admin_obj, monkeypatch):
        class GetCNAClinicalRecordQuerySet:
            def filter(self, student__rotation__school_name__exact):
                return TEST_CNA_CLINICAL_RECORD

        def get_cnaClinicalRecord_qs(self):
            return GetCNAClinicalRecordQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset', get_cnaClinicalRecord_qs)

        assert CNAClinicalRecordManager().get_query(get_request_admin_obj) == TEST_CNA_CLINICAL_RECORD


    def test_cnaClinicalRecord_get_staffuser(self, get_request_staff_obj, monkeypatch):
        class GetCNAClinicalRecordQuerySet:
            def filter(self, student__rotation__school_name__exact):
                return TEST_CNA_CLINICAL_RECORD

        def get_cnaClinicalRecord_qs(self):
            return GetCNAClinicalRecordQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset', get_cnaClinicalRecord_qs)

        assert CNAClinicalRecordManager().get_query(get_request_staff_obj) == TEST_CNA_CLINICAL_RECORD


    def test_cnaClinicalRecord_get_reguser(self, get_request_obj, monkeypatch):
        class GetCNAClinicalRecordQuerySet:
            def filter(self, student__rotation__school_name__exact, student__rotation__instructor_email__contains):
                return TEST_CNA_CLINICAL_RECORD

        def get_cnaClinicalRecord_qs(self):
            return GetCNAClinicalRecordQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset', get_cnaClinicalRecord_qs)

        assert CNAClinicalRecordManager().get_query(get_request_obj) == TEST_CNA_CLINICAL_RECORD



    def test_hhaRotation_get_superuser(self, get_request_super_obj, monkeypatch):
        class GetHHARotationQuerySet:
            def all(self):
                return TEST_HHA_ROTATION

        def get_hhaRotation_qs(self):
            return GetHHARotationQuerySet()
        
        monkeypatch.setattr(models.Manager, 'get_queryset', get_hhaRotation_qs)

        assert HHARotationManager().get_query(get_request_super_obj) == TEST_HHA_ROTATION

    def test_hhaRotation_get_adminuser(self, get_request_admin_obj, monkeypatch):
        class GetHHARotationQuerySet:
            def filter(self, school_name__exact):
                return TEST_HHA_ROTATION

        def get_hhaRotation_qs(self):
            return GetHHARotationQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset', get_hhaRotation_qs)

        assert HHARotationManager().get_query(get_request_admin_obj) == TEST_HHA_ROTATION


    def test_hhaRotation_get_staffuser(self, get_request_staff_obj, monkeypatch):
        class GetHHARotationQuerySet:
            def filter(self, school_name__exact):
                return TEST_HHA_ROTATION

        def get_hhaRotation_qs(self):
            return GetHHARotationQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset', get_hhaRotation_qs)

        assert HHARotationManager().get_query(get_request_staff_obj) == TEST_HHA_ROTATION


    def test_hhaRotation_get_reguser(self, get_request_obj, monkeypatch):
        class GetHHARotationQuerySet:
            def filter(self, school_name__exact, instructor_email__contains):
                return TEST_HHA_ROTATION

        def get_hhaRotation_qs(self):
            return GetHHARotationQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset', get_hhaRotation_qs)

        assert HHARotationManager().get_query(get_request_obj) == TEST_HHA_ROTATION




    def test_hhaStudent_get_superuser(self, get_request_super_obj, monkeypatch):
        class GetHHAStudentQuerySet:
            def all(self):
                return TEST_HHA_STUDENT

        def get_hhaStudent_qs(self):
            return GetHHAStudentQuerySet()
        
        monkeypatch.setattr(models.Manager, 'get_queryset', get_hhaStudent_qs)

        assert HHAStudentManager().get_query(get_request_super_obj) == TEST_HHA_STUDENT

    def test_hhaStudent_get_adminuser(self, get_request_admin_obj, monkeypatch):
        class GetHHAStudentQuerySet:
            def filter(self, rotation__school_name__exact):
                return TEST_HHA_STUDENT

        def get_hhaStudent_qs(self):
            return GetHHAStudentQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset', get_hhaStudent_qs)

        assert HHAStudentManager().get_query(get_request_admin_obj) == TEST_HHA_STUDENT


    def test_hhaStudent_get_staffuser(self, get_request_staff_obj, monkeypatch):
        class GetHHAStudentQuerySet:
            def filter(self, rotation__school_name__exact):
                return TEST_HHA_STUDENT

        def get_hhaStudent_qs(self):
            return GetHHAStudentQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset', get_hhaStudent_qs)

        assert HHAStudentManager().get_query(get_request_staff_obj) == TEST_HHA_STUDENT


    def test_hhaStudent_get_reguser(self, get_request_obj, monkeypatch):
        class GetHHAStudentQuerySet:
            def filter(self, rotation__school_name__exact, rotation__instructor_email__contains):
                return TEST_HHA_STUDENT

        def get_hhaStudent_qs(self):
            return GetHHAStudentQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset', get_hhaStudent_qs)

        assert HHAStudentManager().get_query(get_request_obj) == TEST_HHA_STUDENT



    def test_hhaTheoryRecord_get_superuser(self, get_request_super_obj, monkeypatch):
        class GetHHATheoryRecordQuerySet:
            def all(self):
                return TEST_HHA_THEORY_RECORD

        def get_hhaTheoryRecord_qs(self):
            return GetHHATheoryRecordQuerySet()
        
        monkeypatch.setattr(models.Manager, 'get_queryset', get_hhaTheoryRecord_qs)

        assert HHATheoryRecordManager().get_query(get_request_super_obj) == TEST_HHA_THEORY_RECORD

    def test_hhaTheoryRecord_get_adminuser(self, get_request_admin_obj, monkeypatch):
        class GetHHATheoryRecordQuerySet:
            def filter(self, student__rotation__school_name__exact):
                return TEST_HHA_THEORY_RECORD

        def get_hhaTheoryRecord_qs(self):
            return GetHHATheoryRecordQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset', get_hhaTheoryRecord_qs)

        assert HHATheoryRecordManager().get_query(get_request_admin_obj) == TEST_HHA_THEORY_RECORD


    def test_hhaTheoryRecord_get_staffuser(self, get_request_staff_obj, monkeypatch):
        class GetHHATheoryRecordQuerySet:
            def filter(self, student__rotation__school_name__exact):
                return TEST_HHA_THEORY_RECORD

        def get_hhaTheoryRecord_qs(self):
            return GetHHATheoryRecordQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset', get_hhaTheoryRecord_qs)

        assert HHATheoryRecordManager().get_query(get_request_staff_obj) == TEST_HHA_THEORY_RECORD


    def test_hhaTheoryRecord_get_reguser(self, get_request_obj, monkeypatch):
        class GetHHATheoryRecordQuerySet:
            def filter(self, student__rotation__school_name__exact, student__rotation__instructor_email__contains):
                return TEST_HHA_THEORY_RECORD

        def get_hhaTheoryRecord_qs(self):
            return GetHHATheoryRecordQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset', get_hhaTheoryRecord_qs)

        assert HHATheoryRecordManager().get_query(get_request_obj) == TEST_HHA_THEORY_RECORD



    def test_hhaClinicalRecord_get_superuser(self, get_request_super_obj, monkeypatch):
        class GetHHAClinicalRecordQuerySet:
            def all(self):
                return TEST_HHA_CLINICAL_RECORD

        def get_hhaClinicalRecord_qs(self):
            return GetHHAClinicalRecordQuerySet()
        
        monkeypatch.setattr(models.Manager, 'get_queryset', get_hhaClinicalRecord_qs)

        assert HHAClinicalRecordManager().get_query(get_request_super_obj) == TEST_HHA_CLINICAL_RECORD

    def test_hhaClinicalRecord_get_adminuser(self, get_request_admin_obj, monkeypatch):
        class GetHHAClinicalRecordQuerySet:
            def filter(self, student__rotation__school_name__exact):
                return TEST_HHA_CLINICAL_RECORD

        def get_hhaClinicalRecord_qs(self):
            return GetHHAClinicalRecordQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset', get_hhaClinicalRecord_qs)

        assert HHAClinicalRecordManager().get_query(get_request_admin_obj) == TEST_HHA_CLINICAL_RECORD


    def test_hhaClinicalRecord_get_staffuser(self, get_request_staff_obj, monkeypatch):
        class GetHHAClinicalRecordQuerySet:
            def filter(self, student__rotation__school_name__exact):
                return TEST_HHA_CLINICAL_RECORD

        def get_hhaClinicalRecord_qs(self):
            return GetHHAClinicalRecordQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset', get_hhaClinicalRecord_qs)

        assert HHAClinicalRecordManager().get_query(get_request_staff_obj) == TEST_HHA_CLINICAL_RECORD


    def test_hhaClinicalRecord_get_reguser(self, get_request_obj, monkeypatch):
        class GetHHAClinicalRecordQuerySet:
            def filter(self, student__rotation__school_name__exact, student__rotation__instructor_email__contains):
                return TEST_HHA_CLINICAL_RECORD

        def get_hhaClinicalRecord_qs(self):
            return GetHHAClinicalRecordQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset', get_hhaClinicalRecord_qs)

        assert HHAClinicalRecordManager().get_query(get_request_obj) == TEST_HHA_CLINICAL_RECORD
