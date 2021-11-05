import json


from behave import then

from apps.sms.google_sheets import GoogleSheet
from core.settings.constants import STUDENT_RECORD_HEADERS
from tests.acceptance.steps.constants import (STUDENT_SAMPLE_SAME_SCHOOL_POST_DATA,
                                              STUDENT_SAMPLE_DIFF_SCHOOL_POST_DATA,
                                              SCHOOL_SAMPLE_POST_DATA,
                                              PROGRAM_SAMPLE_POST_DATA,
                                              ROTATION_SAMPLE_POST_DATA,
                                              STUDENT_SAMPLE_PUT_DATA,
                                              JSON_PERMISSION_DENIED_RES,
                                              JSON_OBJ_NOT_FOUND_RES,
                                              FILTER_PARAMS,
                                              PUT_DATA,
                                              PATCH_DATA,
                                              GOOGLE_POST_DATA)


def google_sheet_del(context, student_id):
    school_name = FILTER_PARAMS.get('school_name')
    gs_api = GoogleSheet.init_google_sheet(school_name)

    del_row_num = gs_api.match(gs_api.worksheets, student_id)

    # assert we are matching the student we've created and posted onto google sheet
    gs_api.delete(gs_api.spreadsheet, del_row_num)
    gs_api.refresh(gs_api.spreadsheet)

    # after deleting, assert that match returns none
    del_row_num = gs_api.match(gs_api.worksheets, student_id)
    context.test().assertIsNone(del_row_num)


def google_sheet_create(context, student_id):
    school_name = FILTER_PARAMS.get('school_name')

    gs_api = GoogleSheet.init_google_sheet(school_name)

    gs_api.create(gs_api.worksheets, GOOGLE_POST_DATA)
    gs_api.refresh(gs_api.spreadsheet)

    # assert that we have created!
    matched_row_num = gs_api.match(gs_api.worksheets, student_id)
    context.test().assertIsNotNone(matched_row_num)


def google_sheet_check_edit(context, student_id, partial):
    pass


@then('will receive JSON response of data')
def receive_JSON_data(context):
    response = context.response.data

    no_json_res = []

    context.test().assertJSONNotEqual(
        json.dumps(str(response)), json.dumps(no_json_res))


@then('database will create the student record of another school')
def database_create_student(context):
    response = context.response.data
    posted_student_last_name = STUDENT_SAMPLE_DIFF_SCHOOL_POST_DATA.get(
        'last_name')

    # assert
    context.test().assertEqual(response.get('last_name'), posted_student_last_name)

    # we need to test google sheet migration, and delete student!

    # the student's school that we are testing with
    google_sheet_del(context, response.get('student_id'))


@then('database will create the student record')
def database_create_student(context):
    response = context.response.data
    posted_student_last_name = STUDENT_SAMPLE_SAME_SCHOOL_POST_DATA.get(
        'last_name')

    # assert
    context.test().assertEqual(response.get('last_name'), posted_student_last_name)

    # we need to test google sheet migration, and delete student!

    # the student's school that we are testing with
    google_sheet_del(context, response.get('student_id'))
    # school_name = FILTER_PARAMS.get('school_name')
    # gs_api = GoogleSheet.init_google_sheet(school_name)

    # del_row_num = gs_api.match(gs_api.worksheets, response.get('student_id'))

    # # assert we are matching the student we've created and posted onto google sheet
    # context.test().assertIsNotNone(del_row_num)

    # gs_api.delete(gs_api.spreadsheet, del_row_num)
    # gs_api.refresh(gs_api.spreadsheet)

# when posting to /api/sms/students/ with a rotation of a program that belongs to another school location


@then('database will not create the student record')
def database_will_not_create_student(context):
    response = context.response.data

    posted_student_id = STUDENT_SAMPLE_DIFF_SCHOOL_POST_DATA.get('student_id')

    context.test().assertNotEqual(response.get('student_id'), posted_student_id)


@then('database will edit the student record')
def database_will_edit_student(context):
    response = context.response.data

    editted_last_name = STUDENT_SAMPLE_PUT_DATA.get('last_name')

    context.test().assertEqual(response.get('last_name'), editted_last_name)

    # we need to test google sheet migration, and delete student!
    student_id = response.get('student_id')
    #google_sheet_del(context, student_id)
    # google_sheet_create(context, student_id)


@then('database will partially edit the student record')
def database_will_partially_edit_student(context):
    response = context.response.data

    editted_last_name = PATCH_DATA.get('student__last_name')

    context.test().assertEqual(response.get('last_name'), editted_last_name)

    # we need to test google sheet migration, and delete student!
    # student_id = response.get('student_id')
    # google_sheet_del(context, student_id)
    # google_sheet_create(context, student_id)


@then('database will not delete the student record')
def database_will_not_delete_student(context):
    response = context.response.data

    context.test().assertEqual(response, JSON_PERMISSION_DENIED_RES)


@then('database will delete the student record')
def database_will_delete_student(context):
    context.test().assertEqual(context.response.data, None)

    # same student ID that will be used for matching the student record
    student_id_index = STUDENT_RECORD_HEADERS.index('student_id')
    student_id = GOOGLE_POST_DATA[student_id_index]

    google_sheet_create(context, student_id)


@then('database will create the school record')
def database_will_create_school(context):
    response = context.response.data

    posted_school_code = SCHOOL_SAMPLE_POST_DATA.get('school_code')

    context.test().assertEqual(response.get('school_code'), posted_school_code)


@then('database will edit the school record')
def database_will_edit_school(context):
    response = context.response.data

    editted_school_code = PUT_DATA.get('school__school_code')

    context.test().assertEqual(response.get('school_code'), editted_school_code)


@then('database will partially edit the school record')
def database_will_partially_edit_school(context):
    response = context.response.data

    editted_school_code = PATCH_DATA.get('school__school_code')

    context.test().assertEqual(response.get('school_code'), editted_school_code)


@then('database will delete the school record')
def database_will_delete_school(context):
    context.test().assertEqual(context.response.data, JSON_OBJ_NOT_FOUND_RES)


@then('database will not create the school record')
def database_will_not_create_school(context):
    response = context.response.data

    context.test().assertEqual(response, JSON_PERMISSION_DENIED_RES)


@then('database will not edit the school record')
def database_will_not_edit_school(context):
    response = context.response.data

    context.test().assertEqual(response, JSON_PERMISSION_DENIED_RES)


@then('database will not delete the school record')
def database_will_not_delete_school(context):
    response = context.response.data

    context.test().assertEqual(response, JSON_PERMISSION_DENIED_RES)


@then('database will create the program record')
def database_will_create_program(context):
    response = context.response.data

    posted_program_name = PROGRAM_SAMPLE_POST_DATA.get('program_name')

    context.test().assertEqual(response.get('program_name'), posted_program_name)


@then('database will edit the program record')
def database_will_edit_program(context):
    response = context.response.data

    editted_program_name = PUT_DATA.get('program__program_name')

    context.test().assertEqual(response.get('program_name'), editted_program_name)


@then('database will partially edit the program record')
def database_will_partially_edit_program(context):
    response = context.response.data

    editted_program_name = PATCH_DATA.get('program__program_name')

    context.test().assertEqual(response.get(
        'program_name'), editted_program_name)


@then('database will delete the program record')
def database_will_delete_program(context):
    context.test().assertEqual(context.response.data, JSON_OBJ_NOT_FOUND_RES)


@then('database will not create the program record')
def database_will_not_create_program(context):
    response = context.response.data

    context.test().assertEqual(response, JSON_PERMISSION_DENIED_RES)


@then('database will not edit the program record')
def database_will_not_edit_program(context):
    response = context.response.data

    context.test().assertEqual(response, JSON_PERMISSION_DENIED_RES)


@then('database will not delete the program record')
def database_will_not_delete_program(context):
    response = context.response.data

    context.test().assertEqual(response, JSON_PERMISSION_DENIED_RES)


@then('database will create the rotation record')
def database_will_create_rotation(context):
    response = context.response.data

    posted_rotation_num = ROTATION_SAMPLE_POST_DATA.get('rotation_number')

    context.test().assertEqual(response.get(
        'rotation_number'), posted_rotation_num)


@then('database will edit the rotation record')
def database_will_edit_rotation(context):
    response = context.response.data

    editted_rotation_num = PUT_DATA.get('rotation__rotation_number')

    context.test().assertEqual(response.get(
        'rotation_number'), editted_rotation_num)


@then('database will partially edit the rotation record')
def database_will_partially_edit_rotation(context):
    response = context.response.data

    editted_rotation_num = PATCH_DATA.get('rotation__rotation_number')

    context.test().assertEqual(response.get(
        'rotation_number'), editted_rotation_num)


@then('database will delete the rotation record')
def database_will_delete_rotation(context):
    context.test().assertEqual(context.response.data, JSON_OBJ_NOT_FOUND_RES)


@then('database will not create the rotation record')
def database_will_not_create_rotation(context):
    response = context.response.data

    context.test().assertEqual(response, JSON_PERMISSION_DENIED_RES)


@then('database will not edit the rotation record')
def database_will_not_edit_rotation(context):
    response = context.response.data

    context.test().assertEqual(response, JSON_PERMISSION_DENIED_RES)


@then('database will not delete the rotation record')
def database_will_not_delete_rotation(context):
    response = context.response.data

    context.test().assertEqual(response, JSON_PERMISSION_DENIED_RES)


@then('the specific students data will be returned as JSON response')
def specific_student_JSON_data_response(context):
    response = context.response.data

    filtered_student_lastname = FILTER_PARAMS.get('last_name')

    context.test().assertEqual(response[0].get('last_name'),
                               filtered_student_lastname)


@then('No data response will be sent from server')
def no_response_from_server(context):
    response = context.response.data

    context.test().assertEqual(response, JSON_PERMISSION_DENIED_RES)


@then('server will respond with 405')
def server_responds_405(context):
    context.test().assertEqual(context.response.status_code, 405)


@then('server response status is OK 200')
def server_response_20(context):
    context.test().assertEqual(context.response.status_code, 200)
