
import pytest

from sms.models import Rotation, Program
from sms.validators import SMSValidator
from sms.serializers import StudentSerializer, RotationSerializer, ProgramSerializer

from tests.acceptance.steps.constants import PROGRAM_UUID_TO_TEST


@pytest.mark.current
class TestSMSValidator:

    @pytest.fixture
    def get_rot_obj(self):
        return Rotation.objects.all().first()

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
        mocked_date_validation = mocker.patch('sms.validators.SMSValidator.date_validation')
        mocked_ensure_program_name = mocker.patch('sms.validators.SMSValidator.ensure_program_name')
        mocked_ensure_ensure_same_school = mocker.patch('sms.validators.SMSValidator.ensure_same_school')

        SMSValidator.student_final_validation(get_student_serializer, get_student_serializer_data)

        mocked_date_validation.assert_called_once()
        mocked_ensure_program_name.assert_called_once()
        mocked_ensure_ensure_same_school.assert_called_once()
        

    def test_rotation_final_validation(self, get_rotation_serializer, get_rotation_serializer_data, mocker):
        mocked_ensure_same_school = mocker.patch('sms.validators.SMSValidator.ensure_same_school')
        mocked_ensure_unique_rot = mocker.patch('sms.validators.SMSValidator.ensure_unique_rot')

        SMSValidator.rotation_final_validation(get_rotation_serializer, get_rotation_serializer_data)
    
        mocked_ensure_same_school.assert_called_once()
        mocked_ensure_unique_rot.assert_called_once()

    def test_program_final_validation(self, get_program_serializer, get_program_serializer_data, mocker):
        mocked_ensure_same_school = mocker.patch('sms.validators.SMSValidator.ensure_same_school')

        SMSValidator.program_final_validation(get_program_serializer, get_program_serializer_data)

        mocked_ensure_same_school.assert_called_once()

    def test_reference_does_not_change_on_updates_success(self, get_rot_obj):
        instance = get_rot_obj
        reference = 'program'
        value = instance.program.program_uuid

        assert SMSValidator.reference_does_not_change_on_updates(value, instance, reference) == get_rot_obj.program.program_uuid


    def test_reference_does_not_change_on_updates_failure(self, get_rot_obj):
        instance = get_rot_obj
        reference = 'program'
        value = '__TEST_PROGRAM_UUID__'

        with pytest.raises(Exception):
            SMSValidator.reference_does_not_change_on_updates(value, instance, reference)        

    def test_no_special_chars_and_captialize_string_success(self):
        assert False
        
    def test_no_special_chars_and_captialize_string_failure(self):
        assert False

    def test_phone_number_format_checker_success(self):
        assert False
        
    def test_phone_number_format_checker_failure(self):
        assert False

    def test_student_id_format_checker_success(self):
        assert False

    def test_student_id_format_checker_failure(self):
        assert False

    def test_date_validation_success(self):
        assert False
        
    def test_date_validation_failure(self):
        assert False

    def test_ensure_unique_rot_success(self):
        assert False

    def test_ensure_unique_rot_failure(self):
        assert False

    def test_ensure_program_name_success(self):
        assert False
        
    def test_ensure_program_name_failure(self):
        assert False

    def test_ensure_same_school_success(self):
        assert False
        
    def test_ensure_same_school_failure(self):
        assert False

    def test_email_format_checker_success(self):
        assert False
        
    def test_email_format_checker_failure(self):
        assert False