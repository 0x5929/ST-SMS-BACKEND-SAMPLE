import pytest

from gms.models.cna import CNARotation, CNAStudent

from .gms_constants import GMS_CNA_ROTATION_UUID_TO_TEST, GMS_CNA_STUDENT_UUID_TO_TEST


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