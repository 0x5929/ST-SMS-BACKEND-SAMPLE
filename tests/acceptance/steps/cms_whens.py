from behave import given

from .constants import (GMS_CNA_ROTATIONS_API_URL,
                        GMS_HHA_ROTATIONS_API_URL,
                        GMS_CNA_STUDENTS_API_URL,
                        GMS_HHA_STUDENTS_API_URL,
                        GMS_CNA_THEORY_RECORDS_API_URL,
                        GMS_HHA_THEORY_RECORDS_API_URL,
                        GMS_CNA_CLINICAL_RECORDS_API_URL,
                        GMS_HHA_CLINICAL_RECORDS_API_URL)


@given('request GET to /api/gms/cnaRotations')
def request_GET_to_cnaRotations(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{GMS_CNA_ROTATIONS_API_URL}', headers=headers)


@given('request GET to /api/gms/cnaStudents')
def request_GET_cnaStudents(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{GMS_CNA_STUDENTS_API_URL}', headers=headers)


@given('request GET to /api/gms/cnaTheoryRecords')
def request_GET_cnaTheoryRecords(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{GMS_CNA_THEORY_RECORDS_API_URL}', headers=headers)


@given('request GET to /api/gms/cnaClinicalRecord')
def request_GET_cnaClinicalRecords(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{GMS_CNA_CLINICAL_RECORDS_API_URL}', headers=headers)


@given('request GET to /api/gms/hhaRotations')
def request_GET_hhaRotations(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{GMS_HHA_ROTATIONS_API_URL}', headers=headers)


@given('request GET to /api/gms/hhaStudents')
def request_GET_hhaStudents(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{GMS_HHA_STUDENTS_API_URL}', headers=headers)


@given('request GET to /api/gms/hhaTheoryRecords')
def request_GET_hhaTheoryRecords(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{GMS_HHA_THEORY_RECORDS_API_URL}', headers=headers)


@given('request GET to /api/gms/hhaClinicalRecords')
def requets_GET_hhaClinicalRecords(context):
    headers = {'csrftoken': context.csrf_token,
               'sms-auth': context.access_token}
    context.response = context.test.client.get(
        f'{GMS_HHA_CLINICAL_RECORDS_API_URL}', headers=headers)
