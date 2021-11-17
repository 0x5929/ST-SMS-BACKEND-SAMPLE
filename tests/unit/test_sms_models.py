
import pytest

from tests.acceptance.steps.constants import (SCHOOL_UUID_TO_TEST,
                                              SCHOOL_STR,
                                              PROGRAM_UUID_TO_TEST,
                                              PROGRAM_STR,
                                              ROTATION_UUID_TO_TEST,
                                              ROTATION_STR,
                                              STUDENT_UUID_TO_TEST,
                                              STUDENT_STR,
                                              FILTER_PARAMS)

from sms.models import School, Program, Rotation, Student

pytestmark = pytest.mark.django_db

class TestSMSModelStr:

    """
    Testing str functions of each model (aka how each object is viewed by clients)

    """

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


class TestSMSModelAttrRequirement:
    """
    Testing Mininum Attribute Requirements for each SMS models

    """
    def test_school_model_attr(self):
        school = School.objects.get(school_uuid__exact=SCHOOL_UUID_TO_TEST)
        
        if hasattr(school, 'school_uuid') and \
           hasattr(school, 'school_name') and \
           hasattr(school, 'school_code') and \
           hasattr(school, 'school_address') and \
           hasattr(school, 'year_founded'):

            assert True
        else: 
            assert False

    def test_program_model_attr(self):
        program = Program.objects.get(program_uuid__exact=PROGRAM_UUID_TO_TEST)

        if hasattr(program, 'program_uuid') and \
           hasattr(program, 'program_name') and \
           hasattr(program, 'school'):

            assert True
        else: 
            assert False


    def test_rotation_model_attr(self):
        rotation = Rotation.objects.get(rotation_uuid__exact=ROTATION_UUID_TO_TEST)

        if hasattr(rotation, 'rotation_uuid') and \
           hasattr(rotation, 'rotation_number') and \
           hasattr(rotation, 'program'):

            assert True
        else: 
            assert False



    def test_student_model_attr(self):
        student = Student.objects.get(student_uuid__exact=STUDENT_UUID_TO_TEST)

        if hasattr(student, 'student_uuid') and \
           hasattr(student, 'student_id') and \
           hasattr(student, 'first_name') and \
           hasattr(student, 'last_name') and \
           hasattr(student, 'phone_number') and \
           hasattr(student, 'email') and \
           hasattr(student, 'mailing_address') and \
           hasattr(student, 'course') and \
           hasattr(student, 'start_date') and \
           hasattr(student, 'completion_date') and \
           hasattr(student, 'date_enrollment_agreement_signed') and \
           hasattr(student, 'third_party_payer_info') and \
           hasattr(student, 'course_cost') and \
           hasattr(student, 'total_charges_charged') and \
           hasattr(student, 'total_charges_paid') and \
           hasattr(student, 'graduated') and \
           hasattr(student, 'passed_first_exam') and \
           hasattr(student, 'passed_second_or_third_exam') and \
           hasattr(student, 'employed') and \
           hasattr(student, 'place_of_employment') and \
           hasattr(student, 'employment_address') and \
           hasattr(student, 'position') and \
           hasattr(student, 'starting_wage') and \
           hasattr(student, 'hours_worked_weekly') and \
           hasattr(student, 'description_of_attempts_to_contact_student') and \
           hasattr(student, 'rotation') and \
           hasattr(student, 'google_sheet_migration_issue') and \
           hasattr(student, 'google_sheet_migrated'):

            assert True
        else: 
            assert False


class TestSMSModelAttrExtraLogic:
    """
    Testing additional model methods

    """
    def test_rotation_size(self):
        rotation = Rotation.objects.get(rotation_uuid__exact=ROTATION_UUID_TO_TEST)

        assert rotation.rotation_number == FILTER_PARAMS.get('rotation_num')

    def test_student_school_name(self):
        student = Student.objects.get(student_uuid__exact=STUDENT_UUID_TO_TEST)

        assert student.school_name == FILTER_PARAMS.get('school_name')

    def test_student_pre_hook(self, monkeypatch):
        pass

        def mockreturn_true():
            return True

        def mockreturn_false():
            return False


    # def test_student_save_update_delete_settings_false(self):
    #     # test that right Google Module wont be called
    #     pass

    # def test_student_save_update_delete_settings_true(self):
    #     # test that right Google Module will be called
    #     pass
