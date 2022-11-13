
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
    'starting_wage': '0.00',
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
    'starting_wage': '0.00',
    'hours_worked_weekly': '',
    'description_of_attempts_to_contact_student': '',
    'google_sheet_migrated': False,
    'google_sheet_migration_issue': '',
    'rotation': 'fcd1f629-6449-4672-8dc8-4a2183cc70e9'
}


SMS_ST2_STUDENT_SAMPLE_POST_DATA = {
    'student_id': 'AL-HHA-01-1019-AD',
    'first_name': 'Alvinia',
    'last_name': 'Dipmonks',
    'phone_number': '626-555-3345',
    'email': 'alvinia@email.com',
    'mailing_address': '1020 S. Fake STI2 HHA Student Ave, Alvina, CA 91770',
    'course': 'HHA',
    'start_date': '2021-10-06',
    'completion_date': '2021-12-11',
    'date_enrollment_agreement_signed': '2021-10-06',
    'third_party_payer_info': '',
    'course_cost_currency': 'USD',
    'course_cost': '680.00',
    'total_charges_charged_currency': 'USD',
    'total_charges_charged': '680.00',
    'total_charges_paid_currency': 'USD',
    'total_charges_paid': '680.00',
    'paid': True,
    'graduated': True,
    'passed_first_exam': True,
    'passed_second_or_third_exam': False,
    'employed': True,
    'place_of_employment': '',
    'employment_address': '',
    'position': '',
    'starting_wage_currency': 'USD',
    'starting_wage': '0.00',
    'hours_worked_weekly': '',
    'description_of_attempts_to_contact_student': '',
    'google_sheet_migrated': False,
    'google_sheet_migration_issue': '',
    'rotation': '37b61d4e-ab68-4f49-ae8c-d742da756fcc'
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
    'starting_wage': '0.00',
    'hours_worked_weekly': '',
    'description_of_attempts_to_contact_student': '',
    'google_sheet_migrated': False,
    'google_sheet_migration_issue': '',
    'rotation': '4481466a-7bb3-4ccc-8a51-52f4a534dd4a',

}

SMS_ST2_STUDENT_SAMPLE_PUT_DATA = {
    'student_id': 'AL-HHA-01-1019-AC',
    'first_name': 'Alvinia',
    'last_name': 'Chipmonks',
    'phone_number': '626-555-3345',
    'email': 'alvinia@email.com',
    'mailing_address': '1020 S. Fake STI2 HHA Student Ave, Alvina, CA 91770',
    'course': 'HHA',
    'start_date': '2021-10-06',
    'completion_date': '2021-12-11',
    'date_enrollment_agreement_signed': '2021-10-06',
    'third_party_payer_info': '',
    'course_cost_currency': 'USD',
    'course_cost': '680.00',
    'total_charges_charged_currency': 'USD',
    'total_charges_charged': '680.00',
    'total_charges_paid_currency': 'USD',
    'total_charges_paid': '680.00',
    'paid': True,
    'graduated': True,
    'passed_first_exam': True,
    'passed_second_or_third_exam': False,
    'employed': True,
    'place_of_employment': '',
    'employment_address': '',
    'position': '',
    'starting_wage_currency': 'USD',
    'starting_wage': '0.00',
    'hours_worked_weekly': '',
    'description_of_attempts_to_contact_student': '',
    'google_sheet_migrated': False,
    'google_sheet_migration_issue': '',
    'rotation': '37b61d4e-ab68-4f49-ae8c-d742da756fcc'
}

SMS_FILTER_ROATAION_PARAM = {
    'school_name' : 'STI',
    'program_name': 'HHA',
    'program_uuid': '0af7e2ff-1370-43fb-8bd8-6f4623ecc496'
}

SMS_FILTER_PROGRAM_PARAM = {
    'school_name': 'STI',
    'school_uuid': '0c805318-7706-405e-a66c-5936062617a5'
}

SMS_STUDENT_SAMPLE_PATCH_DATA = {
    'last_name': 'D'
}

SMS_ST2_STUDENT_SAMPLE_PATCH_DATA = {
    'last_name': 'Mctest'
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

SMS_ST2_GOOGLE_POST_DATA = [
    'AL-HHA-01-1019-TB',
    'alvin_mctest',
    'Chipmonk',
    'Alvin',
    '626-333-5545',
    'alvin@email.com',
    '1020 S. Fake STI2 HHA Student Ave, TestA, CA 91770',
    'Home Health Aide',
    '10/6/21',
    '12/11/21',
    '10/6/21',
    '',
    '$680',
    '$680',
    '$680',
    'Y',
    'Y',
    '',
    'Y',
    '',
    '',
    '',
    '',
    '',
    'Information provided by ST office contacting students via phone/text/email.'
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
        '$600'
    ],
}


SMS_ST2_GOOGLE_EDIT_CHECK_DATA = {
    'PUT_DATA': [

        'AL-HHA-01-1019-AC',
        'alvinia_chipmonks',
        'Chipmonks',
        'Alvinia',
        '626-555-3345',
        'alvinia@email.com',
        '1020 S. Fake STI2 HHA Student Ave, Alvina, CA 91770',
        'Home Health Aide',
        '10/6/21',
        '12/11/21',
        '10/6/21',
        '',
        '$680',
        '$680',
        '$680',
        'Y',
        'Y',
        '',
        'Y'
    ],

    'PATCH_DATA': [

        'AL-HHA-01-1019-TB',
        'alvin_mctest',
        'Mctest',
        'Alvin',
        '626-333-5545',
        'alvin@email.com',
        '1020 S. Fake STI2 HHA Student Ave, TestA, CA 91770',
        'Home Health Aide',
        '10/6/21',
        '12/11/21',
        '10/6/21',
        '',
        '$680',
        '$680',
        '$680',
        'Y',
        'Y',
        '',
        'Y'
    ],
}


SMS_SCHOOL_SAMPLE_POST_DATA = {
    'school_name': 'ST3',
    'school_code': '27091742',
    'year_founded': '2011-09-13',
    'school_address': '2209 N. San Gabriel Blvd., Suite C, Rosemead, CA 91770'
}

SMS_ST2_SCHOOL_SAMPLE_POST_DATA = {
    'school_name': 'ST2',
    'school_code': '27091738',
    'school_address': '2209 N. San Gabriel Blvd., Suite C, Rosemead, CA 91770',
    'year_founded': '2009-03-10'
}

SMS_SCHOOL_SAMPLE_PUT_DATA = {
    'school_name': 'STI',
    'school_code': '27091743',
    'school_address': '2209 N. San Gabriel Blvd., Suite C, Rosemead, CA 91770',
    'year_founded': '2009-03-05'
}

SMS_ST2_SCHOOL_SAMPLE_PUT_DATA = {
    'school_name': 'ST2',
    'school_code': '27091748',
    'school_address': '2209 N. San Gabriel Blvd., Suite C, Rosemead, CA 91770',
    'year_founded': '2009-03-10'
}

SMS_SCHOOL_SAMPLE_PATCH_DATA = {
    'school_code': '27091744'
}

SMS_ST2_SCHOOL_SAMPLE_PATCH_DATA = {
    'school_code': '27091749'
}

SMS_PROGRAM_SAMPLE_POST_DATA = {
    'school': '0c805318-7706-405e-a66c-5936062617a5',
    'program_name': 'SG',
    'approval_entities': ['BSIS', 'BPPE']
}


SMS_ST2_PROGRAM_SAMPLE_POST_DATA = {
    'school': '6bfad48c-ecc6-44ac-b53f-c94ccd240119',
    'program_name': 'HSFA',
    'approval_entities': ['CDPH', 'BPPE'],
}


SMS_PROGRAM_SAMPLE_PUT_DATA = {
    'program_name': 'BLS',
    'approval_entities': ['CDPH', 'BPPE'],
    'school': '0c805318-7706-405e-a66c-5936062617a5'
}

SMS_ST2_PROGRAM_SAMPLE_PUT_DATA = {
    'program_name': 'HSFA',
    'approval_entities': ['CDPH', 'BPPE'],
    'school': '6bfad48c-ecc6-44ac-b53f-c94ccd240119'
}


SMS_PROGRAM_SAMPLE_PATCH_DATA = {
    'program_name':  'BLS'
}


SMS_ST2_PROGRAM_SAMPLE_PATCH_DATA = {
    'program_name':  'ESOL'
}

SMS_ROTATION_SAMPLE_POST_DATA = {
    'program': '67301e14-cd3d-493a-a2cf-84d8c490c0ef',
    'rotation_number': 5
}

SMS_ST2_ROTATION_SAMPLE_POST_DATA = {
    'program': 'd682ebed-72a4-499f-9bd5-4ce777c492cd',
    'rotation_number': 50
}

SMS_ROTATION_SAMPLE_PUT_DATA = {
    'rotation_number': 6,
    'program': '67301e14-cd3d-493a-a2cf-84d8c490c0ef'
}

SMS_ST2_ROTATION_SAMPLE_PUT_DATA = {
    'rotation_number': 60,
    'program': 'd682ebed-72a4-499f-9bd5-4ce777c492cd'
}

SMS_ROTATION_SAMPLE_PATCH_DATA = {
    'rotation_number': 7
}

SMS_ST2_ROTATION_SAMPLE_PATCH_DATA = {
    'rotation_number': 70
}

JSON_PERMISSION_DENIED_RES = {
    'detail': 'You do not have permission to perform this action.'
}


JSON_SUPERUSER_ONLY_RES = {
    'detail': 'Sorry, you must be a superuser to perform this action.'
}

JSON_OBJ_NOT_FOUND_RES = None

JSON_404_NOT_FOUND_RES = {
    'detail': 'Not found.'
}

# JSON_400_CROSS_SCHOOL_ADD_ERR = {
#     'non_field_errors' : ["You are adding a student record for the wrong school's program rotation, please add to your own school's program rotation"]
# }

SMS_STUDENT_STATISTIC_SAMPLE_DATA = [
    {
        'enrollment': [
            {'year': 2013, 'count': 0},
            {'year': 2014, 'count': 0},
            {'year': 2015, 'count': 0},
            {'year': 2016, 'count': 0},
            {'year': 2017, 'count': 0},
            {'year': 2018, 'count': 0},
            {'year': 2019, 'count': 0},
            {'year': 2020, 'count': 0},
            {'year': 2021, 'count': 3},
            {'year': 2022, 'count': 0},
        ],
        'employment': [
            {'year': 2013, 'count': 0},
            {'year': 2014, 'count': 0},
            {'year': 2015, 'count': 0},
            {'year': 2016, 'count': 0},
            {'year': 2017, 'count': 0},
            {'year': 2018, 'count': 0},
            {'year': 2019, 'count': 0},
            {'year': 2020, 'count': 0},
            {'year': 2021, 'count': 1},
            {'year': 2022, 'count': 0},
        ],
        'graduate': [
            {'year': 2013, 'count': 0},
            {'year': 2014, 'count': 0},
            {'year': 2015, 'count': 0},
            {'year': 2016, 'count': 0},
            {'year': 2017, 'count': 0},
            {'year': 2018, 'count': 0},
            {'year': 2019, 'count': 0},
            {'year': 2020, 'count': 0},
            {'year': 2021, 'count': 1},
            {'year': 2022, 'count': 0},
        ],
        'exam': [
            {'year': 2013, 'count': 0},
            {'year': 2014, 'count': 0},
            {'year': 2015, 'count': 0},
            {'year': 2016, 'count': 0},
            {'year': 2017, 'count': 0},
            {'year': 2018, 'count': 0},
            {'year': 2019, 'count': 0},
            {'year': 2020, 'count': 0},
            {'year': 2021, 'count': 2},
            {'year': 2022, 'count': 0},
        ]
    }
]

JSON_400_CROSS_SCHOOL_ADD_ERR = {
    'non_field_errors': ["You may only work on your own school's resource, please try changing the school name."]
}

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
TEST_REG_INST_USER = 'testinstructoruser'
TEST_REG_INST_CNA_USER = 'testcnainstructoruser'
TEST_REG_INST_HHA_USER = 'testhhainstructoruser'
TEST_REG_INST_CNA_USER2 = 'testcnainstructoruser2'
TEST_REG_INST_HHA_USER2 = 'testhhainstructoruser2'


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
            'starting_wage': '0.00',
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
    'instructor_email': ['testcnainstructoruser@localhost'],
    'rotation_num': 10,
    'instructor_title': 'LVN',
    'clinical_site': 'Rowland'
}

GMS_ST2_CNA_ROTATION_POST_SAMPLE_DATA = {
    'school_name': 'ST2',
    'start_date': '2021-02-18',
    'end_date': '2021-10-18',
    'instructor_email': ['testcnainstructoruser2@localhost'],
    'rotation_num': 22,
    'instructor_title': 'LVN',
    'clinical_site': 'Rowland'
}

GMS_CNA_ROTATION_PUT_SAMPLE_DATA = {
    'school_name': 'STI',
    'start_date': '2021-09-14',
    'end_date': '2021-10-13',
    'instructor_email': ['testcnainstructoruser@localhost'],
    'rotation_num': 10,
    'instructor_title': 'LVN',
    'clinical_site': 'Rowland'
}

GMS_ST2_CNA_ROTATION_PUT_SAMPLE_DATA = {
    'school_name': 'ST2',
    'start_date': '2021-11-06',
    'end_date': '2021-11-30',
    'instructor_email': ['testcnainstructoruser2@localhost'],
    'rotation_num': 30,
    'instructor_title': 'LVN',
    'clinical_site': 'Rowland'
}

GMS_CNA_ROTATION_PATCH_SAMPLE_DATA = {
    'start_date': '2021-09-15'
}

GMS_ST2_CNA_ROTATION_PATCH_SAMPLE_DATA = {
    'clinical_site': 'Sunnyview'
}


GMS_HHA_ROTATION_POST_SAMPLE_DATA = {
    'school_name': 'STI',
    'start_date': '2021-09-13',
    'end_date': '2021-10-13',
    'instructor_email': ['testhhainstructoruser@localhost'],
    'rotation_num': 10,
    'instructor_title': 'LVN',
    'clinical_site': 'Rowland'
}

# NOTE: REMEMBER that PUT and PATCH and DELETE data is for changing the data we already have installed in DB as fixtures, POST is completely new data we are testing to install
# NOTE: but also I would try not to interfere with filter params of ST2 too, for all POST PUT PATCH and DELETE, so the other tests with gms.filter wouldnt break. hopefully lol

GMS_ST2_HHA_ROTATION_POST_SAMPLE_DATA = {
    'school_name': 'ST2',
    'start_date': '2021-09-03',
    'end_date': '2021-11-03',
    'instructor_email': ['testhhainstructoruser@localhost'],
    'rotation_num': 45,
    'instructor_title': 'LVN',
    'clinical_site': 'Rowland'
}

GMS_HHA_ROTATION_PUT_SAMPLE_DATA = {
    'school_name': 'STI',
    'start_date': '2021-09-14',
    'end_date': '2021-10-13',
    'instructor_email': ['testhhainstructoruser@localhost'],
    'rotation_num': 10,
    'instructor_title': 'LVN',
    'clinical_site': 'Rowland'
}

GMS_ST2_HHA_ROTATION_PUT_SAMPLE_DATA = {
    'school_name': 'ST2',
    'start_date': '2021-09-14',
    'end_date': '2021-10-13',
    'instructor_email': ['testhhainstructoruser@localhost'],
    'rotation_num': 10,
    'instructor_title': 'LVN',
    'clinical_site': 'Rowland'
}

GMS_HHA_ROTATION_PATCH_SAMPLE_DATA = {
    'start_date': '2021-09-15'
}

GMS_ST2_HHA_ROTATION_PATCH_SAMPLE_DATA = {
    'clinical_site': 'Pinegrove'
}

GMS_CNA_STUDENT_POST_SAMPLE_DATA = {
    'rotation': 'fdc7898d-80f0-4a48-9617-d205b1486066',
    'first_name': 'TestA',
    'last_name': 'Alpha',
    'makeup_student': False
}

GMS_ST2_CNA_STUDENT_POST_SAMPLE_DATA = {
    'rotation': 'b42249ec-b354-4ff6-9ffa-f88454fdcd21',
    'first_name': 'TestST2',
    'last_name': 'CNAStudent',
    'makeup_student': False
}


GMS_CNA_STUDENT_PUT_SAMPLE_DATA = {
    'rotation': 'fdc7898d-80f0-4a48-9617-d205b1486066',
    'first_name': 'TestA',
    'last_name': 'Beta',
    'makeup_student': False
}


GMS_ST2_CNA_STUDENT_PUT_SAMPLE_DATA = {
    'rotation': 'fdc7898d-80f0-4a48-9617-d205b1486066',
    'first_name': 'Test',
    'last_name': 'Z',
    'makeup_student': True
}

GMS_CNA_STUDENT_PATCH_SAMPLE_DATA = {
    'last_name': 'Gamma'
}

GMS_ST2_CNA_STUDENT_PATCH_SAMPLE_DATA = {
    'last_name': 'Gamma'
}

GMS_HHA_STUDENT_POST_SAMPLE_DATA = {
    'rotation': 'f1bd7d07-2633-4650-b85f-448f54fd3789',
    'first_name': 'TestA',
    'last_name': 'Alpha',
    'makeup_student': False
}

GMS_ST2_HHA_STUDENT_POST_SAMPLE_DATA = {
    'rotation': '37e1c605-aced-40b6-a3fb-bf2776207f52',
    'first_name': 'TestAAA',
    'last_name': 'AlphaBeta',
    'makeup_student': False
}

GMS_HHA_STUDENT_PUT_SAMPLE_DATA = {
    'rotation': 'f1bd7d07-2633-4650-b85f-448f54fd3789',
    'first_name': 'TestA',
    'last_name': 'Beta',
    'makeup_student': False
}


GMS_ST2_HHA_STUDENT_PUT_SAMPLE_DATA = {
    'rotation': '37e1c605-aced-40b6-a3fb-bf2776207f52',
    'first_name': 'Test',
    'last_name': 'Y',
    'makeup_student': False
}

GMS_HHA_STUDENT_PATCH_SAMPLE_DATA = {
    'last_name': 'Gamma'
}


GMS_ST2_HHA_STUDENT_PATCH_SAMPLE_DATA = {
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


GMS_ST2_CNA_THEORY_RECORD_POST_SAMPLE_DATA = {
    'student': '2ad62709-e450-4498-a28b-df0f8990e9ac',
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


GMS_ST2_CNA_THEORY_RECORD_PUT_SAMPLE_DATA = {
    'student': '2ad62709-e450-4498-a28b-df0f8990e9ac',
    'date': '2021-11-06',
    'completed': False,
    'hours_spent': 1,
    'test_score': 75,
    'topic': 'Module 3 Quiz'
}

GMS_CNA_THEORY_RECORD_PATCH_SAMPLE_DATA = {
    'hours_spent': 10
}


GMS_ST2_CNA_THEORY_RECORD_PATCH_SAMPLE_DATA = {
    'hours_spent': 9
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


GMS_ST2_HHA_THEORY_RECORD_POST_SAMPLE_DATA = {
    'student': 'c13a0659-64cc-4bcb-a153-ba8415f05bd0',
    'date': '2021-11-10',
    'completed': True,
    'start_time': '22:36:21',
    'end_time': '00:00:01',
    'hours_spent': 8,
    'test_score': 55,
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


GMS_ST2_HHA_THEORY_RECORD_PUT_SAMPLE_DATA = {
    'student': 'c13a0659-64cc-4bcb-a153-ba8415f05bd0',
    'date': '2021-11-08',
    'completed': False,
    'start_time': '22:36:21',
    'end_time': '00:00:00',
    'hours_spent': 2,
    'test_score': 40,
    'topic': 'Personal Care Services'
}


GMS_HHA_THEORY_RECORD_PATCH_SAMPLE_DATA = {
    'hours_spent': 10
}

GMS_ST2_HHA_THEORY_RECORD_PATCH_SAMPLE_DATA = {
    'hours_spent': 8
}

GMS_CNA_CLINICAL_RECORD_POST_SAMPLE_DATA = {
    'student': 'ccc37087-32fa-4c26-8af8-e84619dc2e47',
    'date': '2021-09-01',
    'completed': True,
    'comments': '',
    'performance_satisfied': True,
    'topic': 'Knocks on door before entering'
}


GMS_ST2_CNA_CLINICAL_RECORD_POST_SAMPLE_DATA = {
    'student': '2ad62709-e450-4498-a28b-df0f8990e9ac',
    'date': '2020-12-01',
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

GMS_ST2_CNA_CLINICAL_RECORD_PUT_SAMPLE_DATA = {
    'student': '2ad62709-e450-4498-a28b-df0f8990e9ac',
    'date': '2021-11-07',
    'completed': False,
    'comments': '',
    'performance_satisfied': True,
    'topic': 'Positioning of call light'
}


GMS_CNA_CLINICAL_RECORD_PATCH_SAMPLE_DATA = {
    'date': '2021-09-03'
}

GMS_ST2_CNA_CLINICAL_RECORD_PATCH_SAMPLE_DATA = {
    'date': '2021-09-04'
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


GMS_ST2_HHA_CLINICAL_RECORD_POST_SAMPLE_DATA = {
    'student': 'c13a0659-64cc-4bcb-a153-ba8415f05bd0',
    'date': '2021-10-01',
    'completed': True,
    'hours_spent': 3,
    'comments': '',
    'performance_satisfied': False,
    'start_time': '22:38:17',
    'end_time': '00:00:02',
    'start_date': '2021-10-01',
    'end_date': '2021-10-01',
    'topic': 'Nutrition'
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


GMS_ST2_HHA_CLINICAL_RECORD_PUT_SAMPLE_DATA = {
    'student': 'c13a0659-64cc-4bcb-a153-ba8415f05bd0',
    'date': '2021-11-09',
    'completed': False,
    'hours_spent': 2,
    'comments': '',
    'performance_satisfied': True,
    'start_time': '22:38:07',
    'end_time': '00:00:00',
    'start_date': '2021-11-05',
    'end_date': '2021-11-06',
    'topic': 'Cleaning and Care Tasks in the Home'
}

GMS_HHA_CLINICAL_RECORD_PATCH_SAMPLE_DATA = {
    'end_date': '2021-09-03'
}


GMS_ST2_HHA_CLINICAL_RECORD_PATCH_SAMPLE_DATA = {
    'end_date': '2021-12-03'
}


GMS_STI_CNA_HHA_ROTATION_FILTER_PARAMS = {
    'start_date': '2021-10-06',
    'end_date': '2021-12-30',
    'rotation_num': 1
}

GMS_STI_CNA_ROTATION2_FILTER_PARAMS = {
    'start_date': '2022-10-06',
    'end_date': '2022-12-30',
    'rotation_num': 15
}

GMS_STI_HHA_ROTATION2_FILTER_PARAMS = {
    'start_date': '2022-11-06',
    'end_date': '2022-11-30',
    'rotation_num': 25
}


GMS_ST2_CNA_HHA_ROTATION_FILTER_PARAMS = {
    'start_date': '2021-11-06',
    'end_date': '2021-11-30',
    'rotation_num': 30
}


GMS_STI_CNA_STUDENT_FILTER_PARAMS = {
    'first_name': 'Test',
    'last_name': 'A',
    'makeup_student': 'False'
}

GMS_STI_CNA_STUDENT2_FILTER_PARAMS = {
    'first_name': 'George',
    'last_name': 'Abby',
    'makeup_student': 'False'
}


GMS_STI_HHA_STUDENT_FILTER_PARAMS = {
    'first_name': 'Test',
    'last_name': 'B',
    'makeup_student': 'False'
}

GMS_STI_HHA_STUDENT2_FILTER_PARAMS = {
    'first_name': 'Abby',
    'last_name': 'George',
    'makeup_student': 'False'
}


GMS_ST2_CNA_STUDENT_FILTER_PARAMS = {
    'first_name': 'Z',
    'last_name': 'Test',
    'makeup_student': 'True'
}
GMS_ST2_HHA_STUDENT_FILTER_PARAMS = {
    'first_name': 'Y',
    'last_name': 'Test',
    'makeup_student': 'True'
}


GMS_STI_CNA_THEORYRECORD_FILTER_PARAMS = {
    'date': '2021-10-01',
    'completed': 'True',
    'topic': 'Module 2 Quiz'
}

GMS_STI_CNA_THEORYRECORD2_FILTER_PARAMS = {
    'date': '2021-10-05',
    'completed': 'True',
    'topic': 'Module 9 Quiz'
}


GMS_STI_HHA_THEORYRECORD_FILTER_PARAMS = {
    'date': '2021-10-03',
    'completed': 'True',
    'topic': 'Personal Care Services'
}

GMS_STI_HHA_THEORYRECORD2_FILTER_PARAMS = {
    'date': '2021-10-07',
    'completed': 'True',
    'topic': 'Introduction to Aide and Agency Role'
}

GMS_ST2_CNA_THEORYRECORD_FILTER_PARAMS = {
    'date': '2021-11-06',
    'completed': 'False',
    'topic': 'Module 3 Quiz'
}

GMS_ST2_HHA_THEORYRECORD_FILTER_PARAMS = {
    'date': '2021-11-08',
    'completed': 'False',
    'topic': 'Cleaning and Care Tasks in the Home'
}


GMS_STI_CNA_CLINICALRECORD_FILTER_PARAMS = {
    'date': '2021-10-02',
    'completed': 'True',
    'topic': 'Mouth care of the unconscious resident'
}

GMS_STI_CNA_CLINICALRECORD2_FILTER_PARAMS = {
    'date': '2021-10-06',
    'completed': 'True',
    'topic': 'Shampoo with shower or tub bath'
}


GMS_STI_HHA_CLINICALRECORD_FILTER_PARAMS = {
    'date': '2021-10-04',
    'completed': 'True',
    'topic': 'Nutrition'
}

GMS_STI_HHA_CLINICALRECORD2_FILTER_PARAMS = {
    'date': '2021-10-08',
    'completed': 'True',
    'topic': 'Cleaning and Care Tasks in the Home'
}

GMS_ST2_CNA_CLINICALRECORD_FILTER_PARAMS = {
    'date': '2021-11-07',
    'completed': 'False',
    'topic': 'Positioning of call light'
}

GMS_ST2_HHA_CLINICALRECORD_FILTER_PARAMS = {
    'date': '2021-11-09',
    'completed': 'False',
    'topic': 'Cleaning and Care Tasks in the Home'
}

GMS_CNAROTATION_POST_BAD_EMAIL = {
    'school_name': 'STI',
    'start_date': '2021-02-18',
    'end_date': '2021-10-18',
    'instructor_email': ['random@localhost'],
    'rotation_num': 22,
    'instructor_title': 'LVN',
    'clinical_site': 'Rowland'
}

GMS_CNAROTATION_PUT_BAD_EMAIL = {
    'school_name': 'STI',
    'start_date': '2021-09-14',
    'end_date': '2021-10-13',
    'instructor_email': ['random@localhost'],
    'rotation_num': 10,
    'instructor_title': 'LVN',
    'clinical_site': 'Rowland'
}


GMS_CNAROTATION_PATCH_BAD_EMAIL = {
    'instructor_email': ['random@localhost']
}

GMS_HHAROTATION_POST_BAD_EMAIL = {
    'school_name': 'STI',
    'start_date': '2021-09-13',
    'end_date': '2021-10-13',
    'instructor_email': ['random@localhost'],
    'rotation_num': 10,
    'instructor_title': 'LVN',
    'clinical_site': 'Rowland'
}

GMS_HHAROTATION_PUT_BAD_EMAIL = {
    'school_name': 'STI',
    'start_date': '2021-09-14',
    'end_date': '2021-10-13',
    'instructor_email': ['random@localhost'],
    'rotation_num': 10,
    'instructor_title': 'LVN',
    'clinical_site': 'Rowland'
}

GMS_HHAROTATION_PATCH_BAD_EMAIL = {
    'instructor_email': ['random@localhost']
}


# CMS
CMS_CLIENTS_API_URL = '/api/cms/clients/'
CMS_NOTES_API_URL = '/api/cms/notes/'

CMS_SECOND_CLIENT_UUID = '96896bab-cdd5-4f4c-bbe3-a0aa24a33127'
CMS_SECOND_NOTE_UUID = '9bb20ac8-dfbd-4aa9-8adc-3294232e671b'
CMS_ST2_CLIENT_UUID = '1d6f6df2-322f-410e-a069-94147142f766'
CMS_ST2_NOTE_UUID = 'b688b639-73cf-4917-8178-c23425e95f58'


CMS_STI_CLIENT_SAMPLE_POST = {
    'first_name': 'Sample First',
    'last_name': 'Sample Last',
    'phone_number': '123-456-7890',
    'email': 'testysample@email.com',
    'city': 'Arcadia',
    'success': False,
    'recruit_emails': ['testrecruituser@localhost'],
    'school_name': 'STI'
}

CMS_STI_NOTE_SAMPLE_POST = {
    'client': '1b6f00a6-dec7-4766-be71-2ce630eb2df5',
    'product': 'BLS',
    'price': '100.00',
    'content': 'Sample content for sample notes'
}

CMS_STI_CLIENT_SAMPLE_PUT = {
    'first_name': 'First Sample',
    'last_name': 'Last Sample',
    'phone_number': '123-456-7890',
    'email': 'testysample@email.com',
    'city': 'Arcadia',
    'success': False,
    'recruit_emails': ['testrecruituser@localhost'],
    'school_name': 'STI'
}

CMS_STI_NOTE_SAMPLE_PUT = {
    'client': '1b6f00a6-dec7-4766-be71-2ce630eb2df5',
    'product': 'HSFA',
    'price': '150.00',
    'content': 'Sample content for sample notes'
}

CMS_STI_CLIENT_PATCH = {
    'first_name': 'Lastyy'
}

CMS_STI_NOTE_PATCH = {
    'price': '160.00'
}

CMS_ST2_CLIENT_SAMPLE_POST = {
    'first_name': 'Samplez',
    'last_name': 'Lasty',
    'phone_number': '123-456-7890',
    'email': 'testyysamplez@email.com',
    'city': 'Arcadia',
    'success': False,
    'recruit_emails': ['testsuper@localhost'],
    'school_name': 'ST2'
}

CMS_ST2_NOTE_SAMPLE_POST = {
    'client': '1d6f6df2-322f-410e-a069-94147142f766',
    'product': 'ESOL',
    'price': '100.00',
    'content': 'Sample content for sample notes  for ST2'
}

CMS_ST2_CLIENT_SAMPLE_PUT = {
    'first_name': 'Samplezzz',
    'last_name': 'Lastyy',
    'phone_number': '123-456-7800',
    'email': 'testyysamplezz@email.com',
    'city': 'Arcadia',
    'success': False,
    'recruit_emails': ['testsuper@localhost'],
    'school_name': 'ST2'
}

CMS_ST2_NOTE_SAMPLE_PUT = {
    'client': '1d6f6df2-322f-410e-a069-94147142f766',
    'product': 'HSFA',
    'price': '170.00',
    'content': 'Sample content for sample notes'
}

CMS_ST2_CLIENT_PATCH = {
    'first_name': 'John'
}

CMS_ST2_NOTE_PATCH = {
    'price': '175.00'
}

CMS_SECOND_CLIENT_PUT = {
    'first_name': 'Testing',
    'last_name': 'Client',
    'phone_number': '626-123-5555',
    'email': 'testing.clientz@email.com',
    'city': 'Alhambra',
    'success': True,
    'recruit_emails': ['testsuper@localhost'],
    'school_name': 'STI'
}

CMS_SECOND_NOTE_PUT = {
    'client': '96896bab-cdd5-4f4c-bbe3-a0aa24a33127',
    'product': 'HHA',
    'price': '680.00',
    'content': 'Sample Contents'
}

CMS_SECOND_CLIENT_PATCH = {
    'first_name': 'Johnny'
}

CMS_SECOND_NOTE_PATCH = {
    'price': '178.00'
}

CMS_CLIENT_FILTER_PARAMS = {
    'first_name': 'Testclient',
    'last_name': 'A',
    'phone_number': '626-555-5455',
    'email': 'testclienta@email.com',
    'city': 'Rosemead',
    'success': False,
    'initial_contact': '2021-10-06'
}

CMS_NOTE_FILTER_PARAMS = {
    'date': '2021-10-06',
    'content': 'Tried contacting.'
}


CMS_SECOND_CLIENT_FILTER_PARAMS = {
    'first_name': 'Testing',
    'last_name': 'Client',
    'phone_number': '626-123-5555',
    'email': 'testing.client@email.com',
    'city': 'Alhambra',
    'success': True,
    'initial_contact': '2021-11-01'
}

CMS_SECOND_NOTE_FILTER_PARAMS = {
    'date': '2021-11-06',
    'content': 'Sample Content'
}


CMS_ST2_CLIENT_FILTER_PARAMS = {
    'first_name': 'Testy',
    'last_name': 'Clientelle',
    'phone_number': '626-321-5555',
    'email': 'testy.clientelle@email.com',
    'city': 'Temple City',
    'success': True,
    'initial_contact': '2021-12-01'
}

CMS_ST2_NOTE_FILTER_PARAMS = {
    'date': '2021-12-06',
    'content': 'Sample Content for this client'
}
