# constants data for behave testing
# change this if test-sms-initial-data.json changes
SCHOOLS_API_URL = '/api/sms/schools/'
PROGRAMS_API_URL = '/api/sms/programs/'
ROTATIONS_API_URL = '/api/sms/rotations/'
STUDENTS_API_URL = '/api/sms/students/'

# NOTE THE UUID CONTANTS NEEDS TO BE UPDATED IF TEST FIXTURES ARE UPDATED
STUDENT_UUID_TO_TEST = 'db7d3163-7856-4b61-b242-65ef034c4bfe'
SCHOOL_UUID_TO_TEST = '6bfad48c-ecc6-44ac-b53f-c94ccd240119'
PROGRAM_UUID_TO_TEST = 'de47da61-278f-4f67-8fbf-7e60de40e9d4'
ROTATION_UUID_TO_TEST = 'a6a1c1c3-df42-4783-9c20-49b94ad1d6ba'

STUDENT_SAMPLE_DIFF_SCHOOL_POST_DATA = {
    'student_uuid': '7766c4a3-877c-4c23-b3e6-e7ab9ef43c97',
    'student_id': '01-1019-TA',
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
    'student_uuid': '90f120c5-1894-4afc-b204-a912172570a5',
    'student_id': '01-1006-TA',
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

SCHOOL_SAMPLE_POST_DATA = {
    'school_name': 'ST3',
    'school_code': '27091742',
    'year_founded': '2011-09-13',
    'school_address': '2209 N. San Gabriel Blvd., Suite C, Rosemead, CA 91770'
}

PROGRAM_SAMPLE_POST_DATA = {
    'school': '6bfad48c-ecc6-44ac-b53f-c94ccd240119',
    'program_name': 'SG',
    'approval_entities': ['BSIS', 'BPPE']
}

ROTATION_SAMPLE_POST_DATA = {
    'program': 'de47da61-278f-4f67-8fbf-7e60de40e9d4',
    'rotation_number': 5
}

FILTER_PARAMS = {
    'school_name' : 'STI',
    'program_name': 'HHA',
    'rotation_num': 1,
    'first_name': 'Test',
    'last_name': 'B',
    'email': 'testb@email.com',
    'phone': '626-333-5544',
    'id_': '01-1019-TB',
    'start_date': '2021-10-06',
    'completion_date': '2021-12-10',
    'paid': 'True',
    'graduated': 'True',
    'employed': 'False'
}