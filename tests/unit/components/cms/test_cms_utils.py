import pytest

from cms.utils import FilterHandler
from cms.filters import CMSNoteFilter, CMSClientFilter

from .cms_constants import (TEST_CLIENT_QUERY_PARAMS_SUCCESS,
                        TEST_NOTE_QUERY_PARAMS_SUCCESS,
                        TEST_QUERY_PARAMS_FAILURE)

@pytest.mark.cms
class TestFilterHandler:
    """
    Unit tests for FilterHandler class

    """

    def test_is_valid_query_params_client(self):
        assert FilterHandler.is_valid_query_params(
            TEST_CLIENT_QUERY_PARAMS_SUCCESS, CMSClientFilter.Meta.fields) == True

        assert FilterHandler.is_valid_query_params(
            TEST_QUERY_PARAMS_FAILURE, CMSClientFilter.Meta.fields) == False

    def test_is_valid_query_params_note(self):
        assert FilterHandler.is_valid_query_params(
            TEST_NOTE_QUERY_PARAMS_SUCCESS, CMSNoteFilter.Meta.fields) == True

        assert FilterHandler.is_valid_query_params(
            TEST_QUERY_PARAMS_FAILURE, CMSNoteFilter.Meta.fields) == False
