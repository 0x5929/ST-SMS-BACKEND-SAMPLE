
import time


class GoogleSheetDataOps:

    CONSTANTS = {

        'DATABASE_SHEET': 'Sheet1',

        # utilties sheet we need to match/query data
        'MATCH_OPERATION_SHEET': 'Restful',

        # matching a google sheet record with:
        'MATCH_BY_COL':  {'Student ID': 'A'},

        # max recursive calls allowed
        'MAX_RECURSE': 2,

        # refresh sheet request object
        'REFRESH_REQUEST': {

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


    }

    @staticmethod
    def create_record(sheet_id, sheets_api, data, recurse_counter=None):

        recurse_counter = 1 if not recurse_counter else recurse_counter + 1

        spread_sheet_Id = sheet_id
        range_ = GoogleSheetDataOps.CONSTANTS.get('DATABASE_SHEET')
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
            sheets_api.values().append(spreadsheetId=spread_sheet_Id,
                                       range=range_,
                                       valueInputOption=value_input_option,
                                       insertDataOption=insert_data_option,
                                       body=body).execute()

            GoogleSheetDataOps.refresh()

        except Exception as e:
            if recurse_counter and recurse_counter > GoogleSheetDataOps.CONSTANTS.get('MAX_RECURSE'):
                raise e
            else:
                time.sleep(100)
                GoogleSheetDataOps.create(
                    sheet_id, sheets_api, data, recurse_counter)

    @staticmethod
    def update_record(sheet_id, sheets_api, row_num, row_to_update, recurse_counter=None):

        recurse_counter = 1 if not recurse_counter else recurse_counter + 1

        spread_sheet_Id = sheet_id
        range_ = "%s!A%s:Y%s" % \
            (GoogleSheetDataOps.CONSTANTS.get('DATABASE_SHEET'), row_num, row_num)
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
            sheets_api.values().update(spreadsheetId=spread_sheet_Id,
                                       range=range_,
                                       valueInputOption=value_input_option,
                                       includeValuesInResponse=include_values_in_response,
                                       responseValueRenderOption=response_value_render_option,
                                       body=request_body).execute()
            # refresh database
            GoogleSheetDataOps.refresh()

        except Exception as e:

            if recurse_counter and recurse_counter > GoogleSheetDataOps.CONSTANTS.get('MAX_RECURSE'):
                raise e
            else:
                time.sleep(100)
                GoogleSheetDataOps.update(
                    row_num, row_to_update, recurse_counter)

    @staticmethod
    def delete_record(sheet_id, sheets_api, del_row_num, recurse_counter=None):

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
            sheets_api.batchUpdate(spreadsheetId=sheet_id,
                                   body=del_request).execute()

            # refresh database
            GoogleSheetDataOps.refresh()

        except Exception as e:
            if recurse_counter and recurse_counter > GoogleSheetDataOps.CONSTANTS.get('MAX_RECURSE'):
                raise e
            else:
                time.sleep(100)
                GoogleSheetDataOps.delete(
                    sheet_id, sheets_api, del_row_num, recurse_counter)

    @staticmethod
    def match_record(sheet_id, sheets_api, student_id, import_, recurse_counter=None):

        # if we are importing existing google sheet into database, we dont need to create nor update google sheet again
        if import_:
            return

        recurse_counter = 1 if not recurse_counter else recurse_counter + 1

        spread_sheet_Id = sheet_id
        include_values_in_response = True
        response_value_render_option = "FORMATTED_VALUE"
        value_input_option = "USER_ENTERED"
        update_range = "%s!A1" % GoogleSheetDataOps.CONSTANTS.get(
            'MATCH_OPERATION_SHEET')
        major_dimension = "ROWS"
        results_fetch_range = "%s!A:Y" % GoogleSheetDataOps.CONSTANTS.get(
            'MATCH_OPERATION_SHEET')

        match_col = GoogleSheetDataOps.CONSTANTS.get(
            'MATCH_BY_COL').get('Student ID')

        query = '=MATCH("%s", %s!%s:%s, 0)' % \
            (GoogleSheetDataOps.CONSTANTS.get('DATABASE_SHEET'),
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
            sheets_api.values().update(spreadsheetId=spread_sheet_Id,
                                       range=update_range,
                                       valueInputOption=value_input_option,
                                       includeValuesInResponse=include_values_in_response,
                                       responseValueRenderOption=response_value_render_option,
                                       body=request_body).execute()

            # fetch matched result
            query_result = sheets_api.values().get(spreadsheetId=spread_sheet_Id,
                                                   range=results_fetch_range).execute()

            values = query_result.get('values', [])

            return values[0][0] if values else None

        except Exception as e:
            if recurse_counter and recurse_counter > GoogleSheetDataOps.CONSTANTS.get('MAX_RECURSE'):
                raise e
            else:
                time.sleep(20)
                GoogleSheetDataOps.match(sheet_id, sheets_api,
                                         student_id, match_col, import_, recurse_counter)

    @staticmethod
    def refresh(sheet_id, sheets_api, recurse_counter=None):
        recurse_counter = 1 if not recurse_counter else recurse_counter + 1

        # converts all date serial to be rendered as dates
        # convert all currency to dollars, round up to the nearest dollor
        # sorts by Course Start Date
        sort_request = GoogleSheetDataOps.CONSTANTS['REFRESH_REQUEST']

        try:
            sheets_api.batchUpdate(spreadsheetId=sheet_id,
                                   body=sort_request).execute()

        except Exception as e:

            if recurse_counter and recurse_counter > GoogleSheetDataOps.CONSTANTS.get('MAX_RECURSE'):
                raise e
            else:
                time.sleep(100)
                return GoogleSheetDataOps.refresh_database(sheet_id, sheets_api, recurse_counter)
