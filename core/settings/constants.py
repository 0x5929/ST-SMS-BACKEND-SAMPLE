# global constants

"""
    app CONSTANTS for st-sms
        (They are also in here bc some are shared across apps, hence encapsulated on a project lvl)

    SCHOOL_NAME: sms, authentication
    PROGRAM_NAMES: sms, cms
    ENTITY_NAMES: sms
    EMPLOYMENT_STATUS_CHOICES: sms
    SHEET_MIGRATION_ISSUES: sms
    STUDENT_RECORD_HEADERS: sms, google_sheet_connector
    SHEET_CONSTANTS: google_sheet_connector

    NOTE: settings.py contains project CONSTANTS

"""

SCHOOL_NAMES = (
    ('STI', 'Select Therapy Institute'),
)

PROGRAM_NAMES = (
    ('CNA', 'Certified Nurse Assistant'),
    ('HHA', 'Home Health Aide'),
    ('SG', 'Security Guard'),
    ('CG', 'Caregiver'),
    ('ESOL', 'English to Speakers of Other Language'),
    ('BLS', 'Basic Life Support'),
    ('HSFA', 'Heartsaver First Aid'),
)

ENTITY_NAMES = (
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

    'SCOPES': ['https://www.googleapis.com/auth/spreadsheets', ],

    'SPREADSHEET_ID': {'Select Therapy Institute': '1PxgtH1vT3VpeLJhMKjBWmo4Qq29M_RudfRywzQAP3-U'},

    # switch to True when importing csv from view
    'IMPORT': False,

    # master google sheet database sheet name
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
