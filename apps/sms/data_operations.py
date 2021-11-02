
from re import S
from core.settings.constants import SHEET_CONSTANTS

import time


class GoogleSheetDataOps:

    # @staticmethod
    # def create_record(sheet_id, sheets_api, data, recurse_counter=None):
    @staticmethod
    def create_record(google_sheet_client, data, recurse_counter=None):
        recurse_counter = 1 if not recurse_counter else recurse_counter + 1

        #spread_sheet_Id = sheet_id
        range_ = SHEET_CONSTANTS.get('DATABASE_SHEET')
        value_input_option = 'USER_ENTERED'
        insert_data_option = 'INSERT_ROWS'
        major_dimension = 'ROWS'
        values = [data]

        body = {
            "majorDimension": major_dimension,
            "range": range_,
            "values": [data]
        }

        try:
            # this needs to be configurable for dev, test and production, perferrably in the parent class
            db_worksheet = google_sheet_client.open('test_DB').get_worksheet_by_id(0)

            db_worksheet.append_rows(values=values, value_input_option=value_input_option, insert_data_option=insert_data_option)


            # append
            # sheets_api.values().append(spreadsheetId=spread_sheet_Id,
            #                            range=range_,
            #                            valueInputOption=value_input_option,
            #                            insertDataOption=insert_data_option,
            #                            body=body).execute()

            # GoogleSheetDataOps.refresh(sheet_id, sheets_api)
            GoogleSheetDataOps.refresh(google_sheet_client)

        except Exception as e:
            if recurse_counter and recurse_counter > SHEET_CONSTANTS.get('MAX_RECURSE'):
                raise e
            else:
                time.sleep(100)
                # GoogleSheetDataOps.create(
                #     sheet_id, sheets_api, data, recurse_counter)
                GoogleSheetDataOps.create_record(
                    google_sheet_client, data, recurse_counter)

    # @staticmethod
    # def update_record(sheet_id, sheets_api, row_num, row_to_update, recurse_counter=None):
    @staticmethod
    def update_record(google_sheet_client, row_num, row_to_update, recurse_counter=None):

        recurse_counter = 1 if not recurse_counter else recurse_counter + 1

        # spread_sheet_Id = sheet_id
        range_ = f"{SHEET_CONSTANTS.get('DATABSE_SHEET')}!A{row_num}:Y{row_num}"

        # keep in case needed for backwards compatibility
        # range_ = "%s!A%s:Y%s" % \
        #     (SHEET_CONSTANTS.get('DATABASE_SHEET'), row_num, row_num)
 
 
        # value_input_option = "USER_ENTERED"
        # include_values_in_response = True
        # response_value_render_option = "FORMATTED_VALUE"
        # major_dimension = "ROWS"

        # request_body = {
        #     "majorDimension": major_dimension,
        #     "range": range_,
        #     "values": [row_to_update]

        # }

        values = [row_to_update]


        try:
            db_worksheet = google_sheet_client.open('test_DB').get_worksheet_by_id(0)

            db_worksheet.update(range_, values)

            # update row
            # sheets_api.values().update(
            #     spreadsheetId=spread_sheet_Id,
            #     range=range_,
            #     valueInputOption=value_input_option,
            #     includeValuesInResponse=include_values_in_response,
            #     responseValueRenderOption=response_value_render_option,
            #     body=request_body).execute()
            # refresh database
            
            # GoogleSheetDataOps.refresh(sheet_id, sheets_api)
            GoogleSheetDataOps.refresh(google_sheet_client)

        except Exception as e:

            if recurse_counter and recurse_counter > SHEET_CONSTANTS.get('MAX_RECURSE'):
                raise e
            else:
                time.sleep(100)
                # GoogleSheetDataOps.update_record(sheet_id, sheets_api, row_num, row_to_update, recurse_counter)

                GoogleSheetDataOps.update_record(google_sheet_client, row_num, row_to_update, recurse_counter)

    # @staticmethod
    # def delete_record(sheet_id, sheets_api, del_row_num, recurse_counter=None):
    @staticmethod
    def delete_record(google_sheet_client, del_row_num, recurse_counter=None):

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


                        
            spreadsheet = google_sheet_client.open('test_DB')

            spreadsheet.batch_update(body=del_request)



            # sheets_api.batchUpdate(spreadsheetId=sheet_id,
            #                        body=del_request).execute()

            # refresh database
            # GoogleSheetDataOps.refresh(sheet_id, sheets_api)
            GoogleSheetDataOps.refresh(google_sheet_client)

        except Exception as e:
            if recurse_counter and recurse_counter > SHEET_CONSTANTS.get('MAX_RECURSE'):
                raise e
            else:
                time.sleep(100)
                # GoogleSheetDataOps.delete_record(
                #     sheet_id, sheets_api, del_row_num, recurse_counter)
                GoogleSheetDataOps.delete_record(
                    google_sheet_client, del_row_num, recurse_counter)



    # @staticmethod
    # def match_record(sheet_id, sheets_api, student_id, import_, recurse_counter=None):
    @staticmethod
    def match_record(google_sheet_client, student_id, recurse_counter=None):
        # if we are importing existing google sheet into database, we dont need to create nor update google sheet again
        # if import_:
        #     return

        recurse_counter = 1 if not recurse_counter else recurse_counter + 1

        #spread_sheet_Id = sheet_id
        #include_values_in_response = True
        #response_value_render_option = "FORMATTED_VALUE"
        #value_input_option = "USER_ENTERED"
        update_range = f"{SHEET_CONSTANTS.get('MATCH_OPERATION_SHEET')}!A1"
        # update_range = "%s!A1" % SHEET_CONSTANTS.get(
        #     'MATCH_OPERATION_SHEET')
        #major_dimension = "ROWS"
        
        
        results_fetch_range = f"{SHEET_CONSTANTS.get('MATCH_OPERATION_SHEET')}!A:Y"
        # results_fetch_range = "%s!A:Y" % SHEET_CONSTANTS.get(
        #     'MATCH_OPERATION_SHEET')

        match_col = SHEET_CONSTANTS.get(
            'MATCH_BY_COL').get('Student ID')

        query = f'=MATCH("{student_id}", {SHEET_CONSTANTS.get("DATABASE_SHEET")}!{match_col}:{match_col}, 0)'

        # query = '=MATCH("%s", %s!%s:%s, 0)' % \
        #     (student_id, SHEET_CONSTANTS.get('DATABASE_SHEET'), match_col, match_col)

        # request_body = {
        #     "majorDimension": major_dimension,
        #     "range": update_range,
        #     "values": [
        #         [
        #             query
        #         ]
        #     ]
        # }

        try:


            db_worksheet = google_sheet_client.open('test_DB').get_worksheet_by_id(0)

            db_worksheet.update(update_range, query, raw=False)

            # send in the match
            # sheets_api.values().update(
            #     spreadsheetId=spread_sheet_Id,
            #     range=update_range,
            #     valueInputOption=value_input_option,
            #     includeValuesInResponse=include_values_in_response,
            #     responseValueRenderOption=response_value_render_option,
            #     body=request_body).execute()

            
            


            query_result = db_worksheet.get(results_fetch_range)
            
            # fetch matched result
            # query_result = sheets_api.values().get(spreadsheetId=spread_sheet_Id,
            #                                        range=results_fetch_range).execute()

            print('HELLO WORLD QUERY RESULT, NOT SURE WHAT TYPE IT IS: ', query_result)
            values = query_result.get('values', [])

            return values[0][0] if values else None

        except Exception as e:
            if recurse_counter and recurse_counter > SHEET_CONSTANTS.get('MAX_RECURSE'):
                raise e
            else:
                time.sleep(20)
                # GoogleSheetDataOps.match_record(sheet_id, sheets_api,
                #                          student_id, match_col, import_, recurse_counter)

                GoogleSheetDataOps.match_record(google_sheet_client,
                                         student_id, match_col, recurse_counter)

    # @staticmethod
    # def refresh(sheet_id, sheets_api, recurse_counter=None):
    @staticmethod
    def refresh(google_sheet_client, recurse_counter=None):
        recurse_counter = 1 if not recurse_counter else recurse_counter + 1

        # converts all date serial to be rendered as dates
        # convert all currency to dollars, round up to the nearest dollor
        # sorts by Course Start Date
        sort_request = SHEET_CONSTANTS.get('REFRESH_REQUEST')

        try:

            
            spreadsheet = google_sheet_client.open('test_DB')

            spreadsheet.batch_update(body=sort_request)

            # sheets_api.batchUpdate(spreadsheetId=sheet_id,
            #                        body=sort_request).execute()

        except Exception as e:

            if recurse_counter and recurse_counter > SHEET_CONSTANTS.get('MAX_RECURSE'):
                raise e
            else:
                time.sleep(100)
                # return GoogleSheetDataOps.refresh_database(sheet_id, sheets_api, recurse_counter)
                return GoogleSheetDataOps.refresh_database(google_sheet_client, recurse_counter)
