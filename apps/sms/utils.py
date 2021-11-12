import re
import uuid
from core.settings.constants import STUDENT_RECORD_HEADERS, PROGRAM_NAMES
from django.apps import apps


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
    def get_datadump_res(cls, sheet, school_name):
        sheet_data = sheet.get_all_records(empty2zero=False, head=1)

        data_dump = cls(initial_data=sheet_data, school_name=school_name)

        return_data = data_dump.run()

        return return_data

    def __init__(self, initial_data, school_name):
        self.initial_data = initial_data
        self.school_name = school_name
        self.each_data = {}
        self.final_dump = []

        # initial state of all uuids, so we can check for uniqueness
        self.student_uuids = []
        self.rotation_uuids = []
        self.program_uuids = []
        self.school_uuids = []

    def run(self):

        for index, sr in enumerate(self.initial_data):
            # each student record should go through
            # cleaning and rekey the headers for the validated values
            # add additional keys according to fixture
            self.validate_and_rekey(index, sr)
            rot_uuid = self.build_ref()
            self.finalize_each_record(rot_uuid)
            self.final_dump.append(self.each_data)
            self.each_data = {}

        return self.final_dump

    def validate_and_rekey(self, index, record):
        for header in record.keys():
            self.mapper(index, header)

    def mapper(self, index, key):
        if key == 'Student ID':
            self.rekey(
                *self.validate_student_id(self.initial_data[index][key], key))
        elif key == 'Full Name':
            self.rekey(
                *self.validate_string(self.initial_data[index][key], key))
        elif key == 'Last Name':
            self.rekey(
                *self.validate_string(self.initial_data[index][key], key))
        elif key == 'First Name':
            self.rekey(
                *self.validate_string(self.initial_data[index][key], key))
        elif key == 'Phone Number':
            self.rekey(
                *self.validate_phone(self.initial_data[index][key], key))
        elif key == 'Email Address':
            self.rekey(
                *self.validate_email(self.initial_data[index][key], key))
        elif key == 'Mailing Address':
            self.rekey(
                *self.validate_string(self.initial_data[index][key], key))
        elif key == 'Course':
            self.rekey(
                *self.validate_course(self.initial_data[index][key], key))
        elif key == 'Start Date':
            self.rekey(*self.validate_date(self.initial_data[index][key], key))
        elif key == 'Completion Date':
            self.rekey(*self.validate_date(self.initial_data[index][key], key))
        elif key == 'Date Enrollment Agreement Signed':
            self.rekey(*self.validate_date(self.initial_data[index][key], key))
        elif key == 'Third-party payer identifying information':
            self.rekey(
                *self.validate_string(self.initial_data[index][key], key))
        elif key == 'Course Cost':
            self.rekey(
                *self.validate_currency(self.initial_data[index][key], key))
        elif key == 'Total Institutional Charges Charged':
            self.rekey(
                *self.validate_currency(self.initial_data[index][key], key))
        elif key == 'Total Institutional Charges Paid':
            self.rekey(
                *self.validate_currency(self.initial_data[index][key], key))
        elif key == 'Graduates':
            self.rekey(*self.validate_bool(self.initial_data[index][key], key))
        elif key == 'Passed FIrst Exam Taken':
            self.rekey(*self.validate_bool(self.initial_data[index][key], key))
        elif key == 'Passed Second or Third Exam Taken':
            self.rekey(*self.validate_bool(self.initial_data[index][key], key))
        elif key == 'Employed':
            self.rekey(*self.validate_bool(self.initial_data[index][key], key))
        elif key == 'Place of Employment':
            self.rekey(
                *self.validate_string(self.initial_data[index][key], key))
        elif key == 'Employment Address':
            self.rekey(
                *self.validate_string(self.initial_data[index][key], key))
        elif key == 'Position':
            self.rekey(
                *self.validate_string(self.initial_data[index][key], key))
        elif key == 'Starting Wage':
            self.rekey(*self.validate_wage(self.initial_data[index][key], key))
        elif key == 'Hours Worked per Week':
            self.rekey(
                *self.validate_hours_worked(self.initial_data[index][key], key))
        elif key == 'Description of Attempts to Contact Students':
            self.rekey(
                *self.validate_string(self.initial_data[index][key], key))

        else:
            raise ValidationError(
                'Incorrect google sheet header, not accounted for in data dump.')

    # we will validate each and rekey the dictionary

    def validate_student_id(self, value, key):
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

    def validate_string(self, value, key):
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

            err_msg = f'String value contains suspicious characters in google sheet data dump: {key}:{value}'

            validated_value = SMSValidator.no_special_chars_and_captialize_string(
                value)

            return validated_value, new_key

        except:
            return '', new_key

    def validate_phone(self, value,  key):
        new_key = 'phone_number'
        err_msg = f'Invalid phone number format in google sheet data dump: {value}'

        if value == '' or value == 'N/A' or value == 'n/a':
            return '', new_key
        try:
            validated_value = SMSValidator.phone_number_format_checker(value)

            return validated_value, new_key
        except ValidationError:
            raise ValidationError(err_msg)
        except Exception as e:
            raise ValidationError(repr(e))

    def validate_email(self, value, key):
        new_key = 'email'
        err_msg = f'Invalid email format in google sheet data dump: {value}'

        if value == '' or value == 'N/A' or value == 'n/a':
            return '', new_key

        try:
            validated_value = SMSValidator.email_format_checker(value)

            return validated_value, new_key
        except ValidationError:
            raise ValidationError(err_msg)
        except Exception as e:
            raise ValidationError(repr(e))

    def validate_course(self, value,  key):
        new_key = 'course'
        err_msg = f'Invalid course from google sheet data dump: {value}'

        if value in ['nurse', 'nurse assistant',
                     'cna', 'caregiver', 'care']:
            validated_value = 'CNA',
        elif value in ['aide', 'home health aide', 'hha', 'home']:
            validated_value = 'HHA'
        elif value in ['guard', 'security guard', 'sg', 'security']:
            validated_value = 'SG'
        elif value in ['english', 'esol', 'esl', 'language']:
            validated_value = 'ESOL'

        else:
            validated_value = 'ESOL'
        # machine_indx = 0
        # human_readable_indx = 1

        # for course_sel in PROGRAM_NAMES:
        #     if value.lower() in course_sel[machine_indx].lower() or \
        #             value.lower() in course_sel[human_readable_indx].lower():

        #         validated_value = course_sel[machine_indx]
        #         return validated_value, new_key

        # raise ValidationError(err_msg)

        return validated_value, new_key

    def validate_date(self, value, key):
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
            raise ValidationError(err_msg)

    def validate_currency(self, value, key):
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
        try:
            float(validated_value)
        except ValueError:
            validated_value = '0.00'

        return validated_value, new_key

    def validate_wage(self, value, key):
        new_key = 'starting_wage'

        if not value:
            return None, new_key

        try:
            pattern = '[0-9]+\.?[0-9]*'
            wage = [float(dig) for dig in re.findall(pattern, value)]
        except:
            return None, new_key
        if not wage:
            return None, new_key

        return str(wage[0]), new_key

    def validate_bool(self, value, key):
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

    def validate_hours_worked(self, value,  key):
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

    def rekey(self, value, new_key):
        self.each_data[new_key] = value

    def build_ref(self):
        student_id = self.each_data['student_id']
        pattern = '^(RO|AL)-(CNA|HHA|SG|ESOL)-([0-9]{1,3})-[0-9]{4}-[A-Z]{2}$'
        re_match = re.search(pattern, student_id)

        try:
            school_name = re_match.group(1)
            program_name = re_match.group(2)
            rotation_num = int(re_match.group(3))
        except:
            raise ValidationError(f'bad student id: {student_id}')
        school_uuid = self.check_school_ref(school_name)
        program_uuid = self.check_prog_ref(
            program_name, school_name, school_uuid)
        rotation_uuid = self.check_rot_ref(
            rotation_num, program_name, school_name, program_uuid)

        return rotation_uuid

    def check_school_ref(self, school_name):
        School = apps.get_model('sms', 'School')

        if school_name == 'RO':
            school_name = 'STI'
        elif school_name == 'AL':
            school_name = 'ST2'

        if self.school_uuids:
            for pk, school in self.school_uuids:
                if school == school_name:
                    return pk

        school_exists = School.objects.filter(
            school_name__exact=school_name).exists()

        if not school_exists:
            pk = self.get_pk(School)

            school_dict = {
                'model':  'sms.school',
                'pk': pk,
                'fields': {

                    'school_name': self.school_name,
                    'school_code': 'place holder, please change me',
                    'school_address': 'place holder, please change me along with year_founded',
                    'year_founded': '2009-03-05'

                }

            }

            self.school_uuids.append((pk, school_name))
            self.final_dump.append(school_dict)
            return pk

        return str(School.objects.get(school_name__exact=school_name).school_uuid)

    def check_prog_ref(self, program_name, school_name, school_uuid):
        Program = apps.get_model('sms', 'Program')

        if self.program_uuids:
            for pk, program, school in self.program_uuids:
                if school == school_name and program == program_name:
                    return pk

        program_exists = Program.objects.filter(
            school__school_uuid__exact=school_uuid, program_name__exact=program_name).exists()

        if not program_exists:
            pk = self.get_pk(Program)

            program_dict = {
                'model': 'sms.program',
                'pk': pk,
                'fields': {
                    'program_name': program_name,
                    'approval_entities': ['BPPE'],
                    'school': school_uuid
                }
            }

            self.program_uuids.append((pk, program_name, school_name))
            self.final_dump.append(program_dict)
            return pk
        return str(Program.objects.get(
            school__school_uuid__exact=school_uuid, program_name__exact=program_name).program_uuid)

    def check_rot_ref(self, rot_num, program_name, school_name, program_uuid):
        Rotation = apps.get_model('sms', 'Rotation')

        if self.rotation_uuids:
            for pk, rot, program, school in self.rotation_uuids:
                if school == school_name and program == program_name and rot == rot_num:
                    return pk

        rotation_exists = Rotation.objects.filter(
            program__program_uuid__exact=program_uuid, rotation_number__exact=rot_num).exists()

        if not rotation_exists:
            pk = self.get_pk(Rotation)

            rotation_dict = {
                'model': 'sms.rotation',
                'pk': pk,
                'fields': {
                    'rotation_number': rot_num,
                    'program': program_uuid
                }
            }

            self.rotation_uuids.append(
                (pk, rot_num, program_name, school_name))
            self.final_dump.append(rotation_dict)
            return pk

        return str(Rotation.objects.get(
            program__program_uuid=program_uuid, rotation_number__exact=rot_num).rotation_uuid)

    def get_pk(self, Model):

        pk = str(uuid.uuid4())

        if Model.objects.filter(pk__exact=pk).exists() or \
                not self.ensure_unique(pk, Model.__name__):
            return self.get_pk(Model)
        else:
            return pk

    def ensure_unique(self, uuid_, model_name):

        if model_name == 'School':

            if not self.school_uuids:
                return True

            for pk, school_name in self.school_uuids:
                if pk == uuid_:
                    return False
                else:
                    return True

        elif model_name == 'Program':

            if not self.program_uuids:
                return True

            for pk, program_name, school_name in self.program_uuids:
                if pk == uuid_:

                    return False
                else:
                    return True

        elif model_name == 'Rotation':

            if not self.rotation_uuids:
                return True

            for pk, rotation_num, program_name, school_name in self.rotation_uuids:
                if pk == uuid_:
                    return False
                else:
                    return True

        elif model_name == 'Student':
            return True if not uuid_ in self.student_uuids else False

    def finalize_each_record(self, rot_uuid):
        Student = apps.get_model('sms', 'Student')

        pk = self.get_pk(Student)

        # add model, pk and fields
        final_sr_data_dict = {
            'model': 'sms.student',
            'pk': pk,
            'fields': self.each_data
        }

        # del full_name key
        del final_sr_data_dict['fields']['full_name']

        # set all currency
        for currency in [
                'course_cost_currency',
                'total_charges_charged_currency',
                'total_charges_paid_currency',
                'starting_wage_currency']:

            final_sr_data_dict['fields'][currency] = 'USD'

        # paid
        if float(final_sr_data_dict['fields']['total_charges_paid']) >= \
                float(final_sr_data_dict['fields']['total_charges_charged']):
            final_sr_data_dict['fields']['paid'] = True

        else:
            final_sr_data_dict['fields']['paid'] = False

            # google_sheet_migrated
        final_sr_data_dict['fields']['google_sheet_migrated'] = True

        # google_sheet_migration_issue
        final_sr_data_dict['fields']['google_sheet_migration_issue'] = ''

        # rotation
        final_sr_data_dict['fields']['rotation'] = rot_uuid

        # PUSH TO STUDENT UUID
        self.student_uuids.append(pk)

        # this is the final side effect
        self.each_data = final_sr_data_dict
