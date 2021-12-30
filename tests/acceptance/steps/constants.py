
from tests.common_constants import *


# NOTE: PLEASE EDIT THIS FILE WITH CARE, THIS WILL BREAK ALL ACCEPTANCE/INTEGRATION TESTS RUN WITH BEHAVE


SMS_SCHOOLS_API_URL = '/api/sms/schools/'
SMS_PROGRAMS_API_URL = '/api/sms/programs/'
SMS_ROTATIONS_API_URL = '/api/sms/rotations/'
SMS_STUDENTS_API_URL = '/api/sms/students/'


SMS_STUDENT_SAMPLE_DIFF_SCHOOL_POST_DATA = {
    'student_id': 'AL-CNA-01-1019-TA',
    'first_name': 'Test',
    'last_name': 'A',
    'phone_number': '626-323-1414',
    'email': 'testa@email.com',
    'mailing_address': '1020 S. Fake STI2 Ave, TestA, CA 91770',
    'course': 'CNA',
    'start_date': '2021-10-06',
    'completion_date': '2021-12-30',
    'date_enrollment_agreement_signed': '2021-10-06',
    'third_party_payer_info': '',
    'course_cost_currency': 'USD',
    'course_cost': '2586.00',
    'total_charges_charged_currency': 'USD',
    'total_charges_charged': '2586.00',
    'total_charges_paid_currency': 'USD',
    'total_charges_paid': '2586.00',
    'paid': True,
    'graduated': True,
    'passed_first_exam': True,
    'passed_second_or_third_exam': False,
    'employed': False,
    'place_of_employment': '',
    'employment_address': '',
    'position': '',
    'starting_wage_currency': 'USD',
    'starting_wage': None,
    'hours_worked_weekly': '',
    'description_of_attempts_to_contact_student': '',
    'google_sheet_migrated': False,
    'google_sheet_migration_issue': '',
    'rotation': 'a6a1c1c3-df42-4783-9c20-49b94ad1d6ba'
}

SMS_STUDENT_SAMPLE_SAME_SCHOOL_POST_DATA = {
    'student_id': 'RO-CNA-01-1006-TA',
    'first_name': 'Test',
    'last_name': 'A',
    'phone_number': '626-323-1414',
    'email': 'testa@email.com',
    'mailing_address': '1020 S. Fake Ave, TestA, CA 91770',
    'course': 'CNA',
    'start_date': '2021-10-06',
    'completion_date': '2021-12-30',
    'date_enrollment_agreement_signed': '2021-10-06',
    'third_party_payer_info': '',
    'course_cost_currency': 'USD',
    'course_cost': '2350.00',
    'total_charges_charged_currency': 'USD',
    'total_charges_charged': '2350.00',
    'total_charges_paid_currency': 'USD',
    'total_charges_paid': '2350.00',
    'paid': True,
    'graduated': True,
    'passed_first_exam': False,
    'passed_second_or_third_exam': False,
    'employed': False,
    'place_of_employment': '',
    'employment_address': '',
    'position': '',
    'starting_wage_currency': 'USD',
    'starting_wage': None,
    'hours_worked_weekly': '',
    'description_of_attempts_to_contact_student': '',
    'google_sheet_migrated': False,
    'google_sheet_migration_issue': '',
    'rotation': 'fcd1f629-6449-4672-8dc8-4a2183cc70e9'
}

SMS_STUDENT_SAMPLE_PUT_DATA = {
    'student_id': 'RO-HHA-01-1006-TB',
    'first_name': 'Test',
    'last_name': 'B',
    'phone_number': '626-333-5544',
    'email': 'testb@email.com',
    'mailing_address': '1300 N. Fake Ave, TestB, CA 91888',
    'course': 'HHA',
    'start_date': '2021-12-09',
    'completion_date': '2021-12-10',
    'date_enrollment_agreement_signed': '2021-12-09',
    'third_party_payer_info': '',
    'course_cost_currency': 'USD',
    'course_cost': '680.00',
    'total_charges_charged_currency': 'USD',
    'total_charges_charged': '680.00',
    'total_charges_paid_currency': 'USD',
    'total_charges_paid': '600.00',
    'paid': False,
    'graduated': False,
    'passed_first_exam': False,
    'passed_second_or_third_exam': False,
    'employed': False,
    'place_of_employment': '',
    'employment_address': '',
    'position': '',
    'starting_wage_currency': 'USD',
    'starting_wage': None,
    'hours_worked_weekly': '',
    'description_of_attempts_to_contact_student': '',
    'google_sheet_migrated': False,
    'google_sheet_migration_issue': '',
    'rotation': '4481466a-7bb3-4ccc-8a51-52f4a534dd4a',

}

SMS_STUDENT_SAMPLE_PATCH_DATA = {
    'last_name': 'D'
}

SMS_GOOGLE_POST_DATA = [
    'RO-HHA-01-1006-TB',
    'test_b',
    'B',
    'Test',
    '626-333-5544',
    'testb@email.com',
    '1300 N. Fake Ave, TestB, CA 91888',
    'Home Health Aide',
    '12/9/21',
    '12/10/21',
    '12/9/21',
    '',
    '$680',
    '$680',
    '$600',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
]

SMS_GOOGLE_EDIT_CHECK_DATA = {
    'PUT_DATA': [

        'RO-HHA-01-1006-TB',
        'test_b',
        'B',
        'Test',
        '626-333-5544',
        'testb@email.com',
        '1300 N. Fake Ave, TestB, CA 91888',
        'Home Health Aide',
        '12/9/21',
        '12/10/21',
        '12/9/21',
        '',
        '$680',
        '$680',
        '$600',
    ],

    'PATCH_DATA': [

        'RO-HHA-01-1006-TB',
        'test_d',
        'D',
        'Test',
        '626-333-5544',
        'testb@email.com',
        '1300 N. Fake Ave, TestB, CA 91888',
        'Home Health Aide',
        '12/9/21',
        '12/10/21',
        '12/9/21',
        '',
        '$680',
        '$680',
        '$600',
    ],
}


SMS_SCHOOL_SAMPLE_POST_DATA = {
    'school_name': 'ST3',
    'school_code': '27091742',
    'year_founded': '2011-09-13',
    'school_address': '2209 N. San Gabriel Blvd., Suite C, Rosemead, CA 91770'
}

SMS_SCHOOL_SAMPLE_PUT_DATA = {
    'school_name': 'STI',
    'school_code': '27091743',
    'school_address': '2209 N. San Gabriel Blvd., Suite C, Rosemead, CA 91770',
    'year_founded': '2009-03-05'
}

SMS_SCHOOL_SAMPLE_PATCH_DATA = {
    'school_code': '27091744'
}
SMS_PROGRAM_SAMPLE_POST_DATA = {
    'school': '0c805318-7706-405e-a66c-5936062617a5',
    'program_name': 'SG',
    'approval_entities': ['BSIS', 'BPPE']
}
SMS_PROGRAM_SAMPLE_PUT_DATA = {
    'program_name': 'HSFA',
    'approval_entities': ['CDPH', 'BPPE'],
    'school': '0c805318-7706-405e-a66c-5936062617a5'
}

SMS_PROGRAM_SAMPLE_PATCH_DATA = {
    'program_name':  'BLS'
}

SMS_ROTATION_SAMPLE_POST_DATA = {
    'program': '67301e14-cd3d-493a-a2cf-84d8c490c0ef',
    'rotation_number': 5
}

SMS_ROTATION_SAMPLE_PUT_DATA = {
    'rotation_number': 6,
    'program': '67301e14-cd3d-493a-a2cf-84d8c490c0ef'
}

SMS_ROTATION_SAMPLE_PATCH_DATA = {
    'rotation_number': 7
}

# PUT_DATA = {
#     'school__school_code': '27091743',
#     'program__program_name': 'HSFA',
#     'rotation__rotation_number': 6

# }

# PATCH_DATA = {
#     'student__last_name': 'D',
#     'school__school_code': '27091744',
#     'program__program_name': 'BLS',
#     'rotation__rotation_number': 7
# }

JSON_PERMISSION_DENIED_RES = {
    'detail': 'You do not have permission to perform this action.'
}

JSON_SUPERUSER_ONLY_RES = {
    'detail': 'Sorry, you must be a superuser to perform this action.'
}
JSON_OBJ_NOT_FOUND_RES = None

TEST_SUPERUSER = 'testsuper'

TEST_ADMIN_USER = 'testadmin'
TEST_ADMIN_OFF_USER = 'testofficeadmin'
TEST_ADMIN_REC_USER = 'testrecruitadmin'
TEST_ADMIN_INST_USER = 'testinstructoradmin'

TEST_STAFF_USER = 'teststaff'
TEST_STAFF_OFF_USER = 'testofficestaff'
TEST_STAFF_REC_USER = 'testrecruitstaff'
TEST_STAFF_CNA_INST_USER = 'testcnainstructorstaff'
TEST_STAFF_HHA_INST_USER = 'testhhainstructorstaff'

TEST_REG_USER = 'testuser'
TEST_REG_OFF_USER = 'testofficeuser'
TEST_REG_REC_USER = 'testrecruituser'
TEST_REG_INST_CNA_USER = 'testcnainstructoruser'
TEST_REG_INST_HHA_USER = 'testhhainstructoruser'


DATADUMP_API_URL = '/api/sms/google_sheet_datadump/'
TEST_SPREADSHEET_ID = '1R0G-gByZYrDkf6Va1X3ywRA-A51nNVp_z51moOxe-VU'
TEST_SHEET_ID = '0'
TEST_SCHOOL_NAME = 'STI'

TEST_DATADUMP_DUMMY_DATA = {
    'ssid': TEST_SPREADSHEET_ID,
    'sid': TEST_SHEET_ID,
    'school_name': TEST_SCHOOL_NAME
}

TEST_DATADUMP_SUCCESS_DATA = [
    {
        'model': 'sms.rotation',
        'pk': 'dea04e7e-0d4b-4f43-a315-253d7d61d572',
        'fields': {
            'rotation_number': 1,
            'program': '0af7e2ff-1370-43fb-8bd8-6f4623ecc496'
        }
    },
    {
        'model': 'sms.student',
        'pk': '12a1b5a2-aa7a-4882-a482-0d0cbcf980d7',
        'fields': {
            'student_id': 'RO-HHA-01-1006-TB',
            'last_name': 'B',
            'first_name': 'Test',
            'phone_number': '626-333-5544',
            'email': 'testb@email.com',
            'mailing_address': '1300 N. Fake Ave, TestB, CA 91888',
            'course': 'HHA',
            'start_date': '2021-12-9',
            'completion_date': '2021-12-10',
            'date_enrollment_agreement_signed': '2021-12-9',
            'third_party_payer_info': '',
            'course_cost': '680',
            'total_charges_charged': '680',
            'total_charges_paid': '600',
            'graduated': False,
            'passed_first_exam': False,
            'passed_second_or_third_exam': False,
            'employed': False,
            'place_of_employment': '',
            'employment_address': '',
            'position': '',
            'starting_wage': None,
            'hours_worked_weekly': 'P',
            'description_of_attempts_to_contact_student': '',
            'course_cost_currency': 'USD',
            'total_charges_charged_currency': 'USD',
            'total_charges_paid_currency': 'USD',
            'starting_wage_currency': 'USD',
            'paid': False,
            'google_sheet_migrated': True,
            'google_sheet_migration_issue': '',
            'rotation': 'dea04e7e-0d4b-4f43-a315-253d7d61d572'
        }
    }
]


GMS_CNA_ROTATIONS_API_URL = '/api/gms/cnaRotations/'
GMS_HHA_ROTATIONS_API_URL = '/api/gms/hhaRotations/'
GMS_CNA_STUDENTS_API_URL = '/api/gms/cnaStudents/'
GMS_HHA_STUDENTS_API_URL = '/api/gms/hhaStudents/'
GMS_CNA_THEORY_RECORDS_API_URL = '/api/gms/cnaTheoryRecords/'
GMS_HHA_THEORY_RECORDS_API_URL = '/api/gms/hhaTheoryRecords/'
GMS_CNA_CLINICAL_RECORDS_API_URL = '/api/gms/cnaClinicalRecords/'
GMS_HHA_CLINICAL_RECORDS_API_URL = '/api/gms/hhaClinicalRecords/'

GMS_CNA_ROTATION_POST_SAMPLE_DATA = {
    'school_name': 'STI',
    'start_date': '2021-09-13',
    'end_date': '2021-10-13',
    'instructor_email': 'testcnainstructoruser@localhost',
    'rotation_num': 10,
    'instructor_title': 'LVN',
    'clinical_site': 'Rowland'
}

GMS_CNA_ROTATION_PUT_SAMPLE_DATA = {
    'school_name': 'STI',
    'start_date': '2021-09-14',
    'end_date': '2021-10-13',
    'instructor_email': 'testcnainstructoruser@localhost',
    'rotation_num': 10,
    'instructor_title': 'LVN',
    'clinical_site': 'Rowland'
}

GMS_CNA_ROTATION_PATCH_SAMPLE_DATA = {
    'start_date': '2021-09-15'
}

GMS_HHA_ROTATION_POST_SAMPLE_DATA = {
    'school_name': 'STI',
    'start_date': '2021-09-13',
    'end_date': '2021-10-13',
    'instructor_email': 'testhhainstructoruser@localhost',
    'rotation_num': 10,
    'instructor_title': 'LVN',
    'clinical_site': 'Rowland'
}

GMS_HHA_ROTATION_PUT_SAMPLE_DATA = {
    'school_name': 'STI',
    'start_date': '2021-09-14',
    'end_date': '2021-10-13',
    'instructor_email': 'testhhainstructoruser@localhost',
    'rotation_num': 10,
    'instructor_title': 'LVN',
    'clinical_site': 'Rowland'
}

GMS_HHA_ROTATION_PATCH_SAMPLE_DATA = {
    'start_date': '2021-09-15'
}

GMS_CNA_STUDENT_POST_SAMPLE_DATA = {
    'rotation': 'fdc7898d-80f0-4a48-9617-d205b1486066',
    'first_name': 'TestA',
    'last_name': 'Alpha',
    'makeup_student': False
}

GMS_CNA_STUDENT_PUT_SAMPLE_DATA = {
    'rotation': 'fdc7898d-80f0-4a48-9617-d205b1486066',
    'first_name': 'TestA',
    'last_name': 'Beta',
    'makeup_student': False
}

GMS_CNA_STUDENT_PATCH_SAMPLE_DATA = {
    'last_name': 'Gamma'
}

GMS_HHA_STUDENT_POST_SAMPLE_DATA = {
    'rotation': 'f1bd7d07-2633-4650-b85f-448f54fd3789',
    'first_name': 'TestA',
    'last_name': 'Alpha',
    'makeup_student': False
}

GMS_HHA_STUDENT_PUT_SAMPLE_DATA = {
    'rotation': 'f1bd7d07-2633-4650-b85f-448f54fd3789',
    'first_name': 'TestA',
    'last_name': 'Beta',
    'makeup_student': False
}

GMS_HHA_STUDENT_PATCH_SAMPLE_DATA = {
    'last_name': 'Gamma'
}

GMS_CNA_THEORY_RECORD_POST_SAMPLE_DATA = {
    'student': 'ccc37087-32fa-4c26-8af8-e84619dc2e47',
    'date': '2021-09-01',
    'completed': True,
    'hours_spent': 8,
    'test_score': 100,
    'topic': 'Module 1 Quiz'
}

GMS_CNA_THEORY_RECORD_PUT_SAMPLE_DATA = {
    'student': 'ccc37087-32fa-4c26-8af8-e84619dc2e47',
    'date': '2021-09-01',
    'completed': True,
    'hours_spent': 9,
    'test_score': 100,
    'topic': 'Module 2 Quiz'
}

GMS_CNA_THEORY_RECORD_PATCH_SAMPLE_DATA = {
    'hours_spent': 10
}

GMS_HHA_THEORY_RECORD_POST_SAMPLE_DATA = {
    'student': 'd4125d1a-56af-4522-846d-dd09cff85162',
    'date': '2021-09-01',
    'completed': True,
    'start_time': '22:36:21',
    'end_time': '00:00:00',
    'hours_spent': 8,
    'test_score': 50,
    'topic': 'Introduction to Aide and Agency Role'
}

GMS_HHA_THEORY_RECORD_PUT_SAMPLE_DATA = {
    'student': 'd4125d1a-56af-4522-846d-dd09cff85162',
    'date': '2021-09-01',
    'completed': True,
    'start_time': '22:36:21',
    'end_time': '00:00:00',
    'hours_spent': 9,
    'test_score': 50,
    'topic': 'Personal Care Services'
}

GMS_HHA_THEORY_RECORD_PATCH_SAMPLE_DATA = {
    'hours_spent': 10
}

GMS_CNA_CLINICAL_RECORD_POST_SAMPLE_DATA = {
    'student': 'ccc37087-32fa-4c26-8af8-e84619dc2e47',
    'date': '2021-09-01',
    'completed': True,
    'comments': '',
    'performance_satisfied': True,
    'topic': 'Knocks on door before entering'
}

GMS_CNA_CLINICAL_RECORD_PUT_SAMPLE_DATA = {
    'student': 'ccc37087-32fa-4c26-8af8-e84619dc2e47',
    'date': '2021-09-02',
    'completed': True,
    'comments': '',
    'performance_satisfied': True,
    'topic': 'Mouth care of the unconscious resident'
}

GMS_CNA_CLINICAL_RECORD_PATCH_SAMPLE_DATA = {
    'date': '2021-09-03'
}

GMS_HHA_CLINICAL_RECORD_POST_SAMPLE_DATA = {
    'student': 'd4125d1a-56af-4522-846d-dd09cff85162',
    'date': '2021-09-01',
    'completed': True,
    'hours_spent': 2,
    'comments': '',
    'performance_satisfied': True,
    'start_time': '22:38:07',
    'end_time': '00:00:00',
    'start_date': '2021-09-01',
    'end_date': '2021-09-01',
    'topic': 'Cleaning and Care Tasks in the Home'
}

GMS_HHA_CLINICAL_RECORD_PUT_SAMPLE_DATA = {
    'student': 'd4125d1a-56af-4522-846d-dd09cff85162',
    'date': '2021-09-02',
    'completed': True,
    'hours_spent': 2,
    'comments': '',
    'performance_satisfied': True,
    'start_time': '22:38:07',
    'end_time': '00:00:00',
    'start_date': '2021-09-01',
    'end_date': '2021-09-02',
    'topic': 'Nutrition'
}

GMS_HHA_CLINICAL_RECORD_PATCH_SAMPLE_DATA = {
    'end_date': '2021-09-03'
}

GMS_CNA_ROTATION_UUID_TO_TEST = 'fdc7898d-80f0-4a48-9617-d205b1486066'
GMS_HHA_ROTATION_UUID_TO_TEST = 'f1bd7d07-2633-4650-b85f-448f54fd3789'
GMS_CNA_STUDENT_UUID_TO_TEST = 'ccc37087-32fa-4c26-8af8-e84619dc2e47'
GMS_HHA_STUDENT_UUID_TO_TEST = 'd4125d1a-56af-4522-846d-dd09cff85162'
GMS_CNA_THEORY_RECORD_UUID_TO_TEST = '868769c7-0742-4ca9-bf6a-9ab5b5cc73c1'
GMS_HHA_THEORY_RECORD_UUID_TO_TEST = '8ab11f0b-6214-4f43-be18-8e1b711db6eb'
GMS_CNA_CLINICAL_RECORD_UUID_TO_TEST = 'bad5926f-3f8e-4c73-b11d-de07b0255624'
GMS_HHA_CLINICAL_RECORD_UUID_TO_TEST = '28b09da5-a7e0-4c9e-abd1-f88ec95c20b7'


# /api/gms/hhaTheoryRecords/b7b559e8-035c-4329-91c7-8800115fc2e6/
