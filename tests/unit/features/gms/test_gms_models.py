import pytest

from gms.models import CNARotation, CNAStudent, CNATheoryRecord, CNAClinicalRecord, HHARotation, HHAStudent, HHATheoryRecord, HHAClinicalRecord

from .gms_constants import (GMS_CNA_ROTATION_UUID_TO_TEST, 
                            GMS_CNA_STUDENT_UUID_TO_TEST,
                            GMS_CNA_THEORY_RECORD_UUID_TO_TEST,
                            GMS_CNA_CLINICAL_RECORD_UUID_TO_TEST,
                            GMS_HHA_ROTATION_UUID_TO_TEST,
                            GMS_HHA_STUDENT_UUID_TO_TEST,
                            GMS_HHA_THEORY_RECORD_UUID_TO_TEST,
                            GMS_HHA_CLINICAL_RECORD_UUID_TO_TEST,
                            CNAROTATION_STR,
                            HHAROTATION_STR,
                            CNASTUDENT_STR,
                            HHASTUDENT_STR,
                            CNATHEORYRECORD_STR,
                            HHATHEORYRECORD_STR,
                            CNACLINICALRECORD_STR,
                            HHACLINICALRECORD_STR)


@pytest.mark.gms
class TestGMSModelAttrRequirement:
    """
    Testing Mininum Attribute Requirements for each GMS models

    """

    def test_cnaRotation_model_attr(self):
        cnaRotation = CNARotation.objects.get(rotation_uuid__exact=GMS_CNA_ROTATION_UUID_TO_TEST)

        if hasattr(cnaRotation, 'rotation_uuid') and \
           hasattr(cnaRotation, 'rotation_num') and \
           hasattr(cnaRotation, 'instructor_title') and \
           hasattr(cnaRotation, 'clinical_site') and \
           hasattr(cnaRotation, 'school_name') and \
           hasattr(cnaRotation, 'start_date')and \
           hasattr(cnaRotation, 'end_date')and \
           hasattr(cnaRotation, 'instructor_email') :

            assert True
        else:
            assert False

    
    def test_cnaStudent_model_attr(self):
        cnaStudent = CNAStudent.objects.get(student_uuid__exact=GMS_CNA_STUDENT_UUID_TO_TEST)

        if hasattr(cnaStudent, 'student_uuid') and \
           hasattr(cnaStudent, 'first_name') and \
           hasattr(cnaStudent, 'last_name') and \
           hasattr(cnaStudent, 'makeup_student') and \
           hasattr(cnaStudent, 'rotation') :

            assert True
        else:
            assert False

    
    def test_cnaTheoryRecord_model_attr(self):
        cnaTheoryRecord = CNATheoryRecord.objects.get(record_uuid__exact=GMS_CNA_THEORY_RECORD_UUID_TO_TEST)

        if hasattr(cnaTheoryRecord, 'record_uuid') and \
           hasattr(cnaTheoryRecord, 'date') and \
           hasattr(cnaTheoryRecord, 'completed') and \
           hasattr(cnaTheoryRecord, 'hours_spent') and \
           hasattr(cnaTheoryRecord, 'test_score') and \
           hasattr(cnaTheoryRecord, 'topic') and \
           hasattr(cnaTheoryRecord, 'student') :

            assert True
        else:
            assert False


    def test_cnaClinicalRecord_model_attr(self):
        cnaClinicalRecord = CNAClinicalRecord.objects.get(record_uuid__exact=GMS_CNA_CLINICAL_RECORD_UUID_TO_TEST)
    
    
        if hasattr(cnaClinicalRecord, 'record_uuid') and \
           hasattr(cnaClinicalRecord, 'date') and \
           hasattr(cnaClinicalRecord, 'completed') and \
           hasattr(cnaClinicalRecord, 'comments') and \
           hasattr(cnaClinicalRecord, 'performance_satisfied') and \
           hasattr(cnaClinicalRecord, 'topic') and \
           hasattr(cnaClinicalRecord, 'student') :

            assert True
        else:
            assert False

    def test_hhaRotation_model_attr(self):
        hhaRotation = HHARotation.objects.get(rotation_uuid__exact=GMS_HHA_ROTATION_UUID_TO_TEST)

        if hasattr(hhaRotation, 'rotation_uuid') and \
        hasattr(hhaRotation, 'rotation_num') and \
        hasattr(hhaRotation, 'instructor_title') and \
        hasattr(hhaRotation, 'clinical_site') and \
        hasattr(hhaRotation, 'school_name') and \
        hasattr(hhaRotation, 'start_date')and \
        hasattr(hhaRotation, 'end_date')and \
        hasattr(hhaRotation, 'instructor_email') :

            assert True
        else:
            assert False


    def test_hhaStudent_model_attr(self):
        hhaStudent = HHAStudent.objects.get(student_uuid__exact=GMS_HHA_STUDENT_UUID_TO_TEST)

        if hasattr(hhaStudent, 'student_uuid') and \
           hasattr(hhaStudent, 'first_name') and \
           hasattr(hhaStudent, 'last_name') and \
           hasattr(hhaStudent, 'makeup_student') and \
           hasattr(hhaStudent, 'rotation') :

            assert True
        else:
            assert False



    def test_hhaTheoryRecord_model_attr(self):
        hhaTheoryRecord = HHATheoryRecord.objects.get(record_uuid__exact=GMS_HHA_THEORY_RECORD_UUID_TO_TEST)

        if hasattr(hhaTheoryRecord, 'record_uuid') and \
           hasattr(hhaTheoryRecord, 'date') and \
           hasattr(hhaTheoryRecord, 'completed') and \
           hasattr(hhaTheoryRecord, 'start_time') and \
           hasattr(hhaTheoryRecord, 'end_time') and \
           hasattr(hhaTheoryRecord, 'hours_spent') and \
           hasattr(hhaTheoryRecord, 'test_score') and \
           hasattr(hhaTheoryRecord, 'topic') and \
           hasattr(hhaTheoryRecord, 'student') :

            assert True
        else:
            assert False


    def test_hhaClinicalRecord_model_attr(self):
        hhaClinicalRecord = HHAClinicalRecord.objects.get(record_uuid__exact=GMS_HHA_CLINICAL_RECORD_UUID_TO_TEST)
    
    
        if hasattr(hhaClinicalRecord, 'record_uuid') and \
           hasattr(hhaClinicalRecord, 'date') and \
           hasattr(hhaClinicalRecord, 'completed') and \
           hasattr(hhaClinicalRecord, 'hours_spent') and \
           hasattr(hhaClinicalRecord, 'comments') and \
           hasattr(hhaClinicalRecord, 'performance_satisfied') and \
           hasattr(hhaClinicalRecord, 'start_time') and \
           hasattr(hhaClinicalRecord, 'end_time') and \
           hasattr(hhaClinicalRecord, 'start_date') and \
           hasattr(hhaClinicalRecord, 'end_date') and \
           hasattr(hhaClinicalRecord, 'topic') and \
           hasattr(hhaClinicalRecord, 'student') :

            assert True
        else:
            assert False





@pytest.mark.gms
class TestGMSModelStr:

    """
    Testing str functions of each model in GMS app (aka how each object is viewed by clients)

    """

    def test_cnaRotation_model_str(self):
        cnaRotation = CNARotation.objects.get(rotation_uuid__exact=GMS_CNA_ROTATION_UUID_TO_TEST)

        assert str(cnaRotation) == CNAROTATION_STR

    def test_cnaStudent_model_str(self):
        cnaStudent = CNAStudent.objects.get(
            student_uuid__exact=GMS_CNA_STUDENT_UUID_TO_TEST)

        assert str(cnaStudent) == CNASTUDENT_STR

    def test_cnaTheoryRecord_model_str(self):
        cnaTheoryRecord = CNATheoryRecord.objects.get(
            record_uuid__exact=GMS_CNA_THEORY_RECORD_UUID_TO_TEST)

        assert str(cnaTheoryRecord) == CNATHEORYRECORD_STR

    def test_cnaClinicalRecord_model_str(self):
        cnaClinicalRecord = CNAClinicalRecord.objects.get(
            record_uuid__exact=GMS_CNA_CLINICAL_RECORD_UUID_TO_TEST)

        assert str(cnaClinicalRecord) == CNACLINICALRECORD_STR



    def test_hhaRotation_model_str(self):
        hhaRotation = HHARotation.objects.get(rotation_uuid__exact=GMS_HHA_ROTATION_UUID_TO_TEST)

        assert str(hhaRotation) == HHAROTATION_STR

    def test_hhaStudent_model_str(self):
        hhaStudent = HHAStudent.objects.get(
            student_uuid__exact=GMS_HHA_STUDENT_UUID_TO_TEST)

        assert str(hhaStudent) == HHASTUDENT_STR

    def test_hhaTheoryRecord_model_str(self):
        hhaTheoryRecord = HHATheoryRecord.objects.get(
            record_uuid__exact=GMS_HHA_THEORY_RECORD_UUID_TO_TEST)

        assert str(hhaTheoryRecord) == HHATHEORYRECORD_STR

    def test_hhaClinicalRecord_model_str(self):
        hhaClinicalRecord = HHAClinicalRecord.objects.get(
            record_uuid__exact=GMS_HHA_CLINICAL_RECORD_UUID_TO_TEST)

        assert str(hhaClinicalRecord) == HHACLINICALRECORD_STR
