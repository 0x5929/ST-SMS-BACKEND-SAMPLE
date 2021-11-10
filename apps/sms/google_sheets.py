import time
import gspread

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from core.settings.constants import SHEET_CONSTANTS
from oauth2client.service_account import ServiceAccountCredentials


from .utils import DataHelper
from .data_operations import GoogleSheetDataOps

from core.settings.constants import SHEET_CONSTANTS


class GoogleSheet:

    @classmethod
    def master_sheet_save(cls, data):
        # also takes care of taking out school_name column,
        # it wont be necessary since every school should have separate and their own spreadsheet to manage
        school = data.pop('school_name')

        # connect_google_api
        gs_api = cls.init_google_sheet(school)

        insert_ready_data = DataHelper.finalize_data(data)

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
                'st-sms-creds.json', scopes)

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
                time.sleep(20)
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
