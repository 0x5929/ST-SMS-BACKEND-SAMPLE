from os import stat
import re
from core.settings.constants import STUDENT_RECORD_HEADERS
import uuid

from rest_framework.exceptions import ValidationError


# no need for the following either, we are only interested in read only nested repr anyways,
# which is default by DRF, so no need to write extra code for nested writing operations
# when we need to write, ie: POST/PUT/PATCH/DELETE we will call that specific endpoint, and not from a parent model
# please do the same changes across cms and gms when the time comes to testing for those apps
# class DatabaseHandler:

#     @staticmethod
#     def create_or_update(validated_data, instance, model):
#         if model.__name__ == 'School':
#             # no nested relations need to be attached when creating, or updating
#             pass
#         elif model.__name__ == 'Program':
#             # get school ID from request
#             school_id = validated_data.get('school').school_uuid

#             # retrieve said school from the DB using ID
#             from .models import School
#             school = School.objects.get(school_uuid__exact=school_id)

#             # add school to the program object
#             validated_data['school'] = school

#         elif model.__name__ == 'Rotation':
#             # get program ID from request

#             program_id = validated_data.get('program').program_uuid

#             # retrieve said program from the DB using ID
#             from .models import Program
#             program = Program.objects.get(program_uuid__exact=program_id)

#             # add program to the rotation object
#             validated_data['program'] = program

#         elif model.__name__ == 'Student':
#             # get rotation ID from request
#             rotation_id = validated_data.get('rotation').rotation_uuid

#             print('before: ', validated_data['rotation'])
#             # retrieve said rotation from the DB using ID
#             from .models import Rotation
#             rotation = Rotation.objects.get(rotation_uuid__exact=rotation_id)

#             # add rotation to the student object
#             validated_data['rotation'] = rotation

#             print('after: ', validated_data['rotation'])

#         return (instance, validated_data) if instance else validated_data


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
