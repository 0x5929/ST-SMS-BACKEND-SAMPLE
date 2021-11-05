
# NOTE: PLEASE EDIT THIS FILE WITH CARE, THIS WILL BREAK ALL ACCEPTANCE/INTEGRATION TESTS RUN WITH BEHAVE


# constants data for behave testing
# change this if test-sms-initial-data.json changes
SCHOOLS_API_URL = '/api/sms/schools/'
PROGRAMS_API_URL = '/api/sms/programs/'
ROTATIONS_API_URL = '/api/sms/rotations/'
STUDENTS_API_URL = '/api/sms/students/'

# NOTE THE UUID CONTANTS NEEDS TO BE UPDATED IF TEST FIXTURES ARE UPDATED
STUDENT_UUID_TO_TEST = 'db7d3163-7856-4b61-b242-65ef034c4bfe'
SCHOOL_UUID_TO_TEST = '0c805318-7706-405e-a66c-5936062617a5'
PROGRAM_UUID_TO_TEST = '67301e14-cd3d-493a-a2cf-84d8c490c0ef'
ROTATION_UUID_TO_TEST = 'fcd1f629-6449-4672-8dc8-4a2183cc70e9'

STUDENT_SAMPLE_DIFF_SCHOOL_POST_DATA = {
    #  'student_uuid': '7766c4a3-877c-4c23-b3e6-e7ab9ef43c97',
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

STUDENT_SAMPLE_SAME_SCHOOL_POST_DATA = {
    #   'student_uuid': '90f120c5-1894-4afc-b204-a912172570a5',
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

STUDENT_SAMPLE_PUT_DATA = {
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
    'rotation': '4481466a-7bb3-4ccc-8a51-52f4a534dd4a'

}

GOOGLE_POST_DATA = [
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

# 		B							12/10/21	12/9/21			$680	$600
SCHOOL_SAMPLE_POST_DATA = {
    'school_name': 'ST3',
    'school_code': '27091742',
    'year_founded': '2011-09-13',
    'school_address': '2209 N. San Gabriel Blvd., Suite C, Rosemead, CA 91770'
}

PROGRAM_SAMPLE_POST_DATA = {
    'school': '0c805318-7706-405e-a66c-5936062617a5',
    'program_name': 'SG',
    'approval_entities': ['BSIS', 'BPPE']
}

ROTATION_SAMPLE_POST_DATA = {
    'program': '67301e14-cd3d-493a-a2cf-84d8c490c0ef',
    'rotation_number': 5
}

# this is the STI HHA student, please change this if test fixture changes
FILTER_PARAMS = {
    'school_name': 'STI',
    'program_name': 'HHA',
    'rotation_num': 1,
    'first_name': 'Test',
    'last_name': 'B',
    'email': 'testb@email.com',
    'phone': '626-333-5544',
    'id_': 'RO-HHA-01-1006-TB',
    'start_date': '2021-12-09',
    'completion_date': '2021-12-10',
    'paid': 'False',
    'graduated': 'False',
    'employed': 'False'
}

PUT_DATA = {
    'student__last_name': 'C',
    'school__school_code': '27091743',
    'program__program_name': 'HSFA',
    'rotation__rotation_number': 6

}

PATCH_DATA = {
    'student__last_name': 'D',
    'school__school_code': '27091744',
    'program__program_name': 'BLS',
    'rotation__rotation_number': 7
}

JSON_PERMISSION_DENIED_RES = {
    'detail': 'You do not have permission to perform this action.'
}

# JSON_OBJ_NOT_FOUND_RES = {
#     'detail': 'Not found.'
# }
JSON_OBJ_NOT_FOUND_RES = None

TEST_SUPERUSER = 'testsuper'

TEST_ADMIN_USER = 'testadmin'
TEST_ADMIN_OFF_USER = 'testofficeadmin'
TEST_ADMIN_REC_USER = 'testrecruitadmin'
TEST_ADMIN_INST_USER = 'testinstructoradmin'

TEST_STAFF_USER = 'teststaff'
TEST_STAFF_OFF_USER = 'testofficestaff'
TEST_STAFF_REC_USER = 'testrecruitstaff'
TEST_STAFF_INST_USER = 'testinstructorstaff'

TEST_REG_USER = 'testuser'
TEST_REG_OFF_USER = 'testofficeuser'
TEST_REG_REC_USER = 'testrecruituser'
TEST_REG_INST_USER = 'testinstructoruser'
