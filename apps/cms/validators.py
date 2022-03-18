import re

from rest_framework.exceptions import ValidationError

from core.common import UserEmailValidator

class CMSValidator:

    @staticmethod
    def reference_does_not_change_on_updates(value, instance, reference):
        err_msg = 'This field is immutable once set.'

        if not instance:
            return value
        # note we may need to convert into str(UUID) if this complains
        if instance and str(getattr(instance, reference)) == str(value):
            return value

        raise ValidationError(err_msg)

    @staticmethod
    def no_special_chars_and_captialize_string(value):
        err_msg = 'Only limited special characters are allowed, please only enter alphanumeric characters and (, . #).'
        pattern = '[A-Za-z0-9,.#\s]{1,150}'

        if bool(re.match(pattern, value)):
            return value.strip().capitalize()
        else:
            raise ValidationError(err_msg)

    @staticmethod
    def phone_number_format_checker(value):
        err_msg = 'Please follow the following example format for the phone number: "+1-888-888-8888"'
        pattern = '^(\+[0-9]-)?[0-9]{3}-[0-9]{3}-[0-9]{4}$'

        if bool(re.match(pattern, value)): 
            return value
        else:
            raise ValidationError(err_msg)

    # validation used by Client model
    @staticmethod
    def ensure_same_school_name(data, request):
        err_msg = 'You may only work on your own school\'s resource, please try changing the school name.'
        request_user_school = request.user.school_name
        school_name = data.get('school_name')

        if request.user.is_superuser:
            return data
        elif request_user_school == school_name:
            return data
        else:
            raise ValidationError(err_msg)

    @staticmethod
    def client_final_validation(serializer, data):
        if data.get('recruit_emails'):
            data['recruit_emails'] = UserEmailValidator.user_email_checker(
                data.get('recruit_emails'), 'recruit_emails', serializer.instance, serializer.partial)

        return data