from behave import when


@when('request GET to /api/sms/schools')
def request_GET_to_schools(context):
    pass


@when('request GET to /api/sms/programs')
def request_GET_to_programs(context):
    pass


@when('request GET to /api/sms/rotations')
def request_GET_to_rotations(context):
    pass


@when('request GET to /api/sms/students')
def request_GET_to_students(context):
    pass


@when('request POST to /api/sms/students of the same school')
def request_POST_to_students_same_school(context):
    pass


@when('request POST to /api/sms/students to a program rotation of another school')
def request_POST_to_students_diff_school(context):
    pass


@when('request PUT to /api/sms/students/student_uuid')
def request_PUT_to_student(context):
    pass


@when('request PATCH to /api/sms/students/student_uuid')
def request_PATCH_to_student(context):
    pass


@when('request DELETE to /api/sms/students/student_uuid')
def request_DELETE_to_student(context):
    pass


@when('request POST to /api/sms/schools')
def request_POST_to_schools(context):
    pass


@when('request PUT to /api/sms/schools/school_uuid')
def request_PUT_to_school(context):
    pass


@when('request PATCH to /api/sms/schools/school_uuid')
def request_PATCH_to_school(context):
    pass


@when('request DELETE to /api/sms/schools/school_uuid')
def request_DEL_to_school(context):
    pass


@when('request POST to /api/sms/programs')
def request_POST_to_programs(context):
    pass


@when('request PUT to /api/sms/programs/program_uuid')
def request_PUT_to_program(context):
    pass


@when('request PATCH to /api/sms/programs/program_uuid')
def request_PATCH_to_program(context):
    pass


@when('request DELETE to /api/sms/programs/program_uuid')
def request_DEL_to_program(context):
    pass


@when('request POST to /api/sms/rotations')
def request_POST_to_rotations(context):
    pass


@when('request PUT to /api/sms/rotations/rotation_uuid')
def request_PUT_to_rotaiton(context):
    pass


@when('request PATCH to /api/sms/rotations/rotation_uuid')
def request_PATCH_to_rotation(context):
    pass


@when('request DELETE to /api/sms/rotations/rotation_uuid')
def request_DEL_to_rotations(context):
    pass


@when('request GET to /api/sms/students with filters by school name')
def request_GET_by_school_name(context):
    pass


@when('request GET to /api/sms/students with filters by program name')
def request_GET_by_program_name(context):
    pass


@when('request GET to /api/sms/students with filters by rotation number')
def request_GET_by_rot_num(context):
    pass


@when('request GET to /api/sms/students with filters by student first name')
def request_GET_by_first_name(context):
    pass


@when('request GET to /api/sms/students with filters by student last name')
def request_GET_by_last_name(context):
    pass


@when('request GET to /api/sms/students with filters by student email')
def request_GET_by_email(context):
    pass


@when('request GET to /api/sms/students with filters by student phone number')
def request_GET_by_phone(context):
    pass


@when('request GET to /api/sms/students with filters by student ID')
def request_GET_by_ID(context):
    pass


@when('request GET to /api/sms/students with filters by student program start date')
def request_GET_by_program_start(context):
    pass


@when('request GET to /api/sms/students with filters by student program end date')
def request_GET_by_program_end(context):
    pass


@when('request GET to /api/sms/students with filters by student payment completions')
def request_GET_by_payment(context):
    pass


@when('request GET to /api/sms/students with filters by student program completions')
def request_GET_by_completion(context):
    pass


@when('request GET to /api/sms/students with filters by student employment status')
def request_GET_by_employment(context):
    pass
