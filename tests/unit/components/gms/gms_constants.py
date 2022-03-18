from tests.common_constants import *



CNAROTATION_STR = 'STI: CNA Rotation #1'
CNASTUDENT_STR = 'Test A'
CNATHEORYRECORD_STR = '868769c7-0742-4ca9-bf6a-9ab5b5cc73c1'
CNACLINICALRECORD_STR = 'bad5926f-3f8e-4c73-b11d-de07b0255624'

HHAROTATION_STR = 'STI: HHA Rotation #1'
HHASTUDENT_STR = 'Test B'
HHATHEORYRECORD_STR = '8ab11f0b-6214-4f43-be18-8e1b711db6eb'
HHACLINICALRECORD_STR = '28b09da5-a7e0-4c9e-abd1-f88ec95c20b7'


TEST_CNA_ROTATION = '__CNA_ROTATIONS__'
TEST_CNA_STUDENT = '__CNA_STUDENTS__'
TEST_CNA_THEORY_RECORD = '__CNA_THEORY_RECORD__'
TEST_CNA_CLINICAL_RECORD = '__CNA_CLINICAL_RECORD__'



TEST_HHA_ROTATION = '__HHA_ROTATIONS__'
TEST_HHA_STUDENT = '__HHA_STUDENTS__'
TEST_HHA_THEORY_RECORD = '__HHA_THEORY_RECORD__'
TEST_HHA_CLINICAL_RECORD = '__HHA_CLINICAL_RECORD__'



TEST_GMS_ROTATION_QUERY_PARAMS_SUCCESS = {
    'start_date': '2021-10-11',
    'end_date': '2021-10-12',
    'rotation_num' : 10
}

TEST_GMS_STUDENT_QUERY_PARAMS_SUCCESS = {
    'first_name': 'Test',
    'last_name': 'A',
    'makeup_student': True
}

TEST_GMS_RECORD_QUERY_PARAMS_SUCCESS = {
    'date': '2021-10-11',
    'completed' : True,
    'topic' : '__RANDOM__'
}

TEST_QUERY_PARAMS_FAILURE = {
    '__INCORRECT_PARAM_NAME__': '__RANDOM_STRING__'
}



# used by gms.permissions
AUTH_REG_HHA_INSTR_MSG = 'Please be sure to log in with a HHA intructor account and try again.'
AUTH_REG_CNA_INSTR_MSG = 'Please be sure to log in with a CNA intructor account and try again.'
AUTH_STAFF_HHA_INSTR_MSG = 'Please be sure to log in with a HHA staff instructor account and try again.'
AUTH_STAFF_CNA_INSTR_MSG = 'Please be sure to log in with a CNA staff instructor account and try again.'
AUTH_ADMIN_INSTR_MSG = 'Please be sure to log in with an admin instructor account and try again.'
AUTH_SUPERUSER_MSG = 'Sorry, you must be a superuser to perform this action.'





# used by gms.validators
TEST_STUDENT_UUID = '__TEST_STUDENT_UUID__'
TEST_RECORD_TOPIC = '__RANDOM_TOPIC__'