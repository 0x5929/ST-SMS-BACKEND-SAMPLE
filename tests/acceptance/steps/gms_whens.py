from behave import when

from constants import (GMS_CNA_ROTATIONS_API_URL,
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
                        GMS_HHA_CLINICAL_RECORD_PATCH_SAMPLE_DATA)


@when('request GET to /api/gms/cnaRotations')
def request_GET_to_cnaRotations(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{GMS_CNA_ROTATIONS_API_URL}', headers=headers)


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


@when('request GET to /api/gms/cnaClinicalRecord')
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


@when('request POST to /api/gms/cnaStudents')
def request_POST_cnaStudents(context):
    post_data = GMS_CNA_STUDENT_POST_SAMPLE_DATA
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


@when('request POST to /api/gms/cnaClinicalRecords')
def request_POST_cnaClinicalRecords(context):
    post_data = GMS_CNA_CLINICAL_RECORD_POST_SAMPLE_DATA
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


@when('request POST to /api/gms/hhaStudents')
def request_POST_hhaStudents(context):
    post_data = GMS_HHA_STUDENT_POST_SAMPLE_DATA
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


@when('request POST to /api/gms/hhaClinicalRecords')
def request_POST_hhaClinicalRecords(context):
    post_data = GMS_HHA_CLINICAL_RECORD_POST_SAMPLE_DATA
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


@when('request PUT to /api/gms/cnaStudents')
def request_PUT_cnaStudents(context):
    put_data = GMS_CNA_STUDENT_PUT_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.put(
        f'{GMS_CNA_STUDENTS_API_URL}{GMS_CNA_STUDENT_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PUT to /api/gms/cnaTheoryRecords')
def request_PUT_cnaTheoryRecords(context):
    put_data = GMS_CNA_THEORY_RECORD_PUT_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.put(
        f'{GMS_CNA_THEORY_RECORDS_API_URL}{GMS_CNA_THEORY_RECORD_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PUT to /api/gms/cnaClinicalRecords')
def request_PUT_cnaClinicalRecords(context):
    put_data = GMS_CNA_CLINICAL_RECORD_PUT_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.put(
        f'{GMS_CNA_CLINICAL_RECORDS_API_URL}{GMS_CNA_CLINICAL_RECORD_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PUT to /api/gms/hhaRotations')
def request_PUT_hhaRotations(context):
    put_data = GMS_HHA_ROTATION_PUT_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.put(
        f'{GMS_HHA_ROTATIONS_API_URL}{GMS_HHA_ROTATION_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PUT to /api/gms/hhaStudents')
def request_PUT_hhaStudents(context):
    put_data = GMS_HHA_STUDENT_PUT_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.put(
        f'{GMS_HHA_STUDENTS_API_URL}{GMS_HHA_STUDENT_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PUT to /api/gms/hhaTheoryRecords')
def request_PUT_hhaTheoryRecords(context):
    put_data = GMS_HHA_THEORY_RECORD_PUT_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.put(
        f'{GMS_HHA_THEORY_RECORDS_API_URL}{GMS_HHA_THEORY_RECORD_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PUT to /api/gms/hhaClinicalRecords')
def request_PUT_hhaClinicalRecords(context):
    put_data = GMS_HHA_CLINICAL_RECORD_PUT_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.put(
        f'{GMS_HHA_CLINICAL_RECORDS_API_URL}{GMS_HHA_CLINICAL_RECORD_UUID_TO_TEST}/', put_data, format='json', headers=headers)


@when('request PATCH to /api/gms/cnaRotations')
def request_PATCH_cnaRotations(context):
    patch_data = GMS_CNA_ROTATION_PATCH_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.patch(
        f'{GMS_CNA_ROTATIONS_API_URL}{GMS_CNA_ROTATION_UUID_TO_TEST}/', patch_data, format='json', headers=headers)


@when('request PATCH to /api/gms/cnaStudents')
def request_PATCH_cnaStudents(context):
    patch_data = GMS_CNA_STUDENT_PATCH_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.patch(
        f'{GMS_CNA_STUDENTS_API_URL}{GMS_CNA_STUDENT_UUID_TO_TEST}/', patch_data, format='json', headers=headers)


@when('request PATCH to /api/gms/cnaTheoryRecords')
def request_PATCH_cnaTheoryRecords(context):
    patch_data = GMS_CNA_THEORY_RECORD_PATCH_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.patch(
        f'{GMS_CNA_THEORY_RECORDS_API_URL}{GMS_CNA_THEORY_RECORD_UUID_TO_TEST}/', patch_data, format='json', headers=headers)


@when('request PATCH to /api/gms/cnaClinicalRecords')
def request_PATCH_cnaClinicalRecords(context):
    patch_data = GMS_CNA_CLINICAL_RECORD_PATCH_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.patch(
        f'{GMS_CNA_CLINICAL_RECORDS_API_URL}{GMS_CNA_CLINICAL_RECORD_UUID_TO_TEST}/', patch_data, format='json', headers=headers)


@when('request PATCH to /api/gms/hhaRotations')
def request_PATCH_hhaRotations(context):
    patch_data = GMS_HHA_ROTATION_PATCH_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.patch(
        f'{GMS_HHA_ROTATIONS_API_URL}{GMS_HHA_ROTATION_UUID_TO_TEST}/', patch_data, format='json', headers=headers)


@when('request PATCH to /api/gms/hhaStudents')
def request_PATCH_hhaStudents(context):
    patch_data = GMS_HHA_STUDENT_PATCH_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.patch(
        f'{GMS_HHA_STUDENTS_API_URL}{GMS_HHA_STUDENT_UUID_TO_TEST}/', patch_data, format='json', headers=headers)


@when('request PATCH to /api/gms/hhaTheoryRecords')
def request_PATCH_hhaTheoryRecords(context):
    patch_data = GMS_HHA_THEORY_RECORD_PATCH_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.patch(
        f'{GMS_HHA_THEORY_RECORDS_API_URL}{GMS_HHA_THEORY_RECORD_UUID_TO_TEST}/', patch_data, format='json', headers=headers)


@when('request PATCH to /api/gms/hhaClinicalRecords')
def request_PATCH_hhaClinicalRecords(context):
    patch_data = GMS_HHA_CLINICAL_RECORD_PATCH_SAMPLE_DATA
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.response = context.test.client.patch(
        f'{GMS_HHA_CLINICAL_RECORDS_API_URL}{GMS_HHA_CLINICAL_RECORD_UUID_TO_TEST}/', patch_data, format='json', headers=headers)


@when('request DELETE to /api/gms/cnaRotations')
def request_DELETE_cnaRotations(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.uuid = GMS_CNA_ROTATION_UUID_TO_TEST
    context.response = context.test.client.delete(
        f'{GMS_CNA_ROTATIONS_API_URL}{GMS_CNA_ROTATION_UUID_TO_TEST}/', headers=headers)


@when('request DELETE to /api/gms/cnaStudents')
def request_DELETE_cnaStudents(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.uuid = GMS_CNA_STUDENT_UUID_TO_TEST
    context.response = context.test.client.delete(
        f'{GMS_CNA_STUDENTS_API_URL}{GMS_CNA_STUDENT_UUID_TO_TEST}/', headers=headers)


@when('request DELETE to /api/gms/cnaTheoryRecords')
def request_DELETE_cnaTheoryRecords(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.uuid = GMS_CNA_THEORY_RECORD_UUID_TO_TEST
    context.response = context.test.client.delete(
        f'{GMS_CNA_THEORY_RECORDS_API_URL}{GMS_CNA_THEORY_RECORD_UUID_TO_TEST}/', headers=headers)


@when('request DELETE to /api/gms/cnaClinicalRecords')
def request_DELETE_cnaClinicalRecords(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.uuid = GMS_CNA_CLINICAL_RECORD_UUID_TO_TEST
    context.response = context.test.client.delete(
        f'{GMS_CNA_CLINICAL_RECORDS_API_URL}{GMS_CNA_CLINICAL_RECORD_UUID_TO_TEST}/', headers=headers)


@when('request DELETE to /api/gms/hhaRotations')
def request_DELETE_hhaRotations(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.uuid = GMS_HHA_ROTATION_UUID_TO_TEST
    context.response = context.test.client.delete(
        f'{GMS_HHA_ROTATIONS_API_URL}{GMS_HHA_ROTATION_UUID_TO_TEST}/', headers=headers)


@when('request DELETE to /api/gms/hhaStudents')
def request_DELETE_hhaStudents(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.uuid = GMS_HHA_STUDENT_UUID_TO_TEST
    context.response = context.test.client.delete(
        f'{GMS_HHA_STUDENTS_API_URL}{GMS_HHA_STUDENT_UUID_TO_TEST}/', headers=headers)


@when('request DELETE to /api/gms/hhaTheoryRecords')
def request_DELETE_hhaTheoryRecords(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.uuid = GMS_HHA_THEORY_RECORD_UUID_TO_TEST
    context.response = context.test.client.delete(
        f'{GMS_HHA_THEORY_RECORDS_API_URL}{GMS_HHA_THEORY_RECORD_UUID_TO_TEST}/', headers=headers)


@when('request DELETE to /api/gms/hhaClinicalRecords')
def request_DELETE_hhaClinicalRecords(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}

    context.uuid = GMS_HHA_CLINICAL_RECORD_UUID_TO_TEST
    context.response = context.test.client.delete(
        f'{GMS_HHA_CLINICAL_RECORDS_API_URL}{GMS_HHA_CLINICAL_RECORD_UUID_TO_TEST}/', headers=headers)
