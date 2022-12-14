import json
from urllib import response


from behave import then

from apps.sms.google_sheets import GoogleSheet
from apps.sms.constants import STUDENT_RECORD_HEADERS

from constants import (SMS_STUDENT_SAMPLE_SAME_SCHOOL_POST_DATA,
                       SMS_STUDENT_SAMPLE_DIFF_SCHOOL_POST_DATA,
                       SMS_SCHOOL_SAMPLE_POST_DATA,
                       SMS_PROGRAM_SAMPLE_POST_DATA,
                       SMS_ROTATION_SAMPLE_POST_DATA,
                       SMS_STUDENT_SAMPLE_PUT_DATA,
                       JSON_PERMISSION_DENIED_RES,
                       JSON_OBJ_NOT_FOUND_RES,
                       SMS_FILTER_PARAMS,
                       SMS_FILTER_ROATAION_PARAM,
                       SMS_FILTER_PROGRAM_PARAM,
                       SMS_SCHOOL_SAMPLE_PUT_DATA,
                       SMS_PROGRAM_SAMPLE_PUT_DATA,
                       SMS_ROTATION_SAMPLE_PUT_DATA,
                       SMS_STUDENT_SAMPLE_PATCH_DATA,
                       SMS_SCHOOL_SAMPLE_PATCH_DATA,
                       SMS_PROGRAM_SAMPLE_PATCH_DATA,
                       SMS_ROTATION_SAMPLE_PATCH_DATA,
                       SMS_GOOGLE_POST_DATA,
                       SMS_GOOGLE_EDIT_CHECK_DATA,
                       SMS_ST2_PROGRAM_SAMPLE_PATCH_DATA,
                       SMS_ST2_ROTATION_SAMPLE_PATCH_DATA,
                       SMS_STUDENT_STATISTIC_SAMPLE_DATA,
                       JSON_SUPERUSER_ONLY_RES,
                       GMS_CNA_ROTATION_POST_SAMPLE_DATA,
                       GMS_CNA_STUDENT_POST_SAMPLE_DATA,
                       GMS_CNA_THEORY_RECORD_POST_SAMPLE_DATA,
                       GMS_CNA_CLINICAL_RECORD_POST_SAMPLE_DATA,
                       GMS_HHA_ROTATION_POST_SAMPLE_DATA,
                       GMS_HHA_STUDENT_POST_SAMPLE_DATA,
                       GMS_HHA_THEORY_RECORD_POST_SAMPLE_DATA,
                       GMS_HHA_CLINICAL_RECORD_POST_SAMPLE_DATA,
                       GMS_CNA_ROTATION_PUT_SAMPLE_DATA,
                       GMS_CNA_STUDENT_PUT_SAMPLE_DATA,
                       GMS_CNA_THEORY_RECORD_PUT_SAMPLE_DATA,
                       GMS_CNA_CLINICAL_RECORD_PUT_SAMPLE_DATA,
                       GMS_HHA_ROTATION_PUT_SAMPLE_DATA,
                       GMS_HHA_STUDENT_PUT_SAMPLE_DATA,
                       GMS_HHA_THEORY_RECORD_PUT_SAMPLE_DATA,
                       GMS_HHA_CLINICAL_RECORD_PUT_SAMPLE_DATA,
                       GMS_CNA_ROTATION_PATCH_SAMPLE_DATA,
                       GMS_CNA_STUDENT_PATCH_SAMPLE_DATA,
                       GMS_CNA_THEORY_RECORD_PATCH_SAMPLE_DATA,
                       GMS_CNA_CLINICAL_RECORD_PATCH_SAMPLE_DATA,
                       GMS_HHA_ROTATION_PATCH_SAMPLE_DATA,
                       GMS_HHA_STUDENT_PATCH_SAMPLE_DATA,
                       GMS_HHA_THEORY_RECORD_PATCH_SAMPLE_DATA,
                       GMS_HHA_CLINICAL_RECORD_PATCH_SAMPLE_DATA,
                       GMS_STI_CNA_HHA_ROTATION_FILTER_PARAMS,
                       GMS_ST2_CNA_HHA_ROTATION_FILTER_PARAMS,
                       GMS_STI_CNA_STUDENT_FILTER_PARAMS,
                       GMS_STI_HHA_STUDENT_FILTER_PARAMS,
                       GMS_ST2_CNA_STUDENT_FILTER_PARAMS,
                       GMS_ST2_HHA_STUDENT_FILTER_PARAMS,
                       GMS_STI_HHA_ROTATION2_FILTER_PARAMS,
                       GMS_STI_CNA_ROTATION2_FILTER_PARAMS,
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
                       SMS_FILTER_PARAMS_ST2,
                       SMS_ST2_STUDENT_SAMPLE_PATCH_DATA,
                       SMS_ST2_GOOGLE_EDIT_CHECK_DATA,
                       JSON_404_NOT_FOUND_RES,
                       SMS_ST2_STUDENT_SAMPLE_POST_DATA,
                       SMS_ST2_SCHOOL_SAMPLE_POST_DATA,
                       SMS_ST2_PROGRAM_SAMPLE_POST_DATA,
                       SMS_ST2_ROTATION_SAMPLE_POST_DATA,
                       JSON_400_CROSS_SCHOOL_ADD_ERR,
                       SMS_ST2_SCHOOL_SAMPLE_PUT_DATA,
                       SMS_ST2_PROGRAM_SAMPLE_PUT_DATA,
                       SMS_ST2_ROTATION_SAMPLE_PUT_DATA,
                       SMS_ST2_STUDENT_SAMPLE_PUT_DATA,
                       SMS_ST2_SCHOOL_SAMPLE_PATCH_DATA,
                       SMS_ST2_GOOGLE_POST_DATA,
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
                       GMS_ST2_HHA_CLINICAL_RECORD_POST_SAMPLE_DATA,
                       JSON_400_CROSS_SCHOOL_ADD_ERR,
                       CMS_STI_CLIENT_SAMPLE_POST,
                       CMS_STI_NOTE_SAMPLE_POST,
                       CMS_STI_CLIENT_SAMPLE_PUT,
                       CMS_STI_NOTE_SAMPLE_PUT,
                       CMS_SECOND_CLIENT_PUT,
                       CMS_SECOND_NOTE_PUT,
                       CMS_STI_CLIENT_PATCH,
                       CMS_STI_NOTE_PATCH,
                       CMS_ST2_CLIENT_SAMPLE_POST,
                       CMS_ST2_NOTE_SAMPLE_POST,
                       CMS_ST2_CLIENT_SAMPLE_PUT,
                       CMS_ST2_NOTE_SAMPLE_PUT,
                       CMS_ST2_CLIENT_PATCH,
                       CMS_ST2_NOTE_PATCH,
                       CMS_SECOND_NOTE_PATCH,
                       CMS_SECOND_CLIENT_PATCH,
                       CMS_CLIENT_FILTER_PARAMS,
                       CMS_NOTE_FILTER_PARAMS,
                       CMS_SECOND_CLIENT_FILTER_PARAMS,
                       CMS_SECOND_NOTE_FILTER_PARAMS,
                       CMS_ST2_CLIENT_FILTER_PARAMS,
                       CMS_ST2_NOTE_FILTER_PARAMS,
                       )


from django.apps import apps


# NOTE: BELOW ARE SMS RELATED @THENS

def google_sheet_del(context, student_id, school_name):
    gs_api = GoogleSheet.init_google_sheet(school_name)

    del_row_num = gs_api.match(gs_api.worksheets, student_id)

    # assert we are matching the student we've created and posted onto google sheet
    gs_api.delete(gs_api.spreadsheet, del_row_num)
    gs_api.refresh(gs_api.spreadsheet)

    # after deleting, assert that match returns none
    del_row_num = gs_api.match(gs_api.worksheets, student_id)
    context.test().assertIsNone(del_row_num)


def google_sheet_create(context, student_id, school_name, post_data):

    gs_api = GoogleSheet.init_google_sheet(school_name)

    gs_api.create(gs_api.worksheets, post_data)
    gs_api.refresh(gs_api.spreadsheet)

    # assert that we have created!
    matched_row_num = gs_api.match(gs_api.worksheets, student_id)
    context.test().assertIsNotNone(matched_row_num)


# dependent on what is passed to check, make sure [] lists are passed in
def google_sheet_check_edit(context, student_id, data_to_check, school_name):
    gs_api = GoogleSheet.init_google_sheet(school_name)

    row = gs_api.match(gs_api.worksheets, student_id)
    context.test().assertIsNotNone(row)
    range_ = f'A{row}:Y{row}'

    database_worksheet = gs_api.worksheets.get('db_worksheet')

    values = database_worksheet.get(range_)

    context.test().assertEqual(values, [data_to_check])


@then('will receive JSON response of data')
def receive_JSON_data(context):
    response = context.response.data

    no_json_res = []

    context.test().assertJSONNotEqual(
        json.dumps(str(response)), json.dumps(no_json_res))

    context.test().assertEqual(context.response.status_code, 200)


@then('database will create the student record of another school')
def database_create_student(context):
    response = context.response.data
    posted_student_last_name = SMS_STUDENT_SAMPLE_DIFF_SCHOOL_POST_DATA.get(
        'last_name')

    # assert response
    context.test().assertEqual(response.get('last_name'), posted_student_last_name)

    # assert DB
    Student = apps.get_model('sms', 'Student')

    if not Student.objects.filter(last_name__exact=posted_student_last_name).exists():
        assert False
    else:
        Student.objects.filter(
            last_name__exact=posted_student_last_name).delete()

    # we need to test google sheet migration, and delete student!
    # the student's school that we are testing with
    google_sheet_del(context, response.get('student_id'), 'ST2')


@then('database will create the student record')
def database_create_student(context):
    response = context.response.data
    posted_student_last_name = SMS_STUDENT_SAMPLE_SAME_SCHOOL_POST_DATA.get(
        'last_name')

    # assert
    context.test().assertEqual(response.get('last_name'), posted_student_last_name)

    # assert DB
    Student = apps.get_model('sms', 'Student')

    if not Student.objects.filter(last_name__exact=posted_student_last_name).exists():
        assert False
    else:
        Student.objects.filter(
            last_name__exact=posted_student_last_name).delete()

    # we need to test google sheet migration, and delete student!

    # the student's school that we are testing with
    google_sheet_del(context, response.get('student_id'), 'STI')


@then('database will create the ST2 student record')
def database_create_ST2_student(context):
    response = context.response.data
    posted_student_last_name = SMS_ST2_STUDENT_SAMPLE_POST_DATA.get(
        'last_name')

    # assert response
    context.test().assertEqual(response.get('last_name'), posted_student_last_name)

    # assert DB
    Student = apps.get_model('sms', 'Student')

    if not Student.objects.filter(last_name__exact=posted_student_last_name).exists():
        assert False
    else:
        Student.objects.filter(
            last_name__exact=posted_student_last_name).delete()

    # we need to test google sheet migration, and delete student!
    # the student's school that we are testing with
    google_sheet_del(context, response.get('student_id'), 'ST2')


@then('database will not create the student record')
def database_will_not_create_student(context):
    response = context.response.data

    posted_student_id = SMS_STUDENT_SAMPLE_DIFF_SCHOOL_POST_DATA.get(
        'student_id')

    context.test().assertNotEqual(response.get('student_id'), posted_student_id)

    Student = apps.get_model('sms', 'Student')

    if Student.objects.filter(
            student_id__exact=posted_student_id).exists():
        assert False


@then('database will edit the student record')
def database_will_edit_student(context):
    response = context.response.data

    editted_last_name = SMS_STUDENT_SAMPLE_PUT_DATA.get('last_name')

    context.test().assertEqual(response.get('last_name'), editted_last_name)

    # we need to test google sheet migration, and delete student!
    student_id = response.get('student_id')

    google_sheet_check_edit(context, student_id,
                            SMS_GOOGLE_EDIT_CHECK_DATA.get('PUT_DATA'), 'STI')

    Student = apps.get_model('sms', 'Student')
    if not Student.objects.filter(
            last_name__exact=editted_last_name).exists():
        assert False


@then('database will partially edit the student record')
def database_will_partially_edit_student(context):
    response = context.response.data

    editted_last_name = SMS_STUDENT_SAMPLE_PATCH_DATA.get('last_name')

    context.test().assertEqual(response.get('last_name'), editted_last_name)

    # we need to test google sheet migration, and delete student!
    student_id = response.get('student_id')
    google_sheet_check_edit(context, student_id,
                            SMS_GOOGLE_EDIT_CHECK_DATA.get('PATCH_DATA'), 'STI')

    Student = apps.get_model('sms', 'Student')
    if not Student.objects.filter(
            last_name__exact=editted_last_name).exists():
        assert False


@then('database will partially edit the ST2 student record')
def database_will_partially_edit_ST2_student(context):
    response = context.response.data

    editted_last_name = SMS_ST2_STUDENT_SAMPLE_PATCH_DATA.get('last_name')

    context.test().assertEqual(response.get('last_name'), editted_last_name)

    Student = apps.get_model('sms', 'Student')
    if not Student.objects.filter(
            last_name__exact=editted_last_name).exists():
        assert False

    student_id = response.get('student_id')
    google_sheet_check_edit(
        context, student_id, SMS_ST2_GOOGLE_EDIT_CHECK_DATA.get('PATCH_DATA'), 'ST2')

    Student = apps.get_model('sms', 'Student')
    if not Student.objects.filter(
            last_name__exact=editted_last_name).exists():
        assert False


@then('database will delete the student record')
def database_will_delete_student(context):
    context.test().assertEqual(context.response.data, None)

    Student = apps.get_model('sms', 'Student')
    if Student.objects.filter(student_uuid__exact=context.uuid).exists():
        assert False

    student_id = SMS_GOOGLE_POST_DATA[STUDENT_RECORD_HEADERS.index(
        'student_id')]

    google_sheet_create(context, student_id, 'STI', SMS_GOOGLE_POST_DATA)


@then('database will delete the ST2 student record')
def database_will_delete_ST2_student(context):
    context.test().assertEqual(context.response.data, None)

    Student = apps.get_model('sms', 'Student')
    if Student.objects.filter(student_uuid__exact=context.uuid).exists():
        assert False

    student_id = SMS_ST2_GOOGLE_POST_DATA[STUDENT_RECORD_HEADERS.index(
        'student_id')]

    google_sheet_create(context, student_id, 'ST2', SMS_ST2_GOOGLE_POST_DATA)


@then('database will create the school record')
def database_will_create_school(context):
    response = context.response.data

    posted_school_code = SMS_SCHOOL_SAMPLE_POST_DATA.get('school_code')

    context.test().assertEqual(response.get('school_code'), posted_school_code)

    School = apps.get_model('sms', 'School')

    if not School.objects.filter(
            school_code__exact=posted_school_code).exists():
        assert False
    else:
        School.objects.filter(
            school_code__exact=posted_school_code).delete()


@then('database will create the ST2 school record')
def database_will_create_ST2_school(context):
    response = context.response.data

    posted_school_code = SMS_ST2_SCHOOL_SAMPLE_POST_DATA.get('school_code')

    context.test().assertEqual(response.get('school_code'), posted_school_code)

    School = apps.get_model('sms', 'School')

    if not School.objects.filter(
            school_code__exact=posted_school_code).exists():
        assert False
    else:
        School.objects.filter(
            school_code__exact=posted_school_code).delete()


@then('database will edit the school record')
def database_will_edit_school(context):
    response = context.response.data

    editted_school_code = SMS_SCHOOL_SAMPLE_PUT_DATA.get('school_code')

    context.test().assertEqual(response.get('school_code'), editted_school_code)

    School = apps.get_model('sms', 'School')
    if not School.objects.filter(
            school_code__exact=editted_school_code).exists():
        assert False


@then('database will edit the ST2 school record')
def database_will_edit_ST2_school(context):
    response = context.response.data

    editted_school_code = SMS_ST2_SCHOOL_SAMPLE_PUT_DATA.get('school_code')

    context.test().assertEqual(response.get('school_code'), editted_school_code)

    School = apps.get_model('sms', 'School')
    if not School.objects.filter(
            school_code__exact=editted_school_code).exists():
        assert False


@then('database will edit the ST2 program record')
def database_will_edit_ST2_program(context):
    response = context.response.data
    editted_program_name = SMS_ST2_PROGRAM_SAMPLE_PUT_DATA.get('program_name')

    context.test().assertEqual(response.get('program_name'), editted_program_name)

    Program = apps.get_model('sms', 'Program')
    if not Program.objects.filter(
            program_name__exact=editted_program_name).exists():
        assert False


@then('database will edit the ST2 rotation record')
def database_will_edit_ST2_rotation(context):
    response = context.response.data

    editted_rotation_num = SMS_ST2_ROTATION_SAMPLE_PUT_DATA.get(
        'rotation_number')

    context.test().assertEqual(response.get(
        'rotation_number'), editted_rotation_num)

    Rotation = apps.get_model('sms', 'Rotation')

    if not Rotation.objects.filter(
            rotation_number__exact=editted_rotation_num).exists():
        assert False


@then('database will edit the ST2 student record')
def database_will_edit_ST2_student(context):
    response = context.response.data

    editted_last_name = SMS_ST2_STUDENT_SAMPLE_PUT_DATA.get('last_name')

    context.test().assertEqual(response.get('last_name'), editted_last_name)

    # we need to test google sheet migration, and delete student!
    student_id = response.get('student_id')

    google_sheet_check_edit(context, student_id,
                            SMS_ST2_GOOGLE_EDIT_CHECK_DATA.get('PUT_DATA'), 'ST2')

    Student = apps.get_model('sms', 'Student')
    if not Student.objects.filter(
            last_name__exact=editted_last_name).exists():
        assert False


@then('database will partially edit the school record')
def database_will_partially_edit_school(context):
    response = context.response.data

    editted_school_code = SMS_SCHOOL_SAMPLE_PATCH_DATA.get('school_code')

    context.test().assertEqual(response.get('school_code'), editted_school_code)

    School = apps.get_model('sms', 'School')
    if not School.objects.filter(
            school_code__exact=editted_school_code).exists():
        assert False


@then('database will partially edit the ST2 school record')
def database_will_partially_edit_ST2_school(context):
    response = context.response.data

    editted_school_code = SMS_ST2_SCHOOL_SAMPLE_PATCH_DATA.get('school_code')

    context.test().assertEqual(response.get('school_code'), editted_school_code)

    School = apps.get_model('sms', 'School')
    if not School.objects.filter(
            school_code__exact=editted_school_code).exists():
        assert False


@then('database will delete the school record')
def database_will_delete_school(context):
    context.test().assertEqual(context.response.data, JSON_OBJ_NOT_FOUND_RES)

    School = apps.get_model('sms', 'School')
    if School.objects.filter(pk__exact=context.uuid).exists():
        assert False


@then('database will delete the ST2 school record')
def database_will_delete_ST2_school(context):
    context.test().assertEqual(context.response.data, JSON_OBJ_NOT_FOUND_RES)

    School = apps.get_model('sms', 'School')
    if School.objects.filter(pk__exact=context.uuid).exists():
        assert False


@then('database will not create the school record')
def database_will_not_create_school(context):
    response = context.response.data

    context.test().assertEqual(response, JSON_PERMISSION_DENIED_RES)

    School = apps.get_model('sms', 'School')

    if School.objects.filter(school_code__exact=SMS_PROGRAM_SAMPLE_POST_DATA.get('school_code')).exists():
        assert False


@then('database will create the program record')
def database_will_create_program(context):
    response = context.response.data

    posted_program_name = SMS_PROGRAM_SAMPLE_POST_DATA.get('program_name')

    context.test().assertEqual(response.get('program_name'), posted_program_name)

    Program = apps.get_model('sms', 'Program')
    if not Program.objects.filter(
            program_name__exact=posted_program_name).exists():
        assert False
    else:
        Program.objects.filter(
            program_name__exact=posted_program_name).delete()


@then('database will create the ST2 program record')
def database_will_create_ST2_program(context):
    response = context.response.data

    posted_program_name = SMS_ST2_PROGRAM_SAMPLE_POST_DATA.get('program_name')

    context.test().assertEqual(response.get('program_name'), posted_program_name)

    Program = apps.get_model('sms', 'Program')
    if not Program.objects.filter(
            program_name__exact=posted_program_name).exists():
        assert False
    else:
        Program.objects.filter(
            program_name__exact=posted_program_name).delete()


@then('database will edit the program record')
def database_will_edit_program(context):
    response = context.response.data

    editted_program_name = SMS_PROGRAM_SAMPLE_PUT_DATA.get('program_name')

    context.test().assertEqual(response.get('program_name'), editted_program_name)

    Program = apps.get_model('sms', 'Program')
    if not Program.objects.filter(
            program_name__exact=editted_program_name).exists():
        assert False


@then('database will partially edit the program record')
def database_will_partially_edit_program(context):
    response = context.response.data

    editted_program_name = SMS_PROGRAM_SAMPLE_PATCH_DATA.get('program_name')

    context.test().assertEqual(response.get(
        'program_name'), editted_program_name)

    Program = apps.get_model('sms', 'Program')
    if not Program.objects.filter(
            program_name__exact=editted_program_name).exists():
        assert False


@then('database will partially edit the ST2 program record')
def database_will_partially_edit_ST2_program(context):
    response = context.response.data

    editted_program_name = SMS_ST2_PROGRAM_SAMPLE_PATCH_DATA.get(
        'program_name')

    context.test().assertEqual(response.get(
        'program_name'), editted_program_name)

    Program = apps.get_model('sms', 'Program')
    if not Program.objects.filter(
            program_name__exact=editted_program_name).exists():
        assert False


@then('database will delete the program record')
def database_will_delete_program(context):
    context.test().assertEqual(context.response.data, JSON_OBJ_NOT_FOUND_RES)

    Program = apps.get_model('sms', 'Program')
    if Program.objects.filter(
            program_uuid__exact=context.uuid).exists():
        assert False


@then('database will delete the ST2 program record')
def database_will_delete_ST2_program(context):
    context.test().assertEqual(context.response.data, JSON_OBJ_NOT_FOUND_RES)

    Program = apps.get_model('sms', 'Program')
    if Program.objects.filter(
            program_uuid__exact=context.uuid).exists():
        assert False


@then('database will not create the program record')
def database_will_not_create_program(context):
    response = context.response.data

    context.test().assertEqual(response, JSON_PERMISSION_DENIED_RES)

    Program = apps.get_model('sms', 'Program')

    if Program.objects.filter(program_name__exact=SMS_PROGRAM_SAMPLE_POST_DATA.get('program_name')).exists():
        assert False


@then('database will create the rotation record')
def database_will_create_rotation(context):
    response = context.response.data

    posted_rotation_num = SMS_ROTATION_SAMPLE_POST_DATA.get('rotation_number')

    context.test().assertEqual(response.get(
        'rotation_number'), posted_rotation_num)

    Rotation = apps.get_model('sms', 'Rotation')

    if not Rotation.objects.filter(
            rotation_number__exact=posted_rotation_num).exists():
        assert False
    else:
        Rotation.objects.filter(
            rotation_number__exact=posted_rotation_num).delete()


@then('database will create the ST2 rotation record')
def database_will_create_ST2_rotation(context):
    response = context.response.data

    posted_rotation_num = SMS_ST2_ROTATION_SAMPLE_POST_DATA.get(
        'rotation_number')

    context.test().assertEqual(response.get(
        'rotation_number'), posted_rotation_num)

    Rotation = apps.get_model('sms', 'Rotation')

    if not Rotation.objects.filter(
            rotation_number__exact=posted_rotation_num).exists():
        assert False
    else:
        Rotation.objects.filter(
            rotation_number__exact=posted_rotation_num).delete()


@then('database will edit the rotation record')
def database_will_edit_rotation(context):
    response = context.response.data

    editted_rotation_num = SMS_ROTATION_SAMPLE_PUT_DATA.get('rotation_number')

    context.test().assertEqual(response.get(
        'rotation_number'), editted_rotation_num)

    Rotation = apps.get_model('sms', 'Rotation')

    if not Rotation.objects.filter(
            rotation_number__exact=editted_rotation_num).exists():
        assert False


@then('database will partially edit the rotation record')
def database_will_partially_edit_rotation(context):
    response = context.response.data

    editted_rotation_num = SMS_ROTATION_SAMPLE_PATCH_DATA.get(
        'rotation_number')

    context.test().assertEqual(response.get(
        'rotation_number'), editted_rotation_num)

    Rotation = apps.get_model('sms', 'Rotation')

    if not Rotation.objects.filter(
            rotation_number__exact=editted_rotation_num).exists():
        assert False


@then('database will partially edit the ST2 rotation record')
def database_will_partially_edit_ST2_rotation(context):

    response = context.response.data
    editted_rotation_num = SMS_ST2_ROTATION_SAMPLE_PATCH_DATA.get(
        'rotation_number')

    context.test().assertEqual(response.get(
        'rotation_number'), editted_rotation_num)

    Rotation = apps.get_model('sms', 'Rotation')

    if not Rotation.objects.filter(
            rotation_number__exact=editted_rotation_num).exists():
        assert False


@then('database will delete the rotation record')
def database_will_delete_rotation(context):
    context.test().assertEqual(context.response.data, JSON_OBJ_NOT_FOUND_RES)

    Rotation = apps.get_model('sms', 'Rotation')

    if Rotation.objects.filter(
            rotation_uuid__exact=context.uuid).exists():
        assert False


@then('database will delete the ST2 rotation record')
def database_will_delete_ST2_rotation(context):
    context.test().assertEqual(context.response.data, JSON_OBJ_NOT_FOUND_RES)

    Rotation = apps.get_model('sms', 'Rotation')

    if Rotation.objects.filter(
            rotation_uuid__exact=context.uuid).exists():
        assert False


@then('database will not create the rotation record')
def database_will_not_create_rotation(context):
    response = context.response.data

    context.test().assertEqual(response, JSON_PERMISSION_DENIED_RES)

    Rotation = apps.get_model('sms', 'Rotation')

    if Rotation.objects.filter(rotation_number__exact=SMS_ROTATION_SAMPLE_POST_DATA.get('rotation_number')).exists():
        assert False


@then('the specific students data will be returned as JSON response')
def specific_student_JSON_data_response(context):
    response = context.response.data

    filtered_student_lastname = SMS_FILTER_PARAMS.get('last_name')

    # context.test().assertEqual(response[0].get('last_name'),
    #                            filtered_student_lastname)

    if len(response) == 0:
        assert False

    for indx, data in enumerate(response):
        if data.get('last_name') == filtered_student_lastname:
            assert True
            break
        if indx == (len(response) - 1) and data.get('last_name') != filtered_student_lastname:
            assert False


@then('the specific rotation data will be returned as JSON response')
def specific_rotation_JSON_data_response(context):
    response = context.response.data

    filtered_rotation_program_uuid = SMS_FILTER_ROATAION_PARAM.get(
        'program_uuid')

    if len(response) == 0:
        assert False

    for indx, data in enumerate(response):
        if str(data.get('program')) == filtered_rotation_program_uuid:
            assert True
            break
        if indx == (len(response) - 1) and data.get('program') != filtered_rotation_program_uuid:
            assert False



@then('the specific program data will be returned as JSON response')
def specific_program_JSON_data_response(context):
    response = context.response.data

    filtered_school_school_uuid = SMS_FILTER_PROGRAM_PARAM.get('school_uuid')

    if len(response) == 0:
        assert False
        
    for indx, data in enumerate(response):
        if str(data.get('school')) == filtered_school_school_uuid:
            assert True
            break

        if indx == (len(response) - 1) and data.get('school') != filtered_school_school_uuid:
            assert False


@then('will receive statistics JSON response')
def specific_statistics_response(context):
    response = context.response.data

    assert response == SMS_STUDENT_STATISTIC_SAMPLE_DATA


@then('server will respond with 405')
def server_responds_405(context):
    context.test().assertEqual(context.response.status_code, 405)


@then('server response status is OK 200')
def server_response_200(context):
    context.test().assertEqual(context.response.status_code, 200)


@then('server response status is bad request 400')
def server_response_400(context):
    context.test().assertEqual(context.response.status_code, 400)


@then('server response status is forbidden 403')
def server_response_403(context):
    context.test().assertEqual(context.response.status_code, 403)


@then('will receive student data in json datadump')
def server_response_with_datadump_json(context):
    response_data = context.response.data

    # NOTE: if fixture change on google sheet (test db sheet), this test WILL fail, change the proper assert values to pass
    for dict_ in response_data:
        if dict_.get('model') == 'sms.rotation':
            context.test().assertEqual(dict_.get('fields').get('rotation_number'), 1)

        elif dict_.get('model') == 'sms.student':
            context.test().assertEqual(dict_.get('fields').get('student_id'), 'RO-HHA-01-1006-TB')


@then('will receive superuser only message')
def server_response_with_superuser_only(context):
    response = context.response.data

    context.test().assertEqual(response, JSON_SUPERUSER_ONLY_RES)


@then('the specific ST2 students data will be returned as JSON response')
def specific_ST2_smsStudent_data_JSON_response(context):
    response = context.response.data

    if len(response) == 0:
        assert False

    for indx, data in enumerate(response):
        if data.get('first_name') == SMS_FILTER_PARAMS_ST2.get('first_name') and \
           data.get('last_name') == SMS_FILTER_PARAMS_ST2.get('last_name') and \
           data.get('email') == SMS_FILTER_PARAMS_ST2.get('email'):
            assert True
            break

        if indx == (len(response) - 1) and \
           (data.get('first_name') != SMS_FILTER_PARAMS_ST2.get('first_name') or
           data.get('last_name') != SMS_FILTER_PARAMS_ST2.get('last_name') or
           data.get('email') != SMS_FILTER_PARAMS_ST2.get('email')):
            assert False


@then('no desired ST2 students data filtered by rotation or program will be returned as JSON response')
def no_specific_ST2_smsStudents_JSON_data_response(context):
    response = context.response.data

    for data in response:
        if data.get('first_name') == SMS_FILTER_PARAMS_ST2.get('first_name') and \
           str(data.get('last_name')) == GMS_ST2_HHA_CLINICALRECORD_FILTER_PARAMS.get('last_name') and \
           data.get('email') == GMS_ST2_HHA_CLINICALRECORD_FILTER_PARAMS.get('email'):
            assert False

    assert True


@then('server will respond with 404')
def server_responds_with_404_not_found(context):
    context.test().assertEqual(context.response.data, JSON_404_NOT_FOUND_RES)


@then('server will respond with 400 bad request due to cross school student additions')
def server_responds_with_400_cross_school_additions(context):
    context.test().assertEqual(context.response.data, JSON_400_CROSS_SCHOOL_ADD_ERR)

# NOTE: BELOW ARE GMS RELATED @THENS


@then('will be permission denied')
def permission_denied(context):
    context.test().assertEqual(context.response.data, JSON_PERMISSION_DENIED_RES)


@then('database will create the cna rotation record')
def database_create_cnaRotation_record(context):
    response_data = context.response.data

    posted_rotation_start_date = GMS_CNA_ROTATION_POST_SAMPLE_DATA.get(
        'start_date')

    context.test().assertEqual(response_data.get(
        'start_date'), posted_rotation_start_date)

    CNARotation = apps.get_model('gms', 'CNARotation')

    if not CNARotation.objects.filter(
            start_date__exact=posted_rotation_start_date).exists():
        assert False
    else:
        CNARotation.objects.filter(
            start_date__exact=posted_rotation_start_date).delete()


@then('database will create the ST2 cna rotation record')
def database_create_ST2_cnaRotation(context):
    response_data = context.response.data

    posted_rotation_start_date = GMS_ST2_CNA_ROTATION_POST_SAMPLE_DATA.get(
        'start_date')

    context.test().assertEqual(response_data.get(
        'start_date'), posted_rotation_start_date)

    CNARotation = apps.get_model('gms', 'CNARotation')

    if not CNARotation.objects.filter(
            start_date__exact=posted_rotation_start_date).exists():
        assert False
    else:
        CNARotation.objects.filter(
            start_date__exact=posted_rotation_start_date).delete()


@then('database will create the cna student record')
def database_create_cnaStudent_record(context):
    response_data = context.response.data

    posted_student_last_name = GMS_CNA_STUDENT_POST_SAMPLE_DATA.get(
        'last_name')

    context.test().assertEqual(response_data.get(
        'last_name'), posted_student_last_name)

    CNAStudent = apps.get_model('gms', 'CNAStudent')

    if not CNAStudent.objects.filter(
            last_name__exact=posted_student_last_name).exists():
        assert False
    else:
        CNAStudent.objects.filter(
            last_name__exact=posted_student_last_name).delete()


@then('database will create the ST2 cna student record')
def database_create_ST2_cnaStudent_record(context):
    response_data = context.response.data

    posted_student_last_name = GMS_ST2_CNA_STUDENT_POST_SAMPLE_DATA.get(
        'last_name')

    context.test().assertEqual(response_data.get(
        'last_name'), posted_student_last_name)

    CNAStudent = apps.get_model('gms', 'CNAStudent')

    if not CNAStudent.objects.filter(
            last_name__exact=posted_student_last_name).exists():
        assert False
    else:
        CNAStudent.objects.filter(
            last_name__exact=posted_student_last_name).delete()


@then('database will create the cna theory record')
def database_create_cnaTheory_record(context):
    response_data = context.response.data

    posted_cnaTheory_hrs_spent = GMS_CNA_THEORY_RECORD_POST_SAMPLE_DATA.get(
        'hours_spent')

    context.test().assertEqual(response_data.get(
        'hours_spent'), posted_cnaTheory_hrs_spent)

    CNATheoryRecord = apps.get_model('gms', 'CNATheoryRecord')

    if not CNATheoryRecord.objects.filter(
            hours_spent__exact=posted_cnaTheory_hrs_spent).exists():
        assert False
    else:
        CNATheoryRecord.objects.filter(
            hours_spent__exact=posted_cnaTheory_hrs_spent).delete()


@then('database will create the ST2 cna theory record')
def database_create_ST2_cnaTheoryRecord(context):
    response_data = context.response.data

    posted_cnaTheory_hrs_spent = GMS_ST2_CNA_THEORY_RECORD_POST_SAMPLE_DATA.get(
        'hours_spent')

    context.test().assertEqual(response_data.get(
        'hours_spent'), posted_cnaTheory_hrs_spent)

    CNATheoryRecord = apps.get_model('gms', 'CNATheoryRecord')

    if not CNATheoryRecord.objects.filter(
            hours_spent__exact=posted_cnaTheory_hrs_spent).exists():
        assert False
    else:
        CNATheoryRecord.objects.filter(
            hours_spent__exact=posted_cnaTheory_hrs_spent).delete()


@then('database will create the cna clinical record')
def database_create_cnaClinical_record(context):
    response_data = context.response.data

    posted_cnaClinical_date = GMS_CNA_CLINICAL_RECORD_POST_SAMPLE_DATA.get(
        'date')

    context.test().assertEqual(response_data.get('date'), posted_cnaClinical_date)

    CNAClinicalRecord = apps.get_model('gms', 'CNAClinicalRecord')

    if not CNAClinicalRecord.objects.filter(
            date__exact=posted_cnaClinical_date).exists():
        assert False
    else:
        CNAClinicalRecord.objects.filter(
            date__exact=posted_cnaClinical_date).delete()


@then('database will create the ST2 cna clinical record')
def database_create_ST2_cnaClinicalRecords(context):
    response_data = context.response.data

    posted_cnaClinical_date = GMS_ST2_CNA_CLINICAL_RECORD_POST_SAMPLE_DATA.get(
        'date')

    context.test().assertEqual(response_data.get('date'), posted_cnaClinical_date)

    CNAClinicalRecord = apps.get_model('gms', 'CNAClinicalRecord')

    if not CNAClinicalRecord.objects.filter(
            date__exact=posted_cnaClinical_date).exists():
        assert False
    else:
        CNAClinicalRecord.objects.filter(
            date__exact=posted_cnaClinical_date).delete()


@then('database will create the hha rotation record')
def database_create_hhaRotation_record(context):
    response_data = context.response.data

    posted_rotation_start_date = GMS_HHA_ROTATION_POST_SAMPLE_DATA.get(
        'start_date')

    context.test().assertEqual(response_data.get(
        'start_date'), posted_rotation_start_date)

    HHARotation = apps.get_model('gms', 'HHARotation')

    if not HHARotation.objects.filter(
            start_date__exact=posted_rotation_start_date).exists():
        assert False
    else:
        HHARotation.objects.filter(
            start_date__exact=posted_rotation_start_date).delete()


@then('database will create the ST2 hha rotation record')
def database_create_ST2_hhaRotation_record(context):
    response_data = context.response.data

    posted_rotation_start_date = GMS_ST2_HHA_ROTATION_POST_SAMPLE_DATA.get(
        'start_date')

    context.test().assertEqual(response_data.get(
        'start_date'), posted_rotation_start_date)

    HHARotation = apps.get_model('gms', 'HHARotation')

    if not HHARotation.objects.filter(
            start_date__exact=posted_rotation_start_date).exists():
        assert False
    else:
        HHARotation.objects.filter(
            start_date__exact=posted_rotation_start_date).delete()


@then('database will create the hha student record')
def database_create_hhaStudent_record(context):
    response_data = context.response.data

    posted_student_last_name = GMS_HHA_STUDENT_POST_SAMPLE_DATA.get(
        'last_name')

    context.test().assertEqual(response_data.get(
        'last_name'), posted_student_last_name)

    HHAStudent = apps.get_model('gms', 'HHAStudent')

    if not HHAStudent.objects.filter(
            last_name__exact=posted_student_last_name).exists():
        assert False
    else:
        HHAStudent.objects.filter(
            last_name__exact=posted_student_last_name).delete()


@then('database will create the ST2 hha student record')
def database_create_ST2_hhaStudent(context):
    response_data = context.response.data

    posted_student_last_name = GMS_ST2_HHA_STUDENT_POST_SAMPLE_DATA.get(
        'last_name')

    context.test().assertEqual(response_data.get(
        'last_name'), posted_student_last_name)

    HHAStudent = apps.get_model('gms', 'HHAStudent')

    if not HHAStudent.objects.filter(
            last_name__exact=posted_student_last_name).exists():
        assert False
    else:
        HHAStudent.objects.filter(
            last_name__exact=posted_student_last_name).delete()


@then('database will create the hha theory record')
def database_create_hhaTheory_record(context):
    response_data = context.response.data

    posted_hhaTheory_hrs_spent = GMS_HHA_THEORY_RECORD_POST_SAMPLE_DATA.get(
        'hours_spent')

    context.test().assertEqual(response_data.get(
        'hours_spent'), posted_hhaTheory_hrs_spent)

    HHATheoryRecord = apps.get_model('gms', 'HHATheoryRecord')
    if not HHATheoryRecord.objects.filter(
            hours_spent__exact=posted_hhaTheory_hrs_spent).exists():
        assert False

    else:
        HHATheoryRecord.objects.filter(
            hours_spent__exact=posted_hhaTheory_hrs_spent).delete()


@then('database will create the ST2 hha theory record')
def database_create_ST2_hhaTheoryRecord(context):
    response_data = context.response.data

    posted_hhaTheory_hrs_spent = GMS_ST2_HHA_THEORY_RECORD_POST_SAMPLE_DATA.get(
        'hours_spent')

    context.test().assertEqual(response_data.get(
        'hours_spent'), posted_hhaTheory_hrs_spent)

    HHATheoryRecord = apps.get_model('gms', 'HHATheoryRecord')
    if not HHATheoryRecord.objects.filter(
            hours_spent__exact=posted_hhaTheory_hrs_spent).exists():
        assert False

    else:
        HHATheoryRecord.objects.filter(
            hours_spent__exact=posted_hhaTheory_hrs_spent).delete()


@then('database will create the hha clinical record')
def database_create_hhaClinical_record(context):
    response_data = context.response.data

    posted_hhaClinical_date = GMS_HHA_CLINICAL_RECORD_POST_SAMPLE_DATA.get(
        'date')

    context.test().assertEqual(response_data.get('date'), posted_hhaClinical_date)

    HHAClinicalRecord = apps.get_model('gms', 'HHAClinicalRecord')

    if not HHAClinicalRecord.objects.filter(
            date__exact=posted_hhaClinical_date).exists():
        assert False
    else:
        HHAClinicalRecord.objects.filter(
            date__exact=posted_hhaClinical_date).delete()


@then('database will create the ST2 hha clinical record')
def database_create_ST2_hhaClinicalRecord(context):
    response_data = context.response.data

    posted_hhaClinical_date = GMS_ST2_HHA_CLINICAL_RECORD_POST_SAMPLE_DATA.get(
        'date')

    context.test().assertEqual(response_data.get('date'), posted_hhaClinical_date)

    HHAClinicalRecord = apps.get_model('gms', 'HHAClinicalRecord')

    if not HHAClinicalRecord.objects.filter(
            date__exact=posted_hhaClinical_date).exists():
        assert False
    else:
        HHAClinicalRecord.objects.filter(
            date__exact=posted_hhaClinical_date).delete()


@then("bad request error since we cannot add another school's resource")
def bad_request_cannot_add_another_school_resource_gms(context):
    err_string = JSON_400_CROSS_SCHOOL_ADD_ERR.get('non_field_errors')[0]
    for indx, rd in enumerate(context.response.data.values()):
        res_string = rd[0]
        if res_string == err_string:
            assert True
        if indx == (len(context.response.data.values()) - 1) and \
                res_string != err_string:
            assert False


@then('database will not create the cna rotation record')
def database_no_create_cnaRotation_record(context):
    response_data = context.response.data

    posted_rotation_start_date = GMS_CNA_ROTATION_POST_SAMPLE_DATA.get(
        'start_date')

    context.test().assertNotEqual(response_data.get(
        'start_date'), posted_rotation_start_date)

    CNARotation = apps.get_model('gms', 'CNARotation')

    if CNARotation.objects.filter(
            start_date__exact=posted_rotation_start_date).exists():
        assert False


@then('database will not create the cna student record')
def database_no_create_cnaStudent_record(context):
    response_data = context.response.data

    posted_student_last_name = GMS_CNA_STUDENT_POST_SAMPLE_DATA.get(
        'last_name')

    context.test().assertNotEqual(response_data.get(
        'last_name'), posted_student_last_name)

    CNAStudent = apps.get_model('gms', 'CNAStudent')

    if CNAStudent.objects.filter(
            last_name__exact=posted_student_last_name).exists():
        assert False


@then('database will not create the cna theory record')
def database_no_create_cnaTheory_record(context):
    response_data = context.response.data

    posted_cnaTheory_hrs_spent = GMS_CNA_THEORY_RECORD_POST_SAMPLE_DATA.get(
        'hours_spent')

    context.test().assertNotEqual(response_data.get(
        'hours_spent'), posted_cnaTheory_hrs_spent)

    CNATheoryRecord = apps.get_model('gms', 'CNATheoryRecord')

    if CNATheoryRecord.objects.filter(
            hours_spent__exact=posted_cnaTheory_hrs_spent).exists():
        assert False


@then('database will not create the cna clinical record')
def database_no_create_cnaClinical_record(context):
    response_data = context.response.data

    posted_cnaClinical_date = GMS_CNA_CLINICAL_RECORD_POST_SAMPLE_DATA.get(
        'date')

    context.test().assertNotEqual(response_data.get('date'), posted_cnaClinical_date)

    CNAClinicalRecord = apps.get_model('gms', 'CNAClinicalRecord')

    if CNAClinicalRecord.objects.filter(
            date__exact=posted_cnaClinical_date).exists():
        assert False


@then('database will not create the hha rotation record')
def database_no_create_hhaRotation_record(context):
    response_data = context.response.data

    posted_rotation_start_date = GMS_HHA_ROTATION_POST_SAMPLE_DATA.get(
        'start_date')

    context.test().assertNotEqual(response_data.get(
        'start_date'), posted_rotation_start_date)

    HHARotation = apps.get_model('gms', 'HHARotation')

    if HHARotation.objects.filter(
            start_date__exact=posted_rotation_start_date).exists():
        assert False


@then('database will not create the hha student record')
def database_no_create_hhaStudent_record(context):
    response_data = context.response.data

    posted_student_last_name = GMS_HHA_STUDENT_POST_SAMPLE_DATA.get(
        'last_name')

    context.test().assertNotEqual(response_data.get(
        'last_name'), posted_student_last_name)

    HHAStudent = apps.get_model('gms', 'HHAStudent')
    if HHAStudent.objects.filter(
            last_name__exact=posted_student_last_name).exists():
        assert False


@then('database will not create the hha theory record')
def database_no_create_hhaTheory_record(context):
    response_data = context.response.data

    posted_hhaTheory_hrs_spent = GMS_HHA_THEORY_RECORD_POST_SAMPLE_DATA.get(
        'hours_spent')

    context.test().assertNotEqual(response_data.get(
        'hours_spent'), posted_hhaTheory_hrs_spent)

    HHATheoryRecord = apps.get_model('gms', 'HHATheoryRecord')
    if HHATheoryRecord.objects.filter(
            hours_spent__exact=posted_hhaTheory_hrs_spent).exists():
        assert False


@then('database will not create the hha clinical record')
def database_no_create_hhaClinical_record(context):
    response_data = context.response.data

    posted_hhaClinical_date = GMS_HHA_CLINICAL_RECORD_POST_SAMPLE_DATA.get(
        'date')

    context.test().assertNotEqual(response_data.get('date'), posted_hhaClinical_date)

    HHAClinicalRecord = apps.get_model('gms', 'HHAClinicalRecord')
    if HHAClinicalRecord.objects.filter(
            date__exact=posted_hhaClinical_date).exists():
        assert False


@then('database will fully update the cna rotation record')
def database_edit_cnaRotation_record(context):
    response_data = context.response.data

    editted_rotation_start_date = GMS_CNA_ROTATION_PUT_SAMPLE_DATA.get(
        'start_date')

    context.test().assertEqual(response_data.get(
        'start_date'), editted_rotation_start_date)

    CNARotation = apps.get_model('gms', 'CNARotation')
    if not CNARotation.objects.filter(
            start_date__exact=editted_rotation_start_date).exists():
        assert False


@then('database will fully update the ST2 cna rotation record')
def database_edit_ST2_cnaRotation_record(context):
    response_data = context.response.data

    editted_rotation_start_date = GMS_ST2_CNA_ROTATION_PUT_SAMPLE_DATA.get(
        'start_date')

    context.test().assertEqual(response_data.get(
        'start_date'), editted_rotation_start_date)

    CNARotation = apps.get_model('gms', 'CNARotation')
    if not CNARotation.objects.filter(
            start_date__exact=editted_rotation_start_date).exists():
        assert False


@then('database will fully update the cna student record')
def database_edit_cnaStudent_record(context):
    response_data = context.response.data

    editted_student_last_name = GMS_CNA_STUDENT_PUT_SAMPLE_DATA.get(
        'last_name')

    context.test().assertEqual(response_data.get(
        'last_name'), editted_student_last_name)

    CNAStudent = apps.get_model('gms', 'CNAStudent')
    if not CNAStudent.objects.filter(
            last_name__exact=editted_student_last_name).exists():
        assert False


@then('database will fully update the ST2 cna student record')
def database_edit_ST2_cnaStudent(context):
    response_data = context.response.data

    editted_student_last_name = GMS_ST2_CNA_STUDENT_PUT_SAMPLE_DATA.get(
        'last_name')

    context.test().assertEqual(response_data.get(
        'last_name'), editted_student_last_name)

    CNAStudent = apps.get_model('gms', 'CNAStudent')
    if not CNAStudent.objects.filter(
            last_name__exact=editted_student_last_name).exists():
        assert False


@then('database will fully update the cna theory record')
def database_edit_cnaTheory_record(context):
    response_data = context.response.data

    editted_cnaTheory_hrs_spent = GMS_CNA_THEORY_RECORD_PUT_SAMPLE_DATA.get(
        'hours_spent')

    context.test().assertEqual(response_data.get(
        'hours_spent'), editted_cnaTheory_hrs_spent)

    CNATheoryRecord = apps.get_model('gms', 'CNATheoryRecord')
    if not CNATheoryRecord.objects.filter(
            hours_spent__exact=editted_cnaTheory_hrs_spent).exists():
        assert False


@then('database will fully update the ST2 cna theory record')
def database_edit_ST2_cnaTheory(context):
    response_data = context.response.data

    editted_cnaTheory_hrs_spent = GMS_ST2_CNA_THEORY_RECORD_PUT_SAMPLE_DATA.get(
        'hours_spent')

    context.test().assertEqual(response_data.get(
        'hours_spent'), editted_cnaTheory_hrs_spent)

    CNATheoryRecord = apps.get_model('gms', 'CNATheoryRecord')
    if not CNATheoryRecord.objects.filter(
            hours_spent__exact=editted_cnaTheory_hrs_spent).exists():
        assert False


@then('database will fully update the cna clinical record')
def database_edit_cnaClinical_record(context):
    response_data = context.response.data

    editted_cnaClinical_date = GMS_CNA_CLINICAL_RECORD_PUT_SAMPLE_DATA.get(
        'date')

    context.test().assertEqual(response_data.get('date'), editted_cnaClinical_date)

    CNAClinicalRecord = apps.get_model('gms', 'CNAClinicalRecord')
    if not CNAClinicalRecord.objects.filter(
            date__exact=editted_cnaClinical_date).exists():
        assert False


@then('database will fully update the ST2 cna clinical record')
def database_edit_ST2_cnaClinicalRecords(context):
    response_data = context.response.data

    editted_cnaClinical_date = GMS_ST2_CNA_CLINICAL_RECORD_PUT_SAMPLE_DATA.get(
        'date')

    context.test().assertEqual(response_data.get('date'), editted_cnaClinical_date)

    CNAClinicalRecord = apps.get_model('gms', 'CNAClinicalRecord')
    if not CNAClinicalRecord.objects.filter(
            date__exact=editted_cnaClinical_date).exists():
        assert False


@then('database will fully update the hha rotation record')
def database_edit_hhaRotation_record(context):
    response_data = context.response.data

    editted_rotation_start_date = GMS_HHA_ROTATION_PUT_SAMPLE_DATA.get(
        'start_date')

    context.test().assertEqual(response_data.get(
        'start_date'), editted_rotation_start_date)

    HHARotation = apps.get_model('gms', 'HHARotation')
    if not HHARotation.objects.filter(
            start_date__exact=editted_rotation_start_date).exists():
        assert False


@then('database will fully update the ST2 hha rotation record')
def database_edit_ST2_hhaRotations(context):
    response_data = context.response.data

    editted_rotation_start_date = GMS_ST2_HHA_ROTATION_PUT_SAMPLE_DATA.get(
        'start_date')

    context.test().assertEqual(response_data.get(
        'start_date'), editted_rotation_start_date)

    HHARotation = apps.get_model('gms', 'HHARotation')
    if not HHARotation.objects.filter(
            start_date__exact=editted_rotation_start_date).exists():
        assert False


@then('database will fully update the hha student record')
def database_edit_hhaStudent_record(context):
    response_data = context.response.data

    editted_student_last_name = GMS_HHA_STUDENT_PUT_SAMPLE_DATA.get(
        'last_name')

    context.test().assertEqual(response_data.get(
        'last_name'), editted_student_last_name)

    HHAStudent = apps.get_model('gms', 'HHAStudent')
    if not HHAStudent.objects.filter(
            last_name__exact=editted_student_last_name).exists():
        assert False


@then('database will fully update the ST2 hha student record')
def database_edit_ST2_hhaStudent(context):
    response_data = context.response.data

    editted_student_last_name = GMS_ST2_HHA_STUDENT_PUT_SAMPLE_DATA.get(
        'last_name')

    context.test().assertEqual(response_data.get(
        'last_name'), editted_student_last_name)

    HHAStudent = apps.get_model('gms', 'HHAStudent')
    if not HHAStudent.objects.filter(
            last_name__exact=editted_student_last_name).exists():
        assert False


@then('database will fully update the hha theory record')
def database_edit_hhaTheory_record(context):
    response_data = context.response.data

    editted_hhaTheory_hrs_spent = GMS_HHA_THEORY_RECORD_PUT_SAMPLE_DATA.get(
        'hours_spent')

    context.test().assertEqual(response_data.get(
        'hours_spent'), editted_hhaTheory_hrs_spent)

    HHATheoryRecord = apps.get_model('gms', 'HHATheoryRecord')
    if not HHATheoryRecord.objects.filter(
            hours_spent__exact=editted_hhaTheory_hrs_spent).exists():
        assert False


@then('database will fully update the ST2 hha theory record')
def database_edit_ST2_hhaTheory(context):
    response_data = context.response.data

    editted_hhaTheory_hrs_spent = GMS_ST2_HHA_THEORY_RECORD_PUT_SAMPLE_DATA.get(
        'hours_spent')

    context.test().assertEqual(response_data.get(
        'hours_spent'), editted_hhaTheory_hrs_spent)

    HHATheoryRecord = apps.get_model('gms', 'HHATheoryRecord')
    if not HHATheoryRecord.objects.filter(
            hours_spent__exact=editted_hhaTheory_hrs_spent).exists():
        assert False


@then('database will fully update the hha clinical record')
def database_edit_hhaClinical_record(context):
    response_data = context.response.data

    edittedd_hhaClinical_date = GMS_HHA_CLINICAL_RECORD_PUT_SAMPLE_DATA.get(
        'date')

    context.test().assertEqual(response_data.get('date'), edittedd_hhaClinical_date)

    HHAClinicalRecord = apps.get_model('gms', 'HHAClinicalRecord')
    if not HHAClinicalRecord.objects.filter(
            date__exact=edittedd_hhaClinical_date).exists():
        assert False


@then('database will fully update the ST2 hha clinical record')
def database_edit_ST2_hhaClinical(context):
    response_data = context.response.data

    edittedd_hhaClinical_date = GMS_ST2_HHA_CLINICAL_RECORD_PUT_SAMPLE_DATA.get(
        'date')

    context.test().assertEqual(response_data.get('date'), edittedd_hhaClinical_date)

    HHAClinicalRecord = apps.get_model('gms', 'HHAClinicalRecord')
    if not HHAClinicalRecord.objects.filter(
            date__exact=edittedd_hhaClinical_date).exists():
        assert False


@then('database will partially update the cna rotation record')
def database_partially_edit_cnaRotation_record(context):
    response_data = context.response.data

    partially_editted_rotation_start_date = GMS_CNA_ROTATION_PATCH_SAMPLE_DATA.get(
        'start_date')

    context.test().assertEqual(response_data.get(
        'start_date'), partially_editted_rotation_start_date)

    CNARotation = apps.get_model('gms', 'CNARotation')
    if not CNARotation.objects.filter(
            start_date__exact=partially_editted_rotation_start_date).exists():
        assert False


@then('database will partially update the ST2 cna rotation record')
def database_partially_edit_ST2_cnaRotation_record(context):
    response_data = context.response.data

    partially_editted_rotation_clinical_site = GMS_ST2_CNA_ROTATION_PATCH_SAMPLE_DATA.get(
        'clinical_site')

    context.test().assertEqual(response_data.get(
        'clinical_site'), partially_editted_rotation_clinical_site)

    CNARotation = apps.get_model('gms', 'CNARotation')
    if not CNARotation.objects.filter(
            clinical_site__exact=partially_editted_rotation_clinical_site).exists():
        assert False


@then('database will partially update the cna student record')
def database_partially_edit_cnaStudent_record(context):
    response_data = context.response.data

    partially_editted_student_last_name = GMS_CNA_STUDENT_PATCH_SAMPLE_DATA.get(
        'last_name')

    context.test().assertEqual(response_data.get(
        'last_name'), partially_editted_student_last_name)

    CNAStudent = apps.get_model('gms', 'CNAStudent')
    if not CNAStudent.objects.filter(
            last_name__exact=partially_editted_student_last_name).exists():
        assert False


@then('database will partially update the ST2 cna student record')
def database_partially_edit_ST2_cnaStudent_record(context):
    response_data = context.response.data

    partially_editted_student_last_name = GMS_ST2_CNA_STUDENT_PATCH_SAMPLE_DATA.get(
        'last_name')

    context.test().assertEqual(response_data.get(
        'last_name'), partially_editted_student_last_name)

    CNAStudent = apps.get_model('gms', 'CNAStudent')
    if not CNAStudent.objects.filter(
            last_name__exact=partially_editted_student_last_name).exists():
        assert False


@then('database will partially update the cna theory record')
def database_partially_edit_cnaTheory_record(context):
    response_data = context.response.data

    partially_editted_cnaTheory_hrs_spent = GMS_CNA_THEORY_RECORD_PATCH_SAMPLE_DATA.get(
        'hours_spent')

    context.test().assertEqual(response_data.get(
        'hours_spent'), partially_editted_cnaTheory_hrs_spent)

    CNATheoryRecord = apps.get_model('gms', 'CNATheoryRecord')
    if not CNATheoryRecord.objects.filter(
            hours_spent__exact=partially_editted_cnaTheory_hrs_spent).exists():
        assert False


@then('database will partially update the ST2 cna theory record')
def database_partially_edit_ST2_cnaTheory_record(context):
    response_data = context.response.data

    partially_editted_cnaTheory_hrs_spent = GMS_ST2_CNA_THEORY_RECORD_PATCH_SAMPLE_DATA.get(
        'hours_spent')

    context.test().assertEqual(response_data.get(
        'hours_spent'), partially_editted_cnaTheory_hrs_spent)

    CNATheoryRecord = apps.get_model('gms', 'CNATheoryRecord')
    if not CNATheoryRecord.objects.filter(
            hours_spent__exact=partially_editted_cnaTheory_hrs_spent).exists():
        assert False


@then('database will partially update the cna clinical record')
def database_partially_edit_cnaClinical_record(context):
    response_data = context.response.data

    partially_editted_cnaClinical_date = GMS_CNA_CLINICAL_RECORD_PATCH_SAMPLE_DATA.get(
        'date')

    context.test().assertEqual(response_data.get(
        'date'), partially_editted_cnaClinical_date)

    CNAClinicalRecord = apps.get_model('gms', 'CNAClinicalRecord')
    if not CNAClinicalRecord.objects.filter(
            date__exact=partially_editted_cnaClinical_date).exists():
        assert False


@then('database will partially update the ST2 cna clinical record')
def database_partially_edit_ST2_cnaClinical_record(context):
    response_data = context.response.data

    partially_editted_cnaClinical_date = GMS_ST2_CNA_CLINICAL_RECORD_PATCH_SAMPLE_DATA.get(
        'date')

    context.test().assertEqual(response_data.get(
        'date'), partially_editted_cnaClinical_date)

    CNAClinicalRecord = apps.get_model('gms', 'CNAClinicalRecord')
    if not CNAClinicalRecord.objects.filter(
            date__exact=partially_editted_cnaClinical_date).exists():
        assert False


@then('database will partially update the hha rotation record')
def database_partially_edit_hhaRotation_record(context):
    response_data = context.response.data

    partially_editted_rotation_start_date = GMS_HHA_ROTATION_PATCH_SAMPLE_DATA.get(
        'start_date')

    context.test().assertEqual(response_data.get(
        'start_date'), partially_editted_rotation_start_date)

    HHARotation = apps.get_model('gms', 'HHARotation')
    if not HHARotation.objects.filter(
            start_date__exact=partially_editted_rotation_start_date).exists():
        assert False


@then('database will partially update the ST2 hha rotation record')
def database_partially_edit_ST2_hhaRotation_record(context):
    response_data = context.response.data

    partially_editted_rotation_clinical_site = GMS_ST2_HHA_ROTATION_PATCH_SAMPLE_DATA.get(
        'clinical_site')

    context.test().assertEqual(response_data.get(
        'clinical_site'), partially_editted_rotation_clinical_site)

    HHARotation = apps.get_model('gms', 'HHARotation')
    if not HHARotation.objects.filter(
            clinical_site__exact=partially_editted_rotation_clinical_site).exists():
        assert False


@then('database will partially update the hha student record')
def database_partially_edit_hhaStudent_record(context):
    response_data = context.response.data

    partially_editted_student_last_name = GMS_HHA_STUDENT_PATCH_SAMPLE_DATA.get(
        'last_name')

    context.test().assertEqual(response_data.get(
        'last_name'), partially_editted_student_last_name)

    HHAStudent = apps.get_model('gms', 'HHAStudent')
    if not HHAStudent.objects.filter(
            last_name__exact=partially_editted_student_last_name).exists():
        assert False


@then('database will partially update the ST2 hha student record')
def database_partially_edit_ST2_hhaStudent_record(context):
    response_data = context.response.data

    partially_editted_student_last_name = GMS_ST2_HHA_STUDENT_PATCH_SAMPLE_DATA.get(
        'last_name')

    context.test().assertEqual(response_data.get(
        'last_name'), partially_editted_student_last_name)

    HHAStudent = apps.get_model('gms', 'HHAStudent')
    if not HHAStudent.objects.filter(
            last_name__exact=partially_editted_student_last_name).exists():
        assert False


@then('database will partially update the hha theory record')
def database_partially_edit_hhaTheory_record(context):
    response_data = context.response.data

    partially_editted_hhaTheory_hrs_spent = GMS_HHA_THEORY_RECORD_PATCH_SAMPLE_DATA.get(
        'hours_spent')

    context.test().assertEqual(response_data.get(
        'hours_spent'), partially_editted_hhaTheory_hrs_spent)

    HHATheoryRecord = apps.get_model('gms', 'HHATheoryRecord')
    if not HHATheoryRecord.objects.filter(
            hours_spent__exact=partially_editted_hhaTheory_hrs_spent).exists():
        assert False


@then('database will partially update the ST2 hha theory record')
def database_partially_edit_ST2_hhaTheory_record(context):
    response_data = context.response.data

    partially_editted_hhaTheory_hrs_spent = GMS_ST2_HHA_THEORY_RECORD_PATCH_SAMPLE_DATA.get(
        'hours_spent')

    context.test().assertEqual(response_data.get(
        'hours_spent'), partially_editted_hhaTheory_hrs_spent)

    HHATheoryRecord = apps.get_model('gms', 'HHATheoryRecord')
    if not HHATheoryRecord.objects.filter(
            hours_spent__exact=partially_editted_hhaTheory_hrs_spent).exists():
        assert False


@then('database will partially update the hha clinical record')
def database_partially_edit_hhaClinical_record(context):
    response_data = context.response.data

    partially_editted_hhaClinical_date = GMS_HHA_CLINICAL_RECORD_PATCH_SAMPLE_DATA.get(
        'end_date')

    context.test().assertEqual(response_data.get(
        'end_date'), partially_editted_hhaClinical_date)

    HHAClinicalRecord = apps.get_model('gms', 'HHAClinicalRecord')
    if not HHAClinicalRecord.objects.filter(
            end_date__exact=partially_editted_hhaClinical_date).exists():
        assert False


@then('database will partially update the ST2 hha clinical record')
def database_partially_edit_ST2_hhaClinical_record(context):
    response_data = context.response.data

    partially_editted_hhaClinical_date = GMS_ST2_HHA_CLINICAL_RECORD_PATCH_SAMPLE_DATA.get(
        'end_date')

    context.test().assertEqual(response_data.get(
        'end_date'), partially_editted_hhaClinical_date)

    HHAClinicalRecord = apps.get_model('gms', 'HHAClinicalRecord')
    if not HHAClinicalRecord.objects.filter(
            end_date__exact=partially_editted_hhaClinical_date).exists():
        assert False


@then('database will delete the cna rotation record')
def database_delete_cnaRotation_record(context):
    context.test().assertEqual(context.response.data, JSON_OBJ_NOT_FOUND_RES)

    CNARotation = apps.get_model('gms', 'CNARotation')
    if CNARotation.objects.filter(pk__exact=context.uuid).exists():
        assert False


@then('database will delete the ST2 cna rotation record')
def database_delete_ST2_cnaRotation(context):
    context.test().assertEqual(context.response.data, JSON_OBJ_NOT_FOUND_RES)

    CNARotation = apps.get_model('gms', 'CNARotation')
    if CNARotation.objects.filter(pk__exact=context.uuid).exists():
        assert False


@then('database will delete the cna student record')
def database_delete_cnaStudent_record(context):
    context.test().assertEqual(context.response.data, JSON_OBJ_NOT_FOUND_RES)

    CNAStudent = apps.get_model('gms', 'CNAStudent')
    if CNAStudent.objects.filter(pk__exact=context.uuid).exists():
        assert False


@then('database will delete the ST2 cna student record')
def database_delete_ST2_cnaStudent(context):
    context.test().assertEqual(context.response.data, JSON_OBJ_NOT_FOUND_RES)

    CNAStudent = apps.get_model('gms', 'CNAStudent')
    if CNAStudent.objects.filter(pk__exact=context.uuid).exists():
        assert False


@then('database will delete the cna theory record')
def database_delete_cnaTheory_record(context):
    context.test().assertEqual(context.response.data, JSON_OBJ_NOT_FOUND_RES)

    CNATheoryRecord = apps.get_model('gms', 'CNATheoryRecord')
    if CNATheoryRecord.objects.filter(pk__exact=context.uuid).exists():
        assert False


@then('database will delete the ST2 cna theory record')
def database_delete_ST2_cnaTheory(context):
    context.test().assertEqual(context.response.data, JSON_OBJ_NOT_FOUND_RES)

    CNATheoryRecord = apps.get_model('gms', 'CNATheoryRecord')
    if CNATheoryRecord.objects.filter(pk__exact=context.uuid).exists():
        assert False


@then('database will delete the cna clinical record')
def database_delete_cnaClinical_record(context):
    context.test().assertEqual(context.response.data, JSON_OBJ_NOT_FOUND_RES)

    CNAClinicalRecord = apps.get_model('gms', 'CNAClinicalRecord')
    if CNAClinicalRecord.objects.filter(pk__exact=context.uuid).exists():
        assert False


@then('database will delete the ST2 cna clinical record')
def database_delete_cnaClinicalRecord(context):
    context.test().assertEqual(context.response.data, JSON_OBJ_NOT_FOUND_RES)

    CNAClinicalRecord = apps.get_model('gms', 'CNAClinicalRecord')
    if CNAClinicalRecord.objects.filter(pk__exact=context.uuid).exists():
        assert False


@then('database will delete the hha rotation record')
def database_delete_hhaRotation_record(context):
    context.test().assertEqual(context.response.data, JSON_OBJ_NOT_FOUND_RES)

    HHARotation = apps.get_model('gms', 'HHARotation')
    if HHARotation.objects.filter(pk__exact=context.uuid).exists():
        assert False


@then('database will delete the ST2 hha rotation record')
def database_delete_ST2_hhaRotation(context):
    context.test().assertEqual(context.response.data, JSON_OBJ_NOT_FOUND_RES)

    HHARotation = apps.get_model('gms', 'HHARotation')
    if HHARotation.objects.filter(pk__exact=context.uuid).exists():
        assert False


@then('database will delete the hha student record')
def database_delete_hhaStudent_record(context):
    context.test().assertEqual(context.response.data, JSON_OBJ_NOT_FOUND_RES)

    HHAStudent = apps.get_model('gms', 'HHAStudent')
    if HHAStudent.objects.filter(pk__exact=context.uuid).exists():
        assert False


@then('database will delete the ST2 hha student record')
def database_delete_ST2_hhaStudent(context):
    context.test().assertEqual(context.response.data, JSON_OBJ_NOT_FOUND_RES)

    HHAStudent = apps.get_model('gms', 'HHAStudent')
    if HHAStudent.objects.filter(pk__exact=context.uuid).exists():
        assert False


@then('database will delete the hha theory record')
def database_delete_hhaTheory_record(context):
    context.test().assertEqual(context.response.data, JSON_OBJ_NOT_FOUND_RES)

    HHATheoryRecord = apps.get_model('gms', 'HHATheoryRecord')
    if HHATheoryRecord.objects.filter(pk__exact=context.uuid).exists():
        assert False


@then('database will delete the ST2 hha theory record')
def database_delete_ST2_hhaTheory(context):
    context.test().assertEqual(context.response.data, JSON_OBJ_NOT_FOUND_RES)

    HHATheoryRecord = apps.get_model('gms', 'HHATheoryRecord')
    if HHATheoryRecord.objects.filter(pk__exact=context.uuid).exists():
        assert False


@then('database will delete the hha clinical record')
def database_delete_hhaClinical_record(context):
    context.test().assertEqual(context.response.data, JSON_OBJ_NOT_FOUND_RES)

    HHAClinicalRecord = apps.get_model('gms', 'HHAClinicalRecord')
    if HHAClinicalRecord.objects.filter(pk__exact=context.uuid).exists():
        assert False


@then('database will delete the ST2 hha clinical record')
def database_delete_ST2_hhaClinicalRecords(context):
    context.test().assertEqual(context.response.data, JSON_OBJ_NOT_FOUND_RES)

    HHAClinicalRecord = apps.get_model('gms', 'HHAClinicalRecord')
    if HHAClinicalRecord.objects.filter(pk__exact=context.uuid).exists():
        assert False


@then('the specific STI cnaRotations data will be returned as JSON response')
def specific_cnaRotation_JSON_data_response(context):
    response = context.response.data
    if len(response) == 0:
        assert False

    for indx, data in enumerate(response):
        if data.get('end_date') == GMS_STI_CNA_HHA_ROTATION_FILTER_PARAMS.get('end_date') and \
           data.get('start_date') == GMS_STI_CNA_HHA_ROTATION_FILTER_PARAMS.get('start_date') and \
           data.get('rotation_num') == GMS_STI_CNA_HHA_ROTATION_FILTER_PARAMS.get('rotation_num'):
            assert True
            break
        if indx == (len(response) - 1) and \
           (data.get('end_date') != GMS_STI_CNA_HHA_ROTATION_FILTER_PARAMS.get('end_date') or
           data.get('start_date') != GMS_STI_CNA_HHA_ROTATION_FILTER_PARAMS.get('start_date') or
           data.get('rotation_num') != GMS_STI_CNA_HHA_ROTATION_FILTER_PARAMS.get('rotation_num')):
            assert False


@then('the specific STI hhaRotations data will be returned as JSON response')
def specific_hhaRotations_JSON_data_response(context):
    response = context.response.data

    if len(response) == 0:
        assert False
    for indx, data in enumerate(response):
        if data.get('end_date') == GMS_STI_CNA_HHA_ROTATION_FILTER_PARAMS.get('end_date') and \
           data.get('start_date') == GMS_STI_CNA_HHA_ROTATION_FILTER_PARAMS.get('start_date') and \
           data.get('rotation_num') == GMS_STI_CNA_HHA_ROTATION_FILTER_PARAMS.get('rotation_num'):
            assert True
            break
        if indx == (len(response) - 1) and \
           (data.get('end_date') != GMS_STI_CNA_HHA_ROTATION_FILTER_PARAMS.get('end_date') or
           data.get('start_date') != GMS_STI_CNA_HHA_ROTATION_FILTER_PARAMS.get('start_date') or
           data.get('rotation_num') != GMS_STI_CNA_HHA_ROTATION_FILTER_PARAMS.get('rotation_num')):
            print('data', data.get('end_date'), data.get(
                'start_date'), data.get('rotation_num'))
            print('HELLO MOTHERFUCKIN WORLD',
                  GMS_STI_CNA_HHA_ROTATION_FILTER_PARAMS.get('end_date'), GMS_STI_CNA_HHA_ROTATION_FILTER_PARAMS.get('start_date'), GMS_STI_CNA_HHA_ROTATION_FILTER_PARAMS.get('rotation_num'))
            print('type of :', type(GMS_STI_CNA_HHA_ROTATION_FILTER_PARAMS))
            assert False


@then('the specific ST2 cnaRotations data will be returned as JSON response')
def specific_cnaRotation_JSON_data_response(context):
    response = context.response.data

    if len(response) == 0:
        assert False
    for indx, data in enumerate(response):
        if data.get('end_date') == GMS_ST2_CNA_HHA_ROTATION_FILTER_PARAMS.get('end_date') and \
           data.get('start_date') == GMS_ST2_CNA_HHA_ROTATION_FILTER_PARAMS.get('start_date') and \
           data.get('rotation_num') == GMS_ST2_CNA_HHA_ROTATION_FILTER_PARAMS.get('rotation_num'):
            assert True
            break
        if indx == (len(response) - 1) and \
           (data.get('end_date') != GMS_ST2_CNA_HHA_ROTATION_FILTER_PARAMS.get('end_date') or
           data.get('start_date') != GMS_ST2_CNA_HHA_ROTATION_FILTER_PARAMS.get('start_date') or
           data.get('rotation_num') != GMS_ST2_CNA_HHA_ROTATION_FILTER_PARAMS.get('rotation_num')):
            assert False


@then('the specific ST2 hhaRotations data will be returned as JSON response')
def specific_hhaRotations_JSON_data_response(context):
    response = context.response.data

    if len(response) == 0:
        assert False

    for indx, data in enumerate(response):
        if data.get('end_date') == GMS_ST2_CNA_HHA_ROTATION_FILTER_PARAMS.get('end_date') and \
           data.get('start_date') == GMS_ST2_CNA_HHA_ROTATION_FILTER_PARAMS.get('start_date') and \
           data.get('rotation_num') == GMS_ST2_CNA_HHA_ROTATION_FILTER_PARAMS.get('rotation_num'):
            assert True
            break
        if indx == (len(response) - 1) and \
           (data.get('end_date') != GMS_ST2_CNA_HHA_ROTATION_FILTER_PARAMS.get('end_date') or
           data.get('start_date') != GMS_ST2_CNA_HHA_ROTATION_FILTER_PARAMS.get('start_date') or
           data.get('rotation_num') != GMS_ST2_CNA_HHA_ROTATION_FILTER_PARAMS.get('rotation_num')):
            assert False


@then('no data will be returned as JSON response')
def no_json_response(context):
    response_data = context.response.data

    if len(response_data) == 0:
        assert True
    else:
        for data in response_data:
            for param in context.test_param:
                if str(data[param]) == str(context.test_data[param]):
                    assert False


@then('the specific STI cnaStudents data will be returned as JSON response')
def specific_cnaStudents_JSON_data_response(context):
    response = context.response.data

    if len(response) == 0:
        assert False

    for indx, data in enumerate(response):
        if data.get('last_name') == GMS_STI_CNA_STUDENT_FILTER_PARAMS.get('last_name') and \
           data.get('first_name') == GMS_STI_CNA_STUDENT_FILTER_PARAMS.get('first_name') and \
           str(data.get('makeup_student')) == GMS_STI_CNA_STUDENT_FILTER_PARAMS.get('makeup_student'):
            assert True
            break
        if indx == (len(response) - 1) and \
           (data.get('last_name') != GMS_STI_CNA_STUDENT_FILTER_PARAMS.get('last_name') or
           data.get('first_name') != GMS_STI_CNA_STUDENT_FILTER_PARAMS.get('first_name') or
           str(data.get('makeup_student')) != GMS_STI_CNA_STUDENT_FILTER_PARAMS.get('makeup_student')):

            assert False


@then('the specific STI hhaStudents data will be returned as JSON response')
def specific_hhaStudents_JSON_data_response(context):
    response = context.response.data

    if len(response) == 0:
        assert False

    for indx, data in enumerate(response):
        if data.get('last_name') == GMS_STI_HHA_STUDENT_FILTER_PARAMS.get('last_name') and \
           data.get('first_name') == GMS_STI_HHA_STUDENT_FILTER_PARAMS.get('first_name') and \
           str(data.get('makeup_student')) == GMS_STI_HHA_STUDENT_FILTER_PARAMS.get('makeup_student'):
            assert True
            break
        if indx == (len(response) - 1) and \
           (data.get('last_name') != GMS_STI_HHA_STUDENT_FILTER_PARAMS.get('last_name') or
           data.get('first_name') != GMS_STI_HHA_STUDENT_FILTER_PARAMS.get('first_name') or
           str(data.get('makeup_student')) != GMS_STI_HHA_STUDENT_FILTER_PARAMS.get('makeup_student')):
            assert False


@then('the specific ST2 cnaStudents data will be returned as JSON response')
def specific_cnaStudents_JSON_data_response(context):
    response = context.response.data

    if len(response) == 0:
        assert False

    for indx, data in enumerate(response):
        if data.get('last_name') == GMS_ST2_CNA_STUDENT_FILTER_PARAMS.get('last_name') and \
           data.get('first_name') == GMS_ST2_CNA_STUDENT_FILTER_PARAMS.get('first_name') and \
           str(data.get('makeup_student')) == GMS_ST2_CNA_STUDENT_FILTER_PARAMS.get('makeup_student'):
            assert True
            break
        if indx == (len(response) - 1) and \
           (data.get('last_name') != GMS_ST2_CNA_STUDENT_FILTER_PARAMS.get('last_name') or
           data.get('first_name') != GMS_ST2_CNA_STUDENT_FILTER_PARAMS.get('first_name') or
           str(data.get('makeup_student')) != GMS_ST2_CNA_STUDENT_FILTER_PARAMS.get('makeup_student')):
            assert False


@then('the specific ST2 hhaStudents data will be returned as JSON response')
def specific_hhaStudents_JSON_data_response(context):
    response = context.response.data

    if len(response) == 0:
        assert False

    for indx, data in enumerate(response):
        if data.get('last_name') == GMS_ST2_HHA_STUDENT_FILTER_PARAMS.get('last_name') and \
           data.get('first_name') == GMS_ST2_HHA_STUDENT_FILTER_PARAMS.get('first_name') and \
           str(data.get('makeup_student')) == GMS_ST2_HHA_STUDENT_FILTER_PARAMS.get('makeup_student'):
            assert True
            break
        if indx == (len(response) - 1) and \
           (data.get('last_name') != GMS_ST2_HHA_STUDENT_FILTER_PARAMS.get('last_name') or
           data.get('first_name') != GMS_ST2_HHA_STUDENT_FILTER_PARAMS.get('first_name') or
           str(data.get('makeup_student')) != GMS_ST2_HHA_STUDENT_FILTER_PARAMS.get('makeup_student')):
            assert False


@then('the specific STI second hhaRotations data will be returned as JSON response')
def specific_second_hhaRotations_JSON_data_response(context):
    response = context.response.data

    if len(response) == 0:
        assert False

    for indx, data in enumerate(response):
        if data.get('end_date') == GMS_STI_HHA_ROTATION2_FILTER_PARAMS.get('end_date') and \
           data.get('start_date') == GMS_STI_HHA_ROTATION2_FILTER_PARAMS.get('start_date') and \
           data.get('rotation_num') == GMS_STI_HHA_ROTATION2_FILTER_PARAMS.get('rotation_num'):
            assert True
            break
        if indx == (len(response) - 1) and \
           (data.get('end_date') != GMS_STI_HHA_ROTATION2_FILTER_PARAMS.get('end_date') or
           data.get('start_date') != GMS_STI_HHA_ROTATION2_FILTER_PARAMS.get('start_date') or
           data.get('rotation_num') != GMS_STI_HHA_ROTATION2_FILTER_PARAMS.get('rotation_num')):
            assert False


@then('the specific STI second cnaRotations data will be returned as JSON response')
def specific_second_cnaRotations_JSON_data_response(context):
    response = context.response.data

    if len(response) == 0:
        assert False

    for indx, data in enumerate(response):
        if data.get('end_date') == GMS_STI_CNA_ROTATION2_FILTER_PARAMS.get('end_date') and \
           data.get('start_date') == GMS_STI_CNA_ROTATION2_FILTER_PARAMS.get('start_date') and \
           data.get('rotation_num') == GMS_STI_CNA_ROTATION2_FILTER_PARAMS.get('rotation_num'):
            assert True
            break
        if indx == (len(response) - 1) and \
           (data.get('end_date') != GMS_STI_CNA_ROTATION2_FILTER_PARAMS.get('end_date') or
           data.get('start_date') != GMS_STI_CNA_ROTATION2_FILTER_PARAMS.get('start_date') or
           data.get('rotation_num') != GMS_STI_CNA_ROTATION2_FILTER_PARAMS.get('rotation_num')):
            assert False


@then('the specific STI second cnaStudents data will be returned as JSON response')
def specific_second_cnaStudents_JSON_data_response(context):
    response = context.response.data

    if len(response) == 0:
        assert False

    for indx, data in enumerate(response):
        if data.get('last_name') == GMS_STI_CNA_STUDENT2_FILTER_PARAMS.get('last_name') and \
           data.get('first_name') == GMS_STI_CNA_STUDENT2_FILTER_PARAMS.get('first_name') and \
           str(data.get('makeup_student')) == GMS_STI_CNA_STUDENT2_FILTER_PARAMS.get('makeup_student'):
            assert True
            break
        if indx == (len(response) - 1) and \
           (data.get('last_name') != GMS_STI_CNA_STUDENT2_FILTER_PARAMS.get('last_name') or
           data.get('first_name') != GMS_STI_CNA_STUDENT2_FILTER_PARAMS.get('first_name') or
           str(data.get('makeup_student')) != GMS_STI_CNA_STUDENT2_FILTER_PARAMS.get('makeup_student')):
            assert False


@then('the specific STI second hhaStudents data will be returned as JSON response')
def specific_second_hhaStudents_JSON_data_response(context):
    response = context.response.data

    if len(response) == 0:
        assert False

    for indx, data in enumerate(response):
        if data.get('last_name') == GMS_STI_HHA_STUDENT2_FILTER_PARAMS.get('last_name') and \
           data.get('first_name') == GMS_STI_HHA_STUDENT2_FILTER_PARAMS.get('first_name') and \
           str(data.get('makeup_student')) == GMS_STI_HHA_STUDENT2_FILTER_PARAMS.get('makeup_student'):
            assert True
            break
        if indx == (len(response) - 1) and \
           (data.get('last_name') != GMS_STI_HHA_STUDENT2_FILTER_PARAMS.get('last_name') or
           data.get('first_name') != GMS_STI_HHA_STUDENT2_FILTER_PARAMS.get('first_name') or
           str(data.get('makeup_student')) != GMS_STI_HHA_STUDENT2_FILTER_PARAMS.get('makeup_student')):
            assert False


@then('the specific STI cnaTheoryRecords data will be returned as JSON response')
def specific_cnaTheoryRecords_JSON_data_response(context):
    response = context.response.data

    if len(response) == 0:
        assert False

    for indx, data in enumerate(response):
        if data.get('date') == GMS_STI_CNA_THEORYRECORD_FILTER_PARAMS.get('date') and \
           str(data.get('completed')) == GMS_STI_CNA_THEORYRECORD_FILTER_PARAMS.get('completed') and \
           data.get('topic') == GMS_STI_CNA_THEORYRECORD_FILTER_PARAMS.get('topic'):
            assert True
            break
        if indx == (len(response) - 1) and \
           (data.get('date') != GMS_STI_CNA_THEORYRECORD_FILTER_PARAMS.get('date') or
           str(data.get('completed')) != GMS_STI_CNA_THEORYRECORD_FILTER_PARAMS.get('completed') or
           data.get('topic') != GMS_STI_CNA_THEORYRECORD_FILTER_PARAMS.get('topic')):
            assert False


@then('the specific STI second cnaTheoryRecords data will be returned as JSON response')
def specific_second_cnaTheoryRecords_JSON_data_response(context):
    response = context.response.data

    if len(response) == 0:
        assert False

    for indx, data in enumerate(response):
        if data.get('date') == GMS_STI_CNA_THEORYRECORD2_FILTER_PARAMS.get('date') and \
           str(data.get('completed')) == GMS_STI_CNA_THEORYRECORD2_FILTER_PARAMS.get('completed') and \
           data.get('topic') == GMS_STI_CNA_THEORYRECORD2_FILTER_PARAMS.get('topic'):
            assert True
            break
        if indx == (len(response) - 1) and \
           (data.get('date') != GMS_STI_CNA_THEORYRECORD2_FILTER_PARAMS.get('date') or
           str(data.get('completed')) != GMS_STI_CNA_THEORYRECORD2_FILTER_PARAMS.get('completed') or
           data.get('topic') != GMS_STI_CNA_THEORYRECORD2_FILTER_PARAMS.get('topic')):
            assert False


@then('the specific ST2 cnaTheoryRecords data will be returned as JSON response')
def specific_cnaTheoryRecords_ST2_JSON_data_response(context):
    response = context.response.data

    if len(response) == 0:
        assert False

    for indx, data in enumerate(response):
        if data.get('date') == GMS_ST2_CNA_THEORYRECORD_FILTER_PARAMS.get('date') and \
           str(data.get('completed')) == GMS_ST2_CNA_THEORYRECORD_FILTER_PARAMS.get('completed') and \
           data.get('topic') == GMS_ST2_CNA_THEORYRECORD_FILTER_PARAMS.get('topic'):
            assert True
            break
        if indx == (len(response) - 1) and \
           (data.get('date') != GMS_ST2_CNA_THEORYRECORD_FILTER_PARAMS.get('date') or
           str(data.get('completed')) != GMS_ST2_CNA_THEORYRECORD_FILTER_PARAMS.get('completed') or
           data.get('topic') != GMS_ST2_CNA_THEORYRECORD_FILTER_PARAMS.get('topic')):
            assert False


@then('the specific STI hhaTheoryRecords data will be returned as JSON response')
def specific_hhaTheoryRecords_JSON_data_response(context):
    response = context.response.data

    if len(response) == 0:
        assert False

    for indx, data in enumerate(response):
        if data.get('date') == GMS_STI_HHA_THEORYRECORD_FILTER_PARAMS.get('date') and \
           str(data.get('completed')) == GMS_STI_HHA_THEORYRECORD_FILTER_PARAMS.get('completed') and \
           data.get('topic') == GMS_STI_HHA_THEORYRECORD_FILTER_PARAMS.get('topic'):
            assert True
            break
        if indx == (len(response) - 1) and \
           (data.get('date') != GMS_STI_HHA_THEORYRECORD_FILTER_PARAMS.get('date') or
           str(data.get('completed')) != GMS_STI_HHA_THEORYRECORD_FILTER_PARAMS.get('completed') or
           data.get('topic') != GMS_STI_HHA_THEORYRECORD_FILTER_PARAMS.get('topic')):
            assert False


@then('the specific STI second hhaTheoryRecords data will be returned as JSON response')
def specific_second_hhaTheoryRecords_JSON_data_response(context):
    response = context.response.data

    if len(response) == 0:
        assert False

    for indx, data in enumerate(response):
        if data.get('date') == GMS_STI_HHA_THEORYRECORD2_FILTER_PARAMS.get('date') and \
           str(data.get('completed')) == GMS_STI_HHA_THEORYRECORD2_FILTER_PARAMS.get('completed') and \
           data.get('topic') == GMS_STI_HHA_THEORYRECORD2_FILTER_PARAMS.get('topic'):
            assert True
            break
        if indx == (len(response) - 1) and \
           (data.get('date') != GMS_STI_HHA_THEORYRECORD2_FILTER_PARAMS.get('date') or
           str(data.get('completed')) != GMS_STI_HHA_THEORYRECORD2_FILTER_PARAMS.get('completed') or
           data.get('topic') != GMS_STI_HHA_THEORYRECORD2_FILTER_PARAMS.get('topic')):
            print('data: ', data.get('date'), data.get(
                'completed'), data.get('topic'))
            print('GMS_STI_HHA_THEORYRECORD2_FILTER_PARAMS: ', GMS_STI_HHA_THEORYRECORD2_FILTER_PARAMS.get(
                'date'), GMS_STI_HHA_THEORYRECORD2_FILTER_PARAMS.get('completed'), GMS_STI_HHA_THEORYRECORD2_FILTER_PARAMS.get('topic'))
            print('HELLO WORLD')
            assert False


@then('the specific ST2 hhaTheoryRecords data will be returned as JSON response')
def specific_hhaTheoryRecords_ST2_JSON_data_response(context):
    response = context.response.data

    if len(response) == 0:
        assert False

    for indx, data in enumerate(response):
        if data.get('date') == GMS_ST2_HHA_THEORYRECORD_FILTER_PARAMS.get('date') and \
           str(data.get('completed')) == GMS_ST2_HHA_THEORYRECORD_FILTER_PARAMS.get('completed') and \
           data.get('topic') == GMS_ST2_HHA_THEORYRECORD_FILTER_PARAMS.get('topic'):
            assert True
            break
        if indx == (len(response) - 1) and \
           (data.get('date') != GMS_ST2_HHA_THEORYRECORD_FILTER_PARAMS.get('date') or
           str(data.get('completed')) != GMS_ST2_HHA_THEORYRECORD_FILTER_PARAMS.get('completed') or
           data.get('topic') != GMS_ST2_HHA_THEORYRECORD_FILTER_PARAMS.get('topic')):
            assert False


@then('the specific STI cnaClinicalRecords data will be returned as JSON response')
def specific_cnaClinicalRecords_JSON_data_response(context):
    response = context.response.data

    if len(response) == 0:
        assert False

    for indx, data in enumerate(response):
        if data.get('date') == GMS_STI_CNA_CLINICALRECORD_FILTER_PARAMS.get('date') and \
           str(data.get('completed')) == GMS_STI_CNA_CLINICALRECORD_FILTER_PARAMS.get('completed') and \
           data.get('topic') == GMS_STI_CNA_CLINICALRECORD_FILTER_PARAMS.get('topic'):
            assert True
            break
        if indx == (len(response) - 1) and \
           (data.get('date') != GMS_STI_CNA_CLINICALRECORD_FILTER_PARAMS.get('date') or
           str(data.get('completed')) != GMS_STI_CNA_CLINICALRECORD_FILTER_PARAMS.get('completed') or
           data.get('topic') != GMS_STI_CNA_CLINICALRECORD_FILTER_PARAMS.get('topic')):
            assert False


@then('the specific STI second cnaClinicalRecords data will be returned as JSON response')
def specific_second_cnaClinicalRecords_JSON_data_response(context):
    response = context.response.data

    if len(response) == 0:
        assert False

    for indx, data in enumerate(response):
        if data.get('date') == GMS_STI_CNA_CLINICALRECORD2_FILTER_PARAMS.get('date') and \
           str(data.get('completed')) == GMS_STI_CNA_CLINICALRECORD2_FILTER_PARAMS.get('completed') and \
           data.get('topic') == GMS_STI_CNA_CLINICALRECORD2_FILTER_PARAMS.get('topic'):
            assert True
            break
        if indx == (len(response) - 1) and \
           (data.get('date') != GMS_STI_CNA_CLINICALRECORD2_FILTER_PARAMS.get('date') or
           str(data.get('completed')) != GMS_STI_CNA_CLINICALRECORD2_FILTER_PARAMS.get('completed') or
           data.get('topic') != GMS_STI_CNA_CLINICALRECORD2_FILTER_PARAMS.get('topic')):
            assert False


@then('the specific ST2 cnaClinicalRecords data will be returned as JSON response')
def specific_cnaClinicalRecords_ST2_JSON_data_response(context):
    response = context.response.data

    if len(response) == 0:
        assert False

    for indx, data in enumerate(response):
        if data.get('date') == GMS_ST2_CNA_CLINICALRECORD_FILTER_PARAMS.get('date') and \
           str(data.get('completed')) == GMS_ST2_CNA_CLINICALRECORD_FILTER_PARAMS.get('completed') and \
           data.get('topic') == GMS_ST2_CNA_CLINICALRECORD_FILTER_PARAMS.get('topic'):
            assert True
            break
        if indx == (len(response) - 1) and \
           (data.get('date') != GMS_ST2_CNA_CLINICALRECORD_FILTER_PARAMS.get('date') or
           str(data.get('completed')) != GMS_ST2_CNA_CLINICALRECORD_FILTER_PARAMS.get('completed') or
           data.get('topic') != GMS_ST2_CNA_CLINICALRECORD_FILTER_PARAMS.get('topic')):
            assert False


@then('the specific STI hhaClinicalRecords data will be returned as JSON response')
def specific_hhaClinicalRecords_JSON_data_response(context):
    response = context.response.data

    if len(response) == 0:
        assert False

    for indx, data in enumerate(response):

        if data.get('date') == GMS_STI_HHA_CLINICALRECORD_FILTER_PARAMS.get('date') and \
           str(data.get('completed')) == GMS_STI_HHA_CLINICALRECORD_FILTER_PARAMS.get('completed') and \
           data.get('topic') == GMS_STI_HHA_CLINICALRECORD_FILTER_PARAMS.get('topic'):
            assert True
            break
        if indx == (len(response) - 1) and \
           (data.get('date') != GMS_STI_HHA_CLINICALRECORD_FILTER_PARAMS.get('date') or
           str(data.get('completed')) != GMS_STI_HHA_CLINICALRECORD_FILTER_PARAMS.get('completed') or
           data.get('topic') != GMS_STI_HHA_CLINICALRECORD_FILTER_PARAMS.get('topic')):
            assert False


@then('the specific STI second hhaClinicalRecords data will be returned as JSON response')
def specific_second_hhaClinicalRecords_JSON_data_response(context):
    response = context.response.data

    if len(response) == 0:
        assert False

    for indx, data in enumerate(response):
        if data.get('date') == GMS_STI_HHA_CLINICALRECORD2_FILTER_PARAMS.get('date') and \
           str(data.get('completed')) == GMS_STI_HHA_CLINICALRECORD2_FILTER_PARAMS.get('completed') and \
           data.get('topic') == GMS_STI_HHA_CLINICALRECORD2_FILTER_PARAMS.get('topic'):
            assert True
            break
        if indx == (len(response) - 1) and \
           (data.get('date') != GMS_STI_HHA_CLINICALRECORD2_FILTER_PARAMS.get('date') or
           str(data.get('completed')) != GMS_STI_HHA_CLINICALRECORD2_FILTER_PARAMS.get('completed') or
           data.get('topic') != GMS_STI_HHA_CLINICALRECORD2_FILTER_PARAMS.get('topic')):

            assert False


@then('the specific ST2 hhaClinicalRecords data will be returned as JSON response')
def specific_hhaClinicalRecords_ST2_JSON_data_response(context):
    response = context.response.data

    if len(response) == 0:
        assert False

    for indx, data in enumerate(response):
        if (data.get('date') == GMS_ST2_HHA_CLINICALRECORD_FILTER_PARAMS.get('date') and
           str(data.get('completed')) == GMS_ST2_HHA_CLINICALRECORD_FILTER_PARAMS.get('completed') and
           data.get('topic') == GMS_ST2_HHA_CLINICALRECORD_FILTER_PARAMS.get('topic')):
            assert True
            break
        if indx == (len(response) - 1) and \
           (data.get('date') != GMS_ST2_HHA_CLINICALRECORD_FILTER_PARAMS.get('date') or
           str(data.get('completed')) != GMS_ST2_HHA_CLINICALRECORD_FILTER_PARAMS.get('completed') or
           data.get('topic') != GMS_ST2_HHA_CLINICALRECORD_FILTER_PARAMS.get('topic')):

            assert False


@then('no desired ST2 cnaStudents data will be returned as JSON response')
def no_specific_cnaStudents_ST2_JSON_data_response(context):
    response = context.response.data

    for data in response:
        if data.get('last_name') == GMS_ST2_CNA_STUDENT_FILTER_PARAMS.get('last_name') and \
           data.get('first_name') == GMS_ST2_CNA_STUDENT_FILTER_PARAMS.get('first_name') and \
           str(data.get('makeup_student')) == GMS_ST2_CNA_STUDENT_FILTER_PARAMS.get('makeup_student'):
            assert False

    assert True


@then('no desired second instructor cnaClinicalRecords data will be returned as JSON response')
def no_specific_second_cnaClinicalRecords_JSON_data_response(context):
    response = context.response.data

    for data in response:
        if data.get('date') == GMS_STI_CNA_CLINICALRECORD2_FILTER_PARAMS.get('date') and \
           str(data.get('completed')) == GMS_STI_CNA_CLINICALRECORD2_FILTER_PARAMS.get('completed') and \
           data.get('topic') == GMS_STI_CNA_CLINICALRECORD2_FILTER_PARAMS.get('topic'):
            assert False

    assert True


@then('no desired second instructor cnaTheoryRecords data filterd by completed will be returned as JSON response')
def no_specific_second_cnaTheoryRecords_JSON_data_response(context):
    response = context.response.data

    for data in response:
        if data.get('date') == GMS_STI_CNA_THEORYRECORD2_FILTER_PARAMS.get('date') and \
           str(data.get('completed')) == GMS_STI_CNA_THEORYRECORD2_FILTER_PARAMS.get('completed') and \
           data.get('topic') == GMS_STI_CNA_THEORYRECORD2_FILTER_PARAMS.get('topic'):
            assert False

    assert True


@then('no desired ST2 hhaClinicalRecords data filtered by topic will be returned as JSON response')
def no_specific_ST2_hhaClinicalRecords_JSON_data_response(context):
    response = context.response.data

    for data in response:
        if data.get('date') == GMS_ST2_HHA_CLINICALRECORD_FILTER_PARAMS.get('date') and \
           str(data.get('completed')) == GMS_ST2_HHA_CLINICALRECORD_FILTER_PARAMS.get('completed') and \
           data.get('topic') == GMS_ST2_HHA_CLINICALRECORD_FILTER_PARAMS.get('topic'):
            assert False

    assert True


@then('bad request since the email added does not belong to an active user')
def bad_request_due_to_bad_user_email_when_adding_access(context):
    context.test().assertEqual(context.response.status_code, 400)
    data = context.response.data
    print('DATA: ', data)
    if 'you are trying to add for access doesn\'t exist.' in data.get('non_field_errors')[0]:
        assert True
    else:
        assert False


# CMS specific thens
@then('database will create the client record')
def database_will_create_client(context):
    response = context.response.data

    posted_email = CMS_STI_CLIENT_SAMPLE_POST.get('email')

    context.test().assertEqual(response.get('email'), posted_email)

    Client = apps.get_model('cms', 'Client')

    if not Client.objects.filter(
            email__exact=posted_email).exists():
        assert False
    else:
        Client.objects.filter(
            email__exact=posted_email).delete()


@then('database will create the note record')
def database_will_create_note(context):
    response = context.response.data

    posted_content = CMS_STI_NOTE_SAMPLE_POST.get('content')

    context.test().assertEqual(response.get('content'), posted_content)

    Note = apps.get_model('cms', 'Note')

    if not Note.objects.filter(
            content__exact=posted_content).exists():
        assert False
    else:
        Note.objects.filter(
            content__exact=posted_content).delete()


@then('database will create the ST2 client record')
def database_will_create_ST2_client(context):
    response = context.response.data

    posted_email = CMS_ST2_CLIENT_SAMPLE_POST.get('email')

    context.test().assertEqual(response.get('email'), posted_email)

    Client = apps.get_model('cms', 'Client')

    if not Client.objects.filter(
            email__exact=posted_email).exists():
        assert False
    else:
        Client.objects.filter(
            email__exact=posted_email).delete()


@then('database will create the ST2 note record')
def database_will_create_ST2_note(context):
    response = context.response.data

    posted_content = CMS_ST2_NOTE_SAMPLE_POST.get('content')

    context.test().assertEqual(response.get('content'), posted_content)

    Note = apps.get_model('cms', 'Note')

    if not Note.objects.filter(
            content__exact=posted_content).exists():
        assert False
    else:
        Note.objects.filter(
            content__exact=posted_content).delete()


@then('database will fully update the client record')
def database_will_edit_client(context):
    response_data = context.response.data

    editted_client_email = CMS_STI_CLIENT_SAMPLE_PUT.get(
        'email')

    context.test().assertEqual(response_data.get(
        'email'), editted_client_email)

    Client = apps.get_model('cms', 'Client')
    if not Client.objects.filter(
            email__exact=editted_client_email).exists():
        assert False


@then('database will fully update the note record')
def database_will_edit_client(context):
    response_data = context.response.data

    editted_note_content = CMS_STI_NOTE_SAMPLE_PUT.get(
        'content')

    context.test().assertEqual(response_data.get(
        'content'), editted_note_content)

    Note = apps.get_model('cms', 'Note')
    if not Note.objects.filter(
            content__exact=editted_note_content).exists():
        assert False


@then('database will fully update the second client record')
def database_will_edit_second_client(context):
    response_data = context.response.data

    editted_client_email = CMS_SECOND_CLIENT_PUT.get(
        'email')

    context.test().assertEqual(response_data.get(
        'email'), editted_client_email)

    Client = apps.get_model('cms', 'Client')
    if not Client.objects.filter(
            email__exact=editted_client_email).exists():
        assert False


@then('database will fully update the second note record')
def database_will_edit_note(context):
    response_data = context.response.data

    editted_note_content = CMS_SECOND_NOTE_PUT.get(
        'content')

    context.test().assertEqual(response_data.get(
        'content'), editted_note_content)

    Note = apps.get_model('cms', 'Note')
    if not Note.objects.filter(
            content__exact=editted_note_content).exists():
        assert False


@then('database will fully update the ST2 client record')
def database_will_edit_ST2_client(context):
    response_data = context.response.data

    editted_client_email = CMS_ST2_CLIENT_SAMPLE_PUT.get(
        'email')

    context.test().assertEqual(response_data.get(
        'email'), editted_client_email)

    Client = apps.get_model('cms', 'Client')
    if not Client.objects.filter(
            email__exact=editted_client_email).exists():
        assert False


@then('database will fully update the ST2 note record')
def database_will_edit_ST2_note(context):
    response_data = context.response.data

    editted_note_content = CMS_ST2_NOTE_SAMPLE_PUT.get(
        'content')

    context.test().assertEqual(response_data.get(
        'content'), editted_note_content)

    Note = apps.get_model('cms', 'Note')
    if not Note.objects.filter(
            content__exact=editted_note_content).exists():
        assert False


@then('database will partially update the client record')
def database_will_partially_edit_client(context):
    response = context.response.data

    editted_first_name = CMS_STI_CLIENT_PATCH.get('first_name')

    context.test().assertEqual(response.get('first_name'), editted_first_name)

    Client = apps.get_model('cms', 'Client')
    if not Client.objects.filter(
            first_name__exact=editted_first_name).exists():
        assert False


@then('database will partially update the note record')
def database_will_partially_edit_note(context):
    response_data = context.response.data

    editted_price = CMS_STI_NOTE_PATCH.get(
        'price')

    context.test().assertEqual(response_data.get(
        'price'), editted_price)

    Note = apps.get_model('cms', 'Note')
    if not Note.objects.filter(
            price__exact=editted_price).exists():
        assert False


@then('database will partially update the second client record')
def database_will_partially_update_second_client(context):
    response = context.response.data

    editted_first_name = CMS_SECOND_CLIENT_PATCH.get('first_name')

    context.test().assertEqual(response.get('first_name'), editted_first_name)

    Client = apps.get_model('cms', 'Client')
    if not Client.objects.filter(
            first_name__exact=editted_first_name).exists():
        assert False


@then('database will partially update the second note record')
def database_will_partially_update_second_note(context):
    response_data = context.response.data

    editted_price = CMS_SECOND_NOTE_PATCH.get(
        'price')

    context.test().assertEqual(response_data.get(
        'price'), editted_price)

    Note = apps.get_model('cms', 'Note')
    if not Note.objects.filter(
            price__exact=editted_price).exists():
        assert False


@then('database will partially update the ST2 client record')
def database_will_partially_update_ST2_client(context):
    response = context.response.data

    editted_first_name = CMS_ST2_CLIENT_PATCH.get('first_name')

    context.test().assertEqual(response.get('first_name'), editted_first_name)

    Client = apps.get_model('cms', 'Client')
    if not Client.objects.filter(
            first_name__exact=editted_first_name).exists():
        assert False


@then('database will partially update the ST2 note record')
def database_will_partially_update_ST2_note(context):
    response_data = context.response.data

    editted_price = CMS_ST2_NOTE_PATCH.get(
        'price')

    context.test().assertEqual(response_data.get(
        'price'), editted_price)

    Note = apps.get_model('cms', 'Note')
    if not Note.objects.filter(
            price__exact=editted_price).exists():
        assert False


@then('database will delete the client record')
def database_will_delete_client(context):
    context.test().assertEqual(context.response.data, JSON_OBJ_NOT_FOUND_RES)

    Client = apps.get_model('cms', 'Client')
    if Client.objects.filter(pk__exact=context.uuid).exists():
        assert False


@then('database will delete the note record')
def database_will_delete_note(context):
    context.test().assertEqual(context.response.data, JSON_OBJ_NOT_FOUND_RES)

    Note = apps.get_model('cms', 'Note')
    if Note.objects.filter(pk__exact=context.uuid).exists():
        assert False


@then('database will delete the second client record')
def databaew_will_delete_second_client(context):
    context.test().assertEqual(context.response.data, JSON_OBJ_NOT_FOUND_RES)

    Client = apps.get_model('cms', 'Client')
    if Client.objects.filter(pk__exact=context.uuid).exists():
        assert False


@then('database will delete the second note record')
def database_will_delete_second_note(context):
    context.test().assertEqual(context.response.data, JSON_OBJ_NOT_FOUND_RES)

    Note = apps.get_model('cms', 'Note')
    if Note.objects.filter(pk__exact=context.uuid).exists():
        assert False


@then('database will delete the ST2 client record')
def database_will_delete_ST2_client(context):
    context.test().assertEqual(context.response.data, JSON_OBJ_NOT_FOUND_RES)

    Client = apps.get_model('cms', 'Client')
    if Client.objects.filter(pk__exact=context.uuid).exists():
        assert False


@then('database will delete the ST2 note record')
def database_will_delete_ST2_note(context):
    context.test().assertEqual(context.response.data, JSON_OBJ_NOT_FOUND_RES)

    Note = apps.get_model('cms', 'Note')
    if Note.objects.filter(pk__exact=context.uuid).exists():
        assert False


@then('the specific clients data will be returned as JSON response')
def specific_client_data_JSON_response(context):
    response = context.response.data
    if len(response) == 0:
        assert False

    for indx, data in enumerate(response):
        if data.get('first_name') == CMS_CLIENT_FILTER_PARAMS.get('first_name') and \
           data.get('last_name') == CMS_CLIENT_FILTER_PARAMS.get('last_name') and \
           data.get('email') == CMS_CLIENT_FILTER_PARAMS.get('email') and \
           data.get('city') == CMS_CLIENT_FILTER_PARAMS.get('city') and \
           data.get('success') == CMS_CLIENT_FILTER_PARAMS.get('success') and \
           data.get('initial_contact') == CMS_CLIENT_FILTER_PARAMS.get('initial_contact') and \
           data.get('phone_number') == CMS_CLIENT_FILTER_PARAMS.get('phone_number'):
            assert True
            break

        if indx == (len(response) - 1) and \
           (data.get('first_name') != CMS_CLIENT_FILTER_PARAMS.get('first_name') or
           data.get('last_name') != CMS_CLIENT_FILTER_PARAMS.get('last_name') or
           data.get('email') != CMS_CLIENT_FILTER_PARAMS.get('email') or
           data.get('city') != CMS_CLIENT_FILTER_PARAMS.get('city') or
           data.get('success') != CMS_CLIENT_FILTER_PARAMS.get('success') or
           data.get('initial_contact') != CMS_CLIENT_FILTER_PARAMS.get('initial_contact') or
           data.get('phone_number') != CMS_CLIENT_FILTER_PARAMS.get('phone_number')):
            assert False


@then('the specific notes data will be returned as JSON response')
def specific_note_data_JSON_response(context):
    response = context.response.data
    if len(response) == 0:
        assert False

    for indx, data in enumerate(response):
        if data.get('date') == CMS_NOTE_FILTER_PARAMS.get('date') and \
           data.get('content') == CMS_NOTE_FILTER_PARAMS.get('content'):
            assert True
            break

        if indx == (len(response) - 1) and \
           (data.get('date') != CMS_NOTE_FILTER_PARAMS.get('date') or
           data.get('content') != CMS_NOTE_FILTER_PARAMS.get('content')):
            assert False


@then('the specific second clients data will be returned as JSON response')
def specific_second_client_data_JSON_response(context):
    response = context.response.data

    if len(response) == 0:
        assert False

    for indx, data in enumerate(response):
        if data.get('first_name') == CMS_SECOND_CLIENT_FILTER_PARAMS.get('first_name') and \
           data.get('last_name') == CMS_SECOND_CLIENT_FILTER_PARAMS.get('last_name') and \
           data.get('email') == CMS_SECOND_CLIENT_FILTER_PARAMS.get('email') and \
           data.get('city') == CMS_SECOND_CLIENT_FILTER_PARAMS.get('city') and \
           data.get('success') == CMS_SECOND_CLIENT_FILTER_PARAMS.get('success') and \
           data.get('initial_contact') == CMS_SECOND_CLIENT_FILTER_PARAMS.get('initial_contact') and \
           data.get('phone_number') == CMS_SECOND_CLIENT_FILTER_PARAMS.get('phone_number'):
            assert True
            break

        if indx == (len(response) - 1) and \
           (data.get('first_name') != CMS_SECOND_CLIENT_FILTER_PARAMS.get('first_name') or
           data.get('last_name') != CMS_SECOND_CLIENT_FILTER_PARAMS.get('last_name') or
           data.get('email') != CMS_SECOND_CLIENT_FILTER_PARAMS.get('email') or
           data.get('city') != CMS_SECOND_CLIENT_FILTER_PARAMS.get('city') or
           data.get('success') != CMS_SECOND_CLIENT_FILTER_PARAMS.get('success') or
           data.get('initial_contact') != CMS_SECOND_CLIENT_FILTER_PARAMS.get('initial_contact') or
           data.get('phone_number') != CMS_SECOND_CLIENT_FILTER_PARAMS.get('phone_number')):
            assert False


@then('the specific second notes data will be returned as JSON response')
def specific_note_data_JSON_response(context):
    response = context.response.data

    if len(response) == 0:
        assert False

    for indx, data in enumerate(response):
        if data.get('date') == CMS_SECOND_NOTE_FILTER_PARAMS.get('date') and \
           data.get('content') == CMS_SECOND_NOTE_FILTER_PARAMS.get('content'):
            assert True
            break

        if indx == (len(response) - 1) and \
           (data.get('date') != CMS_SECOND_NOTE_FILTER_PARAMS.get('date') or
           data.get('content') != CMS_SECOND_NOTE_FILTER_PARAMS.get('content')):
            assert False


@then('the specific ST2 clients data will be returned as JSON response')
def specific_second_client_data_JSON_response(context):
    response = context.response.data

    if len(response) == 0:
        assert False

    for indx, data in enumerate(response):
        if data.get('first_name') == CMS_ST2_CLIENT_FILTER_PARAMS.get('first_name') and \
           data.get('last_name') == CMS_ST2_CLIENT_FILTER_PARAMS.get('last_name') and \
           data.get('email') == CMS_ST2_CLIENT_FILTER_PARAMS.get('email') and \
           data.get('city') == CMS_ST2_CLIENT_FILTER_PARAMS.get('city') and \
           data.get('success') == CMS_ST2_CLIENT_FILTER_PARAMS.get('success') and \
           data.get('initial_contact') == CMS_ST2_CLIENT_FILTER_PARAMS.get('initial_contact') and \
           data.get('phone_number') == CMS_ST2_CLIENT_FILTER_PARAMS.get('phone_number'):
            assert True
            break

        if indx == (len(response) - 1) and \
           (data.get('first_name') != CMS_ST2_CLIENT_FILTER_PARAMS.get('first_name') or
           data.get('last_name') != CMS_ST2_CLIENT_FILTER_PARAMS.get('last_name') or
           data.get('email') != CMS_ST2_CLIENT_FILTER_PARAMS.get('email') or
           data.get('city') != CMS_ST2_CLIENT_FILTER_PARAMS.get('city') or
           data.get('success') != CMS_ST2_CLIENT_FILTER_PARAMS.get('success') or
           data.get('initial_contact') != CMS_ST2_CLIENT_FILTER_PARAMS.get('initial_contact') or
           data.get('phone_number') != CMS_ST2_CLIENT_FILTER_PARAMS.get('phone_number')):
            assert False


@then('the specific ST2 notes data will be returned as JSON response')
def specific_note_data_JSON_response(context):
    response = context.response.data

    if len(response) == 0:
        assert False

    for indx, data in enumerate(response):
        if data.get('date') == CMS_ST2_NOTE_FILTER_PARAMS.get('date') and \
           data.get('content') == CMS_ST2_NOTE_FILTER_PARAMS.get('content'):
            assert True
            break

        if indx == (len(response) - 1) and \
           (data.get('date') != CMS_ST2_NOTE_FILTER_PARAMS.get('date') or
           data.get('content') != CMS_ST2_NOTE_FILTER_PARAMS.get('content')):
            assert False
