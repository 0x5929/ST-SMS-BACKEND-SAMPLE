from behave import when


SCHOOLS_API_URL = '/api/sms/schools/'
PROGRAMS_API_URL = '/api/sms/programs/'
ROTATIONS_API_URL = '/api/sms/rotations/'
STUDENTS_API_URL = '/api/sms/students/'

# NOTE: NEED TO CHANGE THE FOLLOWING
STUDENT_SAMPLE_DIFF_SCHOOL_POST_DATA = {
    "student_id": "01-1019-TA",
    "first_name": "Test",
    "last_name": "A",
    "phone_number": "626-323-1414",
    "email": "testa@email.com",
    "mailing_address": "1020 S. Fake STI2 Student Ave, TestA, CA 91770",
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

    context.response = context.browser.post(
        'POST', f'{context.server_url}{STUDENTS_API_URL}', data=post_data)


@when('request POST to /api/sms/students to a program rotation of another school')
def request_POST_to_students_diff_school(context):
    post_data = STUDENT_SAMPLE_DIFF_SCHOOL_POST_DATA

    context.response = context.browser.post(
        'POST', f'{context.server_url}{STUDENTS_API_URL}', data=post_data)


@when('request PUT to /api/sms/students/student_uuid')
def request_PUT_to_student(context):
    pass


@when('request PATCH to /api/sms/students/student_uuid')
def request_PATCH_to_student(context):
    pass


@when('request DELETE to /api/sms/students/student_uuid')
def request_DELETE_to_student(context):
    pass


@when('request POST to /api/sms/schools')
def request_POST_to_schools(context):
    pass


@when('request PUT to /api/sms/schools/school_uuid')
def request_PUT_to_school(context):
    pass


@when('request PATCH to /api/sms/schools/school_uuid')
def request_PATCH_to_school(context):
    pass


@when('request DELETE to /api/sms/schools/school_uuid')
def request_DEL_to_school(context):
    pass


@when('request POST to /api/sms/programs')
def request_POST_to_programs(context):
    pass


@when('request PUT to /api/sms/programs/program_uuid')
def request_PUT_to_program(context):
    pass


@when('request PATCH to /api/sms/programs/program_uuid')
def request_PATCH_to_program(context):
    pass


@when('request DELETE to /api/sms/programs/program_uuid')
def request_DEL_to_program(context):
    pass


@when('request POST to /api/sms/rotations')
def request_POST_to_rotations(context):
    pass


@when('request PUT to /api/sms/rotations/rotation_uuid')
def request_PUT_to_rotaiton(context):
    pass


@when('request PATCH to /api/sms/rotations/rotation_uuid')
def request_PATCH_to_rotation(context):
    pass


@when('request DELETE to /api/sms/rotations/rotation_uuid')
def request_DEL_to_rotations(context):
    pass


@when('request GET to /api/sms/students with filters by school name')
def request_GET_by_school_name(context):
    pass


@when('request GET to /api/sms/students with filters by program name')
def request_GET_by_program_name(context):
    pass


@when('request GET to /api/sms/students with filters by rotation number')
def request_GET_by_rot_num(context):
    pass


@when('request GET to /api/sms/students with filters by student first name')
def request_GET_by_first_name(context):
    pass


@when('request GET to /api/sms/students with filters by student last name')
def request_GET_by_last_name(context):
    pass


@when('request GET to /api/sms/students with filters by student email')
def request_GET_by_email(context):
    pass


@when('request GET to /api/sms/students with filters by student phone number')
def request_GET_by_phone(context):
    pass


@when('request GET to /api/sms/students with filters by student ID')
def request_GET_by_ID(context):
    pass


@when('request GET to /api/sms/students with filters by student program start date')
def request_GET_by_program_start(context):
    pass


@when('request GET to /api/sms/students with filters by student program end date')
def request_GET_by_program_end(context):
    pass


@when('request GET to /api/sms/students with filters by student payment completions')
def request_GET_by_payment(context):
    pass


@when('request GET to /api/sms/students with filters by student program completions')
def request_GET_by_completion(context):
    pass


@when('request GET to /api/sms/students with filters by student employment status')
def request_GET_by_employment(context):
    pass
