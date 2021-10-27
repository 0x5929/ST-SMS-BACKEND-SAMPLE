import re
import uuid
from .utils import ExceptionHandler

"""
    Note, these validators are called from the Serializer

"""


class SMSValidator:


    @classmethod
    def student_final_validation(cls, serializer, data):
        request = serializer.context.get('request')
        #instance = serializer.instance
        partial = serializer.partial

        date_verified_data = cls.date_validation(data, partial)

        program_validated_data = cls.ensure_program_name(
            date_verified_data, partial)

        return cls.ensure_same_school(program_validated_data, request, partial)

        #return cls.ensure_no_dup_student_id(same_school_verified, instance, partial)

    @classmethod
    def rotation_final_validation(cls, serializer, data):
        return cls.ensure_unique_rot(data, serializer.partial)


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
        print('hello world')
        err_msg = 'Only limited special characters are allowed, please only enter alphanumeric characters and (, . #).'

        pattern = '[A-Za-z0-9,.#\s]{1,150}'
        return value.strip().capitalize() if re.match(pattern, value) else ExceptionHandler.raise_verror(err_msg)

    @staticmethod
    def phone_number_format_checker(value):
        err_msg = 'Please follow the following example format for the phone number: "+1-888-888-8888"'
        pattern = '^(\+[0-9]-)?[0-9]{3}-[0-9]{3}-[0-9]{4}$'

        return value if re.match(pattern, value) else ExceptionHandler.raise_verror(err_msg)

    @staticmethod
    def student_id_format_checker(value):
        err_msg = 'Please follow the following format for the student ID: "RO-(CNA|HHA|SG|ESOL)-###-MMYY-FL"'
        pattern = '^RO-(CNA|HHA|SG|ESOL)-[0-9]{1,3}-[0-9]{4}-[A-Z]{2}$'

        return value if re.match(pattern, value) else ExceptionHandler.raise_verror(err_msg)

    @staticmethod
    def date_validation(data, partial=False):
        # validate start and end date logic
        date_err_msg = 'Please make sure program end date is after the program start date.'
        update_err_msg = 'Cannot update start date or completion date without the other.'

        if partial:
            if not data.get('start_date') and not data.get('completion_date'):
                return data

            elif not data.get('start_date') or not data.get('completion_date'):
                return ExceptionHandler.raise_verror(update_err_msg)

            elif data.get('start_date') and data.get('completion_date'):
                pass
        
        return data if data.get('start_date') < data.get('completion_date') else ExceptionHandler.raise_verror(date_err_msg)




    @staticmethod
    def ensure_unique_rot(data, partial=False):
        err_msg = 'This rotation number already exist for this program, please try again with a different rotation number.'
        update_err_msg = 'Cannot update rotation number without providing program.'

        if partial:
            if not data.get('program') and not data.get('rotation_number'):
                return data

            elif not data.get('program') or not data.get('rotation_number'):
                return ExceptionHandler.raise_verror(update_err_msg)

            elif data.get('program') and data.get('rotation_number'):
                pass


        # grab program id from request data
        program_id = data.get('program').program_uuid

        # check if rotation's have one with the same number and program ID
        from .models import Rotation
        rot_exists = Rotation.objects.filter(
            program__program_uuid=program_id, rotation_number=data.get('rotation_number')).exists()

        # if there is a rotation already, raise error
        if rot_exists:
            ExceptionHandler.raise_verror(err_msg)

        return data

    @staticmethod
    def ensure_program_name(data, partial=False):
        err_msg = 'Your rotation\'s program name and your student course do not match.'
        update_err_msg = 'Cannot update course name without providing rotation.'


        if partial:
            if not data.get('course') and not data.get('rotation'):
                return data

            elif not data.get('course') and not data.get('rotation'):
                return ExceptionHandler.raise_verror(update_err_msg)

            elif data.get('course') and data.get('rotation'):
                pass


        rot_id = data.get('rotation').rotation_uuid

        from .models import Rotation
        rot = Rotation.objects.get(rotation_uuid__exact=rot_id)

        program_name = rot.program.program_name

        if data.get('course') != program_name:
            ExceptionHandler.raise_verror(err_msg)

        return data

    @staticmethod
    def ensure_same_school(data, request, partial=False):
        err_msg = 'You are adding a student record for the wrong school\'s program rotation, please add to your own school\'s program rotation'


        if partial and not data.get('rotation'):
            return data

        school_name = data.get('rotation').program.school.school_name


        if not request.user.is_superuser and school_name != request.user.school_name:

            ExceptionHandler.raise_verror(err_msg)

        return data




    # no need for this method since we are checking uniqueness at the database lvl, 
    # also student id is given a longer format, to distinguish between schools and programs
    # much lesser chance to duplicate any student IDs
    # @staticmethod
    # def ensure_no_dup_student_id(data, instance, partial=False):
    #     err_msg = 'You are adding/updating a student ID that already exists, please try again.'




    #     if partial and not data.get('student_id'):
    #         return data
    #     elif partial and data.get('student_id'):
    #         ExceptionHandler.raise_verror(
    #             'Please use PUT when updating student id')

    #     school_name = data.get('rotation').program.school.school_name

    #     from .models import Student

    #     student_exists = Student.objects.filter(
    #         rotation__program__school__school_name__exact=school_name, student_id__exact=data.get('student_id')).exists()

    #     # if updating we should have exactly one student record, and if we are not changing the student ID,
    #     # then we can return data
    #     if instance and student_exists and data.get('student_id') == getattr(instance, 'student_id'):
    #         return data

    #     # if we are creating and there is exactly 0 student record with the student ID, return data
    #     elif not instance and not student_exists == 0:
    #         return data

    #     # all else, raise validation error
    #     else:
    #         return ExceptionHandler.raise_verror(err_msg)

