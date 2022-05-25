from .constants import SHEET_CONSTANTS

import time
from datetime import date
from django.db.models import Q


# tested by intergration/acceptance, no unit tests written for this class
class GoogleSheetDataOps:

    @staticmethod
    def create_record(worksheets, data, recurse_counter=None):
        recurse_counter = 1 if not recurse_counter else recurse_counter + 1

        value_input_option = 'USER_ENTERED'
        insert_data_option = 'INSERT_ROWS'
        values = [data]

        try:
            # this needs to be configurable for dev, test and production, perferrably in the parent class
            db_worksheet = worksheets.get('db_worksheet')

            # append
            db_worksheet.append_rows(
                values=values, value_input_option=value_input_option, insert_data_option=insert_data_option)

        except Exception as e:
            if recurse_counter and recurse_counter > SHEET_CONSTANTS.get('MAX_RECURSE'):
                raise e
            else:
                time.sleep(SHEET_CONSTANTS.get('MAX_DATAOP_WAIT'))
                return GoogleSheetDataOps.create_record(
                    worksheets, data, recurse_counter)

    @staticmethod
    def update_record(spreadsheet, row_num, row_to_update, recurse_counter=None):

        # NOTE: this method uses gspread.spreadsheet.values_update instead of gspread.spreadsheet.worksheet.update
        # this is bc that refresh() does not work well with gspread.spreadsheet.worksheet.update,
        # but since we dont need to refresh the matching page, in match_records we use gspread.spreadsheet.worksheet.update

        recurse_counter = 1 if not recurse_counter else recurse_counter + 1

        # spread_sheet_Id = sheet_id
        range_ = f"{SHEET_CONSTANTS.get('DATABASE_SHEET')}!A{row_num}:Y{row_num}"
        value_input_option = "USER_ENTERED"
        include_values_in_response = True
        response_value_render_option = "FORMATTED_VALUE"
        major_dimension = "ROWS"

        request_body = {
            "majorDimension": major_dimension,
            "values": [row_to_update]

        }

        try:
            spreadsheet.values_update(range_, params={
                'valueInputOption': value_input_option,
                'responseValueRenderOption': response_value_render_option,
                'includeValuesInResponse': include_values_in_response},
                body=request_body)

        except Exception as e:

            if recurse_counter and recurse_counter > SHEET_CONSTANTS.get('MAX_RECURSE'):
                raise e
            else:
                time.sleep(SHEET_CONSTANTS.get('MAX_DATAOP_WAIT'))
                return GoogleSheetDataOps.update_record(spreadsheet, row_num, row_to_update, recurse_counter)

    @staticmethod
    def delete_record(spreadsheet, del_row_num, recurse_counter=None):

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

            spreadsheet.batch_update(body=del_request)

        except Exception as e:
            if recurse_counter and recurse_counter > SHEET_CONSTANTS.get('MAX_RECURSE'):
                raise e
            else:
                time.sleep(SHEET_CONSTANTS.get('MAX_DATAOP_WAIT'))
                return GoogleSheetDataOps.delete_record(
                    spreadsheet, del_row_num, recurse_counter)

    @staticmethod
    def match_record(worksheets, student_id, recurse_counter=None):

        recurse_counter = 1 if not recurse_counter else recurse_counter + 1

        update_cell = 'A1'
        results_fetch_range = 'A:Y'

        match_col = SHEET_CONSTANTS.get(
            'MATCH_BY_COL').get('Student ID')

        query = f'=MATCH("{student_id}", {SHEET_CONSTANTS.get("DATABASE_SHEET")}!{match_col}:{match_col}, 0)'

        try:
            match_worksheet = worksheets.get('match_worksheet')

            # send in the MATCH request
            match_worksheet.update(update_cell, query, raw=False)

            query_result = match_worksheet.get(results_fetch_range)

            # fetch MATCH result
            return None if query_result[0][0] == '#N/A' else query_result[0][0]

        except Exception as e:
            if recurse_counter and recurse_counter > SHEET_CONSTANTS.get('MAX_RECURSE'):
                raise e
            else:
                time.sleep(20)
                return GoogleSheetDataOps.match_record(worksheets,
                                                       student_id, recurse_counter)

    @staticmethod
    def refresh(spreadsheet, recurse_counter=None):
        recurse_counter = 1 if not recurse_counter else recurse_counter + 1

        # converts all date serial to be rendered as dates
        # convert all currency to dollars, round up to the nearest dollor
        # sorts by Course Start Date
        sort_request = SHEET_CONSTANTS.get('REFRESH_REQUEST')

        try:

            spreadsheet.batch_update(body=sort_request)

        except Exception as e:

            if recurse_counter and recurse_counter > SHEET_CONSTANTS.get('MAX_RECURSE'):
                raise e
            else:
                time.sleep(SHEET_CONSTANTS.get('MAX_DATAOP_WAIT'))
                return GoogleSheetDataOps.refresh_database(spreadsheet, recurse_counter)


# tested by intergration, some units tests are written for some methods in this class
class StudentDataStatistics:

    @staticmethod
    def get_years():
        current_year = date.today().year  # 2022
        first_year = '2013'

        return [str(year) for year in range(int(first_year), current_year + 1)]

    @classmethod
    def get_date_ranges(cls):
        return [[f'{year}-01-01', f'{year}-12-31'] for year in cls.get_years()]

    @classmethod
    def fetch_enrollment_stats(cls, StudentModel):
        stats = []

        for range_ in cls.get_date_ranges():
            year = int(range_[0][0:4])
            year_count = StudentModel.objects.filter(
                date_enrollment_agreement_signed__range=range_).count()

            stats.append({'year': year, 'count': year_count})

        return stats

    @classmethod
    def fetch_employment_stats(cls, StudentModel):
        stats = []

        for range_ in cls.get_date_ranges():
            year = int(range_[0][0:4])
            year_count = StudentModel.objects.filter(employed=True,
                                                     date_enrollment_agreement_signed__range=range_).count()

            stats.append({'year': year, 'count': year_count})

        return stats

    @classmethod
    def fetch_graduates_stats(cls, StudentModel):
        stats = []

        for range_ in cls.get_date_ranges():
            year = int(range_[0][0:4])
            year_count = StudentModel.objects.filter(graduated=True,
                                                     date_enrollment_agreement_signed__range=range_).count()

            stats.append({'year': year, 'count': year_count})

        return stats

    @classmethod
    def fetch_exam_stats(cls, StudentModel):
        stats = []

        for range_ in cls.get_date_ranges():
            year = int(range_[0][0:4])
            year_count = StudentModel.objects.filter(Q(passed_first_exam=True) | Q(passed_second_or_third_exam=True),
                                                     date_enrollment_agreement_signed__range=range_).count()

            stats.append({'year': year, 'count': year_count})

        return stats

    @classmethod
    def fetch_statistics(cls, StudentModel):
        return [{
            'enrollment': cls.fetch_enrollment_stats(StudentModel),
            'employment': cls.fetch_employment_stats(StudentModel),
            'graduate': cls.fetch_graduates_stats(StudentModel),
            'exam': cls.fetch_exam_stats(StudentModel)
        }]
