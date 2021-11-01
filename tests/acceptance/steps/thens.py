from typing import Container
from behave import then
import json

from tests.acceptance.steps.constants import (STUDENT_SAMPLE_SAME_SCHOOL_POST_DATA,
                                              STUDENT_SAMPLE_DIFF_SCHOOL_POST_DATA,
                                              SCHOOL_SAMPLE_POST_DATA,
                                              PROGRAM_SAMPLE_POST_DATA,
                                              ROTATION_SAMPLE_POST_DATA,
                                              JSON_PERMISSION_DENIED_RES,
                                              JSON_OBJ_NOT_FOUND_RES,
                                              FILTER_PARAMS,
                                              PUT_DATA,
                                              PATCH_DATA)


@then('will receive JSON response of data')
def receive_JSON_data(context):
    response = context.response.data

    no_json_res = []

    # asserting that JSON response is not [] empty
    # print('24: ', json.dumps(context.response.__dict__, indent=2, default=str))
    context.test().assertJSONNotEqual(
        json.dumps(str(response)), json.dumps(no_json_res))


@then('database will create the student record')
def database_create_student(context):
    response = context.response.data
    posted_student_first_name = STUDENT_SAMPLE_SAME_SCHOOL_POST_DATA.get(
        'first_name')

    # assert
    context.test().assertEqual(response.get('first_name'), posted_student_first_name)


# when posting to /api/sms/students/ with a rotation of a program that belongs to another school location
@ then('database will not create the student record')
def database_will_not_create_student(context):
    response = context.response.data

    posted_student_id = STUDENT_SAMPLE_DIFF_SCHOOL_POST_DATA.get('student_id')

    context.test().assertNotEqual(response.get('student_id'), posted_student_id)


@ then('database will edit the student record')
def database_will_edit_student(context):
    response = context.response.data

    editted_last_name = PUT_DATA.get('student__last_name')

    context.test().assertEqual(response.get('last_name'), editted_last_name)


@ then('database will partially edit the student record')
def database_will_partially_edit_student(context):
    response = context.response.data

    editted_last_name = PATCH_DATA.get('student__last_name')

    context.test().assertEqual(response.get('last_name'), editted_last_name)


@ then('database will not delete the student record')
def database_will_not_delete_student(context):
    response = context.response.data

    context.test().assertEqual(response, JSON_PERMISSION_DENIED_RES)


@ then('database will delete the student record')
def database_will_delete_student(context):
    context.test().assertEqual(context.response.data, None)


@ then('database will create the school record')
def database_will_create_school(context):
    response = context.response.data

    posted_school_code = SCHOOL_SAMPLE_POST_DATA.get('school_code')

    context.test().assertEqual(response.get('school_code'), posted_school_code)


@ then('database will edit the school record')
def database_will_edit_school(context):
    response = context.response.data

    editted_school_code = PUT_DATA.get('school__school_code')

    context.test().assertEqual(response.get('school_code'), editted_school_code)


@ then('database will partially edit the school record')
def database_will_partially_edit_school(context):
    response = context.response.data

    editted_school_code = PATCH_DATA.get('school__school_code')

    context.test().assertEqual(response.get('school_code'), editted_school_code)


@ then('database will delete the school record')
def database_will_delete_school(context):
    context.test().assertEqual(context.response.data, JSON_OBJ_NOT_FOUND_RES)


@ then('database will not create the school record')
def database_will_not_create_school(context):
    response = context.response.data

    context.test().assertEqual(response, JSON_PERMISSION_DENIED_RES)


@ then('database will not edit the school record')
def database_will_not_edit_school(context):
    response = context.response.data

    context.test().assertEqual(response, JSON_PERMISSION_DENIED_RES)


@ then('database will not delete the school record')
def database_will_not_delete_school(context):
    response = context.response.data

    context.test().assertEqual(response, JSON_PERMISSION_DENIED_RES)


@ then('database will create the program record')
def database_will_create_program(context):
    response = context.response.data

    posted_program_name = PROGRAM_SAMPLE_POST_DATA.get('program_name')

    context.test().assertEqual(response.get('program_name'), posted_program_name)


@ then('database will edit the program record')
def database_will_edit_program(context):
    response = context.response.data

    editted_program_name = PUT_DATA.get('program__program_name')

    context.test().assertEqual(response.get('program_name'), editted_program_name)


@ then('database will partially edit the program record')
def database_will_partially_edit_program(context):
    response = context.response.data

    editted_program_name = PATCH_DATA.get('program__program_name')

    context.test().assertEqual(response.get(
        'program_name'), editted_program_name)


@ then('database will delete the program record')
def database_will_delete_program(context):
    context.test().assertEqual(context.response.data, JSON_OBJ_NOT_FOUND_RES)


@ then('database will not create the program record')
def database_will_not_create_program(context):
    response = context.response.data

    context.test().assertEqual(response, JSON_PERMISSION_DENIED_RES)


@ then('database will not edit the program record')
def database_will_not_edit_program(context):
    response = context.response.data

    context.test().assertEqual(response, JSON_PERMISSION_DENIED_RES)


@ then('database will not delete the program record')
def database_will_not_delete_program(context):
    response = context.response.data

    context.test().assertEqual(response, JSON_PERMISSION_DENIED_RES)


@ then('database will create the rotation record')
def database_will_create_rotation(context):
    response = context.response.data

    posted_rotation_num = ROTATION_SAMPLE_POST_DATA.get('rotation_number')

    context.test().assertEqual(response.get(
        'rotation_number'), posted_rotation_num)


@ then('database will edit the rotation record')
def database_will_edit_rotation(context):
    response = context.response.data

    editted_rotation_num = PUT_DATA.get('rotation__rotation_number')

    context.test().assertEqual(response.get(
        'rotation_number'), editted_rotation_num)


@ then('database will partially edit the rotation record')
def database_will_partially_edit_rotation(context):
    response = context.response.data

    editted_rotation_num = PATCH_DATA.get('rotation__rotation_number')

    context.test().assertEqual(response.get(
        'rotation_number'), editted_rotation_num)

    # NOTE: rotation object only consists of rotation number and program.
    # NOTE: since our SMS validator states that rotation number cannot be changed without supplying program. (to ensure unique rot number in that specific program)


@ then('database will delete the rotation record')
def database_will_delete_rotation(context):
    context.test().assertEqual(context.response.data, JSON_OBJ_NOT_FOUND_RES)


@ then('database will not create the rotation record')
def database_will_not_create_rotation(context):
    response = context.response.data

    context.test().assertEqual(response, JSON_PERMISSION_DENIED_RES)


@ then('database will not edit the rotation record')
def database_will_not_edit_rotation(context):
    response = context.response.data

    context.test().assertEqual(response, JSON_PERMISSION_DENIED_RES)


@ then('database will not delete the rotation record')
def database_will_not_delete_rotation(context):
    response = context.response.data

    context.test().assertEqual(response, JSON_PERMISSION_DENIED_RES)


@ then('the specific students data will be returned as JSON response')
def specific_student_JSON_data_response(context):
    response = context.response.data

    filtered_student_lastname = FILTER_PARAMS.get('last_name')

#    print('244', json.dumps(context.response.data, indent=2, default=str))
    #context.test().assertEqual(len(response), 2)
    context.test().assertEqual(response[0].get('last_name'),
                               filtered_student_lastname)


@ then('No data response will be sent from server')
def no_response_from_server(context):
    response = context.response.data

    context.test().assertEqual(response, JSON_PERMISSION_DENIED_RES)


@ then('server will respond with 405')
def server_responds_405(context):
    context.test().assertEqual(context.response.status_code, 405)


@then('server response status is OK 200')
def server_response_20(context):
    context.test().assertEqual(context.response.status_code, 200)
