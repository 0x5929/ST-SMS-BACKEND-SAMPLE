
import pytest

from tests.acceptance.steps.constants import (SCHOOL_UUID_TO_TEST,
                                              SCHOOL_STR,
                                              PROGRAM_UUID_TO_TEST,
                                              PROGRAM_STR,
                                              ROTATION_UUID_TO_TEST,
                                              ROTATION_STR,
                                              STUDENT_UUID_TO_TEST,
                                              STUDENT_STR)

from sms.models import School, Program, Rotation, Student


@pytest.mark.django_db
class TestSMSModelStr:
    pytestmark = pytest.mark.django_db

    def test_school_model_str(self):
        school = School.objects.get(school_uuid__exact=SCHOOL_UUID_TO_TEST)

        assert str(school) == SCHOOL_STR

    def test_program_model_str(self):
        program = Program.objects.get(program_uuid__exact=PROGRAM_UUID_TO_TEST)

        assert str(program) == PROGRAM_STR

    def test_rotation_model_str(self):
        rotation = Rotation.objects.get(
            rotation_uuid__exact=ROTATION_UUID_TO_TEST)

        assert str(rotation) == ROTATION_STR

    def test_student_model_str(self):
        student = Student.objects.get(
            student_uuid__exact=STUDENT_UUID_TO_TEST)

        assert str(student) == STUDENT_STR


# class TestSMSModelAttrRequirement(APITestCase):
#     def test_school_model_attr(self):
#         pass

#     def test_program_model_attr(self):
#         pass

#     def test_rotation_model_attr(self):
#         pass

#     def test_student_model_attr(self):
#         pass


# class TestSMSModelAttrExtraLogic(APITestCase):
#     def test_rotation_size(self):
#         pass

#     def test_student_school_name(self):
#         pass

#     def test_student_pre_hook(self):
#         pass

#     def test_student_save_update_delete_settings_false(self):
#         # test that right Google Module wont be called
#         pass

#     def test_student_save_update_delete_settings_true(self):
#         # test that right Google Module will be called
#         pass
