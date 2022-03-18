import pytest

from gms.utils import FilterHandler
from gms.filters import (GMSCNAStudentFilter, 
                        GMSCNARotationFilter, 
                        GMSHHARotationFilter, 
                        GMSHHAStudentFilter,
                        GMSCNATheoryRecordFilter,
                        GMSCNAClinicalRecordFilter,
                        GMSHHATheoryRecordFilter,
                        GMSHHAClinicalRecordFilter)

from .gms_constants import (TEST_GMS_ROTATION_QUERY_PARAMS_SUCCESS,
                        TEST_GMS_STUDENT_QUERY_PARAMS_SUCCESS,
                        TEST_GMS_RECORD_QUERY_PARAMS_SUCCESS,
                        TEST_QUERY_PARAMS_FAILURE)

@pytest.mark.gms
@pytest.mark.current
class TestFilterHandler:
    """
    Unit tests for FilterHandler class

    """

    def test_is_valid_query_params_cnaRotation(self):
        assert FilterHandler.is_valid_query_params(
            TEST_GMS_ROTATION_QUERY_PARAMS_SUCCESS, GMSCNARotationFilter.Meta.fields) == True

        assert FilterHandler.is_valid_query_params(
            TEST_QUERY_PARAMS_FAILURE, GMSCNARotationFilter.Meta.fields) == False

    def test_is_valid_query_params_cnaStudent(self):
        assert FilterHandler.is_valid_query_params(
            TEST_GMS_STUDENT_QUERY_PARAMS_SUCCESS, GMSCNAStudentFilter.Meta.fields) == True

        assert FilterHandler.is_valid_query_params(
            TEST_QUERY_PARAMS_FAILURE, GMSCNAStudentFilter.Meta.fields) == False

    def test_is_valid_query_params_cnaTheoryRecord(self):
        assert FilterHandler.is_valid_query_params(
            TEST_GMS_RECORD_QUERY_PARAMS_SUCCESS, GMSCNATheoryRecordFilter.Meta.fields) == True

        assert FilterHandler.is_valid_query_params(
            TEST_QUERY_PARAMS_FAILURE, GMSCNATheoryRecordFilter.Meta.fields) == False

    def test_is_valid_query_params_cnaClinicalRecord(self):
        assert FilterHandler.is_valid_query_params(
            TEST_GMS_RECORD_QUERY_PARAMS_SUCCESS, GMSCNAClinicalRecordFilter.Meta.fields) == True

        assert FilterHandler.is_valid_query_params(
            TEST_QUERY_PARAMS_FAILURE, GMSCNAClinicalRecordFilter.Meta.fields) == False

    def test_is_valid_query_params_hhaRotation(self):
        assert FilterHandler.is_valid_query_params(
            TEST_GMS_ROTATION_QUERY_PARAMS_SUCCESS, GMSHHARotationFilter.Meta.fields) == True

        assert FilterHandler.is_valid_query_params(
            TEST_QUERY_PARAMS_FAILURE, GMSHHARotationFilter.Meta.fields) == False

    def test_is_valid_query_params_hhaStudent(self):
        assert FilterHandler.is_valid_query_params(
            TEST_GMS_STUDENT_QUERY_PARAMS_SUCCESS, GMSHHAStudentFilter.Meta.fields) == True

        assert FilterHandler.is_valid_query_params(
            TEST_QUERY_PARAMS_FAILURE, GMSHHAStudentFilter.Meta.fields) == False

    def test_is_valid_query_params_hhaTheoryRecord(self):
        assert FilterHandler.is_valid_query_params(
            TEST_GMS_RECORD_QUERY_PARAMS_SUCCESS, GMSHHATheoryRecordFilter.Meta.fields) == True

        assert FilterHandler.is_valid_query_params(
            TEST_QUERY_PARAMS_FAILURE, GMSHHATheoryRecordFilter.Meta.fields) == False

    def test_is_valid_query_params_hhaaClinicalRecord(self):
        assert FilterHandler.is_valid_query_params(
            TEST_GMS_RECORD_QUERY_PARAMS_SUCCESS, GMSHHAClinicalRecordFilter.Meta.fields) == True

        assert FilterHandler.is_valid_query_params(
            TEST_QUERY_PARAMS_FAILURE, GMSHHAClinicalRecordFilter.Meta.fields) == False