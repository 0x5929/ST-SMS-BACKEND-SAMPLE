from behave import when

from .constants import (SCHOOLS_API_URL,\
                        PROGRAMS_API_URL,\
                        ROTATIONS_API_URL,\
                        STUDENTS_API_URL,\
                        STUDENT_UUID_TO_TEST,\
                        SCHOOL_UUID_TO_TEST,\
                        PROGRAM_UUID_TO_TEST,\
                        ROTATION_UUID_TO_TEST,\
                        STUDENT_SAMPLE_SAME_SCHOOL_POST_DATA,\
                        STUDENT_SAMPLE_DIFF_SCHOOL_POST_DATA,\
                        SCHOOL_SAMPLE_POST_DATA,\
                        PROGRAM_SAMPLE_POST_DATA,\
                        ROTATION_SAMPLE_POST_DATA,\
                        FILTER_PARAMS,\
                        PUT_DATA,\
                        PATCH_DATA)



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
    put_data['last_name'] = PUT_DATA.get('student__last_name')

    context.response = context.browser.request(
        'PUT', f'{context.server_url}{STUDENTS_API_URL}{STUDENT_UUID_TO_TEST}/', data=put_data)


@when('request PATCH to /api/sms/students/student_uuid')
def request_PATCH_to_student(context):
    patch_data = {'last_name': PATCH_DATA.get('student__last_name')}

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
    put_data['school_code'] = PUT_DATA.get('school__school_code')

    context.response = context.browser.request(
        'PUT', f'{context.server_url}{SCHOOLS_API_URL}{SCHOOL_UUID_TO_TEST}/', data=put_data)


@when('request PATCH to /api/sms/schools/school_uuid')
def request_PATCH_to_school(context):
    patch_data = {'school_code': PATCH_DATA.get('school__school_code')}

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

    put_data['program_name'] = PUT_DATA.get('program__program_name')

    context.response = context.browser.request(
        'PUT', f'{context.server_url}{PROGRAMS_API_URL}{PROGRAM_UUID_TO_TEST}/', data=put_data)


@when('request PATCH to /api/sms/programs/program_uuid')
def request_PATCH_to_program(context):
    patch_data = {"program_name": PATCH_DATA.get('program__program_name')}

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
    put_data['rotation_number'] = PUT_DATA.get('rotation__rotation_number')

    context.response = context.browser.request(
        'PUT', f'{context.server_url}{ROTATIONS_API_URL}{ROTATION_UUID_TO_TEST}/', data=put_data)


@when('request PATCH to /api/sms/rotations/rotation_uuid')
def request_PATCH_to_rotation(context):
    patch_data = {
        "rotation_number": PATCH_DATA.get('rotation__rotation_number')
    }

    context.response = context.browser.request(
        'PATCH', f'{context.server_url}{ROTATIONS_API_URL}{ROTATION_UUID_TO_TEST}/', data=patch_data)


@when('request DELETE to /api/sms/rotations/rotation_uuid')
def request_DEL_to_rotations(context):
    context.response = context.browser.request(
        'DELETE', f'{context.server_url}{ROTATIONS_API_URL}{ROTATION_UUID_TO_TEST}/')


@when('request GET to /api/sms/students with filters by school name')
def request_GET_by_school_name(context):
    parameter = f'?school={FILTER_PARAMS.get("school_name")}'

    context.response = context.browser.request(
        'GET', f'{context.server_url}{STUDENTS_API_URL}{parameter}')


@when('request GET to /api/sms/students with filters by program name')
def request_GET_by_program_name(context):
    parameter = f'?program={FILTER_PARAMS.get("program_name")}'

    context.response = context.browser.request(
        'GET', f'{context.server_url}{STUDENTS_API_URL}{parameter}')


@when('request GET to /api/sms/students with filters by rotation number')
def request_GET_by_rot_num(context):
    parameter = f'?rotation={FILTER_PARAMS.get("rotation_num")}'

    context.response = context.browser.request(
        'GET', f'{context.server_url}{STUDENTS_API_URL}{parameter}')


@when('request GET to /api/sms/students with filters by student first name')
def request_GET_by_first_name(context):
    parameter = f'?first_name={FILTER_PARAMS.get("first_name")}'

    context.response = context.browser.request(
        'GET', f'{context.server_url}{STUDENTS_API_URL}{parameter}')


@when('request GET to /api/sms/students with filters by student last name')
def request_GET_by_last_name(context):
    parameter = f'?last_name={FILTER_PARAMS.get("last_name")}'

    context.response = context.browser.request(
        'GET', f'{context.server_url}{STUDENTS_API_URL}{parameter}')


@when('request GET to /api/sms/students with filters by student email')
def request_GET_by_email(context):
    parameter = f'?email={FILTER_PARAMS.get("email")}'

    context.response = context.browser.request(
        'GET', f'{context.server_url}{STUDENTS_API_URL}{parameter}')


@when('request GET to /api/sms/students with filters by student phone number')
def request_GET_by_phone(context):
    parameter = f'?phone={FILTER_PARAMS.get("phone")}'

    context.response = context.browser.request(
        'GET', f'{context.server_url}{STUDENTS_API_URL}{parameter}')


@when('request GET to /api/sms/students with filters by student ID')
def request_GET_by_ID(context):
    parameter = f'?student_id={FILTER_PARAMS.get("id_")}'

    context.response = context.browser.request(
        'GET', f'{context.server_url}{STUDENTS_API_URL}{parameter}')


@when('request GET to /api/sms/students with filters by student program start date')
def request_GET_by_program_start(context):
    parameter = f'?start_date={FILTER_PARAMS.get("start_date")}'

    context.response = context.browser.request(
        'GET', f'{context.server_url}{STUDENTS_API_URL}{parameter}')


@when('request GET to /api/sms/students with filters by student program end date')
def request_GET_by_program_end(context):
    parameter = f'?completion_date={FILTER_PARAMS.get("completion_date")}'

    context.response = context.browser.request(
        'GET', f'{context.server_url}{STUDENTS_API_URL}{parameter}')


@when('request GET to /api/sms/students with filters by student payment completions')
def request_GET_by_payment(context):
    parameter = f'?paid={FILTER_PARAMS.get("paid")}'

    context.response = context.browser.request(
        'GET', f'{context.server_url}{STUDENTS_API_URL}{parameter}')


@when('request GET to /api/sms/students with filters by student program completions')
def request_GET_by_completion(context):
    parameter = f'?graudated={FILTER_PARAMS.get("graudated")}'

    context.response = context.browser.request(
        'GET', f'{context.server_url}{STUDENTS_API_URL}{parameter}')

@when('request GET to /api/sms/students with filters by student employment status')
def request_GET_by_employment(context):
    parameter = f'?employed={FILTER_PARAMS.get("employed")}'

    context.response = context.browser.request(
        'GET', f'{context.server_url}{STUDENTS_API_URL}{parameter}')