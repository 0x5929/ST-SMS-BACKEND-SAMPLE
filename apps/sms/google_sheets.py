import time
import os.path

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


import gspread
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
        # update_row_num = gs_api.match(gs_api.sheet_id, gs_api.sheets_api, data.get(
        #     'student_id'), SHEET_CONSTANTS.get('IMPORT'))

        # print('google_sheet_client: ', gs_api.google_sheet_client)
        update_row_num = gs_api.match(gs_api.google_sheet_client, data.get(
            'student_id'))

        if update_row_num:
            # return gs_api.update(gs_api.sheet_id, gs_api.sheets_api, update_row_num, insert_ready_data)
            gs_api.update(gs_api.google_sheet_client, update_row_num, insert_ready_data)
            #gs_api.refresh(gs_api.google_sheet_client)

        else:
            # return gs_api.create(gs_api.sheet_id, gs_api.sheets_api, insert_ready_data)
            gs_api.create(gs_api.google_sheet_client, insert_ready_data)
            #gs_api.refresh(gs_api.google_sheet_client)
        # create and update accordingly, or save(), dont forget to sort after with refresh

        return gs_api.refresh(gs_api.google_sheet_client)

    @classmethod
    def master_sheet_del(cls, data):
        # also takes care of taking out school_name column,
        # it wont be necessary since every school should have separate and their own spreadsheet to manage
        school = data.pop('school_name')

        # connect_google_api
        gs_api = cls.init_google_sheet(school)

        # lookup by ID
        # del_row_num = gs_api.match(gs_api.sheet_id, gs_api.sheets_api, data.get(
        #     'student_id'), SHEET_CONSTANTS.get('IMPORT'))

        del_row_num = gs_api.match(gs_api.google_sheet_client, data.get(
            'student_id'))


        if del_row_num:
            # return gs_api.delete(gs_api.sheet_id, gs_api.sheets_api, del_row_num)
            gs_api.delete(gs_api.google_sheet_client, del_row_num)
            #gs_api.refresh(gs_api.google_sheet_client)
        else:
            pass

        return gs_api.refresh(gs_api.google_sheet_client)


    @classmethod
    def init_google_sheet(cls, school_name, recurse_counter=None):

        recurse_counter = 1 if not recurse_counter else recurse_counter + 1

        # NOTE the difference from st_master_DB, whereas the previous version used token.pickle, now everything is .json

        try:


            scope = SHEET_CONSTANTS.get('SCOPES')
            creds = ServiceAccountCredentials.from_json_keyfile_name('st-sms-creds.json', scope)

            google_sheet_client = gspread.authorize(creds)

            return cls(
                google_sheet_client=google_sheet_client,
                create=GoogleSheetDataOps.create_record,
                update=GoogleSheetDataOps.update_record,
                delete=GoogleSheetDataOps.delete_record,
                match=GoogleSheetDataOps.match_record,
                refresh=GoogleSheetDataOps.refresh)


            # # connect to google sheet
            # creds = None

            # # The file token.json stores the user's access and refresh tokens, and is
            # # created automatically when the authorization flow completes for the first
            # # time.

            # if os.path.exists('token.json'):
            #     creds = Credentials.from_authorized_user_file(
            #         'token.json', SHEET_CONSTANTS.get('SCOPES'))

            # # If there are no (valid) credentials available, let the user log in.
            # if not creds or not creds.valid:
            #     if creds and creds.expired and creds.refresh_token:
            #         creds.refresh(Request())
            #     else:
            #         flow = InstalledAppFlow.from_client_secrets_file(
            #             'credentials.json', SHEET_CONSTANTS.get('SCOPES'))
            #         creds = flow.run_local_server(port=0)
            #     # Save the credentials for the next run
            #     with open('token.json', 'w') as token:
            #         token.write(creds.to_json())

            # service = build('sheets', 'v4', credentials=creds)

            # # Call the Sheets API
            # sheets_api = service.spreadsheets()

            # sheet_id = cls.parse_sheet_id(school_name)

            # # grab sheet ID, and other constants depending on school name
            # return cls(
            #     sheet=sheets_api,
            #     sheet_id=sheet_id,
            #     create=GoogleSheetDataOps.create_record,
            #     update=GoogleSheetDataOps.update_record,
            #     delete=GoogleSheetDataOps.delete_record)

        except Exception as e:
            if recurse_counter and recurse_counter > SHEET_CONSTANTS.get('MAX_RECURSE'):
                raise e
            else:
                time.sleep(20)
                cls.init_google_sheet(
                    school_name, recurse_counter)
                # note that STUDENT_RECORD_HEADERS is a list with exact order of the header
                # and data_conversion will append in the exact order,
                # therefore updating and creating data on spreadsheet in order as intended.
                # simple solution, but hopefully scalable

    # @classmethod
    # def parse_sheet_id(cls, school_name):
    #     return SHEET_CONSTANTS.get('SPREADSHEET_ID').get(school_name)

    # obj init and database operations from data_operations.py

    # def __init__(self, sheets_api, sheet_id, create, update, delete, match):
    #     self.sheets_api = sheets_api
    #     self.sheet_id = sheet_id
    #     self.create = create
    #     self.update = update
    #     self.delete = delete
    #     self.match = match


    def __init__(self, google_sheet_client, create, update, delete, match, refresh):
        self.google_sheet_client = google_sheet_client
        self.create = create
        self.update = update
        self.delete = delete
        self.match = match
        self.refresh = refresh
