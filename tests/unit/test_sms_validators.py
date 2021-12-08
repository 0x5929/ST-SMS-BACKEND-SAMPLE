import pytest
import datetime

from sms.models import Student, Rotation, Program, School
from sms.validators import SMSValidator
from sms.serializers import StudentSerializer, RotationSerializer, ProgramSerializer

from .sms_constants import (TEST_PROGRAM_UUID, 
                            TEST_NOCAP_MATCHING_STR, 
                            TEST_CAP_MATCHING_STR, 
                            TEST_MATCHING_PHONE_NO, 
                            TEST_NON_MATCHING_PHONE, 
                            TEST_MATCHING_STUDENT_ID,
                            TEST_NON_MATCHING_STUDENT_ID, 
                            TEST_NON_MATCHING_STR, 
                            TEST_PROGRAM_NAME, 
                            TEST_SCHOOL_NAME,
                            TEST_DIFF_SCHOOL_NAME,
                            TEST_DIFF_PROG_NAME,
                            TEST_NON_MATCHING_EMAILS)

class User:
    def __init__(self, superuser=False):
        self.is_superuser = superuser
        self.school_name = None


class Request:
    def __init__(self, superuser=False):
        self.user = User(superuser=superuser)


@pytest.mark.sms
class TestSMSValidator:

    @pytest.fixture
    def get_request_obj(self):
        return Request(superuser=False)

    @pytest.fixture
    def get_request_super_obj(self):
        return Request(superuser=True)

    @pytest.fixture
    def get_student_obj(self):
        return Student.objects.all().first()

    @pytest.fixture
    def get_rot_obj(self):
        return Rotation.objects.all().first()

    @pytest.fixture
    def get_prog_obj(self):
        return Program.objects.all().first()

    @pytest.fixture
    def get_school_obj(self):
        return School.objects.all().first()

    @pytest.fixture
    def get_rot_reference(self, get_prog_obj):
        return {'program': get_prog_obj}

    @pytest.fixture
    def get_student_serializer(self):
        return StudentSerializer()

    @pytest.fixture
    def get_rotation_serializer(self):
        return RotationSerializer()

    @pytest.fixture
    def get_program_serializer(self):
        return ProgramSerializer()

    @pytest.fixture
    def get_student_serializer_data(self, get_student_serializer):
        return get_student_serializer.data

    @pytest.fixture
    def get_rotation_serializer_data(self, get_rotation_serializer):
        return get_rotation_serializer.data

    @pytest.fixture
    def get_program_serializer_data(self, get_program_serializer):
        return get_program_serializer.data

    def test_student_final_validation(self, get_student_serializer, get_student_serializer_data, mocker):
        mocked_date_validation = mocker.patch(
            'sms.validators.SMSValidator.date_validation')
        mocked_ensure_program_name = mocker.patch(
            'sms.validators.SMSValidator.ensure_program_name')
        mocked_ensure_ensure_same_school = mocker.patch(
            'sms.validators.SMSValidator.ensure_same_school')

        SMSValidator.student_final_validation(
            get_student_serializer, get_student_serializer_data)

        mocked_date_validation.assert_called_once()
        mocked_ensure_program_name.assert_called_once()
        mocked_ensure_ensure_same_school.assert_called_once()

    def test_rotation_final_validation(self, get_rotation_serializer, get_rotation_serializer_data, mocker):
        mocked_ensure_same_school = mocker.patch(
            'sms.validators.SMSValidator.ensure_same_school')
        mocked_ensure_unique_rot = mocker.patch(
            'sms.validators.SMSValidator.ensure_unique_rot')

        SMSValidator.rotation_final_validation(
            get_rotation_serializer, get_rotation_serializer_data)

        mocked_ensure_same_school.assert_called_once()
        mocked_ensure_unique_rot.assert_called_once()

    def test_program_final_validation(self, get_program_serializer, get_program_serializer_data, mocker):
        mocked_ensure_same_school = mocker.patch(
            'sms.validators.SMSValidator.ensure_same_school')

        SMSValidator.program_final_validation(
            get_program_serializer, get_program_serializer_data)

        mocked_ensure_same_school.assert_called_once()

    def test_reference_does_not_change_on_updates_success(self, get_rot_obj):
        instance = get_rot_obj
        reference = 'program'
        value = instance.program

        assert SMSValidator.reference_does_not_change_on_updates(
            value, instance, reference).program_uuid == get_rot_obj.program.program_uuid

    def test_reference_does_not_change_on_updates_failure(self, get_rot_obj):
        instance = get_rot_obj
        reference = 'program'
        value = TEST_PROGRAM_UUID

        with pytest.raises(Exception):
            SMSValidator.reference_does_not_change_on_updates(
                value, instance, reference)

    def test_no_special_chars_and_captialize_string_success(self):
        matching_str = TEST_NOCAP_MATCHING_STR

        assert SMSValidator.no_special_chars_and_captialize_string(
            matching_str, capitalize=True) == TEST_CAP_MATCHING_STR

        assert SMSValidator.no_special_chars_and_captialize_string(
            matching_str) == TEST_NOCAP_MATCHING_STR

    def test_no_special_chars_and_captialize_string_failure(self):

        with pytest.raises(Exception):
            for string in TEST_NON_MATCHING_STR:
                SMSValidator.no_special_chars_and_captialize_string(
                    string)

    def test_phone_number_format_checker_success(self):
        matching_phone_num = TEST_MATCHING_PHONE_NO

        assert SMSValidator.phone_number_format_checker(
            matching_phone_num) == matching_phone_num

    def test_phone_number_format_checker_failure(self):
        with pytest.raises(Exception):
            for phone_num in TEST_NON_MATCHING_PHONE:
                SMSValidator.phone_number_format_checker(phone_num)

    def test_student_id_format_checker_success(self):

        for id_ in TEST_MATCHING_STUDENT_ID:
            assert SMSValidator.student_id_format_checker(id_) == id_

    def test_student_id_format_checker_failure(self):
        with pytest.raises(Exception):
            for id_ in TEST_NON_MATCHING_STUDENT_ID:
                SMSValidator.student_id_format_checker(id_)

    def test_date_validation_success(self):
        earlier_date = datetime.datetime(2021, 1, 1)
        later_date = datetime.datetime(2021, 1, 2)

        data = {
            'start_date': earlier_date,
            'completion_date': later_date
        }

        assert SMSValidator.date_validation(data, partial=False) == data
        assert SMSValidator.date_validation(data, partial=True) == data
        assert SMSValidator.date_validation({}, partial=True) == {}

    def test_date_validation_failure(self):
        earlier_date = datetime.datetime(2021, 1, 1)
        later_date = datetime.datetime(2021, 1, 2)

        data = {
            'start_date': later_date,
            'completion_date': earlier_date
        }

        with pytest.raises(Exception):
            SMSValidator.date_validation(data, partial=False)

            # if doing PATCH (partial update), and one of the date is missing, raise exception
            del data['start_date']

            SMSValidator.date_validation(data, partial=True)

    def test_ensure_unique_rot_failure(self, get_rot_reference, monkeypatch):
        def does_exist(program__program_uuid, rotation_number):
            return ExistQuerySet()

        class ExistQuerySet:
            def exists(self):
                return True

        monkeypatch.setattr(Rotation.objects, 'filter', does_exist)

        with pytest.raises(Exception):
            SMSValidator.ensure_unique_rot(get_rot_reference)

    def test_ensure_unique_rot_success(self, get_rot_reference, monkeypatch):
        def doesnt_exist(program__program_uuid, rotation_number):
            return NonExistQuerySet()

        class NonExistQuerySet:
            def exists(self):
                return False

        monkeypatch.setattr(Rotation.objects, 'filter', doesnt_exist)

        assert SMSValidator.ensure_unique_rot(
            get_rot_reference) == get_rot_reference

    def test_ensure_program_name_success(self, get_rot_obj, monkeypatch):
        course_name = TEST_PROGRAM_NAME
        test_data = {'course': course_name, 'rotation': get_rot_obj}

        def output_matching_res(rotation_uuid__exact):
            get_rot_obj.program.program_name = TEST_PROGRAM_NAME
            return get_rot_obj

        monkeypatch.setattr(Rotation.objects, 'get', output_matching_res)
        assert SMSValidator.ensure_program_name(test_data) == test_data
        assert SMSValidator.ensure_program_name({}, partial=True) == {}

    def test_ensure_program_name_failure(self, get_rot_obj, monkeypatch):
        course_name = TEST_PROGRAM_NAME
        test_data = {'course': course_name, 'rotation': get_rot_obj}

        def output_non_match_res(rotation_uuid__exact):
            get_rot_obj.program.program_name = TEST_DIFF_PROG_NAME
            return get_rot_obj

        monkeypatch.setattr(Rotation.objects, 'get', output_non_match_res)

        with pytest.raises(Exception):
            assert SMSValidator.ensure_program_name(test_data)

            del test_data['course']

            assert SMSValidator.ensure_program_name(test_data)

    def test_ensure_same_school_success(self, get_school_obj, get_prog_obj, get_rot_obj, get_request_obj, get_request_super_obj):

        get_rot_obj.program.school.school_name = TEST_SCHOOL_NAME
        get_request_obj.user.school_name = TEST_SCHOOL_NAME
        data = {
            'rotation': get_rot_obj
        }
        assert SMSValidator.ensure_same_school(
            data, get_request_obj, entry_pt='student') == data

        get_prog_obj.school.school_name = TEST_SCHOOL_NAME
        data = {
            'program': get_prog_obj
        }
        assert SMSValidator.ensure_same_school(
            data, get_request_obj, entry_pt='rotation') == data

        get_school_obj.school_name = TEST_SCHOOL_NAME
        data = {
            'school': get_school_obj
        }
        assert SMSValidator.ensure_same_school(
            data, get_request_obj, entry_pt='program') == data

        # superuser case, pass data through
        assert SMSValidator.ensure_same_school(
            {}, get_request_super_obj, 'student', partial=True) == {}

    def test_ensure_same_school_failure(self, get_school_obj, get_prog_obj, get_rot_obj, get_request_obj, get_request_super_obj):

        with pytest.raises(Exception):
            get_rot_obj.program.school.school_name = TEST_SCHOOL_NAME
            get_request_obj.user.school_name = TEST_DIFF_SCHOOL_NAME
            data = {
                'rotation': get_rot_obj
            }

            assert SMSValidator.ensure_same_school(
                data, get_request_obj, entry_pt='student')

            get_prog_obj.school.school_name = TEST_SCHOOL_NAME
            data = {
                'program': get_prog_obj
            }
            assert SMSValidator.ensure_same_school(
                data, get_request_obj, entry_pt='rotation')

            get_school_obj.school_name = TEST_SCHOOL_NAME
            data = {
                'school': get_school_obj
            }
            assert SMSValidator.ensure_same_school(
                data, get_request_obj, entry_pt='program')

    def test_email_format_checker_success(self):
        # NOTE: i know this isn't the best way, we can also try regex,
        # EITHER WAY, someone can supply a faulty email that has current format?
        # it's best to check email by sending a verification email, this is a lazy way
        min_matching_email = '@.'

        assert SMSValidator.email_format_checker(
            min_matching_email) == min_matching_email

    def test_email_format_checker_failure(self):

        with pytest.raises(Exception):
            for email in TEST_NON_MATCHING_EMAILS:
                SMSValidator.email_format_checker(
                    email)
