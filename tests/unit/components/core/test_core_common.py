from inspect import _GetMembersPredicate
import pytest

from core.common import UserEmailValidator
from rest_framework.exceptions import ValidationError

@pytest.mark.core
class TestUserEmailValidator:

    def test_user_email_checker(self, mocker):
        mocked__user_check = mocker.patch('core.common.UserEmailValidator._user_check')

        list_ = ['__SAMPLE_LIST__']
        reference = '__SAMPLE_REFERENCE__'
        instance = '__SAMPLE_INSTANCE__'
        partial = True

        UserEmailValidator.user_email_checker(list_, reference, instance, partial)

        mocked__user_check.assert_called_with(list_, instance, reference)