from behave import when


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
    "student_uuid": "7766c4a3-877c-4c23-b3e6-e7ab9ef43c97",
    "student_id": "01-1019-TA",
    "first_name": "Test",
    "last_name": "A",
    "phone_number": "626-323-1414",
    "email": "testa@email.com",
    "mailing_address": "1020 S. Fake STI2 Ave, TestA, CA 91770",
    "course": "CNA",
    "start_date": "2021-10-06",
    "completion_date": "2021-12-30",
    "date_enrollment_agreement_signed": "2021-10-06",
    "third_party_payer_info": "",
    "course_cost_currency": "USD",
    "course_cost": "2586.00",
    "total_charges_charged_currency": "USD",
    "total_charges_charged": "2586.00",
    "total_charges_paid_currency": "USD",
    "total_charges_paid": "2586.00",
    "paid": True,
    "graduated": True,
    "passed_first_exam": True,
    "passed_second_or_third_exam": False,
    "employed": False,
    "place_of_employment": "",
    "employment_address": "",
    "position": "",
    "starting_wage_currency": "USD",
    "starting_wage": None,
    "hours_worked_weekly": "",
    "description_of_attempts_to_contact_student": "",
    "google_sheet_migrated": False,
    "google_sheet_migration_issue": "",
    "rotation": "a6a1c1c3-df42-4783-9c20-49b94ad1d6ba"
}

STUDENT_SAMPLE_SAME_SCHOOL_POST_DATA = {
    "student_uuid": "90f120c5-1894-4afc-b204-a912172570a5",
    "student_id": "01-1006-TA",
    "first_name": "Test",
    "last_name": "A",
    "phone_number": "626-323-1414",
    "email": "testa@email.com",
    "mailing_address": "1020 S. Fake Ave, TestA, CA 91770",
    "course": "CNA",
    "start_date": "2021-10-06",
    "completion_date": "2021-12-30",
    "date_enrollment_agreement_signed": "2021-10-06",
    "third_party_payer_info": "",
    "course_cost_currency": "USD",
    "course_cost": "2350.00",
    "total_charges_charged_currency": "USD",
    "total_charges_charged": "2350.00",
    "total_charges_paid_currency": "USD",
    "total_charges_paid": "2350.00",
    "paid": True,
    "graduated": True,
    "passed_first_exam": False,
    "passed_second_or_third_exam": False,
    "employed": False,
    "place_of_employment": "",
    "employment_address": "",
    "position": "",
    "starting_wage_currency": "USD",
    "starting_wage": None,
    "hours_worked_weekly": "",
    "description_of_attempts_to_contact_student": "",
    "google_sheet_migrated": False,
    "google_sheet_migration_issue": "",
    "rotation": "fcd1f629-6449-4672-8dc8-4a2183cc70e9"
}

SCHOOL_SAMPLE_POST_DATA = {
    "school_name": "ST3",
    "school_code": "27091742",
    "year_founded": "2011-09-13",
    "school_address": "2209 N. San Gabriel Blvd., Suite C, Rosemead, CA 91770"
}

PROGRAM_SAMPLE_POST_DATA = {
    "school": "6bfad48c-ecc6-44ac-b53f-c94ccd240119",
    "program_name": "SG",
    "approval_entities": ["BSIS", "BPPE"]
}

ROTATION_SAMPLE_POST_DATA = {
    "program": "de47da61-278f-4f67-8fbf-7e60de40e9d4",
    "rotation_number": 5
}


@when('request GET to /api/sms/schools')
def request_GET_to_schools(context):
    context.response = context.browser.request(
        'GET', f'{context.server_url}{SCHOOLS_API_URL}')


@when('request GET to /api/sms/programs')
def request_GET_to_programs(context):
    context.response = context.browser.request(
        'GET', f'{context.server_url}{PROGRAMS_API_URL}')


@when('request GET to /api/sms/rotations')
def request_GET_to_rotations(context):
    context.response = context.browser.request(
        'GET', f'{context.server_url}{ROTATIONS_API_URL}')


@when('request GET to /api/sms/students')
def request_GET_to_students(context):
    context.response = context.browser.request(
        'GET', f'{context.server_url}{STUDENTS_API_URL}')


@when('request POST to /api/sms/students of the same school')
def request_POST_to_students_same_school(context):
    post_data = STUDENT_SAMPLE_SAME_SCHOOL_POST_DATA

    context.response = context.browser.request(
        'POST', f'{context.server_url}{STUDENTS_API_URL}', data=post_data)


@when('request POST to /api/sms/students to a program rotation of another school')
def request_POST_to_students_diff_school(context):
    post_data = STUDENT_SAMPLE_DIFF_SCHOOL_POST_DATA

    context.response = context.browser.request(
        'POST', f'{context.server_url}{STUDENTS_API_URL}', data=post_data)


@when('request PUT to /api/sms/students/student_uuid')
def request_PUT_to_student(context):
    put_data = STUDENT_SAMPLE_SAME_SCHOOL_POST_DATA
    put_data['last_name'] = 'C'

    context.response = context.browser.request(
        'PUT', f'{context.server_url}{STUDENTS_API_URL}{STUDENT_UUID_TO_TEST}/', data=put_data)


@when('request PATCH to /api/sms/students/student_uuid')
def request_PATCH_to_student(context):
    patch_data = {'last_name': 'D'}

    context.response = context.browser.request(
        'PATCH', f'{context.server_url}{STUDENTS_API_URL}{STUDENT_UUID_TO_TEST}/', data=patch_data)


@when('request DELETE to /api/sms/students/student_uuid')
def request_DELETE_to_student(context):
    context.response = context.browser.request(
        'DELETE', f'{context.server_url}{STUDENTS_API_URL}{STUDENT_UUID_TO_TEST}/')


@when('request POST to /api/sms/schools')
def request_POST_to_schools(context):
    post_data = SCHOOL_SAMPLE_POST_DATA

    context.response = context.browser.request(
        'POST', f'{context.server_url}{SCHOOLS_API_URL}', data=post_data)


@when('request PUT to /api/sms/schools/school_uuid')
def request_PUT_to_school(context):
    put_data = SCHOOL_SAMPLE_POST_DATA
    put_data['school_code'] = '27091743'

    context.response = context.browser.request(
        'PUT', f'{context.server_url}{SCHOOLS_API_URL}{SCHOOL_UUID_TO_TEST}/', data=put_data)


@when('request PATCH to /api/sms/schools/school_uuid')
def request_PATCH_to_school(context):
    patch_data = {"school_code": "27091744"}

    context.response = context.browser.request(
        'PATCH', f'{context.server_url}{SCHOOLS_API_URL}{SCHOOL_UUID_TO_TEST}/', data=patch_data)


@when('request DELETE to /api/sms/schools/school_uuid')
def request_DEL_to_school(context):
    context.response = context.browser.request(
        'DELETE', f'{context.server_url}{SCHOOLS_API_URL}{SCHOOL_UUID_TO_TEST}/')


@when('request POST to /api/sms/programs')
def request_POST_to_programs(context):
    post_data = PROGRAM_SAMPLE_POST_DATA

    context.response = context.browser.request(
        'POST', f'{context.server_url}{PROGRAMS_API_URL}', data=post_data)


@when('request PUT to /api/sms/programs/program_uuid')
def request_PUT_to_program(context):
    put_data = PROGRAM_SAMPLE_POST_DATA

    put_data['program_name'] = "HSFA"

    context.response = context.browser.request(
        'PUT', f'{context.server_url}{PROGRAMS_API_URL}{PROGRAM_UUID_TO_TEST}/', data=put_data)


@when('request PATCH to /api/sms/programs/program_uuid')
def request_PATCH_to_program(context):
    patch_data = {"program_name": "BLS"}

    context.response = context.browser.request(
        'PATCH', f'{context.server_url}{PROGRAMS_API_URL}{PROGRAM_UUID_TO_TEST}/', data=patch_data)


@when('request DELETE to /api/sms/programs/program_uuid')
def request_DEL_to_program(context):
    context.response = context.browser.request(
        'DELETE', f'{context.server_url}{PROGRAMS_API_URL}{PROGRAM_UUID_TO_TEST}/')


@when('request POST to /api/sms/rotations')
def request_POST_to_rotations(context):
    post_data = ROTATION_SAMPLE_POST_DATA

    context.response = context.browser.request(
        'POST', f'{context.server_url}{ROTATIONS_API_URL}', data=post_data)


@when('request PUT to /api/sms/rotations/rotation_uuid')
def request_PUT_to_rotaiton(context):
    put_data = ROTATION_SAMPLE_POST_DATA
    put_data['rotation_number'] = 6

    context.response = context.browser.request(
        'PUT', f'{context.server_url}{ROTATIONS_API_URL}{ROTATION_UUID_TO_TEST}/', data=put_data)


@when('request PATCH to /api/sms/rotations/rotation_uuid')
def request_PATCH_to_rotation(context):
    patch_data = {
        "rotation_number": 7
    }

    context.response = context.browser.request(
        'PATCH', f'{context.server_url}{ROTATIONS_API_URL}{ROTATION_UUID_TO_TEST}/', data=patch_data)


@when('request DELETE to /api/sms/rotations/rotation_uuid')
def request_DEL_to_rotations(context):
    context.response = context.browser.request(
        'DELETE', f'{context.server_url}{ROTATIONS_API_URL}{ROTATION_UUID_TO_TEST}/')


@when('request GET to /api/sms/students with filters by school name')
def request_GET_by_school_name(context):
    school_name = 'STI'
    parameter = f'?school={school_name}'

    context.response = context.browser.request(
        'GET', f'{context.server_url}{STUDENTS_API_URL}{parameter}')


@when('request GET to /api/sms/students with filters by program name')
def request_GET_by_program_name(context):
    program_name = 'HHA'
    parameter = f'?program={program_name}'

    context.response = context.browser.request(
        'GET', f'{context.server_url}{STUDENTS_API_URL}{parameter}')


@when('request GET to /api/sms/students with filters by rotation number')
def request_GET_by_rot_num(context):
    rotation_num = 1
    parameter = f'?rotation={rotation_num}'

    context.response = context.browser.request(
        'GET', f'{context.server_url}{STUDENTS_API_URL}{parameter}')


@when('request GET to /api/sms/students with filters by student first name')
def request_GET_by_first_name(context):
    first_name = 'Test'
    parameter = f'?first_name={first_name}'

    context.response = context.browser.request(
        'GET', f'{context.server_url}{STUDENTS_API_URL}{parameter}')


@when('request GET to /api/sms/students with filters by student last name')
def request_GET_by_last_name(context):
    last_name = 'B'
    parameter = f'?last_name={last_name}'

    context.response = context.browser.request(
        'GET', f'{context.server_url}{STUDENTS_API_URL}{parameter}')


@when('request GET to /api/sms/students with filters by student email')
def request_GET_by_email(context):
    email = 'testb@email.com'
    parameter = f'?email={email}'

    context.response = context.browser.request(
        'GET', f'{context.server_url}{STUDENTS_API_URL}{parameter}')


@when('request GET to /api/sms/students with filters by student phone number')
def request_GET_by_phone(context):
    phone = '626-333-5544'
    parameter = f'?phone={phone}'

    context.response = context.browser.request(
        'GET', f'{context.server_url}{STUDENTS_API_URL}{parameter}')


@when('request GET to /api/sms/students with filters by student ID')
def request_GET_by_ID(context):
    id_ = '01-1019-TB'
    parameter = f'?student_id={id_}'

    context.response = context.browser.request(
        'GET', f'{context.server_url}{STUDENTS_API_URL}{parameter}')


@when('request GET to /api/sms/students with filters by student program start date')
def request_GET_by_program_start(context):
    start_date = '2021-10-06'
    parameter = f'?start_date=2021-10-06'

    context.response = context.browser.request(
        'GET', f'{context.server_url}{STUDENTS_API_URL}{parameter}')


@when('request GET to /api/sms/students with filters by student program end date')
def request_GET_by_program_end(context):
    completion_date = '2021-12-10'
    parameter = f'?completion_date=2021-12-10'

    context.response = context.browser.request(
        'GET', f'{context.server_url}{STUDENTS_API_URL}{parameter}')


@when('request GET to /api/sms/students with filters by student payment completions')
def request_GET_by_payment(context):
    pass


@when('request GET to /api/sms/students with filters by student program completions')
def request_GET_by_completion(context):
    pass


@when('request GET to /api/sms/students with filters by student employment status')
def request_GET_by_employment(context):
    pass
