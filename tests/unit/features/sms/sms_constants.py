from tests.common_constants import *

# sms.models testing constants
SCHOOL_STR = 'STI'
PROGRAM_STR = 'STI: CNA'
ROTATION_STR = 'STI: CNA Rotation# 99'
STUDENT_STR = 'test_b'
TEST_ROTATION_SIZE = 1

TEST_UNPAID_CHARGES_PAID = '99.00'
TEST_UNPAID_CHARGES_CHARGED = '100.00'

# sms.utils testing constants
TEST_DICT_DATA = {
    'first_value': 0,
    'second_value': 1,
    'third_value': 2,
    'fourth_value': 3,
    'fifth_value': 4,
    'sixth_value': 5
}
TEST_QUERY_PARAMS_SUCCESS = {
    'first_name': 'John',
    'last_name': 'Doe'
}
TEST_QUERY_PARAMS_FAILURE = {
    '__INCORRECT_PARAM_NAME__': '__RANDOM_STRING__'
}

TEST_INVALID_COURSE = '__INVALID_COURSE__'
TEST_INVALID_NUMBER = '__INVALID_NUMBER__'
TEST_INVALID_BOOL = '__NOT_A_VALID_VALUE__'
TEST_RANDOM_STRING = '__RANDOM_STRING__'
TEST_EMPTY_DATE = ''
TEST_INPUT_DATE = '01/01/14'
TEST_INPUT_CURRENCY = '$1,000.00'
TEST_INPUT_EMPTY_CURRENCY = ''
TEST_Y = 'Y'
TEST_YES = 'YES'
TEST_FULLTIME_STR = ['MORE THAN 32','OVER 32 HOURS','AT LEAST 32 HOURS','40/WEEK','F','FULLTIME']
TEST_PARTTIME_STR = ['LESS THAN 32','UNDER 32 HOURS','P','PARTTIME']

# sms.google_sheets sms.data_operations testing constants (used some in sms.utils as well)
TEST_SPREADSHEET_ID = '1R0G-gByZYrDkf6Va1X3ywRA-A51nNVp_z51moOxe-VU'
TEST_DB_SHEET_ID = '0'
TEST_PROGRAM_NAME = 'CNA'
TEST_ROT_NUM = '1'
TEST_KEY = '__TEST_KEY__'
TEST_VALUE = '__TEST_VALUE__'
TEST_RECORD = {
    TEST_KEY: TEST_VALUE
}
TEST_RECORD_HEADER = TEST_KEY
TEST_INDEX = 0

# NOTE: this is dependent on headers and their validation defined in sms.google_sheets.ExportHandler
TEST_HEADERS_AND_VALIDATIONS = {
    'Student ID': 'validate_student_id',
    'Full Name': 'validate_string',
    'Last Name': 'validate_string',
    'First Name': 'validate_string',
    'Phone Number': 'validate_phone',
    'Email Address': 'validate_email',
    'Mailing Address': 'validate_string',
    'Course': 'validate_course',
    'Start Date': 'validate_date',
    'Completion Date': 'validate_date',
    'Date Enrollment Agreement Signed': 'validate_date',
    'Third-party payer identifying information': 'validate_string',
    'Course Cost': 'validate_currency',
    'Total Institutional Charges Charged': 'validate_currency',
    'Total Institutional Charges Paid': 'validate_currency',
    'Graduates': 'validate_bool',
    'Passed FIrst Exam Taken': 'validate_bool',
    'Passed Second or Third Exam Taken': 'validate_bool',
    'Employed': 'validate_bool',
    'Place of Employment': 'validate_string',
    'Employment Address': 'validate_string',
    'Position': 'validate_string',
    'Starting Wage': 'validate_wage',
    'Hours Worked per Week': 'validate_hours_worked',
    'Description of Attempts to Contact Students': 'validate_string'
}

TEST_STUDENT_ID = 'RO-CNA-01-0101-JD'
TEST_ROW_NUM = '1'

TEST_SCHOOL_NAME_AND_INTERNAL_NAME = (('RO', 'STI'), ('AL', 'ST2'))

TEST_SUCCESS_RETURN = '__SUCCESS_RETURN__'


TEST_NON_MATCH_SID = '__UNMATCHING_STUDENT_ID__'

TEST_SCHOOL_UUID = '__TEST_SCHOOL_UUID__'
TEST_PROGRAM_UUID = '__TEST_PROGRAM_UUID__'
TEST_ROTATION_UUID = '__TEST_ROTATION_UUID__'
TEST_STUDENT_UUID = '__TEST_STUDENT_UUID__'
TEST_PK = '__TEST_PK__'

TEST_CHARGES_PAID = '1.00'
TEST_CHARGES_CHARGED = '1.00'

# used by sms.permissions
AUTH_OFFICE_USER_READ_ONLY_MSG = 'Sorry, you must be at least authenticated and an office user to perform this action.'
AUTH_OFFICE_USER_NO_DEL_MSG = 'Sorry, you must be an office user to perform this action.'
AUTH_OFFICE_STAFF_MSG = 'Sorry, you must be an office administrator to perform this action.'
AUTH_OFFICE_AMDIN_MSG = 'Sorry, you must be an office administrator to perform this action.'
AUTH_SUPERUSER_MSG = 'Sorry, you must be a superuser to perform this action.'

# used by sms.managers
TEST_SCHOOL_FILTER = '__SCHOOL_FILTER__'
TEST_SCHOOL_ALL = '__SCHOOL_ALL__'
TEST_PROGRAM_FILTER = '__PROGRAM_FILTER__'
TEST_PROGRAM_ALL = '__PROGRAM_ALL__'
TEST_ROTATION_FILTER = '__ROTATION_FILTER__'
TEST_ROTATION_ALL = '__ROTATION_ALL__'
TEST_STUDENT_FILTER = '__STUDENT_FILTER__'
TEST_STUDENT_ALL = '__STUDENT_ALL__'

# used by sms.validators
TEST_NOCAP_MATCHING_STR = 'matching string'

TEST_MATCHING_STUDENT_ID = ['RO-CNA-01-0101-JD', 'AL-CNA-01-0101-JD',
                        'RO-HHA-01-0101-JD', 'RO-SG-100-0101-JD']

TEST_NON_MATCHING_STUDENT_ID = ['01-0101-JD', 'CNA-01-0101-JD',
                            'RA-CNA-01-0101-JD', 'RO-RAND-01-0101-JD']

TEST_NON_MATCHING_EMAILS = ['123456798@', '123456789.', 'asdf com']
TEST_DIFF_SCHOOL_NAME = 'ST2'
TEST_DIFF_PROG_NAME = 'HHA'
