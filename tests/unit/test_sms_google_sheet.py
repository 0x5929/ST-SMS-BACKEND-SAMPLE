import pytest

from sms.google_sheets import GoogleSheet
from sms.models import Student
from sms.utils import DataHandler
from tests.acceptance.steps.constants import FILTER_PARAMS, STUDENT_UUID_TO_TEST

pytestmark = pytest.mark.django_db

class TestGoogleSheet:
    """
    Unit tests for Google Sheet Class
    
    """

    @pytest.fixture
    def get_student_obj(self):
        return Student.objects.get(student_uuid__exact=STUDENT_UUID_TO_TEST)

    def test_master_sheet_save(self, get_student_obj, mocker):

        data = DataHandler.data_conversion(get_student_obj)

        gs_api = GoogleSheet.init_google_sheet(data.get('school_name'))

        mocked_init_google = mocker.patch('sms.google_sheets.GoogleSheet.init_google_sheet', return_value=gs_api)

        mocked_match = mocker.patch.object(gs_api, 'match')

        mocked_match.return_value = None   

        mocked_create = mocker.patch.object(gs_api, 'create')

        GoogleSheet.master_sheet_save(data)
        mocked_match.assert_called_once()
        mocked_init_google.assert_called_once()
        mocked_create.assert_called_once()


        mocked_match.return_value = 3
        mocked_update = mocker.patch.object(gs_api, 'update')
        mocked_create = mocker.patch.object(gs_api, 'create')
        data = DataHandler.data_conversion(get_student_obj)
        GoogleSheet.master_sheet_save(data)
        mocked_create.assert_called_once()
        mocked_update.assert_called_once()
        # data = {'school_name', FILTER_PARAMS.get('school_name')}




        # mocked_init_google.return_value = gs_api


        # mocked_finalized_data = mocker.patch('sms.utils.DataHandler.finalize_data')
        # mocked_finalized_data.return_value = []



# class TestExportHandler:
#     """
#     Unit tests for ExportHandler Class

#     """
#     pass