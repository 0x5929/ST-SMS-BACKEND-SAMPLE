import pytest
from datetime import date, timedelta
from tests.acceptance.steps.constants import (SCHOOL_UUID_TO_TEST,
                                              SCHOOL_STR,
                                              PROGRAM_UUID_TO_TEST,
                                              PROGRAM_STR,
                                              ROTATION_UUID_TO_TEST,
                                              ROTATION_STR,
                                              STUDENT_UUID_TO_TEST,
                                              STUDENT_STR,
                                              FILTER_PARAMS,
                                              TEST_ROTATION_SIZE)

from sms.models import School, Program, Rotation, Student
from sms.google_sheets import GoogleSheet

# pytestmark = pytest.mark.django_db


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
        rotation = Rotation.objects.get(
            rotation_uuid__exact=ROTATION_UUID_TO_TEST)

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

    @pytest.fixture
    def get_student_obj(self):
        return Student.objects.get(student_uuid__exact=STUDENT_UUID_TO_TEST)

    @pytest.fixture
    def get_rotation_obj(self):
        return Rotation.objects.get(rotation_uuid__exact=ROTATION_UUID_TO_TEST)

    def test_rotation_size(self, get_rotation_obj):
        assert get_rotation_obj.size == TEST_ROTATION_SIZE

    def test_student_school_name(self, get_student_obj):
        assert get_student_obj.school_name == FILTER_PARAMS.get('school_name')

    def test_student_pre_hook(self, get_student_obj, monkeypatch):

        def mockreturn_true(action):
            return True

        def mockreturn_false(action):
            return False

        monkeypatch.setattr(get_student_obj, 'migrate_google', mockreturn_true)

        assert get_student_obj.pre_hook('save') == True
        assert get_student_obj.pre_hook('delete') == True

        monkeypatch.setattr(
            get_student_obj, 'migrate_google', mockreturn_false)

        assert get_student_obj.pre_hook('save') == False
        assert get_student_obj.pre_hook('delete') == False

    def test_student_migrate_google_setting(self, get_student_obj, monkeypatch):

        from django.conf import settings
        monkeypatch.setattr(settings, 'MIGRATE_GOOGLE_SHEET', False)

        assert get_student_obj.migrate_google('DEL') == True
        assert get_student_obj.migrate_google('POST/PUT/PATCH') == True

        monkeypatch.delattr(settings, 'MIGRATE_GOOGLE_SHEET')

        assert get_student_obj.migrate_google('DEL') == True
        assert get_student_obj.migrate_google('POST/PUT/PATCH') == True

    def test_student_migrate_google(self, get_student_obj, monkeypatch):

        def mockreturn_exception(data):
            raise Exception

        monkeypatch.setattr(GoogleSheet, 'master_sheet_del',
                            mockreturn_exception)
        monkeypatch.setattr(
            GoogleSheet, 'master_sheet_save', mockreturn_exception)

        assert get_student_obj.migrate_google('DEL') == False
        assert get_student_obj.migrate_google('POST/PUT/PATCH') == False

    def test_student_payment_and_date_attr_logic(self, get_student_obj):
        get_student_obj.total_charges_charged = '100.00'
        get_student_obj.total_charges_paid = '99.99'

        get_student_obj.date_enrollment_agreement_signed = date.today().strftime('%Y-%m-%d')
        get_student_obj.start_date = (
            date.today() - timedelta(days=1)).strftime('%Y-%m-%d')

        get_student_obj.payment_and_date_attr_logic()

        assert get_student_obj.paid == False
        assert get_student_obj.date_enrollment_agreement_signed == get_student_obj.start_date

    def test_student_save_exception(self, get_student_obj, monkeypatch):

        def mockreturn_exception(method):
            raise Exception

        monkeypatch.setattr(get_student_obj, 'pre_hook', mockreturn_exception)

        with pytest.raises(Exception):
            get_student_obj.save()


    def test_student_delete_exception(self, get_student_obj, monkeypatch):

        def mockreturn_exception(method):
            raise Exception

        monkeypatch.setattr(get_student_obj, 'pre_hook', mockreturn_exception)

        with pytest.raises(Exception):
            get_student_obj.delete()

    # https://stackoverflow.com/questions/49807449/how-to-check-if-a-function-was-called-in-a-unit-test-using-pytest-mock
    def test_student_save_ensure_super(self, get_student_obj, monkeypatch, mocker):

        def mockreturn_true(method):
            return True

        monkeypatch.setattr(get_student_obj, 'pre_hook', mockreturn_true)

        # assert that super().save() was called
        mocked_super = mocker.patch('django.db.models.Model.save')

        get_student_obj.save()

        mocked_super.assert_called_once()

    def test_student_delete_ensure_super(self, get_student_obj, monkeypatch, mocker):

        def mockreturn_true(method):
            return True

        monkeypatch.setattr(get_student_obj, 'pre_hook', mockreturn_true)

        # assert that super().delete() was called
        mocked_super = mocker.patch('django.db.models.Model.delete')

        get_student_obj.delete()

        mocked_super.assert_called_once()
