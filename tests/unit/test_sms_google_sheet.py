import re
import time
import json
import pytest
import gspread

from random import randrange
from oauth2client.service_account import ServiceAccountCredentials

from django.core.exceptions import ValidationError

from sms.google_sheets import GoogleSheet, ExportHandler
from sms.models import School, Program, Rotation, Student
from sms.utils import DataHandler
from sms.constants import SHEET_CONSTANTS

from tests.acceptance.steps.constants import (STUDENT_UUID_TO_TEST,
                                              SCHOOL_UUID_TO_TEST,
                                              PROGRAM_UUID_TO_TEST,
                                              ROTATION_UUID_TO_TEST,
                                              TEST_SPREADSHEET_ID,
                                              TEST_DB_SHEET_ID,
                                              TEST_SCHOOL_NAME,
                                              TEST_RECORD,
                                              TEST_RECORD_HEADER,
                                              TEST_INDEX,
                                              TEST_HEADERS_AND_VALIDATIONS,
                                              TEST_STUDENT_ID,
                                              TEST_ROTATION_UUID)

# pytestmark = pytest.mark.django_db


@pytest.mark.google
class TestGoogleSheet:
    """
    Unit tests for Google Sheet Class

    """

    @pytest.fixture
    def get_student_obj(self):
        return Student.objects.get(student_uuid__exact=STUDENT_UUID_TO_TEST)

    @pytest.fixture
    def get_data(self, get_student_obj):
        return DataHandler.data_conversion(get_student_obj)

    @pytest.fixture
    def get_gs_api(self, get_data):
        return GoogleSheet.init_google_sheet(get_data.get('school_name'))

    @pytest.fixture
    def get_mocked_init_google(self, get_gs_api, mocker):
        return mocker.patch('sms.google_sheets.GoogleSheet.init_google_sheet', return_value=get_gs_api)

    @pytest.fixture
    def get_mocked_gs_api_methods(self, get_gs_api, mocker):
        return {
            'match': mocker.patch.object(get_gs_api, 'match'),
            'create': mocker.patch.object(get_gs_api, 'create'),
            'update': mocker.patch.object(get_gs_api, 'update'),
            'delete': mocker.patch.object(get_gs_api, 'delete'),
            'refresh': mocker.patch.object(get_gs_api, 'refresh')
        }

    @pytest.fixture
    def get_google_sheet_client(self):
        scopes = SHEET_CONSTANTS.get('SCOPES')
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            'st-sms-creds.json', scopes)

        return gspread.authorize(creds)

    @pytest.fixture
    def get_gspread_authorize(self, get_google_sheet_client, mocker):
        return mocker.patch('gspread.authorize', return_value=get_google_sheet_client)

    @pytest.fixture
    def get_mocked_googlesheet_init(self, mocker):
        # NOTE: __init__ method always returns None, bc it only customize new objs, and if not typeerror will be raised
        return mocker.patch(
            'sms.google_sheets.GoogleSheet.__init__', return_value=None)

    @pytest.fixture
    def test_google_sheet_wait(self, monkeypatch):
        monkeypatch.setitem(SHEET_CONSTANTS, 'MAX_INIT_WAIT', 1)
        monkeypatch.setitem(SHEET_CONSTANTS, 'MAX_DATAOP_WAIT', 1)

    def test_master_sheet_save_create(self, get_data, get_mocked_init_google, get_mocked_gs_api_methods):

        get_mocked_gs_api_methods.get('match').return_value = None

        GoogleSheet.master_sheet_save(get_data)

        get_mocked_init_google.assert_called_once()
        get_mocked_gs_api_methods.get('match').assert_called_once()
        get_mocked_gs_api_methods.get('create').assert_called_once()
        get_mocked_gs_api_methods.get('update').assert_not_called()
        get_mocked_gs_api_methods.get('refresh').assert_called_once()

    def test_master_sheet_save_update(self, get_data, get_mocked_init_google, get_mocked_gs_api_methods):

        get_mocked_gs_api_methods.get('match').return_value = randrange(1, 10)

        GoogleSheet.master_sheet_save(get_data)

        get_mocked_init_google.assert_called_once()
        get_mocked_gs_api_methods.get('match').assert_called_once()
        get_mocked_gs_api_methods.get('update').assert_called_once()
        get_mocked_gs_api_methods.get('create').assert_not_called()
        get_mocked_gs_api_methods.get('refresh').assert_called_once()

    def test_master_sheet_del_none(self, get_data, get_mocked_init_google, get_mocked_gs_api_methods):

        get_mocked_gs_api_methods.get('match').return_value = None

        GoogleSheet.master_sheet_del(get_data)

        get_mocked_init_google.assert_called_once()
        get_mocked_gs_api_methods.get('match').assert_called_once()
        get_mocked_gs_api_methods.get('update').assert_not_called()
        get_mocked_gs_api_methods.get('create').assert_not_called()
        get_mocked_gs_api_methods.get('delete').assert_not_called()
        get_mocked_gs_api_methods.get('refresh').assert_called_once()

    def test_master_sheet_del_row_num(self, get_data, get_mocked_init_google, get_mocked_gs_api_methods):

        get_mocked_gs_api_methods.get('match').return_value = randrange(1, 10)

        GoogleSheet.master_sheet_del(get_data)

        get_mocked_init_google.assert_called_once()
        get_mocked_gs_api_methods.get('match').assert_called_once()
        get_mocked_gs_api_methods.get('update').assert_not_called()
        get_mocked_gs_api_methods.get('create').assert_not_called()
        get_mocked_gs_api_methods.get('delete').assert_called_once()
        get_mocked_gs_api_methods.get('refresh').assert_called_once()

    def test_init_google_sheet_init(self, get_data, get_mocked_googlesheet_init):
        school = get_data.get('school_name')

        GoogleSheet.init_google_sheet(school)

        get_mocked_googlesheet_init.assert_called_once()

    def test_init_google_sheet_exception(self, get_data, get_mocked_googlesheet_init, test_google_sheet_wait):

        def mockedreturn_exception(google_sheet_client, school_name, create, update, delete, match, refresh):
            raise Exception

        get_mocked_googlesheet_init.return_value = mockedreturn_exception

        school = get_data.get('school_name')

        with pytest.raises(Exception):
            GoogleSheet.init_google_sheet(school)

    def test_google_sheet_obj_attr(self, get_gs_api):
        if hasattr(get_gs_api, 'google_sheet_client') and \
           hasattr(get_gs_api, 'school_name') and \
           hasattr(get_gs_api, 'create') and \
           hasattr(get_gs_api, 'update') and \
           hasattr(get_gs_api, 'delete') and \
           hasattr(get_gs_api, 'match') and \
           hasattr(get_gs_api, 'refresh') and \
           hasattr(get_gs_api, 'env') and \
           hasattr(get_gs_api, 'spreadsheet') and \
           hasattr(get_gs_api, 'worksheets'):

            assert True
        else:
            assert False

    def test_google_sheet_get_spreadsheet_no_school(self, get_gs_api):

        get_gs_api.school_name = None

        assert get_gs_api.get_spreadsheet() == None

    def test_google_sheet_get_spreadsheet_dev_env(self, get_gs_api):

        get_gs_api.env = 'DEV'

        assert get_gs_api.get_spreadsheet().id == get_gs_api.google_sheet_client.open_by_key(SHEET_CONSTANTS.get(
            'SPREADSHEET_ID').get(get_gs_api.school_name).get('dev')).id

    def test_google_sheet_get_spreadsheet_test_env(self, get_gs_api):

        get_gs_api.env = 'TEST'

        assert get_gs_api.get_spreadsheet().id == get_gs_api.google_sheet_client.open_by_key(SHEET_CONSTANTS.get(
            'SPREADSHEET_ID').get(get_gs_api.school_name).get('test')).id

    def test_google_sheet_get_spreadsheet_prod_env(self, get_gs_api):

        get_gs_api.env = 'PROD'

        assert get_gs_api.get_spreadsheet().id == get_gs_api.google_sheet_client.open_by_key(SHEET_CONSTANTS.get(
            'SPREADSHEET_ID').get(get_gs_api.school_name).get('prod')).id

    def test_google_sheet_get_worksheets_no_spreadsheet(self, get_gs_api):

        get_gs_api.spreadsheet = None

        assert get_gs_api.get_worksheets() == None

    def test_google_sheet_get_worksheets(self, get_gs_api):

        for key in get_gs_api.get_worksheets().keys():
            assert get_gs_api.worksheets.get(
                key).id == get_gs_api.get_worksheets().get(key).id


@pytest.mark.google
class TestExportHandler:
    """
    Unit tests for ExportHandler Class

    """

    def getting_worksheet(self):

        try:
            gs_api = GoogleSheet.init_google_sheet().google_sheet_client.open_by_key(
                SHEET_CONSTANTS.get(
                    'SPREADSHEET_ID').get(
                        TEST_SCHOOL_NAME).get(
                            'test'))
            worksheet = gs_api.get_worksheet_by_id(
                SHEET_CONSTANTS.get('DATABASE_SHEET_ID'))
        except:
            time.sleep(120)
            return self.getting_worksheet()

        return worksheet

    @pytest.fixture
    def get_worksheet(self):
        return self.getting_worksheet()

    def getting_sheet_data(self, worksheet):

        try:
            sheet_data = worksheet.get_all_records(
                empty2zero=False, head=1)

        except:
            time.sleep(120)
            return self.getting_sheet_data(worksheet)
        return sheet_data

    @pytest.fixture
    def get_sheet_data(self, get_worksheet):

        return self.getting_sheet_data(get_worksheet)

    @pytest.fixture
    def get_export_handler_obj(self, get_sheet_data):
        return ExportHandler(get_sheet_data, TEST_SCHOOL_NAME)

    @pytest.fixture
    def get_school_name(self):
        pattern = '^(RO|AL)-(CNA|HHA|SG|ESOL)-([0-9]{1,3})-[0-9]{4}-[A-Z]{2}$'
        return re.search(pattern, TEST_STUDENT_ID).group(1)

    @pytest.fixture
    def get_converted_school_name(self, get_school_name):
        if get_school_name == 'RO':
            return 'STI'
        elif get_school_name == 'AL':
            return 'ST2'

    @pytest.fixture
    def get_prog_name(self):
        pattern = '^(RO|AL)-(CNA|HHA|SG|ESOL)-([0-9]{1,3})-[0-9]{4}-[A-Z]{2}$'
        return re.search(pattern, TEST_STUDENT_ID).group(2)

    @pytest.fixture
    def get_rot_num(self):
        pattern = '^(RO|AL)-(CNA|HHA|SG|ESOL)-([0-9]{1,3})-[0-9]{4}-[A-Z]{2}$'
        return re.search(pattern, TEST_STUDENT_ID).group(3)

    def test_auth_and_get_sheet(self, get_worksheet):
        test_worksheet = ExportHandler.auth_and_get_sheet(
            TEST_SPREADSHEET_ID, TEST_DB_SHEET_ID)

        assert test_worksheet.id == get_worksheet.id

    def test_run(self, get_worksheet, get_export_handler_obj):
        # assert that run will produce the same object type as creating an obj straight from constructor
        assert type(ExportHandler.run(get_worksheet, TEST_SCHOOL_NAME)) == type(
            get_export_handler_obj)

    def test_ExportHandler_init(self, get_export_handler_obj):
        if hasattr(get_export_handler_obj, 'initial_data') and \
           hasattr(get_export_handler_obj, 'school_name') and \
           hasattr(get_export_handler_obj, 'each_data') and \
           hasattr(get_export_handler_obj, 'final_dump') and \
           hasattr(get_export_handler_obj, 'student_uuids') and \
           hasattr(get_export_handler_obj, 'rotation_uuids') and \
           hasattr(get_export_handler_obj, 'program_uuids') and \
           hasattr(get_export_handler_obj, 'school_uuids'):

            assert True
        else:
            assert False

    def test_get_data(self, get_export_handler_obj, mocker):
        mocked_validate_and_rekey = mocker.patch.object(
            get_export_handler_obj, 'validate_and_rekey')
        mocked_build_ref = mocker.patch.object(
            get_export_handler_obj, 'build_ref')
        mocked_finalize_each_record = mocker.patch.object(
            get_export_handler_obj, 'finalize_each_record', return_value='__SUCCESS_RETURN__')

        final_data = get_export_handler_obj.get_data()

        mocked_validate_and_rekey.assert_called_once()
        mocked_build_ref.assert_called_once()
        mocked_finalize_each_record.assert_called_once()

        # the returned data must be in an iterable and is in dictionary, for json conversion
        for data in final_data:
            if data != '__SUCCESS_RETURN__':
                assert False

    def jsonable(self, data):

        try:
            json.loads(json.dumps(data))
            return True
        except:
            return False

    def test_validate_and_rekey(self, get_export_handler_obj, mocker):
        # NOTE: this function will be responsible to call mapper with index and header
        mocked_mapper = mocker.patch.object(get_export_handler_obj, 'mapper')

        get_export_handler_obj.validate_and_rekey(TEST_INDEX, TEST_RECORD)

        mocked_mapper.assert_called_with(TEST_INDEX, TEST_RECORD_HEADER)
        # assert False

    def test_mapper_success(self, get_export_handler_obj, mocker):
        # NOTE: this function will be responsible to call rekey. And individual validation
        for key, validation in TEST_HEADERS_AND_VALIDATIONS.items():

            mocked_validation = mocker.patch(
                f'sms.utils.DataHandler.{validation}')

            mocked_rekey = mocker.patch.object(get_export_handler_obj, 'rekey')

            get_export_handler_obj.mapper(TEST_INDEX, key)

            mocked_validation.assert_called_once()
            mocked_rekey.assert_called_once()

    def test_mapper_failure(self, get_export_handler_obj, mocker):

        mocked_rekey = mocker.patch.object(get_export_handler_obj, 'rekey')
        with pytest.raises(ValidationError):
            get_export_handler_obj.mapper(
                TEST_INDEX, 'test failure header key')

            mocked_rekey.assert_not_called()

    def test_rekey(self, get_export_handler_obj):

        get_export_handler_obj.rekey('test value', 'test key')

        assert get_export_handler_obj.each_data.get('test key') == 'test value'

    def test_build_ref_success(self, get_export_handler_obj, mocker, monkeypatch):
        mocked_check_school_ref = mocker.patch.object(
            get_export_handler_obj, 'check_school_ref')

        mocked_check_prog_ref = mocker.patch.object(
            get_export_handler_obj, 'check_prog_ref')

        mocked_check_rot_ref = mocker.patch.object(
            get_export_handler_obj, 'check_rot_ref', return_value=TEST_ROTATION_UUID)

        monkeypatch.setitem(get_export_handler_obj.each_data,
                            'student_id', TEST_STUDENT_ID)

        result = get_export_handler_obj.build_ref()

        mocked_check_school_ref.assert_called_once()
        mocked_check_prog_ref.assert_called_once()
        mocked_check_rot_ref.assert_called_once()

        assert result == TEST_ROTATION_UUID

    def test_buid_ref_failure(self, get_export_handler_obj, mocker, monkeypatch):
        mocked_check_school_ref = mocker.patch.object(
            get_export_handler_obj, 'check_school_ref')

        mocked_check_prog_ref = mocker.patch.object(
            get_export_handler_obj, 'check_prog_ref')

        mocked_check_rot_ref = mocker.patch.object(
            get_export_handler_obj, 'check_rot_ref', return_value=TEST_ROTATION_UUID)

        monkeypatch.setitem(get_export_handler_obj.each_data,
                            'student_id', 'a none matching student id')

        with pytest.raises(ValidationError):
            get_export_handler_obj.build_ref()

            mocked_check_school_ref.assert_not_called()
            mocked_check_prog_ref.assert_not_called()
            mocked_check_rot_ref.assert_not_called()

    def test_check_school_ref_wo_school_uuids_school_exists(self, get_export_handler_obj, get_school_name, monkeypatch):
        def does_exist(school_name__exact):
            return ExistQuerySet()

        class ExistQuerySet:
            def exists(self):
                return True

        def found_school(school_name__exact):
            return SchoolQuery()

        class SchoolQuery:
            def __init__(self):
                self.school_uuid = 'test school uuid'

        monkeypatch.setattr(School.objects, 'filter', does_exist)
        monkeypatch.setattr(School.objects, 'get', found_school)
        monkeypatch.setattr(get_export_handler_obj, 'school_uuids', [])

        assert get_export_handler_obj.check_school_ref(
            get_school_name) == 'test school uuid'

    def test_check_school_ref_wo_school_uuids_school_doesnt_exist(self, get_export_handler_obj, get_school_name, mocker, monkeypatch):
        def doesnt_exist(school_name__exact):
            return NonExistQuerySet()

        class NonExistQuerySet:
            def exists(self):
                return False

        monkeypatch.setattr(School.objects, 'filter', doesnt_exist)
        monkeypatch.setattr(get_export_handler_obj, 'school_uuids', [])
        mocked_get_pk = mocker.patch.object(
            get_export_handler_obj, 'get_pk', return_value='test school pk')

        pk = get_export_handler_obj.check_school_ref(
            get_school_name)

        mocked_get_pk.assert_called_once()

        assert get_export_handler_obj.school_uuids != []
        assert get_export_handler_obj.final_dump != []
        assert pk == 'test school pk'

    def test_check_school_ref_with_school_uuids(self, get_export_handler_obj, get_school_name, get_converted_school_name, monkeypatch):
        monkeypatch.setattr(get_export_handler_obj, 'school_uuids', [
                            ('test school pk', get_converted_school_name)])

        assert get_export_handler_obj.check_school_ref(
            get_school_name) == 'test school pk'

    def test_check_prog_ref_wo_prog_uuids_prog_exists(self, get_export_handler_obj, get_school_name, get_prog_name, monkeypatch):
        def does_exist(school__school_uuid__exact, program_name__exact):
            return ExistQuerySet()

        class ExistQuerySet:
            def exists(self):
                return True

        def found_program(school__school_uuid__exact, program_name__exact):
            return SchoolQuery()

        class SchoolQuery:
            def __init__(self):
                self.program_uuid = 'test program uuid'

        monkeypatch.setattr(Program.objects, 'filter', does_exist)
        monkeypatch.setattr(Program.objects, 'get', found_program)
        monkeypatch.setattr(get_export_handler_obj, 'program_uuids', [])

        assert get_export_handler_obj.check_prog_ref(
            get_school_name,
            get_prog_name,
            'test school uuid') == 'test program uuid'

    def test_check_prog_ref_wo_prog_uuids_prog_doesnt_exists(self, get_export_handler_obj, get_school_name, get_prog_name, monkeypatch, mocker):
        def doesnt_exist(school__school_uuid__exact, program_name__exact):
            return NoneExistQuerySet()

        class NoneExistQuerySet:
            def exists(self):
                return False

        monkeypatch.setattr(Program.objects, 'filter', doesnt_exist)
        monkeypatch.setattr(get_export_handler_obj, 'program_uuids', [])
        mocked_get_pk = mocker.patch.object(
            get_export_handler_obj, 'get_pk', return_value='test program pk')

        pk = get_export_handler_obj.check_prog_ref(
            get_prog_name,
            get_school_name,
            'test school uuid')

        mocked_get_pk.assert_called_once()

        assert get_export_handler_obj.program_uuids != []
        assert get_export_handler_obj.final_dump != []
        assert pk == 'test program pk'

    def test_check_prog_ref_with_prog_uuids(self, get_export_handler_obj, get_school_name, get_prog_name, monkeypatch):
        monkeypatch.setattr(get_export_handler_obj, 'program_uuids', [(
                            'test program pk', get_prog_name, get_school_name)])

        assert get_export_handler_obj.check_prog_ref(
            get_prog_name, get_school_name, 'test school uuid') == 'test program pk'

    def test_check_rot_ref_wo_rot_uuids_rot_exists(self, get_export_handler_obj, get_school_name, get_prog_name,  get_rot_num, monkeypatch):
        def does_exist(program__program_uuid__exact, rotation_number__exact):
            return ExistQuerySet()

        class ExistQuerySet:
            def exists(self):
                return True

        def found_rot(program__program_uuid__exact, rotation_number__exact):
            return RotationQuery()

        class RotationQuery:
            def __init__(self):
                self.rotation_uuid = 'test rotation uuid'

        monkeypatch.setattr(Rotation.objects, 'filter', does_exist)
        monkeypatch.setattr(Rotation.objects, 'get', found_rot)
        monkeypatch.setattr(get_export_handler_obj, 'rotation_uuids', [])

        assert get_export_handler_obj.check_rot_ref(
            get_rot_num,
            get_prog_name,
            get_school_name,
            'test program uuid') == 'test rotation uuid'

    def test_check_rot_ref_wo_rot_uuids_rot_doesnt_exist(self,  get_export_handler_obj, get_school_name, get_prog_name, get_rot_num, mocker, monkeypatch):
        def doesnt_exist(program__program_uuid__exact, rotation_number__exact):
            return NonExistQuerySet()

        class NonExistQuerySet:
            def exists(self):
                return False

        monkeypatch.setattr(Rotation.objects, 'filter', doesnt_exist)
        monkeypatch.setattr(get_export_handler_obj, 'rotation_uuids', [])

        mocked_get_pk = mocker.patch.object(
            get_export_handler_obj, 'get_pk', return_value='test rotation pk')

        pk = get_export_handler_obj.check_rot_ref(
            get_rot_num,
            get_prog_name,
            get_school_name,
            'test program uuid')

        mocked_get_pk.assert_called_once()

        assert get_export_handler_obj.rotation_uuids != []
        assert get_export_handler_obj.final_dump != []
        assert pk == 'test rotation pk'

    def test_check_rot_ref_with_rot_uuids(self, get_export_handler_obj, get_school_name, get_prog_name, get_rot_num, monkeypatch):
        monkeypatch.setattr(get_export_handler_obj, 'rotation_uuids', [(
                            'test rotation pk', get_rot_num, get_prog_name, get_school_name)])

        assert get_export_handler_obj.check_rot_ref(
            get_rot_num, get_prog_name, get_school_name, 'test program uuid') == 'test rotation pk'

    def test_get_pk(self, get_export_handler_obj, mocker):
        def doesnt_exist(pk__exact):
            return NonExistQuerySet()

        class NonExistQuerySet:
            def exists(self):
                return False

        mocked_filter = mocker.patch(
            'sms.models.Student.objects.filter', return_value=doesnt_exist('test pk'))

        mocked_ensure_unique = mocker.patch.object(
            get_export_handler_obj, 'ensure_unique')

        get_export_handler_obj.get_pk(Student)

        mocked_filter.assert_called_once()
        mocked_ensure_unique.assert_called_once()

    def test_ensure_unique_empty_lists(self, get_export_handler_obj, monkeypatch):
        monkeypatch.setattr(get_export_handler_obj, 'school_uuids', [])
        monkeypatch.setattr(get_export_handler_obj, 'program_uuids', [])
        monkeypatch.setattr(get_export_handler_obj, 'rotation_uuids', [])
        monkeypatch.setattr(get_export_handler_obj, 'student_uuids', [])

        assert get_export_handler_obj.ensure_unique(
            'test uuid', 'Student') == True
        assert get_export_handler_obj.ensure_unique(
            'test uuid', 'Rotation') == True
        assert get_export_handler_obj.ensure_unique(
            'test uuid', 'Program') == True
        assert get_export_handler_obj.ensure_unique(
            'test uuid', 'School') == True

    def test_ensure_unique_matching(self, get_export_handler_obj, monkeypatch):
        monkeypatch.setattr(get_export_handler_obj,
                            'school_uuids', [(SCHOOL_UUID_TO_TEST, 'test school name')])
        monkeypatch.setattr(get_export_handler_obj,
                            'program_uuids', [(PROGRAM_UUID_TO_TEST, 'test program name', 'test school name')])
        monkeypatch.setattr(get_export_handler_obj,
                            'rotation_uuids', [(ROTATION_UUID_TO_TEST, 'test rot num', 'test program name', 'test school name')])
        monkeypatch.setattr(get_export_handler_obj,
                            'student_uuids', [STUDENT_UUID_TO_TEST])

        assert get_export_handler_obj.ensure_unique(
            STUDENT_UUID_TO_TEST, 'Student') == False
        assert get_export_handler_obj.ensure_unique(
            ROTATION_UUID_TO_TEST, 'Rotation') == False
        assert get_export_handler_obj.ensure_unique(
            PROGRAM_UUID_TO_TEST, 'Program') == False
        assert get_export_handler_obj.ensure_unique(
            SCHOOL_UUID_TO_TEST, 'School') == False

    def test_ensure_unique_nonmatching(self, get_export_handler_obj, monkeypatch):
        monkeypatch.setattr(get_export_handler_obj,
                            'school_uuids', [('test school uuid', 'test school name')])
        monkeypatch.setattr(get_export_handler_obj,
                            'program_uuids', [('test program uuid', 'test program name', 'test school name')])
        monkeypatch.setattr(get_export_handler_obj,
                            'rotation_uuids', [('test rotation uuid', 'test rot num', 'test program name', 'test school name')])
        monkeypatch.setattr(get_export_handler_obj,
                            'student_uuids', ['test student uuid'])

        assert get_export_handler_obj.ensure_unique(
            'test uuid', 'Student') == True
        assert get_export_handler_obj.ensure_unique(
            'test uuid', 'Rotation') == True
        assert get_export_handler_obj.ensure_unique(
            'test uuid', 'Program') == True
        assert get_export_handler_obj.ensure_unique(
            'test uuid', 'School') == True

    def test_finalize_each_record(self, get_export_handler_obj, monkeypatch):
        monkeypatch.setitem(get_export_handler_obj.each_data,
                            'total_charges_paid', '1.00')
        monkeypatch.setitem(get_export_handler_obj.each_data,
                            'total_charges_charged', '1.00')
        monkeypatch.setitem(get_export_handler_obj.each_data,
                            'full_name', 'test_full_name')
        result = get_export_handler_obj.finalize_each_record(
            TEST_ROTATION_UUID)

        assert result.get('fields').get('rotation') == TEST_ROTATION_UUID
        assert result.get('fields').get('google_sheet_migrated') == True
        assert result.get('fields').get('google_sheet_migration_issue') == ''
        assert result.get('fields').get('paid') == True

        for currency in [
                'course_cost_currency',
                'total_charges_charged_currency',
                'total_charges_paid_currency',
                'starting_wage_currency']:

            if result.get('fields').get(currency) != 'USD':
                assert False
