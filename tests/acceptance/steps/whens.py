from behave import when

from tests.acceptance.steps.constants import (SCHOOLS_API_URL,
                                              PROGRAMS_API_URL,
                                              ROTATIONS_API_URL,
                                              STUDENTS_API_URL,
                                              STUDENT_UUID_TO_TEST,
                                              SCHOOL_UUID_TO_TEST,
                                              PROGRAM_UUID_TO_TEST,
                                              ROTATION_UUID_TO_TEST,
                                              STUDENT_SAMPLE_SAME_SCHOOL_POST_DATA,
                                              STUDENT_SAMPLE_DIFF_SCHOOL_POST_DATA,
                                              SCHOOL_SAMPLE_POST_DATA,
                                              PROGRAM_SAMPLE_POST_DATA,
                                              ROTATION_SAMPLE_POST_DATA,
                                              STUDENT_SAMPLE_PUT_DATA,
                                              FILTER_PARAMS,
                                              PUT_DATA,
                                              PATCH_DATA)


@when('request GET to /api/sms/schools')
def request_GET_to_schools(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{SCHOOLS_API_URL}', headers=headers)


@when('request GET to /api/sms/programs')
def request_GET_to_programs(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{PROGRAMS_API_URL}', headers=headers)


@when('request GET to /api/sms/rotations')
def request_GET_to_rotations(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{ROTATIONS_API_URL}', headers=headers)


@when('request GET to /api/sms/students')
def request_GET_to_students(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{STUDENTS_API_URL}', headers=headers)


@when('request POST to /api/sms/students of the same school')
def request_POST_to_students_same_school(context):
    post_data = STUDENT_SAMPLE_SAME_SCHOOL_POST_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{STUDENTS_API_URL}', post_data, format='json', headers=headers)


@when('request POST to /api/sms/students to a program rotation of another school')
def request_POST_to_students_diff_school(context):
    post_data = STUDENT_SAMPLE_DIFF_SCHOOL_POST_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{STUDENTS_API_URL}', post_data, format='json', headers=headers)


@when('request PUT to /api/sms/students/student_uuid')
def request_PUT_to_student(context):
    put_data = STUDENT_SAMPLE_PUT_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.put(
        f'{STUDENTS_API_URL}{STUDENT_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PATCH to /api/sms/students/student_uuid')
def request_PATCH_to_student(context):
    patch_data = {'last_name': PATCH_DATA.get('student__last_name')}

    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.patch(
        f'{STUDENTS_API_URL}{STUDENT_UUID_TO_TEST}/', patch_data, format='json', headers=headers)


@when('request DELETE to /api/sms/students/student_uuid')
def request_DELETE_to_student(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.delete(
        f'{STUDENTS_API_URL}{STUDENT_UUID_TO_TEST}/', headers=headers)


@when('request POST to /api/sms/schools')
def request_POST_to_schools(context):
    post_data = SCHOOL_SAMPLE_POST_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{SCHOOLS_API_URL}', post_data, format='json', headers=headers)


@when('request PUT to /api/sms/schools/school_uuid')
def request_PUT_to_school(context):
    put_data = SCHOOL_SAMPLE_POST_DATA
    put_data['school_code'] = PUT_DATA.get('school__school_code')
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.put(
        f'{SCHOOLS_API_URL}{SCHOOL_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PATCH to /api/sms/schools/school_uuid')
def request_PATCH_to_school(context):
    patch_data = {'school_code': PATCH_DATA.get('school__school_code')}
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.patch(
        f'{SCHOOLS_API_URL}{SCHOOL_UUID_TO_TEST}/', patch_data, format='json', headers=headers)


@when('request DELETE to /api/sms/schools/school_uuid')
def request_DEL_to_school(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.delete(
        f'{SCHOOLS_API_URL}{SCHOOL_UUID_TO_TEST}/', headers=headers)


@when('request POST to /api/sms/programs')
def request_POST_to_programs(context):
    post_data = PROGRAM_SAMPLE_POST_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{PROGRAMS_API_URL}', post_data, format='json', headers=headers)


@when('request PUT to /api/sms/programs/program_uuid')
def request_PUT_to_program(context):
    put_data = PROGRAM_SAMPLE_POST_DATA

    put_data['program_name'] = PUT_DATA.get('program__program_name')
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.put(
        f'{PROGRAMS_API_URL}{PROGRAM_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PATCH to /api/sms/programs/program_uuid')
def request_PATCH_to_program(context):
    patch_data = {"program_name": PATCH_DATA.get('program__program_name')}
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.patch(
        f'{PROGRAMS_API_URL}{PROGRAM_UUID_TO_TEST}/', patch_data, format='json', headers=headers)


@when('request DELETE to /api/sms/programs/program_uuid')
def request_DEL_to_program(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.delete(
        f'{PROGRAMS_API_URL}{PROGRAM_UUID_TO_TEST}/', headers=headers)


@when('request POST to /api/sms/rotations')
def request_POST_to_rotations(context):
    post_data = ROTATION_SAMPLE_POST_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{ROTATIONS_API_URL}', post_data, format='json', headers=headers)


@when('request PUT to /api/sms/rotations/rotation_uuid')
def request_PUT_to_rotaiton(context):
    put_data = ROTATION_SAMPLE_POST_DATA
    put_data['rotation_number'] = PUT_DATA.get('rotation__rotation_number')
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.put(
        f'{ROTATIONS_API_URL}{ROTATION_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PATCH to /api/sms/rotations/rotation_uuid')
def request_PATCH_to_rotation(context):
    patch_data = {
        "rotation_number": PATCH_DATA.get('rotation__rotation_number')
    }
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.patch(
        f'{ROTATIONS_API_URL}{ROTATION_UUID_TO_TEST}/', patch_data, format='json', headers=headers)


@when('request DELETE to /api/sms/rotations/rotation_uuid')
def request_DEL_to_rotations(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.delete(
        f'{ROTATIONS_API_URL}{ROTATION_UUID_TO_TEST}/', headers=headers)


@when('request GET to /api/sms/students with filters by school name')
def request_GET_by_school_name(context):
    parameter = f'?rotation__program__school__school_name={FILTER_PARAMS.get("school_name")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/sms/students with filters by program name')
def request_GET_by_program_name(context):
    parameter = f'?rotation__program__program_name={FILTER_PARAMS.get("program_name")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/sms/students with filters by rotation number')
def request_GET_by_rot_num(context):
    parameter = f'?rotation__rotation_number={FILTER_PARAMS.get("rotation_num")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/sms/students with filters by student first name')
def request_GET_by_first_name(context):
    parameter = f'?first_name={FILTER_PARAMS.get("first_name")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/sms/students with filters by student last name')
def request_GET_by_last_name(context):
    parameter = f'?last_name={FILTER_PARAMS.get("last_name")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/sms/students with filters by student email')
def request_GET_by_email(context):
    parameter = f'?email={FILTER_PARAMS.get("email")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/sms/students with filters by student phone number')
def request_GET_by_phone(context):
    parameter = f'?phone_number={FILTER_PARAMS.get("phone")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/sms/students with filters by student ID')
def request_GET_by_ID(context):
    parameter = f'?student_id={FILTER_PARAMS.get("id_")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/sms/students with filters by student program start date')
def request_GET_by_program_start(context):
    parameter = f'?start_date={FILTER_PARAMS.get("start_date")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/sms/students with filters by student program end date')
def request_GET_by_program_end(context):
    parameter = f'?completion_date={FILTER_PARAMS.get("completion_date")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/sms/students with filters by student payment completions')
def request_GET_by_payment(context):
    parameter = f'?paid={FILTER_PARAMS.get("paid")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/sms/students with filters by student program completions')
def request_GET_by_completion(context):
    parameter = f'?graduated={FILTER_PARAMS.get("graudated")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/sms/students with filters by student employment status')
def request_GET_by_employment(context):
    parameter = f'?employed={FILTER_PARAMS.get("employed")}'

    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /auth/login/')
def request_login_by_GET(context):
    context.response = context.test.client.get('/auth/login/')
