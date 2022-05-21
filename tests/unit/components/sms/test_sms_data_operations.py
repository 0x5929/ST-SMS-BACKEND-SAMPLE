import pytest
from sms.data_operations import StudentDataStatistics

import datetime

from .sms_constants import YEARS, DATE_RANGES


@pytest.mark.stats
class TestStudentDataStatistics:
    """
    Unit tests for StudentDataStatistics Class util methods

    """

    def test_get_years(self, monkeypatch):

        class NewDate(datetime.date):

            @classmethod
            def today(cls):
                return cls(2022, 1, 1)

        datetime.date = NewDate

        assert StudentDataStatistics.get_years() == YEARS

    def test_get_date_ranges(self, monkeypatch):
        def get_years():
            return YEARS

        monkeypatch.setattr(StudentDataStatistics, 'get_years', get_years)

        assert StudentDataStatistics.get_date_ranges() == DATE_RANGES
