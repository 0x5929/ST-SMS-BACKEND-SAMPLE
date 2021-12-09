import pytest
import datetime

from sms.utils import DataHandler, FilterHandler
from sms.models import Student
from sms.validators import SMSValidator
from sms.filters import SMSFilter

from .sms_constants import (TEST_DICT_DATA, 
                            TEST_KEY, 
                            TEST_QUERY_PARAMS_SUCCESS, 
                            TEST_QUERY_PARAMS_FAILURE, 
                            TEST_SUCCESS_RETURN,
                            TEST_VALUE, 
                            TEST_INVALID_COURSE,
                            TEST_INVALID_NUMBER,
                            TEST_INVALID_BOOL,
                            TEST_RANDOM_STRING,
                            TEST_EMPTY_DATE,
                            TEST_INPUT_DATE,
                            TEST_INPUT_CURRENCY,
                            TEST_INPUT_EMPTY_CURRENCY,
                            TEST_Y,
                            TEST_YES,
                            TEST_FULLTIME_STR,
                            TEST_PARTTIME_STR)
                            
@pytest.mark.sms
class TestDataHandler:
    """
    Unit tests for DataHandler class

    """

    @pytest.fixture
    def get_test_model_obj(self):
        return Student.objects.all().first()

    def test_data_conversion(self, get_test_model_obj, mocker):
        """
        Testing that function will call the appropriate conversion methods

        """
        mocked_bool_conv = mocker.patch(
            'sms.utils.DataHandler.bool_conversion')
        mocked_date_conv = mocker.patch(
            'sms.utils.DataHandler.date_conversion')
        mocked_money_conv = mocker.patch(
            'sms.utils.DataHandler.money_conversion')
        mocked_course_conv = mocker.patch(
            'sms.utils.DataHandler.course_conversion')

        data = DataHandler.data_conversion(get_test_model_obj)

        mocked_bool_conv.assert_called()
        mocked_date_conv.assert_called()
        mocked_money_conv.assert_called()
        mocked_course_conv.assert_called()

        assert data.get('graduated') != None
        assert data.get('passed_first_exam') != None
        assert data.get('passed_second_or_third_exam') != None
        assert data.get('employed') != None
        assert data.get('start_date') != None
        assert data.get('completion_date') != None
        assert data.get('date_enrollment_agreement_signed') != None
        assert data.get('course_cost') != None
        assert data.get('total_charges_charged') != None
        assert data.get('total_charges_paid') != None
        assert data.get('starting_wage') != None
        assert data.get('course') != None

    def test_course_conversion(self, get_test_model_obj, mocker):
        mocker.patch.object(get_test_model_obj, 'course', 'CNA')
        assert DataHandler.course_conversion(
            get_test_model_obj, 'course') == 'Nurse Assistant'

        mocker.patch.object(get_test_model_obj, 'course', 'HHA')
        assert DataHandler.course_conversion(
            get_test_model_obj, 'course') == 'Home Health Aide'

        mocker.patch.object(get_test_model_obj, 'course', 'SG')
        assert DataHandler.course_conversion(
            get_test_model_obj, 'course') == 'Security Guard'

        mocker.patch.object(get_test_model_obj, 'course', 'Other')
        assert DataHandler.course_conversion(
            get_test_model_obj, 'course') == 'Other'

    def test_bool_conversion_success(self, get_test_model_obj, mocker):
        mocker.patch.object(get_test_model_obj, 'graduated', True)
        assert DataHandler.bool_conversion(
            get_test_model_obj, 'graduated') == 'Y'

        mocker.patch.object(get_test_model_obj, 'passed_first_exam', True)
        assert DataHandler.bool_conversion(
            get_test_model_obj, 'passed_first_exam') == 'Y'

        mocker.patch.object(get_test_model_obj,
                            'passed_second_or_third_exam', True)
        assert DataHandler.bool_conversion(
            get_test_model_obj, 'passed_second_or_third_exam') == 'Y'

        mocker.patch.object(get_test_model_obj, 'employed', True)
        assert DataHandler.bool_conversion(
            get_test_model_obj, 'employed') == 'Y'

    def test_bool_conversion_failure(self, get_test_model_obj, mocker):

        mocker.patch.object(get_test_model_obj, 'graduated', False)
        assert DataHandler.bool_conversion(
            get_test_model_obj, 'graduated') == ''

        mocker.patch.object(get_test_model_obj, 'passed_first_exam', False)
        assert DataHandler.bool_conversion(
            get_test_model_obj, 'passed_first_exam') == ''

        mocker.patch.object(get_test_model_obj,
                            'passed_second_or_third_exam', False)
        assert DataHandler.bool_conversion(
            get_test_model_obj, 'passed_second_or_third_exam') == ''

        mocker.patch.object(get_test_model_obj, 'employed', False)
        assert DataHandler.bool_conversion(
            get_test_model_obj, 'employed') == ''

    def test_date_conversion(self, get_test_model_obj, mocker):
        today_date = datetime.date.today()

        mocker.patch.object(get_test_model_obj, 'start_date', today_date)
        assert DataHandler.date_conversion(
            get_test_model_obj, 'start_date') == f'{str(today_date.month)}/{str(today_date.day)}/{str(today_date.year)}'

        mocker.patch.object(get_test_model_obj, 'completion_date', today_date)
        assert DataHandler.date_conversion(
            get_test_model_obj, 'completion_date') == f'{str(today_date.month)}/{str(today_date.day)}/{str(today_date.year)}'

        mocker.patch.object(get_test_model_obj,
                            'date_enrollment_agreement_signed', today_date)
        assert DataHandler.date_conversion(
            get_test_model_obj, 'date_enrollment_agreement_signed') == f'{str(today_date.month)}/{str(today_date.day)}/{str(today_date.year)}'

    def test_money_conversion(self, get_test_model_obj, mocker):
        if get_test_model_obj.course_cost:
            assert DataHandler.money_conversion(
                get_test_model_obj, 'course_cost') == str(get_test_model_obj.course_cost)
        else:
            assert DataHandler.money_conversion(
                get_test_model_obj, 'course_cost') == ''

        if get_test_model_obj.total_charges_charged:
            assert DataHandler.money_conversion(get_test_model_obj, 'total_charges_charged') == str(
                get_test_model_obj.total_charges_charged)
        else:
            assert DataHandler.money_conversion(
                get_test_model_obj, 'total_charges_charged') == ''

        if get_test_model_obj.total_charges_paid:
            assert DataHandler.money_conversion(get_test_model_obj, 'total_charges_paid') == str(
                get_test_model_obj.total_charges_paid)
        else:
            assert DataHandler.money_conversion(
                get_test_model_obj, 'total_charges_paid') == ''

        if get_test_model_obj.starting_wage:
            assert DataHandler.money_conversion(
                get_test_model_obj, 'starting_wage') == str(get_test_model_obj.starting_wage)
        else:
            assert DataHandler.money_conversion(
                get_test_model_obj, 'starting_wage') == ''

    def test_finalize_data(self):
        result = DataHandler.finalize_data(TEST_DICT_DATA)

        for index, items in enumerate(result):
            if index != result[index]:
                assert False

    def test_validate_student_id_success(self, mocker):
        mocked_SMSValidator_check = mocker.patch(
            'sms.validators.SMSValidator.student_id_format_checker', return_value=TEST_SUCCESS_RETURN)

        value, new_key = DataHandler.validate_student_id('test student id')

        mocked_SMSValidator_check.assert_called_once()
        assert value == TEST_SUCCESS_RETURN
        assert new_key == 'student_id'

    def test_validate_student_id_failure(self, monkeypatch):
        def return_exception():
            raise Exception

        monkeypatch.setattr(
            SMSValidator, 'student_id_format_checker', return_exception)

        with pytest.raises(Exception):
            DataHandler.validate_student_id('test student id')

    def test_validate_string_success(self, mocker):
        mocked_SMSValidator_check = mocker.patch(
            'sms.validators.SMSValidator.no_special_chars_and_captialize_string', return_value=TEST_SUCCESS_RETURN)

        value, new_key = DataHandler.validate_string(
            TEST_VALUE, 'Full Name')

        mocked_SMSValidator_check.assert_called()
        assert value == TEST_SUCCESS_RETURN
        assert new_key == 'full_name'

        value, new_key = DataHandler.validate_string(
            TEST_VALUE, 'Last Name')

        mocked_SMSValidator_check.assert_called()
        assert value == TEST_SUCCESS_RETURN
        assert new_key == 'last_name'

        value, new_key = DataHandler.validate_string(
            TEST_VALUE, 'First Name')

        mocked_SMSValidator_check.assert_called()
        assert value == TEST_SUCCESS_RETURN
        assert new_key == 'first_name'

        value, new_key = DataHandler.validate_string(
            TEST_VALUE, 'Mailing Address')

        mocked_SMSValidator_check.assert_called()
        assert value == TEST_SUCCESS_RETURN
        assert new_key == 'mailing_address'

        value, new_key = DataHandler.validate_string(
            TEST_VALUE, 'Third-party payer identifying information')

        mocked_SMSValidator_check.assert_called()
        assert value == TEST_SUCCESS_RETURN
        assert new_key == 'third_party_payer_info'

        value, new_key = DataHandler.validate_string(
            TEST_VALUE, 'Place of Employment')

        mocked_SMSValidator_check.assert_called()
        assert value == TEST_SUCCESS_RETURN
        assert new_key == 'place_of_employment'

        value, new_key = DataHandler.validate_string(
            TEST_VALUE, 'Employment Address')

        mocked_SMSValidator_check.assert_called()
        assert value == TEST_SUCCESS_RETURN
        assert new_key == 'employment_address'

        value, new_key = DataHandler.validate_string(
            TEST_VALUE, 'Position')

        mocked_SMSValidator_check.assert_called()
        assert value == TEST_SUCCESS_RETURN
        assert new_key == 'position'

        value, new_key = DataHandler.validate_string(
            TEST_VALUE, 'Description of Attempts to Contact Students')

        mocked_SMSValidator_check.assert_called()
        assert value == TEST_SUCCESS_RETURN
        assert new_key == 'description_of_attempts_to_contact_student'

    def test_validate_string_failure(self, monkeypatch):
        def return_exception():
            raise Exception

        monkeypatch.setattr(
            SMSValidator, 'no_special_chars_and_captialize_string', return_exception)

        value, new_key = DataHandler.validate_string(
            TEST_VALUE, 'Description of Attempts to Contact Students')

        assert value == ''

    def test_validate_phone_success(self, mocker):
        mocked_SMSValidator_check = mocker.patch(
            'sms.validators.SMSValidator.phone_number_format_checker', return_value=TEST_SUCCESS_RETURN)

        value, new_key = DataHandler.validate_phone(TEST_VALUE)

        mocked_SMSValidator_check.assert_called_once()
        assert value == TEST_SUCCESS_RETURN
        assert new_key == 'phone_number'

    def test_validate_phone_none(self):
        value, new_key = DataHandler.validate_phone('N/A')
        assert value == ''
        assert new_key == 'phone_number'

        value, new_key = DataHandler.validate_phone('n/a')
        assert value == ''
        assert new_key == 'phone_number'

        value, new_key = DataHandler.validate_phone('')
        assert value == ''
        assert new_key == 'phone_number'

    def test_validate_phone_failure(self, monkeypatch):
        def return_exception():
            raise Exception

        monkeypatch.setattr(
            SMSValidator, 'phone_number_format_checker', return_exception)

        with pytest.raises(Exception):
            DataHandler.validate_phone(TEST_VALUE)

    def test_validate_email_success(self, mocker):
        mocked_SMSValidator_check = mocker.patch(
            'sms.validators.SMSValidator.email_format_checker', return_value=TEST_SUCCESS_RETURN)

        value, new_key = DataHandler.validate_email(TEST_VALUE)

        mocked_SMSValidator_check.assert_called_once()
        assert value == TEST_SUCCESS_RETURN
        assert new_key == 'email'

    def test_validate_email_none(self):
        value, new_key = DataHandler.validate_email('N/A')
        assert value == ''
        assert new_key == 'email'

        value, new_key = DataHandler.validate_email('n/a')
        assert value == ''
        assert new_key == 'email'

        value, new_key = DataHandler.validate_email('')
        assert value == ''
        assert new_key == 'email'

    def test_validate_email_failure(self, monkeypatch):
        def return_exception():
            raise Exception

        monkeypatch.setattr(
            SMSValidator, 'email_format_checker', return_exception)

        with pytest.raises(Exception):
            DataHandler.validate_email(TEST_VALUE)

    def test_validate_course_success(self):
        assert DataHandler.validate_course('cna') == ('CNA', 'course')
        assert DataHandler.validate_course('nurse') == ('CNA', 'course')
        assert DataHandler.validate_course(
            'nurse assistant') == ('CNA', 'course')
        assert DataHandler.validate_course('caregiver') == ('CNA', 'course')
        assert DataHandler.validate_course('care') == ('CNA', 'course')
        assert DataHandler.validate_course('CNA') == ('CNA', 'course')
        assert DataHandler.validate_course('NURSE') == ('CNA', 'course')
        assert DataHandler.validate_course(
            'NURSE ASSISTANT') == ('CNA', 'course')
        assert DataHandler.validate_course('CAREGIVER') == ('CNA', 'course')
        assert DataHandler.validate_course('aide') == ('HHA', 'course')
        assert DataHandler.validate_course(
            'home health aide') == ('HHA', 'course')
        assert DataHandler.validate_course('hha') == ('HHA', 'course')
        assert DataHandler.validate_course('home') == ('HHA', 'course')
        assert DataHandler.validate_course('AIDE') == ('HHA', 'course')
        assert DataHandler.validate_course(
            'HOME HEALTH AIDE') == ('HHA', 'course')
        assert DataHandler.validate_course('HHA') == ('HHA', 'course')
        assert DataHandler.validate_course('HOME') == ('HHA', 'course')
        assert DataHandler.validate_course('guard') == ('SG', 'course')
        assert DataHandler.validate_course(
            'security guard') == ('SG', 'course')
        assert DataHandler.validate_course('sg') == ('SG', 'course')
        assert DataHandler.validate_course('security') == ('SG', 'course')
        assert DataHandler.validate_course('GUARD') == ('SG', 'course')
        assert DataHandler.validate_course(
            'SECURITY GUARD') == ('SG', 'course')
        assert DataHandler.validate_course('SG') == ('SG', 'course')
        assert DataHandler.validate_course('SECURITY') == ('SG', 'course')
        assert DataHandler.validate_course('english') == ('ESOL', 'course')
        assert DataHandler.validate_course('esol') == ('ESOL', 'course')
        assert DataHandler.validate_course('esl') == ('ESOL', 'course')
        assert DataHandler.validate_course('language') == ('ESOL', 'course')
        assert DataHandler.validate_course('ENGLISH') == ('ESOL', 'course')
        assert DataHandler.validate_course('ESOL') == ('ESOL', 'course')
        assert DataHandler.validate_course('ESL') == ('ESOL', 'course')
        assert DataHandler.validate_course('LANGUAGE') == ('ESOL', 'course')

    def test_validate_course_failure(self):
        with pytest.raises(Exception):
            DataHandler.validate_course(TEST_INVALID_COURSE)

    def test_validate_date_success(self):
        assert DataHandler.validate_date(
            TEST_INPUT_DATE, 'Start Date') == ('2014-01-01', 'start_date')
        assert DataHandler.validate_date(
            TEST_INPUT_DATE, 'Completion Date') == ('2014-01-01', 'completion_date')
        assert DataHandler.validate_date(TEST_INPUT_DATE, 'Date Enrollment Agreement Signed') == (
            '2014-01-01', 'date_enrollment_agreement_signed')

    def test_validate_date_none(self):
        assert DataHandler.validate_date(
            TEST_EMPTY_DATE, 'Start Date') == ('2014-01-01', 'start_date')
        assert DataHandler.validate_date(TEST_EMPTY_DATE, 'Completion Date') == (
            '2014-01-01', 'completion_date')
        assert DataHandler.validate_date(TEST_EMPTY_DATE, 'Date Enrollment Agreement Signed') == (
            '2014-01-01', 'date_enrollment_agreement_signed')

    def test_validate_date_failure(self):
        with pytest.raises(Exception):
            DataHandler.validate_date('01/01', TEST_KEY)

    def test_validate_currency_success(self):
        assert DataHandler.validate_currency(
            TEST_INPUT_CURRENCY, 'Course Cost') == ('1000.00', 'course_cost')
        assert DataHandler.validate_currency(
            TEST_INPUT_CURRENCY, 'Total Institutional Charges Charged') == ('1000.00', 'total_charges_charged')
        assert DataHandler.validate_currency(
            TEST_INPUT_CURRENCY, 'Total Institutional Charges Paid') == ('1000.00', 'total_charges_paid')

    def test_validate_currency_failure(self):
        assert DataHandler.validate_currency(
           TEST_INPUT_EMPTY_CURRENCY, 'Course Cost') == ('0.00', 'course_cost')
        assert DataHandler.validate_currency(
            TEST_INPUT_EMPTY_CURRENCY, 'Total Institutional Charges Charged') == ('0.00', 'total_charges_charged')
        assert DataHandler.validate_currency(
            TEST_INPUT_EMPTY_CURRENCY, 'Total Institutional Charges Paid') == ('0.00', 'total_charges_paid')

        assert DataHandler.validate_currency(
            TEST_INVALID_NUMBER, 'Course Cost') == ('0.00', 'course_cost')
        assert DataHandler.validate_currency(
            TEST_INVALID_NUMBER, 'Total Institutional Charges Charged') == ('0.00', 'total_charges_charged')
        assert DataHandler.validate_currency(
            TEST_INVALID_NUMBER, 'Total Institutional Charges Paid') == ('0.00', 'total_charges_paid')

    def test_validate_bool_success(self):
        assert DataHandler.validate_bool(
            TEST_Y, 'Graduates') == (True, 'graduated')
        assert DataHandler.validate_bool(
            TEST_Y, 'Passed FIrst Exam Taken') == (True, 'passed_first_exam')
        assert DataHandler.validate_bool(TEST_Y, 'Passed Second or Third Exam Taken') == (
            True, 'passed_second_or_third_exam')
        assert DataHandler.validate_bool(TEST_Y, 'Employed') == (True, 'employed')

        assert DataHandler.validate_bool(
            TEST_YES, 'Graduates') == (True, 'graduated')
        assert DataHandler.validate_bool(
            TEST_YES, 'Passed FIrst Exam Taken') == (True, 'passed_first_exam')
        assert DataHandler.validate_bool(TEST_YES, 'Passed Second or Third Exam Taken') == (
            True, 'passed_second_or_third_exam')
        assert DataHandler.validate_bool(
            TEST_YES, 'Employed') == (True, 'employed')

    def test_validate_bool_failure(self):
        assert DataHandler.validate_bool(
            TEST_INVALID_BOOL, 'Graduates') == (False, 'graduated')
        assert DataHandler.validate_bool(
            TEST_INVALID_BOOL, 'Passed FIrst Exam Taken') == (False, 'passed_first_exam')
        assert DataHandler.validate_bool('NOT A CORRECT VALUE', 'Passed Second or Third Exam Taken') == (
            False, 'passed_second_or_third_exam')
        assert DataHandler.validate_bool(
            TEST_INVALID_BOOL, 'Employed') == (False, 'employed')

        assert DataHandler.validate_bool(
            TEST_INVALID_BOOL, 'Graduates') == (False, 'graduated')
        assert DataHandler.validate_bool(
            TEST_INVALID_BOOL, 'Passed FIrst Exam Taken') == (False, 'passed_first_exam')
        assert DataHandler.validate_bool(TEST_INVALID_BOOL, 'Passed Second or Third Exam Taken') == (
            False, 'passed_second_or_third_exam')
        assert DataHandler.validate_bool(
            TEST_INVALID_BOOL, 'Employed') == (False, 'employed')

    def test_validate_hours_worked_fulltime(self):
        assert DataHandler.validate_hours_worked(
            TEST_FULLTIME_STR[0]) == ('F', 'hours_worked_weekly')
        assert DataHandler.validate_hours_worked(
            TEST_FULLTIME_STR[1]) == ('F', 'hours_worked_weekly')
        assert DataHandler.validate_hours_worked(
            TEST_FULLTIME_STR[2]) == ('F', 'hours_worked_weekly')
        assert DataHandler.validate_hours_worked(
            TEST_FULLTIME_STR[3]) == ('F', 'hours_worked_weekly')
        assert DataHandler.validate_hours_worked(
            TEST_FULLTIME_STR[4]) == ('F', 'hours_worked_weekly')
        assert DataHandler.validate_hours_worked(
            TEST_FULLTIME_STR[5]) == ('F', 'hours_worked_weekly')

    def test_validate_hours_worked_parttime(self):
        assert DataHandler.validate_hours_worked(
            TEST_PARTTIME_STR[0]) == ('P', 'hours_worked_weekly')
        assert DataHandler.validate_hours_worked(
            TEST_PARTTIME_STR[1]) == ('P', 'hours_worked_weekly')
        assert DataHandler.validate_hours_worked(
            TEST_PARTTIME_STR[2]) == ('P', 'hours_worked_weekly')
        assert DataHandler.validate_hours_worked(
            TEST_PARTTIME_STR[3]) == ('P', 'hours_worked_weekly')

    def test_validate_hours_worked_failure(self):
        assert DataHandler.validate_hours_worked(
            TEST_RANDOM_STRING) == ('P', 'hours_worked_weekly')


@pytest.mark.sms
class TestFilterHandler:
    """
    Unit tests for FilterHandler class

    """

    def test_is_valid_query_params(self):
        assert FilterHandler.is_valid_query_params(
            TEST_QUERY_PARAMS_SUCCESS, SMSFilter.Meta.fields) == True

        assert FilterHandler.is_valid_query_params(
            TEST_QUERY_PARAMS_FAILURE, SMSFilter.Meta.fields) == False
