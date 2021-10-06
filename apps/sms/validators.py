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
        rot = Rotation.objects.filter(
            program__program_uuid=program_id, rotation_number=data.get('rotation_number'))

        # if there is a rotation already, raise error
        if len(rot) > 0:
            ExceptionHandler.raise_verror(err_msg)

        return data

    @staticmethod
    def ensure_program_name(data):
        err_msg = 'Your rotation\'s program name and your student course do not match.'

        rot_id = data.get('rotation')

        from .models import Rotation
        rot = Rotation.objects.get(rotation_uuid__exact=rot_id)

        program_name = rot.program.program_name

        if data.get('course') != program_name:
            ExceptionHandler.raise_verror(err_msg)

        return data
