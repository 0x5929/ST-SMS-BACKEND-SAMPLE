import time
import os.path

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


class GoogleSheet:

    CONSTANTS = {

        'SCOPES': ['https://www.googleapis.com/auth/spreadsheets', ],

        'SPREADSHEET_ID': {'Select Therapy Institute': '1PxgtH1vT3VpeLJhMKjBWmo4Qq29M_RudfRywzQAP3-U'},

        # database sheet we want to append data
        'DATABASE_SHEET': 'Sheet1',

        # utilties sheet we need to match/query data
        'MATCH_OPERATION_SHEET': 'Restful',

        'MATCH_BY_COL':  {'Student ID': 'A'},

        # switch to True when importing csv from view
        'IMPORT': False,

        'MAX_RECURSE': 2

    }

    @classmethod
    def master_sheet_save(cls, data):
        # also takes care of taking out school_name column,
        # it wont be necessary since every school should have separate and their own spreadsheet to manage
        school = data.pop('school_name')

        # connect_google_api
        gs_api = cls.init_google_sheet(school)

        insert_ready_data = cls.finalize_data(data)
        # lookup by name to determine if this is create or update
        update_row_num = gs_api.match(data.get('student_id'), cls.CONSTANTS.get(
            'MATCH_BY_COL').get('Student ID'), cls.CONSTANTS.get('IMPORT'))

        if update_row_num:
            return gs_api.update(update_row_num, insert_ready_data)
        else:
            return gs_api.create(insert_ready_data)

        # create and update accordingly, or save(), dont forget to sort after with refresh

    @ classmethod
    def master_sheet_del(cls, data):
        # also takes care of taking out school_name column,
        # it wont be necessary since every school should have separate and their own spreadsheet to manage
        school = data.pop('school_name')

        # connect_google_api
        gs_api = cls.init_google_sheet(school)

        # lookup by name to determine if this is create or update
        del_row_num = gs_api.match(data.get('student_id'), cls.CONSTANTS.get(
            'MATCH_BY_COL').get('Student ID'), cls.CONSTANTS.get('IMPORT'))

        if del_row_num:
            return gs_api.delete(del_row_num)
        else:
            pass

    @classmethod
    def parse_sheet_id(cls, school_name):
        return cls.CONSTANTS.get('SPREADSHEET_ID').get(school_name)

    @classmethod
    def init_google_sheet(cls, school_name, recurse_counter=None):

        recurse_counter = 1 if not recurse_counter else recurse_counter + 1

        # NOTE the difference from st_master_DB, whereas the previous version used token.pickle, now everything is .json

        try:

            # connect to google sheet
            creds = None

            # The file token.json stores the user's access and refresh tokens, and is
            # created automatically when the authorization flow completes for the first
            # time.

            if os.path.exists('token.json'):
                creds = Credentials.from_authorized_user_file(
                    'token.json', cls.CONSTANTS.get('SCOPES'))

            # If there are no (valid) credentials available, let the user log in.
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        'credentials.json', cls.CONSTANTS.get('SCOPES'))
                    creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with open('token.json', 'w') as token:
                    token.write(creds.to_json())

            service = build('sheets', 'v4', credentials=creds)

            # Call the Sheets API
            sheets_api = service.spreadsheets()

            sheet_id = cls.parse_sheet_id(school_name)

            # grab sheet ID, and other constants depending on school name
            return cls(
                sheet=sheets_api,
                sheet_id=sheet_id)
        except Exception as e:
            if recurse_counter and recurse_counter > cls.CONSTANTS.get('MAX_RECURSE'):
                raise e
            else:
                time.sleep(20)
                cls.init_google_sheet(
                    school_name, recurse_counter)
                # note that STUDENT_RECORD_HEADERS is a list with exact order of the header
                # and data_conversion will append in the exact order,
                # therefore updating and creating data on spreadsheet in order as intended.
                # simple solution, but hopefully scalable

    @ classmethod
    def data_conversion(cls, model, STUDENT_RECORD_HEADERS):
        data = {}

        for header in STUDENT_RECORD_HEADERS:
            if header == 'graduate' or \
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

            else:
                data[header] = str(getattr(model, header))

        return data

    @ staticmethod
    def bool_conversion(model, header):
        # can i get rid of bool()? test in shell plz
        return 'Y' if bool(getattr(model, header)) else ''

    @ staticmethod
    def date_conversion(date_obj):

        # convert date_obj into string google sheet can easily understand and
        # return string
        pass

    @ staticmethod
    def money_conversion(money_obj):

        # convert money_obj into string google sheet can easily understand and
        # return string
        pass

    # NOTE data keys are assigned by each item inside STUDENT_RECORD_HEADERS,
    # by logic, as long as we dont change and or mess with the way data_conversion and clean_data,
    # order of dict is preserved by assignment by 3.6!
    @ staticmethod
    def finalize_data(data):
        return [value for value in data.values()]

        # obj init and methods

    def __init__(self, sheets_api, sheet_id):
        self.sheets_api = sheets_api
        self.sheet_id = sheet_id

    def create(self, data, recurse_counter=None):

        recurse_counter = 1 if not recurse_counter else recurse_counter + 1

        spread_sheet_Id = self.__class__.CONSTANTS.get('SPREADSHEET_ID')
        range_ = self.__class__.CONSTANTS.get('DATABASE_SHEET')
        value_input_option = 'USER_ENTERED'
        insert_data_option = 'INSERT_ROWS'
        major_dimension = 'ROWS'

        body = {
            "majorDimension": major_dimension,
            "range": range_,
            "values": [data]
        }

        try:
            # append
            self.sheets_api.values().append(spreadsheetId=spread_sheet_Id,
                                            range=range_,
                                            valueInputOption=value_input_option,
                                            insertDataOption=insert_data_option,
                                            body=body).execute()

            self.refresh_sheet()

        except Exception as e:
            if recurse_counter and recurse_counter > self.__class__.CONSTANTS.get('MAX_RECURSE'):
                raise e
            else:
                time.sleep(100)
                self.create(data, recurse_counter)

    def update(self, row_num, row_to_update, recurse_counter):

        recurse_counter = 1 if not recurse_counter else recurse_counter + 1

        spread_sheet_Id = self.__class__.CONSTANTS.get('SPREADSHEET_ID')
        range_ = "%s!A%s:Y%s" % \
            (self.__class__.CONSTANTS.get('DATABASE_SHEET'), row_num, row_num)
        value_input_option = "USER_ENTERED"
        include_values_in_response = True
        response_value_render_option = "FORMATTED_VALUE"
        major_dimension = "ROWS"

        request_body = {
            "majorDimension": major_dimension,
            "range": range_,
            "values": [row_to_update]

        }

        try:
            # update row
            res = self.sheets_api.values().update(spreadsheetId=spread_sheet_Id,
                                                  range=range_,
                                                  valueInputOption=value_input_option,
                                                  includeValuesInResponse=include_values_in_response,
                                                  responseValueRenderOption=response_value_render_option,
                                                  body=request_body).execute()
        except Exception as e:

            if recurse_counter and recurse_counter > self.__class__.CONSTANTS.get('MAX_RECURSE'):
                raise e
            else:
                time.sleep(100)
                self.update(row_num, row_to_update, recurse_counter)

    def delete(self, del_row_num, recurse_counter=None):

        recurse_counter = 1 if not recurse_counter else recurse_counter + 1

        dimension = "ROWS"
        start_index = int(del_row_num) - 1
        end_index = int(del_row_num)

        del_request = {

            "requests": [
                {
                    "deleteDimension": {
                        "range": {
                            "sheetId": 0,
                            "dimension": dimension,
                            "startIndex": start_index,
                            "endIndex": end_index
                        }
                    }
                }
            ]

        }

        try:
            self.sheets_api.batchUpdate(spreadsheetId=self.__class__.CONSTANTS.get('SPREADSHEET_ID'),
                                        body=del_request).execute()

            # refresh database
            self.refresh_sheet()

        except Exception as e:
            if recurse_counter and recurse_counter > self.__class__.CONSTANTS.get('MAX_RECURSE'):
                raise e
            else:
                time.sleep(100)
                self.delete(del_row_num, recurse_counter)

    def match(self, student_id, match_col, import_, recurse_counter):

        # if we are importing existing google sheet into database, we dont need to create nor update google sheet again
        if import_:
            return

        recurse_counter = 1 if not recurse_counter else recurse_counter + 1

        spread_sheet_Id = self.__class__.CONSTANTS.get('SPREADSHEET_ID')
        include_values_in_response = True
        response_value_render_option = "FORMATTED_VALUE"
        value_input_option = "USER_ENTERED"
        update_range = "%s!A1" % self.__class__.CONSTANTS.get(
            'MATCH_OPERATION_SHEET')
        major_dimension = "ROWS"
        results_fetch_range = "%s!A:Y" % self.__class__.CONSTANTS.get(
            'MATCH_OPERATION_SHEET')

        match_col = match_col

        query = '=MATCH("%s", %s!%s:%s, 0)' % \
            (self.__class__.CONSTANTS.get('DATABASE_SHEET'),
             student_id, match_col, match_col)

        request_body = {
            "majorDimension": major_dimension,
            "range": update_range,
            "values": [
                [
                    query
                ]
            ]
        }

        try:

            # send in the match
            self.sheets_api.values().update(spreadsheetId=spread_sheet_Id,
                                            range=update_range,
                                            valueInputOption=value_input_option,
                                            includeValuesInResponse=include_values_in_response,
                                            responseValueRenderOption=response_value_render_option,
                                            body=request_body).execute()

            # fetch matched result
            query_result = self.sheets_api.values().get(spreadsheetId=spread_sheet_Id[1],
                                                        range=results_fetch_range).execute()

            values = query_result.get('values', [])

            return values[0][0] if values else None

        except Exception as e:
            if recurse_counter and recurse_counter > self.__class__.CONSTANTS.get('MAX_RECURSE'):
                raise e
            else:
                time.sleep(20)
                self.match(student_id, match_col, import_, recurse_counter)

    def refresh_sheet(self, recurse_counter=None):
        recurse_counter = 1 if not recurse_counter else recurse_counter + 1

        # converts all date serial to be rendered as dates
        # convert all currency to dollars, round up to the nearest dollor
        # sorts by Course Start Date
        sort_request = {
            "requests": [{
                "repeatCell": {

                    # start index is inclusive, end index is exclusive
                    # For Start Date | Completion Date | Date Enrollment Agreement Signed
                    # Which is column 9,10,11
                    "range": {
                        "sheetId": 0,
                        "startRowIndex": 1,
                        "startColumnIndex": 8,
                        "endColumnIndex": 11
                    },

                    "cell": {

                        "userEnteredFormat": {

                            "numberFormat": {

                                "type": "DATE",
                                        "pattern": "m/d/yy"
                            }
                        }
                    },

                    "fields": "userEnteredFormat.numberFormat"
                }
            }, {
                "repeatCell": {

                    # start index is inclusive, end index is exclusive
                    # For Course Cost | Total Institutional Charges Charged | Total Institutional Charges Paid
                    # Column 13, 14, 15
                    "range": {
                        "sheetId": 0,
                        "startRowIndex": 1,
                        "startColumnIndex": 12,
                        "endColumnIndex": 15
                    },

                    "cell": {

                        "userEnteredFormat": {

                            "numberFormat": {

                                "type": "CURRENCY",
                                        "pattern": "$#,###"
                            }
                        }
                    },

                    "fields": "userEnteredFormat.numberFormat"
                }
            }, {
                "sortRange": {

                    "range": {
                        "sheetId": 0,
                        "startRowIndex": 1,
                        "startColumnIndex": 0
                    },
                    "sortSpecs": [
                        {
                            "sortOrder"	: "ASCENDING",
                            "dimensionIndex": 8
                        }
                    ]
                }

            }]
        }

        try:
            self.sheets_api.batchUpdate(spreadsheetId=self.__class__.CONSTANTS.get('SPREADSHEET_ID'),
                                        body=sort_request).execute()

        except Exception as e:

            if recurse_counter and recurse_counter > self.__class__.CONSTANTS.get('MAX_RECURSE'):
                raise e
            else:
                time.sleep(100)
                return self.refresh_database(recurse_counter)
