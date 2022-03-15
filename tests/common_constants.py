SMS_STUDENT_UUID_TO_TEST = 'db7d3163-7856-4b61-b242-65ef034c4bfe'
SMS_SCHOOL_UUID_TO_TEST = '0c805318-7706-405e-a66c-5936062617a5'
SMS_PROGRAM_UUID_TO_TEST = '67301e14-cd3d-493a-a2cf-84d8c490c0ef'
SMS_ROTATION_UUID_TO_TEST = 'fcd1f629-6449-4672-8dc8-4a2183cc70e9'


SMS_STUDENT_UUID_ST2 = 'c7efabb4-890c-48bb-a5f9-854c899496c8'
SMS_SCHOOL_UUID_ST2 = '6bfad48c-ecc6-44ac-b53f-c94ccd240119'
SMS_PROGRAM_UUID_ST2 = 'd682ebed-72a4-499f-9bd5-4ce777c492cd'
SMS_ROTATION_UUID_ST2 = '37b61d4e-ab68-4f49-ae8c-d742da756fcc'


GMS_CNA_ROTATION_UUID_TO_TEST = 'fdc7898d-80f0-4a48-9617-d205b1486066'
GMS_HHA_ROTATION_UUID_TO_TEST = 'f1bd7d07-2633-4650-b85f-448f54fd3789'
GMS_CNA_STUDENT_UUID_TO_TEST = 'ccc37087-32fa-4c26-8af8-e84619dc2e47'
GMS_HHA_STUDENT_UUID_TO_TEST = 'd4125d1a-56af-4522-846d-dd09cff85162'
GMS_CNA_THEORY_RECORD_UUID_TO_TEST = '868769c7-0742-4ca9-bf6a-9ab5b5cc73c1'
GMS_HHA_THEORY_RECORD_UUID_TO_TEST = '8ab11f0b-6214-4f43-be18-8e1b711db6eb'
GMS_CNA_CLINICAL_RECORD_UUID_TO_TEST = 'bad5926f-3f8e-4c73-b11d-de07b0255624'
GMS_HHA_CLINICAL_RECORD_UUID_TO_TEST = '28b09da5-a7e0-4c9e-abd1-f88ec95c20b7'


GMS_ST2_CNA_ROTATION_UUID_TO_TEST = 'b42249ec-b354-4ff6-9ffa-f88454fdcd21'
GMS_ST2_HHA_ROTATION_UUID_TO_TEST = '37e1c605-aced-40b6-a3fb-bf2776207f52'
GMS_ST2_CNA_STUDENT_UUID_TO_TEST = '2ad62709-e450-4498-a28b-df0f8990e9ac'
GMS_ST2_HHA_STUDENT_UUID_TO_TEST = 'c13a0659-64cc-4bcb-a153-ba8415f05bd0'
GMS_ST2_CNA_THEORY_RECORD_UUID_TO_TEST = '3795d9c5-a0ca-4ad7-ac8d-f8eb1e66be0c'
GMS_ST2_HHA_THEORY_RECORD_UUID_TO_TEST = '136fb640-7cd7-4f2e-892f-67b7a2a4b238'
GMS_ST2_CNA_CLINICAL_RECORD_UUID_TO_TEST = '5c75dd4d-8638-47df-afa8-5e1748e19be7'
GMS_ST2_HHA_CLINICAL_RECORD_UUID_TO_TEST = '85bf2e7d-a51c-41dd-acea-58a751c39e38'

CMS_CLIENT_UUID_TO_TEST = '1b6f00a6-dec7-4766-be71-2ce630eb2df5'
CMS_NOTE_UUID_TO_TEST = 'd598af07-bbab-44f0-9ba2-94cd58f4ecdf'


# this is for filter URLs of the STI HHA student, please change this if test fixture changes
# SMS_FILTER_PARAMS = {
#     'school_name': 'STI',
#     'program_name': 'HHA',
#     'rotation_num': 1,
#     'first_name': 'Test',
#     'last_name': 'B',
#     'full_name': 'test_b',
#     'email': 'testb@email.com',
#     'phone': '626-333-5544',
#     'id_': 'RO-HHA-01-1006-TB',
#     'start_date': '2021-12-09',
#     'completion_date': '2021-12-10',
#     'paid': 'False',
#     'graduated': 'False',
#     'employed': 'False'
# }


SMS_FILTER_PARAMS = {
    'school_name': 'STI',
    'program_name': 'CNA',
    'rotation_num': 99,
    'first_name': 'Ricky',
    'last_name': 'Spanish',
    'full_name': 'ricky_spanish',
    'email': 'ricky.spanish@email.com',
    'phone': '626-589-5984',
    'id_': 'RO-CNA-99-1019-RS',
    'start_date': '2021-10-28',
    'completion_date': '2021-12-13',
    'paid': 'False',
    'graduated': 'False',
    'employed': 'False'
}


SMS_FILTER_PARAMS_ST2 = {
    'school_name': 'ST2',
    'program_name': 'HHA',
    'rotation_num': 1,
    'first_name': 'Alvin',
    'last_name': 'Chipmonk',
    'full_name': 'alvin_chipmonk',
    'email': 'alvin@email.com',
    'phone': '626-333-5545',
    'id_': 'AL-HHA-01-1019-TB',
    'start_date': '2021-10-06',
    'completion_date': '2021-12-11',
    'paid': 'True',
    'graduated': 'True',
    'employed': 'True'
}




TEST_SCHOOL_NAME = 'STI'

TEST_CAP_MATCHING_STR = 'Matching string'
TEST_NON_MATCHING_STR = ['_', '\\', '/', '\'', '"', '?', '!', '@',
                                '$', '%', '^', '&', '(', ')', '[', ']', '{', '}', '>', '<']
TEST_MATCHING_PHONE_NO = '123-456-7890'

TEST_NON_MATCHING_PHONE = ['1234567890', '1234567890', '12345678',
                              '(123)456789', '123-456-789', '123-456-78901', '123.456.7890']
