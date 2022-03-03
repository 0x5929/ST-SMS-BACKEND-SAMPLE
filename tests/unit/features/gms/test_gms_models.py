import pytest

from gms.models import cnaRotation


@pytest.mark.sms
class TestGMSModelAttrRequirement:
    """
    Testing Mininum Attribute Requirements for each GMS models

    """

    # def test_cnaRotation_model_attr(self):
    #     cnaRotation = cnaRotation.objects.get(school_uuid__exact=GMS_CNAROTATION_UUID_TO_TEST)

    #     if hasattr(cnaRotation, 'school_uuid') and \
    #        hasattr(cnaRotation, 'school_name') and \
    #        hasattr(cnaRotation, 'school_code') and \
    #        hasattr(cnaRotation, 'school_address') and \
    #        hasattr(cnaRotation, 'year_founded'):

    #         assert True
    #     else:
    #         assert False