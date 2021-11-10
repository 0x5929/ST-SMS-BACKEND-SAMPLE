import re
from core.settings.constants import STUDENT_RECORD_HEADERS, PROGRAM_NAMES

from rest_framework.exceptions import ValidationError

from .validators import SMSValidator


class DataHelper:

    @ classmethod
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

    @ staticmethod
    def bool_conversion(model, header):
        value = getattr(model, header)
        return 'Y' if value else ''

    @ staticmethod
    def date_conversion(model, header):

        date_obj = getattr(model, header)
        return f'{str(date_obj.month)}/{str(date_obj.day)}/{str(date_obj.year)}'
        # return '%s/%s/%s' % (str(date_obj.day), str(date_obj.month), str(date_obj.year))

    @ staticmethod
    def money_conversion(model, header):

        money_obj = getattr(model, header)
        return f'${str(money_obj.amount)}' if money_obj else ''
        # return '$%s' % str(money_obj.amount)

    # NOTE data keys are assigned by each item inside STUDENT_RECORD_HEADERS,
    # by logic, as long as we dont change and or mess with the way data_conversion and clean_data,
    # order of dict is preserved by assignment by 3.6!
    @ staticmethod
    def finalize_data(data):
        return [value for value in data.values()]


# class ExceptionHandler:

#     @ staticmethod
#     def raise_verror(msg):
#         raise ValidationError(msg)


class FilterHandler:

    @ staticmethod
    def is_valid_query_params(query_params, fields):
        for key in query_params.keys():
            if key not in fields:
                return False
        return True


class GoogleSheetDataDumpHanlder:

    @staticmethod
    def auth_and_get_sheet(GoogleSheet, spreadsheet_id, sheet_id):
        gs_api = GoogleSheet.init_google_sheet().google_sheet_client.open_by_key(
            spreadsheet_id)

        return gs_api.get_worksheet_by_id(int(sheet_id))

    @classmethod
    def get_datadump_res(cls, sheet):
        sheet_data = sheet.get_all_records(empty2zero=False, head=1)

        data_dump = cls(initial_data=sheet_data)

        return_data = data_dump.run()

        return return_data

    def __init__(self, initial_data):
        self.initial_data = initial_data
        self.data_dump = {}

        # initial state of all uuids, so we can check for uniqueness
        self.student_uuids = []
        self.rotation_uuids = []
        self.program_uuids = []
        self.school_uuids = []

    def run(self):

        for sr in self.initial_data:
            # each student record should go through
            # cleaning
            #
            self.validate_and_rekey(sr)
            pass

        return self.initial_data

    def validate_and_rekey(self, record):
        for header in record.keys():
            record[header] = self.mapper(header)

    def mapper(self, key):
        if key == 'Student ID':
            self.rekey(*self.validate_student_id(self.initial_data[key], key))
        elif key == 'Full Name':
            self.rekey(*self.validate_string(self.initial_data[key], key))
        elif key == 'Last Name':
            self.rekey(*self.validate_string(self.initial_data[key], key))
        elif key == 'First Name':
            self.rekey(*self.validate_string(self.initial_data[key], key))
        elif key == 'Phone Number':
            self.rekey(*self.validate_phone(self.initial_data[key], key))
        elif key == 'Email Address':
            self.rekey(*self.validate_email(self.initial_data[key], key))
        elif key == 'Mailing Address':
            self.rekey(*self.validate_string(self.initial_data[key], key))
        elif key == 'Course':
            self.rekey(*self.validate_course(self.initial_data[key], key))
        elif key == 'Start Date':
            self.rekey(*self.validate_date(self.initial_data[key], key))
        elif key == 'Completion Date':
            self.rekey(*self.validate_date(self.initial_data[key], key))
        elif key == 'Date Enrollment Agreement Signed':
            self.rekey(*self.validate_date(self.initial_data[key], key))
        elif key == 'Third-party payer identifying information':
            self.rekey(*self.validate_string(self.initial_data[key], key))
        elif key == 'Course Cost':
            self.rekey(*self.validate_currency(self.initial_data[key], key))
        elif key == 'Total Institutional Charges Charged':
            self.rekey(*self.validate_currency(self.initial_data[key], key))
        elif key == 'Total Institutional Charges Paid':
            self.rekey(*self.validate_currency(self.initial_data[key], key))
        elif key == 'Graduates':
            self.rekey(*self.validate_bool(self.initial_data[key], key))
        elif key == 'Passed FIrst Exam Taken':
            self.rekey(*self.validate_bool(self.initial_data[key], key))
        elif key == 'Passed Second or Third Exam Taken':
            self.rekey(*self.validate_bool(self.initial_data[key], key))
        elif key == 'Employed':
            self.rekey(*self.validate_bool(self.initial_data[key], key))
        elif key == 'Place of Employment':
            self.rekey(*self.validate_string(self.initial_data[key], key))
        elif key == 'Employment Address':
            self.rekey(*self.validate_string(self.initial_data[key], key))
        elif key == 'Position':
            self.rekey(*self.validate_string(self.initial_data[key], key))
        elif key == 'Starting Wage':
            self.rekey(*self.validate_currency(self.initial_data[key], key))
        elif key == 'Hours Worked per Week':
            self.rekey(
                *self.validate_hours_worked(self.initial_data[key], key))
        elif key == 'Description of Attempts to Contact Students':
            self.rekey(*self.validate_string(self.initial_data[key], key))

        else:
            raise ValidationError(
                'Incorrect google sheet header, not accounted for in data dump.')

    # we will validate each and rekey the dictionary

    def validate_student_id(self, value, key):
        old_key = key
        new_key = 'student_id'
        err_msg = f'Invalid student ID format in google sheet data dump: {value}'
        try:
            validated_value = SMSValidator.student_id_format_checker(value)
            return validated_value, old_key, new_key

        except ValidationError:
            raise ValidationError(err_msg)
        except Exception as e:
            raise ValidationError(e.__repr__)

    def validate_string(self, value, key):
        old_key = key

        if key == 'Full Name':
            new_key = 'full_name'
        elif key == 'Last Name':
            new_key = 'last_name'
        elif key == 'First Name':
            new_key = 'first_name'
        elif key == 'Mailing Address':
            new_key = 'mailing_address'
        elif key == 'Third-party payer identifying information':
            new_key = 'third_party_payer_info'
        elif key == 'Place of Employment':
            new_key = 'place_of_employment'
        elif key == 'Employment Address':
            new_key = 'employment_address'
        elif key == 'Position':
            new_key = 'position'
        elif key == 'Description of Attempts to Contact Students':
            new_key = 'description_of_attempts_to_contact_student'

        err_msg = f'String value contains suspicious characters in google sheet data dump: {value}'

        try:
            validated_value = SMSValidator.no_special_chars_and_captialize_string(
                value)
            return validated_value, old_key, new_key

        except ValidationError:
            raise ValidationError(err_msg)
        except Exception as e:
            raise ValidationError(e.__repr__)

    def validate_phone(self, value,  key):
        old_key = key
        new_key = 'phone'
        err_msg = f'Invalid phone number format in google sheet data dump: {value}'

        try:
            validated_value = SMSValidator.phone_number_format_checker(value)

            return validated_value, old_key, new_key
        except ValidationError:
            raise ValidationError(err_msg)
        except Exception as e:
            raise ValidationError(e.__repr__)

        # return (validated_value, old_key, new_key)

    def validate_email(self, value, key):
        old_key = key
        new_key = 'email'
        err_msg = f'Invalid email format in google sheet data dump: {value}'

        try:
            validated_value = SMSValidator.email_format_checker(value)

            return validated_value, old_key, new_key
        except ValidationError:
            raise ValidationError(err_msg)
        except Exception as e:
            raise ValidationError(e.__repr__)

    def validate_course(self, value,  key):
        old_key = key
        new_key = 'course'
        err_msg = f'Invalid course from google sheet data dump: {value}'

        machine_indx = 0
        human_readable_indx = 1

        for course_sel in PROGRAM_NAMES:
            if value.lower() in course_sel[machine_indx].lower() or \
                    value.lower() in course_sel[human_readable_indx].lower():

                validated_value = course_sel[machine_indx]
                return validated_value, old_key, new_key

        raise ValidationError(err_msg)

    def validate_date(self, value, key):
        pass
        # return (validated_value, old_key, new_key)

    def validate_currency(self, value, key):
        pass
        # return (validated_value, old_key, new_key)

    def validate_bool(self, value, key):
        pass
        # return (validated_value, old_key, new_key)

    def validate_hours_worked(self, value,  key):
        pass
        # return (validated_value, old_key, new_key)

    def rekey(self, value, old_key, new_key):
        pass
