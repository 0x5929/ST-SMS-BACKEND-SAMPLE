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
                       SMS_FILTER_ROATAION_PARAM,
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
                       SMS_ROTATION_SAMPLE_PATCH_DATA,
                       GMS_CNA_ROTATIONS_API_URL,
                       GMS_HHA_ROTATIONS_API_URL,
                       GMS_CNA_STUDENTS_API_URL,
                       GMS_HHA_STUDENTS_API_URL,
                       GMS_CNA_THEORY_RECORDS_API_URL,
                       GMS_HHA_THEORY_RECORDS_API_URL,
                       GMS_CNA_CLINICAL_RECORDS_API_URL,
                       GMS_HHA_CLINICAL_RECORDS_API_URL,
                       GMS_CNA_ROTATION_POST_SAMPLE_DATA,
                       GMS_CNA_STUDENT_POST_SAMPLE_DATA,
                       GMS_CNA_THEORY_RECORD_POST_SAMPLE_DATA,
                       GMS_CNA_CLINICAL_RECORD_POST_SAMPLE_DATA,
                       GMS_HHA_ROTATION_POST_SAMPLE_DATA,
                       GMS_HHA_STUDENT_POST_SAMPLE_DATA,
                       GMS_HHA_THEORY_RECORD_POST_SAMPLE_DATA,
                       GMS_HHA_CLINICAL_RECORD_POST_SAMPLE_DATA,
                       GMS_CNA_ROTATION_PUT_SAMPLE_DATA,
                       GMS_HHA_ROTATION_PUT_SAMPLE_DATA,
                       GMS_CNA_STUDENT_PUT_SAMPLE_DATA,
                       GMS_HHA_STUDENT_PUT_SAMPLE_DATA,
                       GMS_CNA_THEORY_RECORD_PUT_SAMPLE_DATA,
                       GMS_HHA_THEORY_RECORD_PUT_SAMPLE_DATA,
                       GMS_CNA_CLINICAL_RECORD_PUT_SAMPLE_DATA,
                       GMS_HHA_CLINICAL_RECORD_PUT_SAMPLE_DATA,
                       GMS_CNA_ROTATION_UUID_TO_TEST,
                       GMS_HHA_ROTATION_UUID_TO_TEST,
                       GMS_CNA_STUDENT_UUID_TO_TEST,
                       GMS_HHA_STUDENT_UUID_TO_TEST,
                       GMS_CNA_THEORY_RECORD_UUID_TO_TEST,
                       GMS_HHA_THEORY_RECORD_UUID_TO_TEST,
                       GMS_CNA_CLINICAL_RECORD_UUID_TO_TEST,
                       GMS_HHA_CLINICAL_RECORD_UUID_TO_TEST,
                       GMS_CNA_ROTATION_PATCH_SAMPLE_DATA,
                       GMS_HHA_ROTATION_PATCH_SAMPLE_DATA,
                       GMS_CNA_STUDENT_PATCH_SAMPLE_DATA,
                       GMS_HHA_STUDENT_PATCH_SAMPLE_DATA,
                       GMS_CNA_THEORY_RECORD_PATCH_SAMPLE_DATA,
                       GMS_HHA_THEORY_RECORD_PATCH_SAMPLE_DATA,
                       GMS_CNA_CLINICAL_RECORD_PATCH_SAMPLE_DATA,
                       GMS_HHA_CLINICAL_RECORD_PATCH_SAMPLE_DATA,
                       GMS_STI_CNA_HHA_ROTATION_FILTER_PARAMS,
                       GMS_ST2_CNA_HHA_ROTATION_FILTER_PARAMS,
                       GMS_STI_CNA_STUDENT_FILTER_PARAMS,
                       GMS_STI_HHA_STUDENT_FILTER_PARAMS,
                       GMS_ST2_CNA_STUDENT_FILTER_PARAMS,
                       GMS_ST2_HHA_STUDENT_FILTER_PARAMS,
                       GMS_STI_CNA_ROTATION2_FILTER_PARAMS,
                       GMS_STI_HHA_ROTATION2_FILTER_PARAMS,
                       GMS_STI_CNA_STUDENT2_FILTER_PARAMS,
                       GMS_STI_HHA_STUDENT2_FILTER_PARAMS,
                       GMS_STI_CNA_THEORYRECORD_FILTER_PARAMS,
                       GMS_STI_CNA_THEORYRECORD2_FILTER_PARAMS,
                       GMS_STI_HHA_THEORYRECORD_FILTER_PARAMS,
                       GMS_STI_HHA_THEORYRECORD2_FILTER_PARAMS,
                       GMS_ST2_CNA_THEORYRECORD_FILTER_PARAMS,
                       GMS_ST2_HHA_THEORYRECORD_FILTER_PARAMS,
                       GMS_STI_CNA_CLINICALRECORD_FILTER_PARAMS,
                       GMS_STI_CNA_CLINICALRECORD2_FILTER_PARAMS,
                       GMS_STI_HHA_CLINICALRECORD_FILTER_PARAMS,
                       GMS_STI_HHA_CLINICALRECORD2_FILTER_PARAMS,
                       GMS_ST2_CNA_CLINICALRECORD_FILTER_PARAMS,
                       GMS_ST2_HHA_CLINICALRECORD_FILTER_PARAMS,
                       GMS_CNAROTATION_POST_BAD_EMAIL,
                       GMS_CNAROTATION_PUT_BAD_EMAIL,
                       GMS_CNAROTATION_PATCH_BAD_EMAIL,
                       GMS_HHAROTATION_POST_BAD_EMAIL,
                       GMS_HHAROTATION_PUT_BAD_EMAIL,
                       GMS_HHAROTATION_PATCH_BAD_EMAIL,
                       SMS_FILTER_PARAMS_ST2,
                       SMS_STUDENT_UUID_ST2,
                       SMS_SCHOOL_UUID_ST2,
                       SMS_PROGRAM_UUID_ST2,
                       SMS_ROTATION_UUID_ST2,
                       SMS_ST2_STUDENT_SAMPLE_PATCH_DATA,
                       SMS_ST2_STUDENT_SAMPLE_POST_DATA,
                       SMS_ST2_PROGRAM_SAMPLE_PATCH_DATA,
                       SMS_ST2_ROTATION_SAMPLE_PATCH_DATA,
                       SMS_ST2_SCHOOL_SAMPLE_PATCH_DATA,
                       SMS_ST2_SCHOOL_SAMPLE_POST_DATA,
                       SMS_ST2_PROGRAM_SAMPLE_POST_DATA,
                       SMS_ST2_ROTATION_SAMPLE_POST_DATA,
                       SMS_ST2_SCHOOL_SAMPLE_PUT_DATA,
                       SMS_ST2_PROGRAM_SAMPLE_PUT_DATA,
                       SMS_ST2_ROTATION_SAMPLE_PUT_DATA,
                       SMS_ST2_STUDENT_SAMPLE_PUT_DATA,
                       GMS_ST2_CNA_ROTATION_UUID_TO_TEST,
                       GMS_ST2_CNA_STUDENT_UUID_TO_TEST,
                       GMS_ST2_CNA_THEORY_RECORD_UUID_TO_TEST,
                       GMS_ST2_CNA_CLINICAL_RECORD_UUID_TO_TEST,
                       GMS_ST2_HHA_ROTATION_UUID_TO_TEST,
                       GMS_ST2_HHA_STUDENT_UUID_TO_TEST,
                       GMS_ST2_HHA_THEORY_RECORD_UUID_TO_TEST,
                       GMS_ST2_HHA_CLINICAL_RECORD_UUID_TO_TEST,
                       GMS_ST2_CNA_ROTATION_PATCH_SAMPLE_DATA,
                       GMS_ST2_HHA_ROTATION_PATCH_SAMPLE_DATA,
                       GMS_ST2_CNA_STUDENT_PATCH_SAMPLE_DATA,
                       GMS_ST2_CNA_THEORY_RECORD_PATCH_SAMPLE_DATA,
                       GMS_ST2_CNA_CLINICAL_RECORD_PATCH_SAMPLE_DATA,
                       GMS_ST2_HHA_STUDENT_PATCH_SAMPLE_DATA,
                       GMS_ST2_HHA_THEORY_RECORD_PATCH_SAMPLE_DATA,
                       GMS_ST2_HHA_CLINICAL_RECORD_PATCH_SAMPLE_DATA,
                       GMS_ST2_CNA_ROTATION_PUT_SAMPLE_DATA,
                       GMS_ST2_CNA_STUDENT_PUT_SAMPLE_DATA,
                       GMS_ST2_CNA_THEORY_RECORD_PUT_SAMPLE_DATA,
                       GMS_ST2_CNA_CLINICAL_RECORD_PUT_SAMPLE_DATA,
                       GMS_ST2_HHA_ROTATION_PUT_SAMPLE_DATA,
                       GMS_ST2_HHA_STUDENT_PUT_SAMPLE_DATA,
                       GMS_ST2_HHA_THEORY_RECORD_PUT_SAMPLE_DATA,
                       GMS_ST2_HHA_CLINICAL_RECORD_PUT_SAMPLE_DATA,
                       GMS_ST2_CNA_ROTATION_POST_SAMPLE_DATA,
                       GMS_ST2_CNA_STUDENT_POST_SAMPLE_DATA,
                       GMS_ST2_CNA_THEORY_RECORD_POST_SAMPLE_DATA,
                       GMS_ST2_CNA_CLINICAL_RECORD_POST_SAMPLE_DATA,
                       GMS_ST2_HHA_ROTATION_POST_SAMPLE_DATA,
                       GMS_ST2_HHA_STUDENT_POST_SAMPLE_DATA,
                       GMS_ST2_HHA_THEORY_RECORD_POST_SAMPLE_DATA,
                       GMS_ST2_HHA_CLINICAL_RECORD_POST_SAMPLE_DATA,
                       CMS_CLIENTS_API_URL,
                       CMS_NOTES_API_URL,
                       CMS_CLIENT_UUID_TO_TEST,
                       CMS_NOTE_UUID_TO_TEST,
                       CMS_SECOND_CLIENT_UUID,
                       CMS_SECOND_NOTE_UUID,
                       CMS_ST2_CLIENT_UUID,
                       CMS_ST2_NOTE_UUID,
                       CMS_STI_CLIENT_SAMPLE_POST,
                       CMS_STI_NOTE_SAMPLE_POST,
                       CMS_STI_CLIENT_SAMPLE_PUT,
                       CMS_STI_NOTE_SAMPLE_PUT,
                       CMS_SECOND_CLIENT_PUT,
                       CMS_SECOND_CLIENT_PATCH,
                       CMS_SECOND_NOTE_PATCH,
                       CMS_SECOND_NOTE_PUT,
                       CMS_STI_CLIENT_PATCH,
                       CMS_STI_NOTE_PATCH,
                       CMS_ST2_CLIENT_SAMPLE_POST,
                       CMS_ST2_NOTE_SAMPLE_POST,
                       CMS_ST2_CLIENT_SAMPLE_PUT,
                       CMS_ST2_NOTE_SAMPLE_PUT,
                       CMS_ST2_CLIENT_PATCH,
                       CMS_ST2_NOTE_PATCH,
                       CMS_CLIENT_FILTER_PARAMS,
                       CMS_NOTE_FILTER_PARAMS,
                       CMS_SECOND_CLIENT_FILTER_PARAMS,
                       CMS_SECOND_NOTE_FILTER_PARAMS,
                       CMS_ST2_NOTE_FILTER_PARAMS,
                       CMS_ST2_CLIENT_FILTER_PARAMS)


# NOTE: BELOW ARE SMS RELATED @WHENS

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
    context.uuid = SMS_STUDENT_UUID_TO_TEST
    context.response = context.test.client.delete(
        f'{SMS_STUDENTS_API_URL}{SMS_STUDENT_UUID_TO_TEST}/', headers=headers)


@when('request POST to /api/sms/schools')
def request_POST_to_schools(context):
    post_data = SMS_SCHOOL_SAMPLE_POST_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{SMS_SCHOOLS_API_URL}', post_data, format='json', headers=headers)


@when('request POST to ST2 /api/sms/students/')
def request_POST_to_ST2_students(context):
    post_data = SMS_ST2_STUDENT_SAMPLE_POST_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{SMS_STUDENTS_API_URL}', post_data, format='json', headers=headers)


@when('request POST to ST2 /api/sms/schools/')
def request_POST_to_ST2_schools(context):
    post_data = SMS_ST2_SCHOOL_SAMPLE_POST_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{SMS_SCHOOLS_API_URL}', post_data, format='json', headers=headers)


@when('request POST to ST2 /api/sms/programs/')
def request_POST_to_ST2_programs(context):
    post_data = SMS_ST2_PROGRAM_SAMPLE_POST_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{SMS_PROGRAMS_API_URL}', post_data, format='json', headers=headers)


@when('request POST to ST2 /api/sms/rotations/')
def request_POST_to_ST2_rotations(context):
    post_data = SMS_ST2_ROTATION_SAMPLE_POST_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{SMS_ROTATIONS_API_URL}', post_data, format='json', headers=headers)


@when('request PUT to /api/sms/schools/school_uuid')
def request_PUT_to_school(context):
    put_data = SMS_SCHOOL_SAMPLE_PUT_DATA

    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.put(
        f'{SMS_SCHOOLS_API_URL}{SMS_SCHOOL_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PUT to ST2 /api/sms/schools/school_uuid')
def request_PUT_to_ST2_school(context):
    put_data = SMS_ST2_SCHOOL_SAMPLE_PUT_DATA

    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.put(
        f'{SMS_SCHOOLS_API_URL}{SMS_SCHOOL_UUID_ST2}/', put_data, format='json', headers=headers)


@when('request PUT to ST2 /api/sms/programs/program_uuid')
def request_PUT_to_ST2_program(context):
    put_data = SMS_ST2_PROGRAM_SAMPLE_PUT_DATA

    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.put(
        f'{SMS_PROGRAMS_API_URL}{SMS_PROGRAM_UUID_ST2}/', put_data, format='json', headers=headers)


@when('request PUT to ST2 /api/sms/rotations/rotation_uuid')
def request_PUT_to_ST2_rotation(context):
    put_data = SMS_ST2_ROTATION_SAMPLE_PUT_DATA

    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.put(
        f'{SMS_ROTATIONS_API_URL}{SMS_ROTATION_UUID_ST2}/', put_data, format='json', headers=headers)


@when('request PUT to ST2 /api/sms/students/student_uuid')
def request_PUT_to_ST2_student(context):
    put_data = SMS_ST2_STUDENT_SAMPLE_PUT_DATA

    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.put(
        f'{SMS_STUDENTS_API_URL}{SMS_STUDENT_UUID_ST2}/', put_data, format='json', headers=headers)


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

    context.uuid = SMS_SCHOOL_UUID_TO_TEST
    context.response = context.test.client.delete(
        f'{SMS_SCHOOLS_API_URL}{SMS_SCHOOL_UUID_TO_TEST}/', headers=headers)


@when('request DELETE to ST2 /api/sms/students/student_uuid')
def request_DEL_to_ST2_student(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.uuid = SMS_STUDENT_UUID_ST2
    context.response = context.test.client.delete(
        f'{SMS_STUDENTS_API_URL}{SMS_STUDENT_UUID_ST2}/', headers=headers)


@when('request DELETE to ST2 /api/sms/schools/school_uuid')
def request_DEL_to_ST2_school(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.uuid = SMS_SCHOOL_UUID_ST2
    context.response = context.test.client.delete(
        f'{SMS_SCHOOLS_API_URL}{SMS_SCHOOL_UUID_ST2}/', headers=headers)


@when('request DELETE to ST2 /api/sms/programs/program_uuid')
def request_DEL_to_ST2_program(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.uuid = SMS_PROGRAM_UUID_ST2
    context.response = context.test.client.delete(
        f'{SMS_PROGRAMS_API_URL}{SMS_PROGRAM_UUID_ST2}/', headers=headers)


@when('request DELETE to ST2 /api/sms/rotations/rotation_uuid')
def request_DEL_to_ST2_rotation(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.uuid = SMS_ROTATION_UUID_ST2
    context.response = context.test.client.delete(
        f'{SMS_ROTATIONS_API_URL}{SMS_ROTATION_UUID_ST2}/', headers=headers)


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

    context.uuid = SMS_PROGRAM_UUID_TO_TEST
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

    context.uuid = SMS_ROTATION_UUID_TO_TEST
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


@when('request GET to /api/sms/students with filters by ST2 school name')
def request_GET_to_smsStudents_by_ST2_school_name(context):
    parameter = f'?rotation__program__school__school_name={SMS_FILTER_PARAMS_ST2.get("school_name")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{SMS_STUDENTS_API_URL}{parameter}', headers=headers)


# need to do a different then for this step for [], since there will be two HHAs in test db
@when('request GET to /api/sms/students with filters by ST2 program name')
def request_GET_to_smsStudents_by_ST2_school_name(context):
    parameter = f'?rotation__program__program_name={SMS_FILTER_PARAMS_ST2.get("program_name")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{SMS_STUDENTS_API_URL}{parameter}', headers=headers)

# need to do a different then for this step for [], since there will be two HHAs rot 1 in test db


@when('request GET to /api/sms/students with filters by ST2 rotation number')
def request_GET_to_smsStudents_by_ST2_school_name(context):
    parameter = f'?rotation__rotation_number={SMS_FILTER_PARAMS_ST2.get("rotation_num")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{SMS_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/sms/students with filters by ST2 student first name')
def request_GET_to_smsStudents_by_ST2_school_name(context):
    parameter = f'?first_name={SMS_FILTER_PARAMS_ST2.get("first_name")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{SMS_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/sms/students with filters by ST2 student last name')
def request_GET_to_smsStudents_by_ST2_school_name(context):
    parameter = f'?last_name={SMS_FILTER_PARAMS_ST2.get("last_name")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{SMS_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/sms/students with filters by ST2 student email')
def request_GET_to_smsStudents_by_ST2_school_name(context):
    parameter = f'?email={SMS_FILTER_PARAMS_ST2.get("email")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{SMS_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/sms/students with filters by ST2 student phone number')
def request_GET_to_smsStudents_by_ST2_school_name(context):
    parameter = f'?phone_number={SMS_FILTER_PARAMS_ST2.get("phone")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{SMS_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/sms/students with filters by ST2 student ID')
def request_GET_to_smsStudents_by_ST2_school_name(context):
    parameter = f'?student_id={SMS_FILTER_PARAMS_ST2.get("id_")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{SMS_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/sms/students with filters by ST2 student program end date')
def request_GET_to_smsStudents_by_ST2_school_name(context):
    parameter = f'?completion_date={SMS_FILTER_PARAMS_ST2.get("completion_date")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{SMS_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/sms/students with filters by ST2 student program start date')
def request_GET_to_smsStudents_by_ST2_school_name(context):
    parameter = f'?start_date={SMS_FILTER_PARAMS_ST2.get("start_date")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{SMS_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/sms/students with filters by ST2 student payment completions')
def request_GET_to_smsStudents_by_ST2_school_name(context):
    parameter = f'?paid={SMS_FILTER_PARAMS_ST2.get("paid")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{SMS_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/sms/students with filters by ST2 student program completions')
def request_GET_to_smsStudents_by_ST2_school_name(context):
    parameter = f'?graduated={SMS_FILTER_PARAMS_ST2.get("graduated")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{SMS_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/sms/students with filters by ST2 student employment status')
def request_GET_to_smsStudents_by_ST2_school_name(context):
    parameter = f'?employed={SMS_FILTER_PARAMS_ST2.get("employed")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{SMS_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/sms/rotations with filters by program name')
def request_GET_to_smsRotations_by_program_name(context):
    parameter = f'?program__program_name={SMS_FILTER_ROATAION_PARAM.get("program_name")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{SMS_ROTATIONS_API_URL}{parameter}', headers=headers)


@when('request GET to ST2 /api/sms/students/student_uuid')
def request_GET_ST2_student(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{SMS_STUDENTS_API_URL}{SMS_STUDENT_UUID_ST2}/', headers=headers)


@when('request GET to ST2 /api/sms/schools/school_uuid')
def request_GET_ST2_school(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{SMS_SCHOOLS_API_URL}{SMS_SCHOOL_UUID_ST2}/', headers=headers)


@when('request GET to ST2 /api/sms/programs/program_uuid')
def request_GET_ST2_program(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{SMS_PROGRAMS_API_URL}{SMS_PROGRAM_UUID_ST2}/', headers=headers)


@when('request GET to ST2 /api/sms/rotations/rotation_uuid')
def request_GET_ST2_rotation(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{SMS_ROTATIONS_API_URL}{SMS_ROTATION_UUID_ST2}/', headers=headers)


@when('request PATCH to ST2 /api/sms/students/student_uuid')
def request_PATCH_ST2_students(context):
    patch_data = SMS_ST2_STUDENT_SAMPLE_PATCH_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.patch(
        f'{SMS_STUDENTS_API_URL}{SMS_STUDENT_UUID_ST2}/', patch_data, format='json', headers=headers)


@when('request PATCH to ST2 /api/sms/schools/school_uuid')
def request_PATCH_ST2_schools(context):
    patch_data = SMS_ST2_SCHOOL_SAMPLE_PATCH_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.patch(
        f'{SMS_SCHOOLS_API_URL}{SMS_SCHOOL_UUID_ST2}/', patch_data, format='json', headers=headers)


@when('request PATCH to ST2 /api/sms/programs/program_uuid')
def request_PATCH_ST2_programs(context):
    patch_data = SMS_ST2_PROGRAM_SAMPLE_PATCH_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.patch(
        f'{SMS_PROGRAMS_API_URL}{SMS_PROGRAM_UUID_ST2}/', patch_data, format='json', headers=headers)


@when('request PATCH to ST2 /api/sms/rotations/rotation_uuid')
def request_PATCH_ST2_rotations(context):
    patch_data = SMS_ST2_ROTATION_SAMPLE_PATCH_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.patch(
        f'{SMS_ROTATIONS_API_URL}{SMS_ROTATION_UUID_ST2}/', patch_data, format='json', headers=headers)


@when('request GET to /api/sms/students/student_statistics')
def request_GET_student_statistics(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'/api/sms/student_statistics/', headers=headers)


# NOTE: BELOW ARE GMS RELATED @WHENS


@when('request GET to /api/gms/cnaRotations')
def request_GET_to_cnaRotations(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{GMS_CNA_ROTATIONS_API_URL}', headers=headers)


@when('request GET to /api/gms/cnaRotations/cnaRotation_uuid')
def request_GET_to_cnaRotation_uuid(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{GMS_CNA_ROTATIONS_API_URL}{GMS_CNA_ROTATION_UUID_TO_TEST}/', headers=headers)


@when('request GET to ST2 /api/gms/cnaRotations/cnaRotation_uuid')
def request_GET_to_ST2_cnaRotation_uuid(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{GMS_CNA_ROTATIONS_API_URL}{GMS_ST2_CNA_ROTATION_UUID_TO_TEST}/', headers=headers)


@when('request GET to /api/gms/cnaStudents/cnaStudent_uuid')
def request_GET_to_cnaStudent_uuid(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{GMS_CNA_STUDENTS_API_URL}{GMS_CNA_STUDENT_UUID_TO_TEST}/', headers=headers)


@when('request GET to ST2 /api/gms/cnaStudents/cnaStudent_uuid')
def request_GET_to_ST2_cnaStudent_uuid(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{GMS_CNA_STUDENTS_API_URL}{GMS_ST2_CNA_STUDENT_UUID_TO_TEST}/', headers=headers)


@when('request GET to /api/gms/cnaTheoryRecords/cnaTheoryRecord_uuid')
def request_GET_to_cnaTheoryRecord_uuid(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{GMS_CNA_THEORY_RECORDS_API_URL}{GMS_CNA_THEORY_RECORD_UUID_TO_TEST}/', headers=headers)


@when('request GET to ST2 /api/gms/cnaTheoryRecords/cnaTheoryRecord_uuid')
def request_GET_to_ST2_cnaTheoryRecord_uuid(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{GMS_CNA_THEORY_RECORDS_API_URL}{GMS_ST2_CNA_THEORY_RECORD_UUID_TO_TEST}/', headers=headers)


@when('request GET to /api/gms/cnaClinicalRecords/cnaClinicalRecord_uuid')
def request_GET_to_cnaClinicalRecord_uuid(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{GMS_CNA_CLINICAL_RECORDS_API_URL}{GMS_CNA_CLINICAL_RECORD_UUID_TO_TEST}/', headers=headers)


@when('request GET to ST2 /api/gms/cnaClinicalRecords/cnaClinicalRecord_uuid')
def request_GET_to_ST2_cnaClinicalRecord_uuid(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{GMS_CNA_CLINICAL_RECORDS_API_URL}{GMS_ST2_CNA_CLINICAL_RECORD_UUID_TO_TEST}/', headers=headers)


@when('request GET to /api/gms/hhaRotations/hhaRotation_uuid')
def request_GET_to_hhaRotation_uuid(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{GMS_HHA_ROTATIONS_API_URL}{GMS_HHA_ROTATION_UUID_TO_TEST}/', headers=headers)


@when('request GET to ST2 /api/gms/hhaRotations/hhaRotation_uuid')
def request_GET_to_ST2_hhaRotation_uuid(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{GMS_HHA_ROTATIONS_API_URL}{GMS_ST2_HHA_ROTATION_UUID_TO_TEST}/', headers=headers)


@when('request GET to /api/gms/hhaStudents/hhaStudent_uuid')
def request_GET_to_hhaStudent_uuid(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{GMS_HHA_STUDENTS_API_URL}{GMS_HHA_STUDENT_UUID_TO_TEST}/', headers=headers)


@when('request GET to ST2 /api/gms/hhaStudents/hhaStudent_uuid')
def request_GET_to_ST2_hhaStudent_uuid(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{GMS_HHA_STUDENTS_API_URL}{GMS_ST2_HHA_STUDENT_UUID_TO_TEST}/', headers=headers)


@when('request GET to /api/gms/hhaTheoryRecords/hhaTheoryRecord_uuid')
def request_GET_to_hhaTheoryRecord_uuid(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{GMS_HHA_THEORY_RECORDS_API_URL}{GMS_HHA_THEORY_RECORD_UUID_TO_TEST}/', headers=headers)


@when('request GET to ST2 /api/gms/hhaTheoryRecords/hhaTheoryRecord_uuid')
def request_GET_to_ST2_hhaTheoryRecord_uuid(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{GMS_HHA_THEORY_RECORDS_API_URL}{GMS_ST2_HHA_THEORY_RECORD_UUID_TO_TEST}/', headers=headers)


@when('request GET to /api/gms/hhaClinicalRecords/hhaClinicalRecord_uuid')
def request_GET_to_hhaClinicalRecord_uuid(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{GMS_HHA_CLINICAL_RECORDS_API_URL}{GMS_HHA_CLINICAL_RECORD_UUID_TO_TEST}/', headers=headers)


@when('request GET to ST2 /api/gms/hhaClinicalRecords/hhaClinicalRecord_uuid')
def request_GET_to_ST2_hhaClinicalRecord_uuid(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{GMS_HHA_CLINICAL_RECORDS_API_URL}{GMS_ST2_HHA_CLINICAL_RECORD_UUID_TO_TEST}/', headers=headers)


@when('request GET to /api/gms/cnaStudents')
def request_GET_cnaStudents(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{GMS_CNA_STUDENTS_API_URL}', headers=headers)


@when('request GET to /api/gms/cnaTheoryRecords')
def request_GET_cnaTheoryRecords(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{GMS_CNA_THEORY_RECORDS_API_URL}', headers=headers)


@when('request GET to /api/gms/cnaClinicalRecords')
def request_GET_cnaClinicalRecords(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{GMS_CNA_CLINICAL_RECORDS_API_URL}', headers=headers)


@when('request GET to /api/gms/hhaRotations')
def request_GET_hhaRotations(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{GMS_HHA_ROTATIONS_API_URL}', headers=headers)


@when('request GET to /api/gms/hhaStudents')
def request_GET_hhaStudents(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{GMS_HHA_STUDENTS_API_URL}', headers=headers)


@when('request GET to /api/gms/hhaTheoryRecords')
def request_GET_hhaTheoryRecords(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{GMS_HHA_THEORY_RECORDS_API_URL}', headers=headers)


@when('request GET to /api/gms/hhaClinicalRecords')
def requets_GET_hhaClinicalRecords(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{GMS_HHA_CLINICAL_RECORDS_API_URL}', headers=headers)


@when('request POST to /api/gms/cnaRotations')
def request_POST_cnaRotations(context):
    post_data = GMS_CNA_ROTATION_POST_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{GMS_CNA_ROTATIONS_API_URL}', post_data, format='json', headers=headers)


@when('request POST to ST2 /api/gms/cnaRotations')
def request_POST_ST2_cnaRotations(context):
    post_data = GMS_ST2_CNA_ROTATION_POST_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{GMS_CNA_ROTATIONS_API_URL}', post_data, format='json', headers=headers)


@when('request POST to /api/gms/cnaStudents')
def request_POST_cnaStudents(context):
    post_data = GMS_CNA_STUDENT_POST_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{GMS_CNA_STUDENTS_API_URL}', post_data, format='json', headers=headers)


@when('request POST to ST2 /api/gms/cnaStudents')
def request_POST_ST2_cnaStudents(context):
    post_data = GMS_ST2_CNA_STUDENT_POST_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{GMS_CNA_STUDENTS_API_URL}', post_data, format='json', headers=headers)


@when('request POST to /api/gms/cnaTheoryRecords')
def request_POST_cnaTheoryRecords(context):
    post_data = GMS_CNA_THEORY_RECORD_POST_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{GMS_CNA_THEORY_RECORDS_API_URL}', post_data, format='json', headers=headers)


@when('request POST to ST2 /api/gms/cnaTheoryRecords')
def request_POST_ST2_cnaTheoryRecords(context):
    post_data = GMS_ST2_CNA_THEORY_RECORD_POST_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{GMS_CNA_THEORY_RECORDS_API_URL}', post_data, format='json', headers=headers)


@when('request POST to /api/gms/cnaClinicalRecords')
def request_POST_cnaClinicalRecords(context):
    post_data = GMS_CNA_CLINICAL_RECORD_POST_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{GMS_CNA_CLINICAL_RECORDS_API_URL}', post_data, format='json', headers=headers)


@when('request POST to ST2 /api/gms/cnaClinicalRecords')
def request_POST_ST2_cnaClinicalRecords(context):
    post_data = GMS_ST2_CNA_CLINICAL_RECORD_POST_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{GMS_CNA_CLINICAL_RECORDS_API_URL}', post_data, format='json', headers=headers)


@when('request POST to /api/gms/hhaRotations')
def request_POST_hhaRotations(context):
    post_data = GMS_HHA_ROTATION_POST_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{GMS_HHA_ROTATIONS_API_URL}', post_data, format='json', headers=headers)


@when('request POST to ST2 /api/gms/hhaRotations')
def request_POST_ST2_hhaRotations(context):
    post_data = GMS_ST2_HHA_ROTATION_POST_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{GMS_HHA_ROTATIONS_API_URL}', post_data, format='json', headers=headers)


@when('request POST to /api/gms/hhaStudents')
def request_POST_hhaStudents(context):
    post_data = GMS_HHA_STUDENT_POST_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{GMS_HHA_STUDENTS_API_URL}', post_data, format='json', headers=headers)


@when('request POST to ST2 /api/gms/hhaStudents')
def request_POST_ST2_hhaStudents(context):
    post_data = GMS_ST2_HHA_STUDENT_POST_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{GMS_HHA_STUDENTS_API_URL}', post_data, format='json', headers=headers)


@when('request POST to /api/gms/hhaTheoryRecords')
def request_POST_hhaTheoryRecords(context):
    post_data = GMS_HHA_THEORY_RECORD_POST_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{GMS_HHA_THEORY_RECORDS_API_URL}', post_data, format='json', headers=headers)


@when('request POST to ST2 /api/gms/hhaTheoryRecords')
def request_ST2_POST_hhaTheoryRecords(context):
    post_data = GMS_ST2_HHA_THEORY_RECORD_POST_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{GMS_HHA_THEORY_RECORDS_API_URL}', post_data, format='json', headers=headers)


@when('request POST to /api/gms/hhaClinicalRecords')
def request_POST_hhaClinicalRecords(context):
    post_data = GMS_HHA_CLINICAL_RECORD_POST_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{GMS_HHA_CLINICAL_RECORDS_API_URL}', post_data, format='json', headers=headers)


@when('request POST to ST2 /api/gms/hhaClinicalRecords')
def request_POST_hhaClinicalRecords(context):
    post_data = GMS_ST2_HHA_CLINICAL_RECORD_POST_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{GMS_HHA_CLINICAL_RECORDS_API_URL}', post_data, format='json', headers=headers)


@when('request PUT to /api/gms/cnaRotations')
def request_PUT_cnaRotations(context):
    put_data = GMS_CNA_ROTATION_PUT_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.put(
        f'{GMS_CNA_ROTATIONS_API_URL}{GMS_CNA_ROTATION_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PUT to ST2 /api/gms/cnaRotations')
def request_PUT_ST2_cnaRotations(context):
    put_data = GMS_ST2_CNA_ROTATION_PUT_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.put(
        f'{GMS_CNA_ROTATIONS_API_URL}{GMS_ST2_CNA_ROTATION_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PUT to /api/gms/cnaStudents')
def request_PUT_cnaStudents(context):
    put_data = GMS_CNA_STUDENT_PUT_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.put(
        f'{GMS_CNA_STUDENTS_API_URL}{GMS_CNA_STUDENT_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PUT to ST2 /api/gms/cnaStudents')
def request_PUT_ST2_cnaStudents(context):
    put_data = GMS_ST2_CNA_STUDENT_PUT_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.put(
        f'{GMS_CNA_STUDENTS_API_URL}{GMS_ST2_CNA_STUDENT_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PUT to /api/gms/cnaTheoryRecords')
def request_PUT_cnaTheoryRecords(context):
    put_data = GMS_CNA_THEORY_RECORD_PUT_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.put(
        f'{GMS_CNA_THEORY_RECORDS_API_URL}{GMS_CNA_THEORY_RECORD_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PUT to ST2 /api/gms/cnaTheoryRecords')
def request_PUT_ST2_cnaTheoryRecords(context):
    put_data = GMS_ST2_CNA_THEORY_RECORD_PUT_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.put(
        f'{GMS_CNA_THEORY_RECORDS_API_URL}{GMS_ST2_CNA_THEORY_RECORD_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PUT to /api/gms/cnaClinicalRecords')
def request_PUT_cnaClinicalRecords(context):
    put_data = GMS_CNA_CLINICAL_RECORD_PUT_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.put(
        f'{GMS_CNA_CLINICAL_RECORDS_API_URL}{GMS_CNA_CLINICAL_RECORD_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PUT to ST2 /api/gms/cnaClinicalRecords')
def request_PUT_ST2_cnaClinicalRecords(context):
    put_data = GMS_ST2_CNA_CLINICAL_RECORD_PUT_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.put(
        f'{GMS_CNA_CLINICAL_RECORDS_API_URL}{GMS_ST2_CNA_CLINICAL_RECORD_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PUT to /api/gms/hhaRotations')
def request_PUT_hhaRotations(context):
    put_data = GMS_HHA_ROTATION_PUT_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.put(
        f'{GMS_HHA_ROTATIONS_API_URL}{GMS_HHA_ROTATION_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PUT to ST2 /api/gms/hhaRotations')
def request_PUT_ST2_hhaRotations(context):
    put_data = GMS_ST2_HHA_ROTATION_PUT_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.put(
        f'{GMS_HHA_ROTATIONS_API_URL}{GMS_ST2_HHA_ROTATION_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PUT to /api/gms/hhaStudents')
def request_PUT_hhaStudents(context):
    put_data = GMS_HHA_STUDENT_PUT_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.put(
        f'{GMS_HHA_STUDENTS_API_URL}{GMS_HHA_STUDENT_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PUT to ST2 /api/gms/hhaStudents')
def request_PUT_ST2_hhaStudents(context):
    put_data = GMS_ST2_HHA_STUDENT_PUT_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.put(
        f'{GMS_HHA_STUDENTS_API_URL}{GMS_ST2_HHA_STUDENT_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PUT to /api/gms/hhaTheoryRecords')
def request_PUT_hhaTheoryRecords(context):
    put_data = GMS_HHA_THEORY_RECORD_PUT_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.put(
        f'{GMS_HHA_THEORY_RECORDS_API_URL}{GMS_HHA_THEORY_RECORD_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PUT to ST2 /api/gms/hhaTheoryRecords')
def request_PUT_ST2_hhaTheoryRecords(context):
    put_data = GMS_ST2_HHA_THEORY_RECORD_PUT_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.put(
        f'{GMS_HHA_THEORY_RECORDS_API_URL}{GMS_ST2_HHA_THEORY_RECORD_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PUT to /api/gms/hhaClinicalRecords')
def request_PUT_hhaClinicalRecords(context):
    put_data = GMS_HHA_CLINICAL_RECORD_PUT_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.put(
        f'{GMS_HHA_CLINICAL_RECORDS_API_URL}{GMS_HHA_CLINICAL_RECORD_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PUT to ST2 /api/gms/hhaClinicalRecords')
def request_PUT_ST2_hhaClinicalRecords(context):
    put_data = GMS_ST2_HHA_CLINICAL_RECORD_PUT_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.put(
        f'{GMS_HHA_CLINICAL_RECORDS_API_URL}{GMS_ST2_HHA_CLINICAL_RECORD_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PATCH to /api/gms/cnaRotations')
def request_PATCH_cnaRotations(context):
    patch_data = GMS_CNA_ROTATION_PATCH_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.patch(
        f'{GMS_CNA_ROTATIONS_API_URL}{GMS_CNA_ROTATION_UUID_TO_TEST}/', patch_data, format='json', headers=headers)


@when('request PATCH to ST2 /api/gms/cnaRotations/cnaRotation_uuid')
def request_PATCH_ST2_cnaRotations(context):
    patch_data = GMS_ST2_CNA_ROTATION_PATCH_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.patch(
        f'{GMS_CNA_ROTATIONS_API_URL}{GMS_ST2_CNA_ROTATION_UUID_TO_TEST}/', patch_data, format='json', headers=headers)


@when('request PATCH to /api/gms/cnaStudents')
def request_PATCH_cnaStudents(context):
    patch_data = GMS_CNA_STUDENT_PATCH_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.patch(
        f'{GMS_CNA_STUDENTS_API_URL}{GMS_CNA_STUDENT_UUID_TO_TEST}/', patch_data, format='json', headers=headers)


@when('request PATCH to ST2 /api/gms/cnaStudents/cnaStudent_uuid')
def request_PATCH_ST2_cnaStudents(context):
    patch_data = GMS_ST2_CNA_STUDENT_PATCH_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.patch(
        f'{GMS_CNA_STUDENTS_API_URL}{GMS_ST2_CNA_STUDENT_UUID_TO_TEST}/', patch_data, format='json', headers=headers)


@when('request PATCH to /api/gms/cnaTheoryRecords')
def request_PATCH_cnaTheoryRecords(context):
    patch_data = GMS_CNA_THEORY_RECORD_PATCH_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.patch(
        f'{GMS_CNA_THEORY_RECORDS_API_URL}{GMS_CNA_THEORY_RECORD_UUID_TO_TEST}/', patch_data, format='json', headers=headers)


@when('request PATCH to ST2 /api/gms/cnaTheoryRecords/cnaTheoryRecord_uuid')
def request_PATCH_ST2_cnaTheoryRecords(context):
    patch_data = GMS_ST2_CNA_THEORY_RECORD_PATCH_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.patch(
        f'{GMS_CNA_THEORY_RECORDS_API_URL}{GMS_ST2_CNA_THEORY_RECORD_UUID_TO_TEST}/', patch_data, format='json', headers=headers)


@when('request PATCH to /api/gms/cnaClinicalRecords')
def request_PATCH_cnaClinicalRecords(context):
    patch_data = GMS_CNA_CLINICAL_RECORD_PATCH_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.patch(
        f'{GMS_CNA_CLINICAL_RECORDS_API_URL}{GMS_CNA_CLINICAL_RECORD_UUID_TO_TEST}/', patch_data, format='json', headers=headers)


@when('request PATCH to ST2 /api/gms/cnaClinicalRecords/cnaClinicalRecord_uuid')
def request_PATCH_ST2_cnaClinicalRecords(context):
    patch_data = GMS_ST2_CNA_CLINICAL_RECORD_PATCH_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.patch(
        f'{GMS_CNA_CLINICAL_RECORDS_API_URL}{GMS_ST2_CNA_CLINICAL_RECORD_UUID_TO_TEST}/', patch_data, format='json', headers=headers)


@when('request PATCH to /api/gms/hhaRotations')
def request_PATCH_hhaRotations(context):
    patch_data = GMS_HHA_ROTATION_PATCH_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.patch(
        f'{GMS_HHA_ROTATIONS_API_URL}{GMS_HHA_ROTATION_UUID_TO_TEST}/', patch_data, format='json', headers=headers)


@when('request PATCH to ST2 /api/gms/hhaRotations/hhaRotation_uuid')
def request_PATCH_ST2_hhaRotations(context):
    patch_data = GMS_ST2_HHA_ROTATION_PATCH_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.patch(
        f'{GMS_HHA_ROTATIONS_API_URL}{GMS_ST2_HHA_ROTATION_UUID_TO_TEST}/', patch_data, format='json', headers=headers)


@when('request PATCH to /api/gms/hhaStudents')
def request_PATCH_hhaStudents(context):
    patch_data = GMS_HHA_STUDENT_PATCH_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.patch(
        f'{GMS_HHA_STUDENTS_API_URL}{GMS_HHA_STUDENT_UUID_TO_TEST}/', patch_data, format='json', headers=headers)


@when('request PATCH to ST2 /api/gms/hhaStudents/hhaStudent_uuid')
def request_PATCH_ST2_hhaStudents(context):
    patch_data = GMS_ST2_HHA_STUDENT_PATCH_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.patch(
        f'{GMS_HHA_STUDENTS_API_URL}{GMS_ST2_HHA_STUDENT_UUID_TO_TEST}/', patch_data, format='json', headers=headers)


@when('request PATCH to /api/gms/hhaTheoryRecords')
def request_PATCH_hhaTheoryRecords(context):
    patch_data = GMS_HHA_THEORY_RECORD_PATCH_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.patch(
        f'{GMS_HHA_THEORY_RECORDS_API_URL}{GMS_HHA_THEORY_RECORD_UUID_TO_TEST}/', patch_data, format='json', headers=headers)


@when('request PATCH to ST2 /api/gms/hhaTheoryRecords/hhaTheoryRecord_uuid')
def request_PATCH_ST2_hhaTheoryRecords(context):
    patch_data = GMS_ST2_HHA_THEORY_RECORD_PATCH_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.patch(
        f'{GMS_HHA_THEORY_RECORDS_API_URL}{GMS_ST2_HHA_THEORY_RECORD_UUID_TO_TEST}/', patch_data, format='json', headers=headers)


@when('request PATCH to /api/gms/hhaClinicalRecords')
def request_PATCH_hhaClinicalRecords(context):
    patch_data = GMS_HHA_CLINICAL_RECORD_PATCH_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.patch(
        f'{GMS_HHA_CLINICAL_RECORDS_API_URL}{GMS_HHA_CLINICAL_RECORD_UUID_TO_TEST}/', patch_data, format='json', headers=headers)


@when('request PATCH to ST2 /api/gms/hhaClinicalRecords/hhaClinicalRecord_uuid')
def request_PATCH_ST2_hhaClinicalRecords(context):
    patch_data = GMS_ST2_HHA_CLINICAL_RECORD_PATCH_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.patch(
        f'{GMS_HHA_CLINICAL_RECORDS_API_URL}{GMS_ST2_HHA_CLINICAL_RECORD_UUID_TO_TEST}/', patch_data, format='json', headers=headers)


@when('request DELETE to /api/gms/cnaRotations')
def request_DELETE_cnaRotations(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.uuid = GMS_CNA_ROTATION_UUID_TO_TEST
    context.response = context.test.client.delete(
        f'{GMS_CNA_ROTATIONS_API_URL}{GMS_CNA_ROTATION_UUID_TO_TEST}/', headers=headers)


@when('request DELETE to ST2 /api/gms/cnaRotations')
def request_DELETE_ST2_cnaRotations(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.uuid = GMS_ST2_CNA_ROTATION_UUID_TO_TEST
    context.response = context.test.client.delete(
        f'{GMS_CNA_ROTATIONS_API_URL}{GMS_ST2_CNA_ROTATION_UUID_TO_TEST}/', headers=headers)


@when('request DELETE to /api/gms/cnaStudents')
def request_DELETE_cnaStudents(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.uuid = GMS_CNA_STUDENT_UUID_TO_TEST
    context.response = context.test.client.delete(
        f'{GMS_CNA_STUDENTS_API_URL}{GMS_CNA_STUDENT_UUID_TO_TEST}/', headers=headers)


@when('request DELETE to ST2 /api/gms/cnaStudents')
def request_DELETE_ST2_cnaStudents(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.uuid = GMS_ST2_CNA_STUDENT_UUID_TO_TEST
    context.response = context.test.client.delete(
        f'{GMS_CNA_STUDENTS_API_URL}{GMS_ST2_CNA_STUDENT_UUID_TO_TEST}/', headers=headers)


@when('request DELETE to /api/gms/cnaTheoryRecords')
def request_DELETE_cnaTheoryRecords(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.uuid = GMS_CNA_THEORY_RECORD_UUID_TO_TEST
    context.response = context.test.client.delete(
        f'{GMS_CNA_THEORY_RECORDS_API_URL}{GMS_CNA_THEORY_RECORD_UUID_TO_TEST}/', headers=headers)


@when('request DELETE to ST2 /api/gms/cnaTheoryRecords')
def request_DELETE_ST2_cnaTheoryRecords(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.uuid = GMS_ST2_CNA_THEORY_RECORD_UUID_TO_TEST
    context.response = context.test.client.delete(
        f'{GMS_CNA_THEORY_RECORDS_API_URL}{GMS_ST2_CNA_THEORY_RECORD_UUID_TO_TEST}/', headers=headers)


@when('request DELETE to /api/gms/cnaClinicalRecords')
def request_DELETE_cnaClinicalRecords(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.uuid = GMS_CNA_CLINICAL_RECORD_UUID_TO_TEST

    context.response = context.test.client.delete(
        f'{GMS_CNA_CLINICAL_RECORDS_API_URL}{GMS_CNA_CLINICAL_RECORD_UUID_TO_TEST}/', headers=headers)


@when('request DELETE to ST2 /api/gms/cnaClinicalRecords')
def request_DELETE_ST2_cnaClinicalRecords(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.uuid = GMS_ST2_CNA_CLINICAL_RECORD_UUID_TO_TEST

    context.response = context.test.client.delete(
        f'{GMS_CNA_CLINICAL_RECORDS_API_URL}{GMS_ST2_CNA_CLINICAL_RECORD_UUID_TO_TEST}/', headers=headers)


@when('request DELETE to /api/gms/hhaRotations')
def request_DELETE_hhaRotations(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.uuid = GMS_HHA_ROTATION_UUID_TO_TEST
    context.response = context.test.client.delete(
        f'{GMS_HHA_ROTATIONS_API_URL}{GMS_HHA_ROTATION_UUID_TO_TEST}/', headers=headers)


@when('request DELETE to ST2 /api/gms/hhaRotations')
def request_DELETE_hhaRotations(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.uuid = GMS_ST2_HHA_ROTATION_UUID_TO_TEST
    context.response = context.test.client.delete(
        f'{GMS_HHA_ROTATIONS_API_URL}{GMS_ST2_HHA_ROTATION_UUID_TO_TEST}/', headers=headers)


@when('request DELETE to /api/gms/hhaStudents')
def request_DELETE_hhaStudents(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.uuid = GMS_HHA_STUDENT_UUID_TO_TEST
    context.response = context.test.client.delete(
        f'{GMS_HHA_STUDENTS_API_URL}{GMS_HHA_STUDENT_UUID_TO_TEST}/', headers=headers)


@when('request DELETE to ST2 /api/gms/hhaStudents')
def request_DELETE_ST2_hhaStudents(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.uuid = GMS_ST2_HHA_STUDENT_UUID_TO_TEST
    context.response = context.test.client.delete(
        f'{GMS_HHA_STUDENTS_API_URL}{GMS_ST2_HHA_STUDENT_UUID_TO_TEST}/', headers=headers)


@when('request DELETE to /api/gms/hhaTheoryRecords')
def request_DELETE_hhaTheoryRecords(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.uuid = GMS_HHA_THEORY_RECORD_UUID_TO_TEST

    context.response = context.test.client.delete(
        f'{GMS_HHA_THEORY_RECORDS_API_URL}{GMS_HHA_THEORY_RECORD_UUID_TO_TEST}/', headers=headers)


@when('request DELETE to ST2 /api/gms/hhaTheoryRecords')
def request_DELETE_ST2_hhaTheoryRecords(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.uuid = GMS_ST2_HHA_THEORY_RECORD_UUID_TO_TEST

    context.response = context.test.client.delete(
        f'{GMS_HHA_THEORY_RECORDS_API_URL}{GMS_ST2_HHA_THEORY_RECORD_UUID_TO_TEST}/', headers=headers)


@when('request DELETE to /api/gms/hhaClinicalRecords')
def request_DELETE_hhaClinicalRecords(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.uuid = GMS_HHA_CLINICAL_RECORD_UUID_TO_TEST
    context.response = context.test.client.delete(
        f'{GMS_HHA_CLINICAL_RECORDS_API_URL}{GMS_HHA_CLINICAL_RECORD_UUID_TO_TEST}/', headers=headers)


@when('request DELETE to ST2 /api/gms/hhaClinicalRecords')
def request_DELETE_ST2_hhaClinicalRecords(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.uuid = GMS_ST2_HHA_CLINICAL_RECORD_UUID_TO_TEST
    context.response = context.test.client.delete(
        f'{GMS_HHA_CLINICAL_RECORDS_API_URL}{GMS_ST2_HHA_CLINICAL_RECORD_UUID_TO_TEST}/', headers=headers)


@when('request GET to /api/gms/cnaRotations with filters by STI start_date')
def request_GET_cnaRotations_by_start_date_STI(context):
    parameter = f'?start_date={GMS_STI_CNA_HHA_ROTATION_FILTER_PARAMS.get("start_date")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_CNA_ROTATIONS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/cnaRotations with filters by STI end_date')
def request_GET_cnaRotations_by_end_date_STI(context):
    parameter = f'?end_date={GMS_STI_CNA_HHA_ROTATION_FILTER_PARAMS.get("end_date")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_CNA_ROTATIONS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/cnaRotations with filters by STI rotation_num')
def request_GET_cnaRotations_by_rotation_num_STI(context):
    parameter = f'?rotation_num={GMS_STI_CNA_HHA_ROTATION_FILTER_PARAMS.get("rotation_num")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_CNA_ROTATIONS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/hhaRotations with filters by STI start_date')
def request_GET_hhaRotations_by_start_date_STI(context):
    parameter = f'?start_date={GMS_STI_CNA_HHA_ROTATION_FILTER_PARAMS.get("start_date")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_HHA_ROTATIONS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/hhaRotations with filters by STI end_date')
def request_GET_hhaRotations_by_end_date_STI(context):
    parameter = f'?end_date={GMS_STI_CNA_HHA_ROTATION_FILTER_PARAMS.get("end_date")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_HHA_ROTATIONS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/hhaRotations with filters by STI rotation_num')
def request_GET_hhaRotations_by_rotation_num_STI(context):
    parameter = f'?rotation_num={GMS_STI_CNA_HHA_ROTATION_FILTER_PARAMS.get("rotation_num")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_HHA_ROTATIONS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/cnaRotations with filters by ST2 start_date')
def request_GET_cnaRotations_by_start_date_ST2(context):
    parameter = f'?start_date={GMS_ST2_CNA_HHA_ROTATION_FILTER_PARAMS.get("start_date")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_CNA_ROTATIONS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/cnaRotations with filters by ST2 end_date')
def request_GET_cnaRotations_by_end_date_ST2(context):
    parameter = f'?end_date={GMS_ST2_CNA_HHA_ROTATION_FILTER_PARAMS.get("end_date")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_CNA_ROTATIONS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/cnaRotations with filters by ST2 rotation_num')
def request_GET_cnaRotations_by_rotation_num_ST2(context):
    parameter = f'?rotation_num={GMS_ST2_CNA_HHA_ROTATION_FILTER_PARAMS.get("rotation_num")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_CNA_ROTATIONS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/hhaRotations with filters by ST2 start_date')
def request_GET_hhaRotations_by_start_date_ST2(context):
    parameter = f'?start_date={GMS_ST2_CNA_HHA_ROTATION_FILTER_PARAMS.get("start_date")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_HHA_ROTATIONS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/hhaRotations with filters by ST2 end_date')
def request_GET_hhaRotations_by_end_date_ST2(context):
    parameter = f'?end_date={GMS_ST2_CNA_HHA_ROTATION_FILTER_PARAMS.get("end_date")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_HHA_ROTATIONS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/hhaRotations with filters by ST2 rotation_num')
def request_GET_hhaRotations_by_rotation_num_ST2(context):
    parameter = f'?rotation_num={GMS_ST2_CNA_HHA_ROTATION_FILTER_PARAMS.get("rotation_num")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_HHA_ROTATIONS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/cnaStudents with filters by STI first_name')
def request_GET_cnaStudents_by_first_name_STI(context):
    parameter = f'?first_name={GMS_STI_CNA_STUDENT_FILTER_PARAMS.get("first_name")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_CNA_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/cnaStudents with filters by STI last_name')
def request_GET_cnaStudents_by_last_name_STI(context):
    parameter = f'?last_name={GMS_STI_CNA_STUDENT_FILTER_PARAMS.get("last_name")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_CNA_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/cnaStudents with filters by STI makeup_student')
def request_GET_cnaStudents_by_makeup_student_STI(context):
    parameter = f'?makeup_student={GMS_STI_CNA_STUDENT_FILTER_PARAMS.get("makeup_student")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_CNA_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/hhaStudents with filters by STI first_name')
def request_GET_hhaStudents_by_first_name_STI(context):
    parameter = f'?first_name={GMS_STI_HHA_STUDENT_FILTER_PARAMS.get("first_name")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_HHA_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/hhaStudents with filters by STI last_name')
def request_GET_hhaStudents_by_last_name_STI(context):
    parameter = f'?last_name={GMS_STI_HHA_STUDENT_FILTER_PARAMS.get("last_name")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_HHA_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/hhaStudents with filters by STI makeup_student')
def request_GET_hhaStudents_by_makeup_student_STI(context):
    parameter = f'?makeup_student={GMS_STI_HHA_STUDENT_FILTER_PARAMS.get("makeup_student")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_HHA_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/cnaStudents with filters by ST2 first_name')
def request_GET_cnaStudents_by_first_name_ST2(context):
    parameter = f'?first_name={GMS_ST2_CNA_STUDENT_FILTER_PARAMS.get("first_name")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_CNA_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/cnaStudents with filters by ST2 last_name')
def request_GET_cnaStudents_by_last_name_ST2(context):
    parameter = f'?last_name={GMS_ST2_CNA_STUDENT_FILTER_PARAMS.get("last_name")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_CNA_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/cnaStudents with filters by ST2 makeup_student')
def request_GET_cnaStudents_by_makeup_student_ST2(context):
    parameter = f'?makeup_student={GMS_ST2_CNA_STUDENT_FILTER_PARAMS.get("makeup_student")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_CNA_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/hhaStudents with filters by ST2 first_name')
def request_GET_hhaStudents_by_first_name_ST2(context):
    parameter = f'?first_name={GMS_ST2_HHA_STUDENT_FILTER_PARAMS.get("first_name")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_HHA_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/hhaStudents with filters by ST2 last_name')
def request_GET_hhaStudents_by_last_name_ST2(context):
    parameter = f'?last_name={GMS_ST2_HHA_STUDENT_FILTER_PARAMS.get("last_name")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_HHA_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/hhaStudents with filters by ST2 makeup_student')
def request_GET_hhaStudents_by_makeup_student_ST2(context):
    parameter = f'?makeup_student={GMS_ST2_HHA_STUDENT_FILTER_PARAMS.get("makeup_student")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_HHA_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to second instructor /api/gms/cnaRotations with filters by STI start_date')
def request_GET_second_cnaRotations_by_start_date(context):
    parameter = f'?start_date={GMS_STI_CNA_ROTATION2_FILTER_PARAMS.get("start_date")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_CNA_ROTATIONS_API_URL}{parameter}', headers=headers)


@when('request GET to second instructor /api/gms/cnaRotations with filters by STI end_date')
def request_GET_second_cnaRotations_by_end_date(context):
    parameter = f'?end_date={GMS_STI_CNA_ROTATION2_FILTER_PARAMS.get("end_date")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_CNA_ROTATIONS_API_URL}{parameter}', headers=headers)


@when('request GET to second instructor /api/gms/cnaRotations with filters by STI rotation_num')
def request_GET_second_cnaRotations_by_rotation_num(context):
    parameter = f'?rotation_num={GMS_STI_CNA_ROTATION2_FILTER_PARAMS.get("rotation_num")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_CNA_ROTATIONS_API_URL}{parameter}', headers=headers)


@when('request GET to second instructor /api/gms/hhaRotations with filters by STI start_date')
def request_GET_second_hhaRotations_by_start_date(context):
    parameter = f'?start_date={GMS_STI_HHA_ROTATION2_FILTER_PARAMS.get("start_date")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_HHA_ROTATIONS_API_URL}{parameter}', headers=headers)


@when('request GET to second instructor /api/gms/hhaRotations with filters by STI end_date')
def request_GET_second_hhaRotations_by_end_date(context):
    parameter = f'?end_date={GMS_STI_HHA_ROTATION2_FILTER_PARAMS.get("end_date")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_HHA_ROTATIONS_API_URL}{parameter}', headers=headers)


@when('request GET to second instructor /api/gms/hhaRotations with filters by STI rotation_num')
def request_GET_second_hhaRotations_by_rotation_num(context):
    parameter = f'?rotation_num={GMS_STI_HHA_ROTATION2_FILTER_PARAMS.get("rotation_num")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_HHA_ROTATIONS_API_URL}{parameter}', headers=headers)


@when('request GET to second instructor /api/gms/cnaStudents with filters by STI first_name')
def request_GET_second_cnaStudents_by_first_name(context):
    parameter = f'?first_name={GMS_STI_CNA_STUDENT2_FILTER_PARAMS.get("first_name")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_CNA_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to second instructor /api/gms/cnaStudents with filters by STI last_name')
def request_GET_second_cnaStudents_by_last_name(context):
    parameter = f'?last_name={GMS_STI_CNA_STUDENT2_FILTER_PARAMS.get("last_name")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_CNA_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to second instructor /api/gms/cnaStudents with filters by STI makeup_student')
def request_GET_second_cnaStudents_by_makeup_student(context):
    parameter = f'?makeup_student={GMS_STI_CNA_STUDENT2_FILTER_PARAMS.get("makeup_student")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_CNA_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to second instructor /api/gms/hhaStudents with filters by STI first_name')
def request_GET_second_hhaStudents_by_first_name(context):
    parameter = f'?first_name={GMS_STI_HHA_STUDENT2_FILTER_PARAMS.get("first_name")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_HHA_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to second instructor /api/gms/hhaStudents with filters by STI last_name')
def request_GET_second_hhaStudents_by_last_name(context):
    parameter = f'?last_name={GMS_STI_HHA_STUDENT2_FILTER_PARAMS.get("last_name")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_HHA_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to second instructor /api/gms/hhaStudents with filters by STI makeup_student')
def request_GET_second_hhaStudents_by_makeup_student(context):
    parameter = f'?makeup_student={GMS_STI_HHA_STUDENT2_FILTER_PARAMS.get("makeup_student")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.test_data = GMS_STI_HHA_STUDENT2_FILTER_PARAMS
    context.test_param = ['first_name', 'last_name']
    context.response = context.test.client.get(
        f'{GMS_HHA_STUDENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/cnaTheoryRecords with filters by STI date')
def request_GET_cnaTheoryRecords_by_date(context):
    parameter = f'?date={GMS_STI_CNA_THEORYRECORD_FILTER_PARAMS.get("date")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_CNA_THEORY_RECORDS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/cnaTheoryRecords with filters by STI completed')
def request_GET_cnaTheoryRecords_by_completed(context):
    parameter = f'?completed={GMS_STI_CNA_THEORYRECORD_FILTER_PARAMS.get("completed")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_CNA_THEORY_RECORDS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/cnaTheoryRecords with filters by STI topic')
def request_GET_cnaTheoryRecords_by_topic(context):
    parameter = f'?topic={GMS_STI_CNA_THEORYRECORD_FILTER_PARAMS.get("topic")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_CNA_THEORY_RECORDS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/hhaTheoryRecords with filters by STI date')
def request_GET_hhaTheoryRecords_by_date(context):
    parameter = f'?date={GMS_STI_HHA_THEORYRECORD_FILTER_PARAMS.get("date")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_HHA_THEORY_RECORDS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/hhaTheoryRecords with filters by STI completed')
def request_GET_hhaTheoryRecords_by_completed(context):
    parameter = f'?completed={GMS_STI_HHA_THEORYRECORD_FILTER_PARAMS.get("completed")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_HHA_THEORY_RECORDS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/hhaTheoryRecords with filters by STI topic')
def request_GET_hhaTheoryRecords_by_topic(context):
    parameter = f'?topic={GMS_STI_HHA_THEORYRECORD_FILTER_PARAMS.get("topic")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_HHA_THEORY_RECORDS_API_URL}{parameter}', headers=headers)


@when('request GET to second instructor /api/gms/cnaTheoryRecords with filters by STI date')
def request_GET_second_cnaTheoryRecords_by_date(context):
    parameter = f'?date={GMS_STI_CNA_THEORYRECORD2_FILTER_PARAMS.get("date")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_CNA_THEORY_RECORDS_API_URL}{parameter}', headers=headers)


@when('request GET to second instructor /api/gms/cnaTheoryRecords with filters by STI completed')
def request_GET_second_cnaTheoryRecords_by_completed(context):
    parameter = f'?completed={GMS_STI_CNA_THEORYRECORD2_FILTER_PARAMS.get("completed")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_CNA_THEORY_RECORDS_API_URL}{parameter}', headers=headers)


@when('request GET to second instructor /api/gms/cnaTheoryRecords with filters by STI topic')
def request_GET_second_cnaTheoryRecords_by_topic(context):
    parameter = f'?topic={GMS_STI_CNA_THEORYRECORD2_FILTER_PARAMS.get("topic")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_CNA_THEORY_RECORDS_API_URL}{parameter}', headers=headers)


@when('request GET to second instructor /api/gms/hhaTheoryRecords with filters by STI date')
def request_GET_second_hhaTheoryRecords_by_date(context):
    parameter = f'?date={GMS_STI_HHA_THEORYRECORD2_FILTER_PARAMS.get("date")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_HHA_THEORY_RECORDS_API_URL}{parameter}', headers=headers)


@when('request GET to second instructor /api/gms/hhaTheoryRecords with filters by STI completed')
def request_GET_second_hhaTheoryRecords_by_completed(context):
    parameter = f'?completed={GMS_STI_HHA_THEORYRECORD2_FILTER_PARAMS.get("completed")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.test_data = GMS_STI_HHA_THEORYRECORD2_FILTER_PARAMS
    context.test_param = ['date', 'topic']

    context.response = context.test.client.get(
        f'{GMS_HHA_THEORY_RECORDS_API_URL}{parameter}', headers=headers)


@when('request GET to second instructor /api/gms/hhaTheoryRecords with filters by STI topic')
def request_GET_second_hhaTheoryRecords_by_topic(context):
    parameter = f'?topic={GMS_STI_HHA_THEORYRECORD2_FILTER_PARAMS.get("topic")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_HHA_THEORY_RECORDS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/cnaTheoryRecords with filters by ST2 date')
def request_GET_cnaTheoryRecords_by_date_ST2(context):
    parameter = f'?date={GMS_ST2_CNA_THEORYRECORD_FILTER_PARAMS.get("date")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_CNA_THEORY_RECORDS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/cnaTheoryRecords with filters by ST2 completed')
def request_GET_cnaTheoryRecords_by_completed_ST2(context):
    parameter = f'?completed={GMS_ST2_CNA_THEORYRECORD_FILTER_PARAMS.get("completed")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_CNA_THEORY_RECORDS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/cnaTheoryRecords with filters by ST2 topic')
def request_GET_cnaTheoryRecords_by_topic_ST2(context):
    parameter = f'?topic={GMS_ST2_CNA_THEORYRECORD_FILTER_PARAMS.get("topic")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_CNA_THEORY_RECORDS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/hhaTheoryRecords with filters by ST2 date')
def request_GET_hhaTheoryRecords_by_date_ST2(context):
    parameter = f'?date={GMS_ST2_HHA_THEORYRECORD_FILTER_PARAMS.get("date")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_HHA_THEORY_RECORDS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/hhaTheoryRecords with filters by ST2 completed')
def request_GET_hhaTheoryRecords_by_completed_ST2(context):
    parameter = f'?completed={GMS_ST2_HHA_THEORYRECORD_FILTER_PARAMS.get("completed")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_HHA_THEORY_RECORDS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/hhaTheoryRecords with filters by ST2 topic')
def request_GET_hhaTheoryRecords_by_topic_ST2(context):
    parameter = f'?topic={GMS_ST2_HHA_THEORYRECORD_FILTER_PARAMS.get("topic")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_HHA_THEORY_RECORDS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/cnaClinicalRecords with filters by STI date')
def request_GET_cnaClinicalRecords_by_date(context):
    parameter = f'?date={GMS_STI_CNA_CLINICALRECORD_FILTER_PARAMS.get("date")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_CNA_CLINICAL_RECORDS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/cnaClinicalRecords with filters by STI completed')
def request_GET_cnaClinicalRecords_by_completed(context):
    parameter = f'?completed={GMS_STI_CNA_CLINICALRECORD_FILTER_PARAMS.get("completed")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_CNA_CLINICAL_RECORDS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/cnaClinicalRecords with filters by STI topic')
def request_GET_cnaClinicalRecords_by_topic(context):
    parameter = f'?topic={GMS_STI_CNA_CLINICALRECORD_FILTER_PARAMS.get("topic")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_CNA_CLINICAL_RECORDS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/hhaClinicalRecords with filters by STI date')
def request_GET_hhaClinicalRecords_by_date(context):
    parameter = f'?date={GMS_STI_HHA_CLINICALRECORD_FILTER_PARAMS.get("date")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_HHA_CLINICAL_RECORDS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/hhaClinicalRecords with filters by STI completed')
def request_GET_hhaClinicalRecords_by_completed(context):
    parameter = f'?completed={GMS_STI_HHA_CLINICALRECORD_FILTER_PARAMS.get("completed")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_HHA_CLINICAL_RECORDS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/hhaClinicalRecords with filters by STI topic')
def request_GET_hhaClinicalRecords_by_topic(context):
    parameter = f'?topic={GMS_STI_HHA_CLINICALRECORD_FILTER_PARAMS.get("topic")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_HHA_CLINICAL_RECORDS_API_URL}{parameter}', headers=headers)


@when('request GET to second instructor /api/gms/cnaClinicalRecords with filters by STI date')
def request_GET_second_cnaClinicalRecords_by_date(context):
    parameter = f'?date={GMS_STI_CNA_CLINICALRECORD2_FILTER_PARAMS.get("date")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_CNA_CLINICAL_RECORDS_API_URL}{parameter}', headers=headers)


@when('request GET to second instructor /api/gms/cnaClinicalRecords with filters by STI completed')
def request_GET_second_cnaClinicalRecords_by_completed(context):
    parameter = f'?completed={GMS_STI_CNA_CLINICALRECORD2_FILTER_PARAMS.get("completed")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_CNA_CLINICAL_RECORDS_API_URL}{parameter}', headers=headers)


@when('request GET to second instructor /api/gms/cnaClinicalRecords with filters by STI topic')
def request_GET_second_cnaClinicalRecords_by_topic(context):
    parameter = f'?topic={GMS_STI_CNA_CLINICALRECORD2_FILTER_PARAMS.get("topic")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_CNA_CLINICAL_RECORDS_API_URL}{parameter}', headers=headers)


@when('request GET to second instructor /api/gms/hhaClinicalRecords with filters by STI date')
def request_GET_second_hhaClinicalRecords_by_date(context):
    parameter = f'?date={GMS_STI_HHA_CLINICALRECORD2_FILTER_PARAMS.get("date")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_HHA_CLINICAL_RECORDS_API_URL}{parameter}', headers=headers)


@when('request GET to second instructor /api/gms/hhaClinicalRecords with filters by STI completed')
def request_GET_second_hhaClinicalRecords_by_completed(context):
    parameter = f'?completed={GMS_STI_HHA_CLINICALRECORD2_FILTER_PARAMS.get("completed")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.test_data = GMS_STI_HHA_CLINICALRECORD2_FILTER_PARAMS
    context.test_param = ['date', 'topic']

    context.response = context.test.client.get(
        f'{GMS_HHA_CLINICAL_RECORDS_API_URL}{parameter}', headers=headers)


@when('request GET to second instructor /api/gms/hhaClinicalRecords with filters by STI topic')
def request_GET_second_hhaClinicalRecords_by_topic(context):
    parameter = f'?topic={GMS_STI_HHA_CLINICALRECORD2_FILTER_PARAMS.get("topic")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_HHA_CLINICAL_RECORDS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/cnaClinicalRecords with filters by ST2 date')
def request_GET_cnaClinicalRecords_by_date_ST2(context):
    parameter = f'?date={GMS_ST2_CNA_CLINICALRECORD_FILTER_PARAMS.get("date")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_CNA_CLINICAL_RECORDS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/cnaClinicalRecords with filters by ST2 completed')
def request_GET_cnaClinicalRecords_by_completed_ST2(context):
    parameter = f'?completed={GMS_ST2_CNA_CLINICALRECORD_FILTER_PARAMS.get("completed")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_CNA_CLINICAL_RECORDS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/cnaClinicalRecords with filters by ST2 topic')
def request_GET_cnaClinicalRecords_by_topic_ST2(context):
    parameter = f'?topic={GMS_ST2_CNA_CLINICALRECORD_FILTER_PARAMS.get("topic")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_CNA_CLINICAL_RECORDS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/hhaClinicalRecords with filters by ST2 date')
def request_GET_hhaClinicalRecords_by_date_ST2(context):
    parameter = f'?date={GMS_ST2_HHA_CLINICALRECORD_FILTER_PARAMS.get("date")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_HHA_CLINICAL_RECORDS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/hhaClinicalRecords with filters by ST2 completed')
def request_GET_hhaClinicalRecords_by_completed_ST2(context):
    parameter = f'?completed={GMS_ST2_HHA_CLINICALRECORD_FILTER_PARAMS.get("completed")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_HHA_CLINICAL_RECORDS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/gms/hhaClinicalRecords with filters by ST2 topic')
def request_GET_hhaClinicalRecords_by_topic_ST2(context):
    parameter = f'?topic={GMS_ST2_HHA_CLINICALRECORD_FILTER_PARAMS.get("topic")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{GMS_HHA_CLINICAL_RECORDS_API_URL}{parameter}', headers=headers)


@when('request POST to /api/gms/cnaRotations with bad email')
def request_POST_cnaRotation_bad_email(context):
    post_data = GMS_CNAROTATION_POST_BAD_EMAIL
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{GMS_CNA_ROTATIONS_API_URL}', post_data, format='json', headers=headers)


@when('request POST to /api/gms/hhaRotations with bad email')
def request_POST_hhaRotation_bad_email(context):
    post_data = GMS_HHAROTATION_POST_BAD_EMAIL
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{GMS_HHA_ROTATIONS_API_URL}', post_data, format='json', headers=headers)


@when('request PUT to /api/gms/cnaRotations with bad email')
def request_PUT_cnaRotation_bad_email(context):
    put_data = GMS_CNAROTATION_PUT_BAD_EMAIL
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.put(
        f'{GMS_CNA_ROTATIONS_API_URL}{GMS_CNA_ROTATION_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PUT to /api/gms/hhaRotations with bad email')
def request_PUT_cnaRotation_bad_email(context):
    put_data = GMS_HHAROTATION_PUT_BAD_EMAIL
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.put(
        f'{GMS_HHA_ROTATIONS_API_URL}{GMS_HHA_ROTATION_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PATCH to /api/gms/cnaRotations with bad email')
def request_PATCH_cnaRotation_bad_email(context):
    patch_data = GMS_CNAROTATION_PATCH_BAD_EMAIL

    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.patch(
        f'{GMS_CNA_ROTATIONS_API_URL}{GMS_CNA_ROTATION_UUID_TO_TEST}/', patch_data, format='json', headers=headers)


@when('request PATCH to /api/gms/hhaRotations with bad email')
def request_PATCH_hhaRotation_bad_email(context):
    patch_data = GMS_HHAROTATION_PATCH_BAD_EMAIL

    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.patch(
        f'{GMS_HHA_ROTATIONS_API_URL}{GMS_HHA_ROTATION_UUID_TO_TEST}/', patch_data, format='json', headers=headers)

# whens for cms component testing


@when('request GET to /api/cms/clients/client_uuid')
def request_GET_clients(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{CMS_CLIENTS_API_URL}', headers=headers)


@when('request GET to /api/cms/notes/note_uuid')
def request_GET_notes(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{CMS_NOTES_API_URL}', headers=headers)


@when('request GET to second /api/cms/clients/client_uuid')
def request_GET_second_client(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{CMS_CLIENTS_API_URL}{CMS_SECOND_CLIENT_UUID}/', headers=headers)


@when('request GET to second /api/cms/notes/note_uuid')
def request_GET_second_note(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{CMS_NOTES_API_URL}{CMS_SECOND_NOTE_UUID}/', headers=headers)


@when('request GET to ST2 /api/cms/clients/client_uuid')
def request_GET_ST2_client(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{CMS_CLIENTS_API_URL}{CMS_ST2_CLIENT_UUID}/', headers=headers)


@when('request GET to ST2 /api/cms/notes/note_uuid')
def request_GET_ST2_client(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{CMS_NOTES_API_URL}{CMS_ST2_NOTE_UUID}/', headers=headers)


@when('request POST to /api/cms/clients')
def request_POST_to_client(context):
    post_data = CMS_STI_CLIENT_SAMPLE_POST
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{CMS_CLIENTS_API_URL}', post_data, format='json', headers=headers)


@when('request POST to /api/cms/notes')
def request_POST_to_note(context):
    post_data = CMS_STI_NOTE_SAMPLE_POST
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{CMS_NOTES_API_URL}', post_data, format='json', headers=headers)


@when('request POST to ST2 /api/cms/clients')
def request_POST_ST2_client(context):
    post_data = CMS_ST2_CLIENT_SAMPLE_POST
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{CMS_CLIENTS_API_URL}', post_data, format='json', headers=headers)


@when('request POST to ST2 /api/cms/notes')
def request_POST_ST2_note(context):
    post_data = CMS_ST2_NOTE_SAMPLE_POST
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{CMS_NOTES_API_URL}', post_data, format='json', headers=headers)


@when('request POST to /api/cms/clients with email to a non-existant user')
def request_POST_bad_email_client(context):
    post_data = CMS_STI_CLIENT_SAMPLE_POST
    post_data.get('recruit_emails')[0] = 'random@email.com'

    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.post(
        f'{CMS_CLIENTS_API_URL}', post_data, format='json', headers=headers)


@when('request PUT to /api/cms/clients/client_uuid')
def request_PUT_client(context):
    put_data = CMS_STI_CLIENT_SAMPLE_PUT
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.put(
        f'{CMS_CLIENTS_API_URL}{CMS_CLIENT_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PUT to /api/cms/notes/note_uuid')
def request_PUT_note(context):
    put_data = CMS_STI_NOTE_SAMPLE_PUT
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.put(
        f'{CMS_NOTES_API_URL}{CMS_NOTE_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PUT to second /api/cms/clients/client_uuid')
def request_PUT_to_second_client(context):
    put_data = CMS_SECOND_CLIENT_PUT
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.put(
        f'{CMS_CLIENTS_API_URL}{CMS_SECOND_CLIENT_UUID}/', put_data, format='json', headers=headers)


@when('request PUT to second /api/cms/notes/note_uuid')
def request_PUT_to_second_note(context):
    put_data = CMS_SECOND_NOTE_PUT
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.put(
        f'{CMS_NOTES_API_URL}{CMS_SECOND_NOTE_UUID}/', put_data, format='json', headers=headers)


@when('request PUT to ST2 /api/cms/clients')
def request_PUT_to_ST2_client(context):
    put_data = CMS_ST2_CLIENT_SAMPLE_PUT
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.put(
        f'{CMS_CLIENTS_API_URL}{CMS_ST2_CLIENT_UUID}/', put_data, format='json', headers=headers)


@when('request PUT to ST2 /api/cms/notes')
def request_PUT_to_ST2_note(context):
    put_data = CMS_ST2_NOTE_SAMPLE_PUT
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.put(
        f'{CMS_NOTES_API_URL}{CMS_ST2_NOTE_UUID}/', put_data, format='json', headers=headers)


@when('request PUT to /api/cms/clients with email to a non-existant user')
def request_PUT_bad_email_client(context):
    put_data = CMS_STI_CLIENT_SAMPLE_PUT
    put_data.get('recruit_emails')[0] = 'random@email.com'

    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.put(
        f'{CMS_CLIENTS_API_URL}{CMS_CLIENT_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PATCH to /api/cms/clients/client_uuid')
def request_PATCH_client(context):
    patch_data = CMS_STI_CLIENT_PATCH

    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.patch(
        f'{CMS_CLIENTS_API_URL}{CMS_CLIENT_UUID_TO_TEST}/', patch_data, format='json', headers=headers)


@when('request PATCH to /api/cms/notes/note_uuid')
def request_PATCH_note(context):
    patch_data = CMS_STI_NOTE_PATCH

    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.patch(
        f'{CMS_NOTES_API_URL}{CMS_NOTE_UUID_TO_TEST}/', patch_data, format='json', headers=headers)


@when('request PATCH to second /api/cms/clients/client_uuid')
def request_PATCH_to_second_client(context):
    patch_data = CMS_SECOND_CLIENT_PATCH

    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.patch(
        f'{CMS_CLIENTS_API_URL}{CMS_SECOND_CLIENT_UUID}/', patch_data, format='json', headers=headers)


@when('request PATCH to second /api/cms/notes/note_uuid')
def request_PATCH_to_second_note(context):
    patch_data = CMS_SECOND_NOTE_PATCH

    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.patch(
        f'{CMS_NOTES_API_URL}{CMS_SECOND_NOTE_UUID}/', patch_data, format='json', headers=headers)


@when('request PATCH to ST2 /api/cms/clients')
def request_PATCH_ST2_client(context):
    patch_data = CMS_ST2_CLIENT_PATCH

    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.patch(
        f'{CMS_CLIENTS_API_URL}{CMS_ST2_CLIENT_UUID}/', patch_data, format='json', headers=headers)


@when('request PATCH to ST2 /api/cms/notes')
def request_PATCH_ST2_note(context):
    patch_data = CMS_ST2_NOTE_PATCH

    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.patch(
        f'{CMS_NOTES_API_URL}{CMS_ST2_NOTE_UUID}/', patch_data, format='json', headers=headers)


@when('request PATCH to /api/cms/clients with email to a non-existant user')
def request_PATCH_with_bad_email_client(context):
    patch_data = CMS_STI_CLIENT_PATCH
    patch_data['recruit_emails'] = ['random@email.com']

    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.patch(
        f'{CMS_CLIENTS_API_URL}{CMS_CLIENT_UUID_TO_TEST}/', patch_data, format='json', headers=headers)


@when('request DELETE to /api/cms/clients/client_uuid')
def request_DEL_client(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.uuid = CMS_CLIENT_UUID_TO_TEST
    context.response = context.test.client.delete(
        f'{CMS_CLIENTS_API_URL}{CMS_CLIENT_UUID_TO_TEST}/', headers=headers)


@when('request DELETE to /api/cms/notes/note_uuid')
def request_DEL_note(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.uuid = CMS_NOTE_UUID_TO_TEST
    context.response = context.test.client.delete(
        f'{CMS_NOTES_API_URL}{CMS_NOTE_UUID_TO_TEST}/', headers=headers)


@when('request DELETE to second /api/cms/clients/client_uuid')
def request_DEL_second_client(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.uuid = CMS_SECOND_CLIENT_UUID
    context.response = context.test.client.delete(
        f'{CMS_CLIENTS_API_URL}{CMS_SECOND_CLIENT_UUID}/', headers=headers)


@when('request DELETE to second /api/cms/notes/note_uuid')
def request_DEL_second_note(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.uuid = CMS_SECOND_NOTE_UUID
    context.response = context.test.client.delete(
        f'{CMS_NOTES_API_URL}{CMS_SECOND_NOTE_UUID}/', headers=headers)


@when('request DELETE to ST2 /api/cms/clients')
def request_DEL_ST2_client(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.uuid = CMS_ST2_CLIENT_UUID
    context.response = context.test.client.delete(
        f'{CMS_CLIENTS_API_URL}{CMS_ST2_CLIENT_UUID}/', headers=headers)


@when('request DELETE to ST2 /api/cms/notes')
def request_DEL_ST2_note(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.uuid = CMS_ST2_NOTE_UUID
    context.response = context.test.client.delete(
        f'{CMS_NOTES_API_URL}{CMS_ST2_NOTE_UUID}/', headers=headers)


@when('request GET to /api/cms/clients with filters by first_name')
def request_client_filter_by_first_name(context):
    parameter = f'?first_name={CMS_CLIENT_FILTER_PARAMS.get("first_name")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{CMS_CLIENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/cms/clients with filters by last_name')
def request_client_filter_by_last_name(context):
    parameter = f'?last_name={CMS_CLIENT_FILTER_PARAMS.get("last_name")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{CMS_CLIENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/cms/clients with filters by phone_number')
def request_client_filter_by_phone_number(context):
    parameter = f'?phone_number={CMS_CLIENT_FILTER_PARAMS.get("phone_number")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{CMS_CLIENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/cms/clients with filters by email')
def request_client_filter_by_email(context):
    parameter = f'?email={CMS_CLIENT_FILTER_PARAMS.get("email")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{CMS_CLIENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/cms/clients with filters by city')
def request_client_filter_by_city(context):
    parameter = f'?city={CMS_CLIENT_FILTER_PARAMS.get("city")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{CMS_CLIENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/cms/clients with filters by success')
def request_client_filter_by_success(context):
    parameter = f'?success={CMS_CLIENT_FILTER_PARAMS.get("success")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{CMS_CLIENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/cms/clients with filters by initial_contact')
def request_client_filter_by_initial_contact_date(context):
    parameter = f'?initial_contact={CMS_CLIENT_FILTER_PARAMS.get("initial_contact")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{CMS_CLIENTS_API_URL}{parameter}', headers=headers)


@when('request GET to /api/cms/notes with filters by date')
def request_note_filter_by_date(context):
    parameter = f'?date={CMS_NOTE_FILTER_PARAMS.get("date")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{CMS_NOTES_API_URL}{parameter}', headers=headers)


@when('request GET to /api/cms/notes with filters by content')
def request_note_filter_by_content(context):
    parameter = f'?content={CMS_NOTE_FILTER_PARAMS.get("content")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{CMS_NOTES_API_URL}{parameter}', headers=headers)


@when('request GET to second /api/cms/clients with filters by first_name')
def request_client_filter_by_first_name(context):
    parameter = f'?first_name={CMS_SECOND_CLIENT_FILTER_PARAMS.get("first_name")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{CMS_CLIENTS_API_URL}{parameter}', headers=headers)


@when('request GET to second /api/cms/clients with filters by last_name')
def request_client_filter_by_last_name(context):
    parameter = f'?last_name={CMS_SECOND_CLIENT_FILTER_PARAMS.get("last_name")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{CMS_CLIENTS_API_URL}{parameter}', headers=headers)


@when('request GET to second /api/cms/clients with filters by phone_number')
def request_client_filter_by_phone_number(context):
    parameter = f'?phone_number={CMS_SECOND_CLIENT_FILTER_PARAMS.get("phone_number")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{CMS_CLIENTS_API_URL}{parameter}', headers=headers)


@when('request GET to second /api/cms/clients with filters by email')
def request_client_filter_by_email(context):
    parameter = f'?email={CMS_SECOND_CLIENT_FILTER_PARAMS.get("email")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{CMS_CLIENTS_API_URL}{parameter}', headers=headers)


@when('request GET to second /api/cms/clients with filters by city')
def request_client_filter_by_city(context):
    parameter = f'?city={CMS_SECOND_CLIENT_FILTER_PARAMS.get("city")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{CMS_CLIENTS_API_URL}{parameter}', headers=headers)


@when('request GET to second /api/cms/clients with filters by success')
def request_client_filter_by_success(context):
    parameter = f'?success={CMS_SECOND_CLIENT_FILTER_PARAMS.get("success")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{CMS_CLIENTS_API_URL}{parameter}', headers=headers)


@when('request GET to second /api/cms/clients with filters by initial_contact')
def request_client_filter_by_initial_contact_date(context):
    parameter = f'?initial_contact={CMS_SECOND_CLIENT_FILTER_PARAMS.get("initial_contact")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{CMS_CLIENTS_API_URL}{parameter}', headers=headers)


@when('request GET to second /api/cms/notes with filters by date')
def request_note_filter_by_date(context):
    parameter = f'?date={CMS_SECOND_NOTE_FILTER_PARAMS.get("date")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{CMS_NOTES_API_URL}{parameter}', headers=headers)


@when('request GET to second /api/cms/notes with filters by content')
def request_note_filter_by_content(context):
    parameter = f'?content={CMS_SECOND_NOTE_FILTER_PARAMS.get("content")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{CMS_NOTES_API_URL}{parameter}', headers=headers)


@when('request GET to ST2 /api/cms/clients with filters by first_name')
def request_client_filter_by_first_name(context):
    parameter = f'?first_name={CMS_ST2_CLIENT_FILTER_PARAMS.get("first_name")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{CMS_CLIENTS_API_URL}{parameter}', headers=headers)


@when('request GET to ST2 /api/cms/clients with filters by last_name')
def request_client_filter_by_last_name(context):
    parameter = f'?last_name={CMS_ST2_CLIENT_FILTER_PARAMS.get("last_name")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{CMS_CLIENTS_API_URL}{parameter}', headers=headers)


@when('request GET to ST2 /api/cms/clients with filters by phone_number')
def request_client_filter_by_phone_number(context):
    parameter = f'?phone_number={CMS_ST2_CLIENT_FILTER_PARAMS.get("phone_number")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{CMS_CLIENTS_API_URL}{parameter}', headers=headers)


@when('request GET to ST2 /api/cms/clients with filters by email')
def request_client_filter_by_email(context):
    parameter = f'?email={CMS_ST2_CLIENT_FILTER_PARAMS.get("email")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{CMS_CLIENTS_API_URL}{parameter}', headers=headers)


@when('request GET to ST2 /api/cms/clients with filters by city')
def request_client_filter_by_city(context):
    parameter = f'?city={CMS_ST2_CLIENT_FILTER_PARAMS.get("city")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{CMS_CLIENTS_API_URL}{parameter}', headers=headers)


@when('request GET to ST2 /api/cms/clients with filters by success')
def request_client_filter_by_success(context):
    parameter = f'?success={CMS_ST2_CLIENT_FILTER_PARAMS.get("success")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.test_data = CMS_ST2_CLIENT_FILTER_PARAMS
    context.test_param = ['first_name', 'last_name',
                          'phone_number', 'email', 'city', 'initial_contact']

    context.response = context.test.client.get(
        f'{CMS_CLIENTS_API_URL}{parameter}', headers=headers)


@when('request GET to ST2 /api/cms/clients with filters by initial_contact')
def request_client_filter_by_initial_contact_date(context):
    parameter = f'?initial_contact={CMS_ST2_CLIENT_FILTER_PARAMS.get("initial_contact")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{CMS_CLIENTS_API_URL}{parameter}', headers=headers)


@when('request GET to ST2 /api/cms/notes with filters by date')
def request_note_filter_by_date(context):
    parameter = f'?date={CMS_ST2_NOTE_FILTER_PARAMS.get("date")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{CMS_NOTES_API_URL}{parameter}', headers=headers)


@when('request GET to ST2 /api/cms/notes with filters by content')
def request_note_filter_by_content(context):
    parameter = f'?content={CMS_ST2_NOTE_FILTER_PARAMS.get("content")}'
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.get(
        f'{CMS_NOTES_API_URL}{parameter}', headers=headers)
