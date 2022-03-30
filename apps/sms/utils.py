import re

from rest_framework.exceptions import ValidationError

from .validators import SMSValidator
from .constants import STUDENT_RECORD_HEADERS


class DataHandler:

    @classmethod
    def data_conversion(cls, model):
        data = {}

        for header in STUDENT_RECORD_HEADERS:
            if header == 'graduated' or \
                    header == 'passed_first_exam' or \
                    header == 'passed_second_or_third_exam' or \
                    header == 'employed':

                data[header] = cls.bool_conversion(model, header)

            elif header == 'start_date' or \
                    header == 'completion_date' or \
                    header == 'date_enrollment_agreement_signed':

                data[header] = cls.date_conversion(model, header)

            elif header == 'course_cost' or \
                    header == 'total_charges_charged' or \
                    header == 'total_charges_paid' or \
                    header == 'starting_wage':

                data[header] = cls.money_conversion(model, header)

            elif header == 'course':
                data[header] = cls.course_conversion(model, header)
            else:
                data[header] = str(getattr(model, header))

        return data

    @staticmethod
    def course_conversion(model, header):
        value = getattr(model, header)

        if value == 'CNA':
            return 'Nurse Assistant'
        elif value == 'HHA':
            return 'Home Health Aide'
        elif value == 'SG':
            return 'Security Guard'
        else:
            return value

    @staticmethod
    def bool_conversion(model, header):
        value = getattr(model, header)
        return 'Y' if value else ''

    @staticmethod
    def date_conversion(model, header):

        date_obj = getattr(model, header)
        return f'{str(date_obj.month)}/{str(date_obj.day)}/{str(date_obj.year)}'

    @staticmethod
    def money_conversion(model, header):

        money_obj = getattr(model, header)
        return f'${str(money_obj.amount)}' if money_obj else ''

    # NOTE data keys are assigned by each item inside STUDENT_RECORD_HEADERS,
    # by logic, as long as we dont change and or mess with the way data_conversion and clean_data,
    # order of dict is preserved by assignment by 3.6!

    @staticmethod
    def finalize_data(data):
        return [value for value in data.values()]

    @staticmethod
    def validate_student_id(value):
        new_key = 'student_id'
        err_msg = f'Invalid student ID format in google sheet data dump: {value}'

        try:
            validated_value = SMSValidator.student_id_format_checker(
                value.replace(' ', ''))
            return validated_value,  new_key

        except ValidationError:
            raise ValidationError(err_msg)
        except Exception as e:
            raise ValidationError(repr(e))

    @staticmethod
    def validate_string(value, key):
        old_key = key

        if value == 'N/A' or value == 'n/a':
            value = ''

        try:

            if old_key == 'Full Name':
                new_key = 'full_name'

            elif old_key == 'Last Name':
                new_key = 'last_name'
                validated_value = SMSValidator.no_special_chars_and_captialize_string(
                    value, capitalize=True)
                return validated_value, new_key

            elif old_key == 'First Name':
                new_key = 'first_name'
                validated_value = SMSValidator.no_special_chars_and_captialize_string(
                    value, capitalize=True)
                return validated_value, new_key

            elif old_key == 'Mailing Address':
                new_key = 'mailing_address'
            elif old_key == 'Third-party payer identifying information':
                new_key = 'third_party_payer_info'
                value = value[:10]

            elif old_key == 'Place of Employment':
                new_key = 'place_of_employment'
            elif old_key == 'Employment Address':
                new_key = 'employment_address'
            elif old_key == 'Position':
                new_key = 'position'
            elif old_key == 'Description of Attempts to Contact Students':
                new_key = 'description_of_attempts_to_contact_student'

            validated_value = SMSValidator.no_special_chars_and_captialize_string(
                value)

            return validated_value, new_key

        except:

            # note we are not raising errors,
            # if there is an error
            # return empty value, a little unforgiven but,
            # keeping it simple
            return '', new_key

    @staticmethod
    def validate_phone(value):
        new_key = 'phone_number'
        err_msg = f'Invalid phone number format in google sheet data dump: {value}'

        if value == '' or value == 'N/A' or value == 'n/a':
            return '', new_key

        # we care about phone numbers, if it is in an incorrect format, raise error
        # and have admin check
        try:
            validated_value = SMSValidator.phone_number_format_checker(value)

            return validated_value, new_key
        except ValidationError:
            raise ValidationError(err_msg)
        except Exception as e:
            raise ValidationError(repr(e))

    @staticmethod
    def validate_email(value):
        new_key = 'email'
        err_msg = f'Invalid email format in google sheet data dump: {value}'

        if value == '' or value == 'N/A' or value == 'n/a':
            return '', new_key

        # we care about emails, if it is in an incorrect format, raise error
        # and have admin check
        try:
            validated_value = SMSValidator.email_format_checker(value)

            return validated_value, new_key
        except ValidationError:
            raise ValidationError(err_msg)
        except Exception as e:
            raise ValidationError(repr(e))

    @staticmethod
    def validate_course(value):
        err_msg = f'Invalid course in google sheet data dump: {value}'
        new_key = 'course'

        if value.lower() in ['nurse', 'nurse assistant',
                             'cna', 'caregiver', 'care']:
            validated_value = 'CNA'
        elif value.lower() in ['aide', 'home health aide', 'hha', 'home']:
            validated_value = 'HHA'
        elif value.lower() in ['guard', 'security guard', 'sg', 'security']:
            validated_value = 'SG'
        elif value.lower() in ['english', 'esol', 'esl', 'language']:
            validated_value = 'ESOL'

        else:
            raise ValidationError(err_msg)

        return validated_value, new_key

    @staticmethod
    def validate_date(value, key):
        old_key = key
        err_msg = f'Invalid date from google sheet data dump: {key}:{value}'

        # hard code a date in case google sheet data is emtpy str
        if value == '':
            value = '01/01/14'

        if old_key == 'Start Date':
            new_key = 'start_date'
        elif old_key == 'Completion Date':
            new_key = 'completion_date'
        elif old_key == 'Date Enrollment Agreement Signed':
            new_key = 'date_enrollment_agreement_signed'

        date_items = re.split('/', value, maxsplit=2)

        if len(date_items) == 3:
            date_items[1]
            validated_value = f'20{date_items[2]}-{date_items[0]}-{date_items[1]}'
            return validated_value, new_key
        else:

            # we care about dates, if it is in an incorrect format, raise error
            # and have admin check
            raise ValidationError(err_msg)

    @staticmethod
    def validate_currency(value, key):
        old_key = key

        if old_key == 'Course Cost':
            new_key = 'course_cost'
        elif old_key == 'Total Institutional Charges Charged':
            new_key = 'total_charges_charged'
        elif old_key == 'Total Institutional Charges Paid':
            new_key = 'total_charges_paid'

        if not value:
            return '0.00', new_key

        validated_value = value.replace('$', '').replace(',', '')

        # we dont care much about money insert atm, if it is in an incorrect format, return 0
        # this should never happen though
        try:
            float(validated_value)
        except ValueError:
            validated_value = '0.00'

        return validated_value, new_key

    @staticmethod
    def validate_wage(value):
        new_key = 'starting_wage'

        if not value:
            return '0.00', new_key

        try:
            pattern = '[0-9]+\.?[0-9]*'
            wage = [float(dig) for dig in re.findall(pattern, value)]
        except:
            return '0.00', new_key
        if not wage:
            return '0.00', new_key

        return str(wage[0]), new_key

    @staticmethod
    def validate_bool(value, key):
        old_key = key

        if old_key == 'Graduates':
            new_key = 'graduated'
        elif old_key == 'Passed FIrst Exam Taken':
            new_key = 'passed_first_exam'
        elif old_key == 'Passed Second or Third Exam Taken':
            new_key = 'passed_second_or_third_exam'
        elif old_key == 'Employed':
            new_key = 'employed'

        if value.lower() == 'y' or \
                value.lower() == 'yes':

            return True, new_key
        else:
            return False, new_key

    @staticmethod
    def validate_hours_worked(value):
        new_key = 'hours_worked_weekly'

        try:
            if 'more' in value.lower() or \
                'over' in value.lower() or \
                'least' in value.lower() or \
                '40' in value.lower() or \
                'full' in value.lower() or \
                    'f' in value.lower():

                return 'F', new_key

            elif 'less' in value.lower() or \
                'under' in value.lower() or \
                'part' in value.lower() or \
                'p' in value.lower() or \
                    any(char.isdigit() for char in value):

                return 'P', new_key

            else:
                return 'P', new_key

        except AttributeError:
            return 'P', new_key


class FilterHandler:

    @staticmethod
    def is_valid_query_params(query_params, fields):
        for key in query_params.keys():
            if key not in fields:
                return False
        return True
