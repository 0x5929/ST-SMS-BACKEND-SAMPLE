

ENTITY_NAMES = (
    ('AHA', 'American Heart Association'),
    ('CDPH', 'California Department of Public Health'),
    ('BPPE', 'Bureau of Postsecondary and for Private Education'),
    ('BSIS', 'Bureau of Security and Investigative Services'),
)
EMPLOYMENT_STATUS_CHOICES = (
    ('F', 'Full time employee, more than 32 hours a week'),
    ('P', 'Part time employee, less than 32 hours a week'),
)

SHEET_MIGRATION_ISSUES = (
    ('POST', 'Could not add new record to Google Sheet'),
    ('PUT', 'Could not update existing record on Google Sheet'),
    ('DEL', 'Could not delete existing record on Google Sheet'),

)

STUDENT_RECORD_HEADERS = (
    'student_id',
    'full_name',
    'last_name',
    'first_name',
    'phone_number',
    'email',
    'mailing_address',
    'course',
    'start_date',
    'completion_date',
    'date_enrollment_agreement_signed',
    'third_party_payer_info',
    'course_cost',
    'total_charges_charged',
    'total_charges_paid',
    'graduated',
    'passed_first_exam',
    'passed_second_or_third_exam',
    'employed',
    'place_of_employment',
    'employment_address',
    'position',
    'starting_wage',
    'hours_worked_weekly',
    'description_of_attempts_to_contact_student',
    'school_name',

)


SHEET_CONSTANTS = {

    'SCOPES': ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'],

    'SPREADSHEET_ID': {
        'STI': {
            'dev':  '1PxgtH1vT3VpeLJhMKjBWmo4Qq29M_RudfRywzQAP3-U',
            'test': '1R0G-gByZYrDkf6Va1X3ywRA-A51nNVp_z51moOxe-VU',
            'prod': '1lniXCNcKlzKqpVmPjRPiKPOly1prOODzaVM_f-UPWoM'
        },

        # second location, mainly for testing purpose, until there is an actual second school loc
        'ST2': {
            'dev':  '1PxgtH1vT3VpeLJhMKjBWmo4Qq29M_RudfRywzQAP3-U',
            'test': '1R0G-gByZYrDkf6Va1X3ywRA-A51nNVp_z51moOxe-VU',
            'prod': '1lniXCNcKlzKqpVmPjRPiKPOly1prOODzaVM_f-UPWoM'
        }
    },


    # google sheet database sheet GID
    'DATABASE_SHEET_ID': 0,

    # google sheet database match sheet GID
    'MATCH_OPERATION_SHEET_ID': 483625289,

    # master google sheet database sheet name
    'DATABASE_SHEET': 'Sheet1',

    # utilties sheet we need to match/query data
    'MATCH_OPERATION_SHEET': 'Restful',

    # matching a google sheet record with:
    'MATCH_BY_COL':  {'Student ID': 'A'},

    # max recursive calls allowed
    'MAX_RECURSE': 2,

    # max waiting between google sheet init errors
    'MAX_INIT_WAIT': 200,

    # max waiting between google sheet data op errors
    'MAX_DATAOP_WAIT': 240,

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
            "repeatCell": {

                # start index is inclusive, end index is exclusive
                # For Course Cost | Total Institutional Charges Charged | Total Institutional Charges Paid
                # Column 13, 14, 15
                "range": {
                    "sheetId": 0,
                    "startRowIndex": 1,
                    "startColumnIndex": 0
                },

                "cell": {

                    "userEnteredFormat": {

                        "textFormat": {

                            "bold": False
                        }
                    }
                },

                "fields": "userEnteredFormat.textFormat"
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
