import pytest

from authentication.models import Account


@pytest.mark.auth
class TestAccountModelAttrRequirement:
    """
    Testing Minimum Attribute Requirements for the Account model

    """

    def test_account_model_attr(self):
        acct = Account.objects.all().first()

        if hasattr(acct, 'email') and \
           hasattr(acct, 'username') and \
           hasattr(acct, 'first_name') and \
           hasattr(acct, 'last_name') and \
           hasattr(acct, 'date_joined') and \
           hasattr(acct, 'phone_number') and \
           hasattr(acct, 'is_office') and \
           hasattr(acct, 'is_recruit') and \
           hasattr(acct, 'is_instructor') and \
           hasattr(acct, 'programs') and \
           hasattr(acct, 'school_name') and \
           hasattr(acct, 'is_active') and \
           hasattr(acct, 'is_staff') and \
           hasattr(acct, 'is_admin') and \
           hasattr(acct, 'is_superuser'):
           assert True
        else:
            assert False