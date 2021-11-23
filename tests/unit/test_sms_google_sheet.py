import pytest
import gspread

from random import randrange
from oauth2client.service_account import ServiceAccountCredentials

from sms.google_sheets import GoogleSheet
from sms.models import Student
from sms.utils import DataHandler
from sms.constants import SHEET_CONSTANTS

from tests.acceptance.steps.constants import STUDENT_UUID_TO_TEST

pytestmark = pytest.mark.django_db


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

# class TestExportHandler:
#     """
#     Unit tests for ExportHandler Class

#     """
    
    