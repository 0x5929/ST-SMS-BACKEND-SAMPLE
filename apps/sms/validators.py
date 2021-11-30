import re

from rest_framework.exceptions import ValidationError
from django.apps import apps

"""
    Note, these validators are called from the Serializer

"""


class SMSValidator:

    @classmethod
    def student_final_validation(cls, serializer, data):
        request = serializer.context.get('request')

        partial = serializer.partial

        date_verified_data = cls.date_validation(data, partial)

        program_validated_data = cls.ensure_program_name(
            date_verified_data, partial)

        return cls.ensure_same_school(program_validated_data, request, 'student', partial)

    @classmethod
    def rotation_final_validation(cls, serializer, data):
        request = serializer.context.get('request')
        partial = serializer.partial

        same_school_verified = cls.ensure_same_school(
            data, request, 'rotation', partial)
        return cls.ensure_unique_rot(same_school_verified, serializer.partial, serializer.instance)

    @classmethod
    def program_final_validation(cls, serializer, data):
        request = serializer.context.get('request')
        partial = serializer.partial

        return cls.ensure_same_school(data, request, 'program', partial)

    @staticmethod
    def reference_does_not_change_on_updates(value, instance, reference):
        err_msg = 'This field is immutable once set.'

        if not instance:
            return value
        
        if reference == 'program' and str(getattr(instance, reference).program_uuid) == str(value):
                return value
        elif reference == 'school' and str(getattr(instance, reference).school_uuid) == str(value):
                return value      
        else:
            raise ValidationError(err_msg)

    @staticmethod
    def no_special_chars_and_captialize_string(value, capitalize=False):
        err_msg = 'Only limited special characters are allowed, please only enter alphanumeric characters and (.#*,. ).'
        pattern = '[^A-Za-z0-9#*,.\s-]{1,150}'

        if not re.match(pattern, value) and capitalize:
            return value.strip().capitalize()
        elif not re.match(pattern, value) and not capitalize:
            return value.strip()
        else:
            raise ValidationError(err_msg)

    @staticmethod
    def phone_number_format_checker(value):
        err_msg = 'Please follow the following example format for the phone number: "+1-888-888-8888"'
        pattern = '^(\+[0-9]-)?[0-9]{3}-[0-9]{3}-[0-9]{4}$'

        if re.match(pattern, value):
            return value
        else:
            raise ValidationError(err_msg)

    @staticmethod
    def student_id_format_checker(value):
        err_msg = 'Please follow the following format for the student ID: "RO-(CNA|HHA|SG|ESOL)-###-MMYY-FL"'
        pattern = '^(RO|AL)-(CNA|HHA|SG|ESOL)-[0-9]{1,3}-[0-9]{4}-[A-Z]{2}$'

        if re.match(pattern, value):
            return value
        else:
            raise ValidationError(err_msg)

    @staticmethod
    def date_validation(data, partial=False):
        # validate start and end date logic
        date_err_msg = 'Please make sure program end date is after the program start date.'
        update_err_msg = 'Cannot update start date or completion date without the other.'

        if partial:
            if not data.get('start_date') and not data.get('completion_date'):
                return data

            elif not data.get('start_date') or not data.get('completion_date'):
                raise ValidationError(update_err_msg)

            elif data.get('start_date') and data.get('completion_date'):
                pass

        if data.get('start_date') and data.get('completion_date'):

            if data.get('start_date') < data.get('completion_date'):
                return data
            else:
                raise ValidationError(date_err_msg)
        else:
            # meaning either one of the dates are None
            return data

    @staticmethod
    def ensure_unique_rot(data, partial=False, instance=None):
        err_msg = 'This rotation number already exist for this program, please try again with a different rotation number.'

        if instance and not partial:
            # put
            program_uuid = getattr(instance, 'program').program_uuid

        elif instance and partial:
            program_uuid = getattr(instance, 'program').program_uuid

        # grab program id from request data
        else:
            program_uuid = data.get('program').program_uuid

        # check if rotation's have one with the same number and program ID
        Rotation = apps.get_model('sms', 'Rotation')
        rot_exists = Rotation.objects.filter(
            program__program_uuid=program_uuid, rotation_number=data.get('rotation_number')).exists()

        # if there is a rotation already, raise error
        if rot_exists:
            raise ValidationError(err_msg)

        return data

    @staticmethod
    def ensure_program_name(data, partial=False):
        err_msg = 'Your rotation\'s program name and your student course do not match.'
        update_err_msg = 'Cannot update course name without providing rotation.'

        if partial:
            if not data.get('course') and not data.get('rotation'):
                return data

            elif not data.get('course') and not data.get('rotation'):
                raise ValidationError(update_err_msg)

            elif data.get('course') and data.get('rotation'):
                pass

        rot_id = data.get('rotation').rotation_uuid

        from .models import Rotation
        rot = Rotation.objects.get(rotation_uuid__exact=rot_id)

        program_name = rot.program.program_name

        if data.get('course') != program_name:
            raise ValidationError(err_msg)

        return data

    @staticmethod
    def ensure_same_school(data, request, entry_pt, partial=False):
        err_msg = 'You are adding a student record for the wrong school\'s program rotation, please add to your own school\'s program rotation'

        if partial:
            return data

        if entry_pt == 'student':
            school_name = data.get('rotation').program.school.school_name
        elif entry_pt == 'rotation':
            school_name = data.get('program').school.school_name
        elif entry_pt == 'program':
            school_name = data.get('school').school_name

        if not request.user.is_superuser and school_name != request.user.school_name:

            raise ValidationError(err_msg)

        return data

    # used by .google_sheet

    @staticmethod
    def email_format_checker(value):
        err_msg = 'Invalid looking email, please ensure you enter a valid email.'

        if value.count('@') == 1 and value.count('.') >= 1:
            return value
        else:
            raise ValidationError(err_msg)
