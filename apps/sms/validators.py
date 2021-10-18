import re
import uuid
from .utils import ExceptionHandler

"""
    Note, these validators are called from the Serializer

"""


class SMSValidator:

    @staticmethod
    def reference_does_not_change_on_updates(value, instance, reference):
        err_msg = 'This field is immutable once set.'

        if not instance:
            return value
        # note we may need to convert into str(UUID) if this complains
        if instance and str(getattr(instance, reference)) == str(value):
            return value

        ExceptionHandler.raise_verror(err_msg)

    @staticmethod
    def no_special_chars_and_captialize_string(value):
        err_msg = 'Only limited special characters are allowed, please only enter alphanumeric characters and (, . #).'
        pattern = '[A-Za-z0-9,.#\s]{1,150}'

        return value.strip().capitalize() if bool(re.match(pattern, value)) else ExceptionHandler.raise_verror(err_msg)

    @staticmethod
    def phone_number_format_checker(value):
        err_msg = 'Please follow the following example format for the phone number: "+1-888-888-8888"'
        pattern = '^(\+[0-9]-)?[0-9]{3}-[0-9]{3}-[0-9]{4}$'

        return value if bool(re.match(pattern, value)) else ExceptionHandler.raise_verror(err_msg)

    @staticmethod
    def student_id_format_checker(value):
        err_msg = 'Please follow the following format for the student ID: "###-MMYY-FL"'
        pattern = '^[0-9]{1,3}-[0-9]{4}-[A-Z]{2}$'

        return value if bool(re.match(pattern, value)) else ExceptionHandler.raise_verror(err_msg)

    @staticmethod
    def date_validation(data):
        # validate start and end date logic
        err_msg = 'Please make sure program end date is after the program start date.'

        return data if data['start_date'] < data['completion_date'] else ExceptionHandler.raise_verror(err_msg)

    @staticmethod
    def ensure_unique_rot(data):
        err_msg = 'This rotation number already exist for this program, please try again with a different rotation number.'

        # grab program id from request data
        program_id = uuid.UUID(str(data.get('program')))

        # check if rotation's have one with the same number and program ID
        from .models import Rotation
        rot_exists = Rotation.objects.filter(
            program__program_uuid=program_id, rotation_number=data.get('rotation_number')).exists()

        # if there is a rotation already, raise error
        if rot_exists:
            ExceptionHandler.raise_verror(err_msg)

        return data

    @staticmethod
    def ensure_program_name(data):
        err_msg = 'Your rotation\'s program name and your student course do not match.'

        rot_id = data.get('rotation').rotation_uuid

        from .models import Rotation
        rot = Rotation.objects.get(rotation_uuid__exact=rot_id)

        program_name = rot.program.program_name

        if data.get('course') != program_name:
            ExceptionHandler.raise_verror(err_msg)

        return data

    @staticmethod
    def ensure_same_school(data, request):
        err_msg = 'You are adding a student record for the wrong school\'s program rotation, please add to your own school\'s program rotation'

        school_name = data.get('rotation').program.school.school_name

        if school_name != request.user.school_name:
            ExceptionHandler.raise_verror(err_msg)

        return data

    @staticmethod
    def ensure_no_dup_student_id(data, instance):
        err_msg = 'You are adding/updating a student ID that already exists, please try again.'

        school_name = data.get('rotation').program.school.school_name

        from .models import Student

        student_exists = Student.objects.filter(
            rotation__program__school__school_name__exact=school_name, student_id__exact=data.get('student_id')).exists()

        # if updating we should have exactly one student record, and if we are not changing the student ID,
        # then we can return data
        if instance and student_exists and data.get('student_id') == instance.get('student_id'):
            return data

        # if we are creating and there is exactly 0 student record with the student ID, return data
        elif not instance and not student_exists == 0:
            return data

        # all else, raise validation error
        else:
            ExceptionHandler.raise_verror(err_msg)

    @staticmethod
    def student_final_validation(data, request, instance):
        date_verified_data = SMSValidator.date_validation(data)

        program_validated_data = SMSValidator.ensure_program_name(
            date_verified_data)

        same_school_verified = SMSValidator.ensure_same_school(
            program_validated_data, request)

        return SMSValidator.ensure_no_dup_student_id(same_school_verified, instance)
