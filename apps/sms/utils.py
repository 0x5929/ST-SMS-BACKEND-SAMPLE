from os import stat
import re
from core.settings.constants import STUDENT_RECORD_HEADERS
import uuid

from rest_framework.exceptions import ValidationError


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


class ExceptionHandler:

    @ staticmethod
    def raise_verror(msg):
        raise ValidationError(msg)


class FilterHandler:

    @ staticmethod
    def is_valid_query_params(query_params, fields):
        for key in query_params.keys():
            if key not in fields:
                return False
        return True
