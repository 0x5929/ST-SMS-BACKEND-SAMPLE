from behave import when

from constants import (SMS_SCHOOLS_API_URL,
                       SMS_PROGRAMS_API_URL,
                       SMS_ROTATIONS_API_URL,
                       SMS_STUDENTS_API_URL,
                       SMS_STUDENT_UUID_TO_TEST,
                       SMS_SCHOOL_UUID_TO_TEST,
                       SMS_PROGRAM_UUID_TO_TEST,
                       SMS_ROTATION_UUID_TO_TEST,
                       SMS_STUDENT_SAMPLE_SAME_SCHOOL_POST_DATA,
                       SMS_STUDENT_SAMPLE_DIFF_SCHOOL_POST_DATA,
                       SMS_SCHOOL_SAMPLE_POST_DATA,
                       SMS_PROGRAM_SAMPLE_POST_DATA,
                       SMS_ROTATION_SAMPLE_POST_DATA,
                       SMS_STUDENT_SAMPLE_PUT_DATA,
                       SMS_FILTER_PARAMS,
                       SMS_STUDENT_SAMPLE_PATCH_DATA,
                       DATADUMP_API_URL,
                       TEST_SPREADSHEET_ID,
                       TEST_SHEET_ID,
                       TEST_SCHOOL_NAME,
                       TEST_DATADUMP_DUMMY_DATA,
                       SMS_SCHOOL_SAMPLE_PUT_DATA,
                       SMS_SCHOOL_SAMPLE_PATCH_DATA,
                       SMS_PROGRAM_SAMPLE_PUT_DATA,
                       SMS_PROGRAM_SAMPLE_PATCH_DATA,
                       SMS_ROTATION_SAMPLE_PUT_DATA,
                       SMS_ROTATION_SAMPLE_PATCH_DATA)


@when('request GET to /api/sms/schools')
def request_GET_to_schools(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{SMS_SCHOOLS_API_URL}', headers=headers)


@when('request GET to /api/sms/programs')
def request_GET_to_programs(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{SMS_PROGRAMS_API_URL}', headers=headers)


@when('request GET to /api/sms/rotations')
def request_GET_to_rotations(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{SMS_ROTATIONS_API_URL}', headers=headers)


@when('request GET to /api/sms/students')
def request_GET_to_students(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{SMS_STUDENTS_API_URL}', headers=headers)


@when('request POST to /api/sms/students of the same school')
def request_POST_to_students_same_school(context):
    post_data = SMS_STUDENT_SAMPLE_SAME_SCHOOL_POST_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{SMS_STUDENTS_API_URL}', post_data, format='json', headers=headers)


@when('request POST to /api/sms/students to a program rotation of another school')
def request_POST_to_students_diff_school(context):
    post_data = SMS_STUDENT_SAMPLE_DIFF_SCHOOL_POST_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{SMS_STUDENTS_API_URL}', post_data, format='json', headers=headers)


@when('request PUT to /api/sms/students/student_uuid')
def request_PUT_to_student(context):
    put_data = SMS_STUDENT_SAMPLE_PUT_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.put(
        f'{SMS_STUDENTS_API_URL}{SMS_STUDENT_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PATCH to /api/sms/students/student_uuid')
def request_PATCH_to_student(context):
    patch_data = SMS_STUDENT_SAMPLE_PATCH_DATA

    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.patch(
        f'{SMS_STUDENTS_API_URL}{SMS_STUDENT_UUID_TO_TEST}/', patch_data, format='json', headers=headers)


@when('request DELETE to /api/sms/students/student_uuid')
def request_DELETE_to_student(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.delete(
        f'{SMS_STUDENTS_API_URL}{SMS_STUDENT_UUID_TO_TEST}/', headers=headers)


@when('request POST to /api/sms/schools')
def request_POST_to_schools(context):
    post_data = SMS_SCHOOL_SAMPLE_POST_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{SMS_SCHOOLS_API_URL}', post_data, format='json', headers=headers)


@when('request PUT to /api/sms/schools/school_uuid')
def request_PUT_to_school(context):
    put_data = SMS_SCHOOL_SAMPLE_PUT_DATA

    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.put(
        f'{SMS_SCHOOLS_API_URL}{SMS_SCHOOL_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PATCH to /api/sms/schools/school_uuid')
def request_PATCH_to_school(context):
    patch_data = SMS_SCHOOL_SAMPLE_PATCH_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.patch(
        f'{SMS_SCHOOLS_API_URL}{SMS_SCHOOL_UUID_TO_TEST}/', patch_data, format='json', headers=headers)


@when('request DELETE to /api/sms/schools/school_uuid')
def request_DEL_to_school(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.delete(
        f'{SMS_SCHOOLS_API_URL}{SMS_SCHOOL_UUID_TO_TEST}/', headers=headers)


@when('request POST to /api/sms/programs')
def request_POST_to_programs(context):
    post_data = SMS_PROGRAM_SAMPLE_POST_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{SMS_PROGRAMS_API_URL}', post_data, format='json', headers=headers)


@when('request PUT to /api/sms/programs/program_uuid')
def request_PUT_to_program(context):
    put_data = SMS_PROGRAM_SAMPLE_PUT_DATA

    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.put(
        f'{SMS_PROGRAMS_API_URL}{SMS_PROGRAM_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PATCH to /api/sms/programs/program_uuid')
def request_PATCH_to_program(context):
    patch_data = SMS_PROGRAM_SAMPLE_PATCH_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.patch(
        f'{SMS_PROGRAMS_API_URL}{SMS_PROGRAM_UUID_TO_TEST}/', patch_data, format='json', headers=headers)


@when('request DELETE to /api/sms/programs/program_uuid')
def request_DEL_to_program(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.delete(
        f'{SMS_PROGRAMS_API_URL}{SMS_PROGRAM_UUID_TO_TEST}/', headers=headers)


@when('request POST to /api/sms/rotations')
def request_POST_to_rotations(context):
    post_data = SMS_ROTATION_SAMPLE_POST_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{SMS_ROTATIONS_API_URL}', post_data, format='json', headers=headers)


@when('request PUT to /api/sms/rotations/rotation_uuid')
def request_PUT_to_rotation(context):
    put_data = SMS_ROTATION_SAMPLE_PUT_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.put(
        f'{SMS_ROTATIONS_API_URL}{SMS_ROTATION_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PATCH to /api/sms/rotations/rotation_uuid')
def request_PATCH_to_rotation(context):
    patch_data = SMS_ROTATION_SAMPLE_PATCH_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.patch(
        f'{SMS_ROTATIONS_API_URL}{SMS_ROTATION_UUID_TO_TEST}/', patch_data, format='json', headers=headers)


@when('request DELETE to /api/sms/rotations/rotation_uuid')
def request_DEL_to_rotations(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.delete(
        f'{SMS_ROTATIONS_API_URL}{SMS_ROTATION_UUID_TO_TEST}/', headers=headers)


@when('request GET to /api/sms/students with filters by school name')
def request_GET_by_school_name(context):
    parameter = f'?rotation__program__school__school_name={SMS_FILTER_PARAMS.get("school_name")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{SMS_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/sms/students with filters by program name')
def request_GET_by_program_name(context):
    parameter = f'?rotation__program__program_name={SMS_FILTER_PARAMS.get("program_name")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{SMS_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/sms/students with filters by rotation number')
def request_GET_by_rot_num(context):
    parameter = f'?rotation__rotation_number={SMS_FILTER_PARAMS.get("rotation_num")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{SMS_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/sms/students with filters by student first name')
def request_GET_by_first_name(context):
    parameter = f'?first_name={SMS_FILTER_PARAMS.get("first_name")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{SMS_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/sms/students with filters by student last name')
def request_GET_by_last_name(context):
    parameter = f'?last_name={SMS_FILTER_PARAMS.get("last_name")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{SMS_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/sms/students with filters by student email')
def request_GET_by_email(context):
    parameter = f'?email={SMS_FILTER_PARAMS.get("email")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{SMS_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/sms/students with filters by student phone number')
def request_GET_by_phone(context):
    parameter = f'?phone_number={SMS_FILTER_PARAMS.get("phone")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{SMS_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/sms/students with filters by student ID')
def request_GET_by_ID(context):
    parameter = f'?student_id={SMS_FILTER_PARAMS.get("id_")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{SMS_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/sms/students with filters by student program start date')
def request_GET_by_program_start(context):
    parameter = f'?start_date={SMS_FILTER_PARAMS.get("start_date")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{SMS_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/sms/students with filters by student program end date')
def request_GET_by_program_end(context):
    parameter = f'?completion_date={SMS_FILTER_PARAMS.get("completion_date")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{SMS_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/sms/students with filters by student payment completions')
def request_GET_by_payment(context):
    parameter = f'?paid={SMS_FILTER_PARAMS.get("paid")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{SMS_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/sms/students with filters by student program completions')
def request_GET_by_completion(context):
    parameter = f'?graduated={SMS_FILTER_PARAMS.get("graudated")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{SMS_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/sms/students with filters by student employment status')
def request_GET_by_employment(context):
    parameter = f'?employed={SMS_FILTER_PARAMS.get("employed")}'

    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{SMS_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /auth/login/')
def request_login_by_GET(context):
    context.response = context.test.client.get('/auth/login/')


@when('request GET to /api/sms/google_sheet_datadump/?ssid=<>&sid=<>&school_name=<>')
def request_for_datadump_with_params(context):
    spread_sheet_id = TEST_SPREADSHEET_ID
    sheet_id = TEST_SHEET_ID
    school_name = TEST_SCHOOL_NAME

    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{DATADUMP_API_URL}?ssid={spread_sheet_id}&sid={sheet_id}&school_name={school_name}', headers=headers)


@when('request GET to /api/sms/google_sheet_datadump/')
def request_for_datadump_wo_params(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{DATADUMP_API_URL}', headers=headers)


@when('request POST to /api/sms/google_sheet_datadump/')
def request_POST_to_datadump(context):
    post_data = TEST_DATADUMP_DUMMY_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{DATADUMP_API_URL}', post_data, format='json', headers=headers)


@when('request PUT to /api/sms/google_sheet_datadump/')
def request_PUT_to_datadump(context):
    put_data = TEST_DATADUMP_DUMMY_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.put(
        f'{DATADUMP_API_URL}', put_data, format='json', headers=headers)


@when('request PATCH to /api/sms/google_sheet_datadump/')
def request_PATCH_to_datadump(context):
    patch_data = TEST_DATADUMP_DUMMY_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.patch(
        f'{DATADUMP_API_URL}', patch_data, format='json', headers=headers)


@when('request DELETE to /api/sms/google_sheet_datadump/')
def request_DELETE_to_datadump(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.delete(
        f'{DATADUMP_API_URL}', headers=headers)
