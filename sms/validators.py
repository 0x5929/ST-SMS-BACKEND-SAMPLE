import re
from .utils import ExceptionHelper

"""
    Note, these validators are called from the Serializer

"""


class SMSValidator:

    @staticmethod
    def reference_does_not_change_on_updates(value, instance, reference):
        err_msg = 'This field is immutable once set.'
        return value if str(getattr(instance, reference)) == str(value) else ExceptionHelper.raise_verror(err_msg)

    @staticmethod
    def no_special_chars_and_captialize_string(value):
        err_msg = 'Only limited special characters are allowed, please only enter alphanumeric characters and (, . #).'
        pattern = '[A-Za-z0-9,.#\s]{1,150}'

        return value.strip().capitalize() if bool(re.match(pattern, value)) else ExceptionHelper.raise_verror(err_msg)

    @staticmethod
    def phone_number_format_checker(value):
        err_msg = 'Please follow the following example format for the phone number: "888-888-8888"'
        pattern = '^[0-9]{3}-[0-9]{3}-[0-9]{4}$'

        return value if bool(re.match(pattern, value)) else ExceptionHelper.raise_verror(err_msg)

    @staticmethod
    def student_id_format_checker(value):
        err_msg = 'Please follow the following format for the student ID: "###-MMYY-FL"'
        pattern = '^[0-9]{1,3}-[0-9]{4}-[A-Z]{2}$'

        return value if bool(re.match(pattern, value)) else ExceptionHelper.raise_verror(err_msg)

    @staticmethod
    def final_obj_validation(data):
        # validate start and end date logic
        err_msg = 'Please make sure program end date is after the program start date.'

        return data if data['start_date'] < data['completion_date'] else ExceptionHelper.raise_verror(err_msg)
