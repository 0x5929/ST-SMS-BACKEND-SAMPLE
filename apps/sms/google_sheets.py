import os
import re
import uuid
import time
import gspread

from django.apps import apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured, ValidationError
from oauth2client.service_account import ServiceAccountCredentials

from .utils import DataHandler
from .data_operations import GoogleSheetDataOps
from .constants import SHEET_CONSTANTS


BASE_DIR = getattr(settings, 'BASE_DIR')

class GoogleSheet:

    @classmethod
    def master_sheet_save(cls, data):
        # also takes care of taking out school_name column,
        # it wont be necessary since every school should have separate and their own spreadsheet to manage
        school = data.pop('school_name')

        # connect_google_api
        gs_api = cls.init_google_sheet(school)

        insert_ready_data = DataHandler.finalize_data(data)

        # MATCH FIRST
        # lookup by ID to determine if this is create or update
        update_row_num = gs_api.match(gs_api.worksheets, data.get(
            'student_id'))

        if update_row_num:
            gs_api.update(gs_api.spreadsheet,
                          update_row_num, insert_ready_data)

        else:
            gs_api.create(gs_api.worksheets, insert_ready_data)

        # create and update accordingly, or save(), dont forget to sort after with refresh
        return gs_api.refresh(gs_api.spreadsheet)

    @classmethod
    def master_sheet_del(cls, data):
        # also takes care of taking out school_name column,
        # it wont be necessary since every school should have separate and their own spreadsheet to manage
        school = data.pop('school_name')

        # connect_google_api
        gs_api = cls.init_google_sheet(school)

        # lookup by ID
        del_row_num = gs_api.match(gs_api.worksheets, data.get('student_id'))

        if del_row_num:
            gs_api.delete(gs_api.spreadsheet, del_row_num)
        else:
            pass

        return gs_api.refresh(gs_api.spreadsheet)

    @classmethod
    def init_google_sheet(cls, school_name=None, recurse_counter=None):

        recurse_counter = 1 if not recurse_counter else recurse_counter + 1

        # NOTE the difference from st_master_DB, whereas the previous version used token.pickle, now everything is .json

        try:

            # # connect to google sheet
            scopes = SHEET_CONSTANTS.get('SCOPES')
            creds = ServiceAccountCredentials.from_json_keyfile_name(
                os.path.join(BASE_DIR, '../st-sms-creds.json'), scopes)

            google_sheet_client = gspread.authorize(creds)

            return cls(
                google_sheet_client=google_sheet_client,
                school_name=school_name,
                create=GoogleSheetDataOps.create_record,
                update=GoogleSheetDataOps.update_record,
                delete=GoogleSheetDataOps.delete_record,
                match=GoogleSheetDataOps.match_record,
                refresh=GoogleSheetDataOps.refresh)

        except Exception as e:
            if recurse_counter and recurse_counter > SHEET_CONSTANTS.get('MAX_RECURSE'):
                raise e
            else:
                time.sleep(SHEET_CONSTANTS.get('MAX_INIT_WAIT'))
                return cls.init_google_sheet(
                    school_name, recurse_counter)
                # note that STUDENT_RECORD_HEADERS is a list with exact order of the header
                # and data_conversion will append in the exact order,
                # therefore updating and creating data on spreadsheet in order as intended.
                # simple solution, but hopefully scalable

    def __init__(self,
                 google_sheet_client,
                 school_name=None,
                 create=None,
                 update=None,
                 delete=None,
                 match=None,
                 refresh=None):

        # in case we want to initiate a GoogleSheet obj and work directly with gspread api
        # the data operation methods can be initialized wo
        self.google_sheet_client = google_sheet_client
        self.school_name = school_name
        self.create = create
        self.update = update
        self.delete = delete
        self.match = match
        self.refresh = refresh
        self.env = getattr(settings, 'ENV')
        self.spreadsheet = self.get_spreadsheet()
        self.worksheets = self.get_worksheets()

    def get_spreadsheet(self):

        if not self.school_name:
            return None

        if self.env == 'DEV':
            return self.google_sheet_client.open_by_key(
                SHEET_CONSTANTS.get(
                    'SPREADSHEET_ID').get(
                        self.school_name).get(
                            'dev'))

        elif self.env == 'TEST':
            return self.google_sheet_client.open_by_key(
                SHEET_CONSTANTS.get(
                    'SPREADSHEET_ID').get(
                        self.school_name).get(
                            'test'))

        elif self.env == 'PROD':
            return self.google_sheet_client.open_by_key(
                SHEET_CONSTANTS.get(
                    'SPREADSHEET_ID').get(
                        self.school_name).get(
                            'prod'))

        else:
            raise ImproperlyConfigured('INVALID SPREADSHEET ID')

    def get_worksheets(self):

        if not self.spreadsheet:
            return None

        return {

            'db_worksheet': self.spreadsheet.get_worksheet_by_id(
                SHEET_CONSTANTS.get(
                    'DATABASE_SHEET_ID')),

            'match_worksheet': self.spreadsheet.get_worksheet_by_id(
                SHEET_CONSTANTS.get('MATCH_OPERATION_SHEET_ID'))
        }


class ExportHandler:

    @staticmethod
    def auth_and_get_sheet(spreadsheet_id, sheet_id):
        gs_api = GoogleSheet.init_google_sheet().google_sheet_client.open_by_key(
            spreadsheet_id)

        return gs_api.get_worksheet_by_id(int(sheet_id))

    @classmethod
    def run(cls, sheet, school_name):
        sheet_data = sheet.get_all_records(empty2zero=False, head=1)

        return cls(initial_data=sheet_data, school_name=school_name)

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

    def get_data(self):

        # note we can also do a check at the end, to remove null/None values if student exists
        # but since we are exporting and importing to an empty DB, this shouldnt matter
        for index, sr in enumerate(self.initial_data):
            # each student record should go through

            # cleaning and rekey the headers for the validated values
            self.validate_and_rekey(index, sr)

            # build references for database
            rot_uuid = self.build_ref()

            # finalize each record according to fixture
            final_data = self.finalize_each_record(rot_uuid)

            # append to data dump 
            self.final_dump.append(final_data)

            # reinitialize each_data dict, which is used in rekey
            self.each_data = {}

        return self.final_dump

    def validate_and_rekey(self, index, record):
        for header in record.keys():
            self.mapper(index, header)

    def mapper(self, index, key):
        if key == 'Student ID':
            self.rekey(
                *DataHandler.validate_student_id(self.initial_data[index][key]))
        elif key == 'Full Name':
            self.rekey(
                *DataHandler.validate_string(self.initial_data[index][key], key))
        elif key == 'Last Name':
            self.rekey(
                *DataHandler.validate_string(self.initial_data[index][key], key))
        elif key == 'First Name':
            self.rekey(
                *DataHandler.validate_string(self.initial_data[index][key], key))
        elif key == 'Phone Number':
            self.rekey(
                *DataHandler.validate_phone(self.initial_data[index][key]))
        elif key == 'Email Address':
            self.rekey(
                *DataHandler.validate_email(self.initial_data[index][key]))
        elif key == 'Mailing Address':
            self.rekey(
                *DataHandler.validate_string(self.initial_data[index][key], key))
        elif key == 'Course':
            self.rekey(
                *DataHandler.validate_course(self.initial_data[index][key]))
        elif key == 'Start Date':
            self.rekey(
                *DataHandler.validate_date(self.initial_data[index][key], key))
        elif key == 'Completion Date':
            self.rekey(
                *DataHandler.validate_date(self.initial_data[index][key], key))
        elif key == 'Date Enrollment Agreement Signed':
            self.rekey(
                *DataHandler.validate_date(self.initial_data[index][key], key))
        elif key == 'Third-party payer identifying information':
            self.rekey(
                *DataHandler.validate_string(self.initial_data[index][key], key))
        elif key == 'Course Cost':
            self.rekey(
                *DataHandler.validate_currency(self.initial_data[index][key], key))
        elif key == 'Total Institutional Charges Charged':
            self.rekey(
                *DataHandler.validate_currency(self.initial_data[index][key], key))
        elif key == 'Total Institutional Charges Paid':
            self.rekey(
                *DataHandler.validate_currency(self.initial_data[index][key], key))
        elif key == 'Graduates':
            self.rekey(
                *DataHandler.validate_bool(self.initial_data[index][key], key))
        elif key == 'Passed FIrst Exam Taken':
            self.rekey(
                *DataHandler.validate_bool(self.initial_data[index][key], key))
        elif key == 'Passed Second or Third Exam Taken':
            self.rekey(
                *DataHandler.validate_bool(self.initial_data[index][key], key))
        elif key == 'Employed':
            self.rekey(
                *DataHandler.validate_bool(self.initial_data[index][key], key))
        elif key == 'Place of Employment':
            self.rekey(
                *DataHandler.validate_string(self.initial_data[index][key], key))
        elif key == 'Employment Address':
            self.rekey(
                *DataHandler.validate_string(self.initial_data[index][key], key))
        elif key == 'Position':
            self.rekey(
                *DataHandler.validate_string(self.initial_data[index][key], key))
        elif key == 'Starting Wage':
            self.rekey(
                *DataHandler.validate_wage(self.initial_data[index][key]))
        elif key == 'Hours Worked per Week':
            self.rekey(
                *DataHandler.validate_hours_worked(self.initial_data[index][key]))
        elif key == 'Description of Attempts to Contact Students':
            self.rekey(
                *DataHandler.validate_string(self.initial_data[index][key], key))

        else:
            raise ValidationError(
                f'Incorrect google sheet header, not accounted for in data dump: [{key}]')

    def rekey(self, validated_value, new_key):
        self.each_data[new_key] = validated_value

    def build_ref(self):
        """
        Reads self.each_data['student_id'] and 
        Builds references from school level model downwards,
        finally returns rotation uuid for student's reference 

        """
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

        # this really shouldn't happen, only testing
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
            program__program_uuid__exact=program_uuid, rotation_number__exact=rot_num).rotation_uuid)

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
        if float(final_sr_data_dict.get('fields').get('total_charges_paid')) >= \
                float(final_sr_data_dict.get('fields').get('total_charges_charged')):

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
        # self.each_data = final_sr_data_dict
        return final_sr_data_dict
