from behave import then

from constants import (GMS_CNA_ROTATION_POST_SAMPLE_DATA,
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
                        JSON_PERMISSION_DENIED_RES,
                        JSON_OBJ_NOT_FOUND_RES)


# from apps.gms.models import (CNARotation,
#                              HHARotation,
#                              CNAStudent,
#                              HHAStudent,
#                              CNATheoryRecord,
#                              HHATheoryRecord,
#                              CNAClinicalRecord,
#                              HHAClinicalRecord)


from django.apps import apps
# CNARotation = apps.get_model('gms', 'CNARotation')
# HHARotation = apps.get_model('gms', 'HHARotation')
# CNAStudent = apps.get_model('gms', 'CNAStudent')
# HHAStudent = apps.get_model('gms', 'HHAStudent')
# CNATheoryRecord = apps.get_model('gms', 'CNATheoryRecord')
# HHATheoryRecord = apps.get_model('gms', 'HHATheoryRecord')
# CNAClinicalRecord = apps.get_model('gms', 'CNAClinicalRecord')
# HHAClinicalRecord = apps.get_model('gms', 'HHAClinicalRecord')
# NOTE: should we also test with database? how would that work with behave? see below?


@then('database will create the cna rotation record')
def database_create_cnaRotation_record(context):
    response_data = context.response.data

    posted_rotation_start_date = GMS_CNA_ROTATION_POST_SAMPLE_DATA.get(
        'start_date')

    context.test().assertEqual(response_data.get(
        'start_date'), posted_rotation_start_date)

    CNARotation = apps.get_model('gms', 'CNARotation')

    if not CNARotation.objects.filter(
            start_date__exact=posted_rotation_start_date).exist():
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


@then('database will create the cna theory record')
def database_create_cnaTheory_record(context):
    response_data = context.response.data

    posted_cnaTheory_hrs_spent = GMS_CNA_THEORY_RECORD_POST_SAMPLE_DATA.get(
        'hours_spent')

    context.test().assertEqual(response_data.data.get(
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


@then('database will create the hha rotation record')
def database_create_hhaRotation_record(context):
    response_data = context.response.data

    posted_rotation_start_date = GMS_HHA_ROTATION_POST_SAMPLE_DATA.get(
        'start_date')

    context.test().assertEqual(response_data.get(
        'start_date'), posted_rotation_start_date)

    HHARotation = apps.get_model('gms', 'HHARotation')

    if not HHARotation.objects.filter(
            start_date__exact=posted_rotation_start_date).exist():
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


@then('database will create the hha theory record')
def database_create_hhaTheory_record(context):
    response_data = context.response.data

    posted_hhaTheory_hrs_spent = GMS_HHA_THEORY_RECORD_POST_SAMPLE_DATA.get(
        'hours_spent')

    context.test().assertEqual(response_data.data.get(
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


@then('database will not create the cna rotation record')
def database_no_create_cnaRotation_record(context):
    response_data = context.response.data

    posted_rotation_start_date = GMS_CNA_ROTATION_POST_SAMPLE_DATA.get(
        'start_date')

    context.test().assertNotEqual(response_data.get(
        'start_date'), posted_rotation_start_date)

    CNARotation = apps.get_model('gms', 'CNARotation')

    if CNARotation.objects.filter(
            start_date__exact=posted_rotation_start_date).exist():
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

    context.test().assertNotEqual(response_data.data.get(
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
            start_date__exact=posted_rotation_start_date).exist():
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

    context.test().assertNotEqual(response_data.data.get(
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
            start_date__exact=editted_rotation_start_date).exist():
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


@then('database will fully update the cna theory record')
def database_edit_cnaTheory_record(context):
    response_data = context.response.data

    editted_cnaTheory_hrs_spent = GMS_CNA_THEORY_RECORD_PUT_SAMPLE_DATA.get(
        'hours_spent')

    context.test().assertEqual(response_data.data.get(
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


@then('database will fully update the hha rotation record')
def database_edit_hhaRotation_record(context):
    response_data = context.response.data

    editted_rotation_start_date = GMS_HHA_ROTATION_PUT_SAMPLE_DATA.get(
        'start_date')

    context.test().assertEqual(response_data.get(
        'start_date'), editted_rotation_start_date)

    HHARotation = apps.get_model('gms', 'HHARotation')
    if not HHARotation.objects.filter(
            start_date__exact=editted_rotation_start_date).exist():
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


@then('database will fully update the hha theory record')
def database_edit_hhaTheory_record(context):
    response_data = context.response.data

    editted_hhaTheory_hrs_spent = GMS_HHA_THEORY_RECORD_PUT_SAMPLE_DATA.get(
        'hours_spent')

    context.test().assertEqual(response_data.data.get(
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


@then('database will not fully update the cna rotation record')
def database_no_edit_cnaRotation_record(context):
    context.test().assertEqual(context.response.data, JSON_PERMISSION_DENIED_RES)


@then('database will not fully update the cna student record')
def database_no_edit_cnaStudent_record(context):
    context.test().assertEqual(context.response.data, JSON_PERMISSION_DENIED_RES)


@then('database will not fully update the cna theory record')
def database_no_edit_cnaTheory_record(context):
    context.test().assertEqual(context.response.data, JSON_PERMISSION_DENIED_RES)


@then('database will not fully update the cna clinical record')
def database_no_edit_cnaClinical_record(context):
    context.test().assertEqual(context.response.data, JSON_PERMISSION_DENIED_RES)


@then('database will not fully update the hha rotation record')
def database_no_edit_hhaRotation_record(context):
    context.test().assertEqual(context.response.data, JSON_PERMISSION_DENIED_RES)


@then('database will not fully update the hha student record')
def database_no_edit_hhaStudent_record(context):
    context.test().assertEqual(context.response.data, JSON_PERMISSION_DENIED_RES)


@then('database will not fully update the hha theory record')
def database_no_edit_hhaTheory_record(context):
    context.test().assertEqual(context.response.data, JSON_PERMISSION_DENIED_RES)


@then('database will not fully update the hha clinical record')
def database_no_edit_hhaClinical_record(context):
    context.test().assertEqual(context.response.data, JSON_PERMISSION_DENIED_RES)


@then('database will partially update the cna rotation record')
def database_partially_edit_cnaRotation_record(context):
    response_data = context.response.data

    partially_editted_rotation_start_date = GMS_CNA_ROTATION_PATCH_SAMPLE_DATA.get(
        'start_date')

    context.test().assertEqual(response_data.get(
        'start_date'), partially_editted_rotation_start_date)

    CNARotation = apps.get_model('gms', 'CNARotation')
    if not CNARotation.objects.filter(
            start_date__exact=partially_editted_rotation_start_date).exist():
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


@then('database will partially update the cna theory record')
def database_partially_edit_cnaTheory_record(context):
    response_data = context.response.data

    partially_editted_cnaTheory_hrs_spent = GMS_CNA_THEORY_RECORD_PATCH_SAMPLE_DATA.get(
        'hours_spent')

    context.test().assertEqual(response_data.data.get(
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


@then('database will partially update the hha rotation record')
def database_partially_edit_hhaRotation_record(context):
    response_data = context.response.data

    partially_editted_rotation_start_date = GMS_HHA_ROTATION_PATCH_SAMPLE_DATA.get(
        'start_date')

    context.test().assertEqual(response_data.get(
        'start_date'), partially_editted_rotation_start_date)

    HHARotation = apps.get_model('gms', 'HHARotation')
    if not HHARotation.objects.filter(
            start_date__exact=partially_editted_rotation_start_date).exist():
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


@then('database will partially update the hha theory record')
def database_partially_edit_hhaTheory_record(context):
    response_data = context.response.data

    partially_editted_hhaTheory_hrs_spent = GMS_HHA_THEORY_RECORD_PATCH_SAMPLE_DATA.get(
        'hours_spent')

    context.test().assertEqual(response_data.data.get(
        'hours_spent'), partially_editted_hhaTheory_hrs_spent)

    HHATheoryRecord = apps.get_model('gms', 'HHATheoryRecord')
    if not HHATheoryRecord.objects.filter(
            hours_spent__exact=partially_editted_hhaTheory_hrs_spent).exists():
        assert False


@then('database will partially update the hha clinical record')
def database_partially_edit_hhaClinical_record(context):
    response_data = context.response.data

    partially_editted_hhaClinical_date = GMS_HHA_CLINICAL_RECORD_PATCH_SAMPLE_DATA.get(
        'date')

    context.test().assertEqual(response_data.get(
        'date'), partially_editted_hhaClinical_date)

    HHAClinicalRecord = apps.get_model('gms', 'HHAClinicalRecord')
    if not HHAClinicalRecord.objects.filter(
            date__exact=partially_editted_hhaClinical_date).exists():
        assert False


@then('database will not partially update the cna rotation record')
def database_no_partially_edit_cnaRotation_record(context):
    context.test().assertEqual(context.response.data, JSON_PERMISSION_DENIED_RES)


@then('database will not partially update the cna student record')
def database_no_partially_edit_cnaStudent_record(context):
    context.test().assertEqual(context.response.data, JSON_PERMISSION_DENIED_RES)


@then('database will not partially update the cna theory record')
def database_no_partially_edit_cnaTheory_record(context):
    context.test().assertEqual(context.response.data, JSON_PERMISSION_DENIED_RES)


@then('database will not partially update the cna clinical record')
def database_no_partially_edit_cnaClinical_record(context):
    context.test().assertEqual(context.response.data, JSON_PERMISSION_DENIED_RES)


@then('database will not partially update the hha rotation record')
def database_no_partially_edit_hhaRotation_record(context):
    context.test().assertEqual(context.response.data, JSON_PERMISSION_DENIED_RES)


@then('database will not partially update the hha student record')
def database_no_partially_edit_hhaStudent_record(context):
    context.test().assertEqual(context.response.data, JSON_PERMISSION_DENIED_RES)


@then('database will not partially update the hha theory record')
def database_no_partially_edit_hhaTheory_record(context):
    context.test().assertEqual(context.response.data, JSON_PERMISSION_DENIED_RES)


@then('database will not partially update the hha clinical record')
def database_no_partially_edit_hhaClinical_record(context):
    context.test().assertEqual(context.response.data, JSON_PERMISSION_DENIED_RES)


@then('database will delete the cna rotation record')
def database_delete_cnaRotation_record(context):
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


@then('database will delete the cna theory record')
def database_delete_cnaTheory_record(context):
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


@then('database will delete the hha rotation record')
def database_delete_hhaRotation_record(context):
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


@then('database will delete the hha theory record')
def database_delete_hhaTheory_record(context):
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


@then('database will not delete the cna rotation record')
def database_no_delete_cnaRotation_record(context):
    context.test().assertEqual(context.response.data, JSON_PERMISSION_DENIED_RES)


@then('database will not delete the cna student record')
def database_no_delete_cnaStudent_record(context):
    context.test().assertEqual(context.response.data, JSON_PERMISSION_DENIED_RES)


@then('database will not delete the cna theory record')
def database_no_delete_cnaTheory_record(context):
    context.test().assertEqual(context.response.data, JSON_PERMISSION_DENIED_RES)


@then('database will not delete the cna clinical record')
def database_no_delete_cnaClinical_record(context):
    context.test().assertEqual(context.response.data, JSON_PERMISSION_DENIED_RES)


@then('database will not delete the hha rotation record')
def database_no_delete_hhaRotation_record(context):
    context.test().assertEqual(context.response.data, JSON_PERMISSION_DENIED_RES)


@then('database will not delete the hha student record')
def database_no_delete_hhaStudent_record(context):
    context.test().assertEqual(context.response.data, JSON_PERMISSION_DENIED_RES)


@then('database will not delete the hha theory record')
def database_no_delete_hhaTheory_record(context):
    context.test().assertEqual(context.response.data, JSON_PERMISSION_DENIED_RES)


@then('database will not delete the hha clinical record')
def database_no_delete_hhaClinical_record(context):
    context.test().assertEqual(context.response.data, JSON_PERMISSION_DENIED_RES)
