import pytest

from authentication.models import Account
from core.common import UserEmailValidator
from rest_framework.exceptions import ValidationError



class Instance:
    def __init__(self):
        self.__SAMPLE_REFERENCE__ = []


@pytest.mark.core
class TestUserEmailValidator:

    @pytest.fixture
    def get_instance_obj(self):
        return Instance()

    def test_user_email_checker(self, mocker):
        mocked__user_check = mocker.patch('core.common.UserEmailValidator._user_check')

        list_ = ['__SAMPLE_LIST__']
        reference = '__SAMPLE_REFERENCE__'
        instance = '__SAMPLE_INSTANCE__'
        partial = True

        UserEmailValidator.user_email_checker(list_, reference, instance, partial)

        mocked__user_check.assert_called_with(list_, instance, reference)

        partial = False

        UserEmailValidator.user_email_checker(list_, reference, instance, partial)

        mocked__user_check.assert_called_with(list_, instance, reference)

        instance = None
        partial = True

        UserEmailValidator.user_email_checker(list_, reference, instance, partial)

        mocked__user_check.assert_called_with(list_, None, reference)

    
    def test__user_check(self, get_instance_obj, mocker):
        mocked__email_filter = mocker.patch('core.common.UserEmailValidator._email_filter')

        list_ = ['__SAMPLE_LIST__']
        reference = '__SAMPLE_REFERENCE__'
        instance = get_instance_obj

        UserEmailValidator._user_check(list_, instance, reference)

        mocked__email_filter.assert_has_calls([mocker.call(mocker.ANY, raise_=True), mocker.call(getattr(instance, reference), raise_=False)])

        instance = None

        UserEmailValidator._user_check(list_, instance, reference)

        mocked__email_filter.assert_called_with(list_, raise_=True)

    
    def test__email_filter_exists(self, monkeypatch):
        def does_exist(email__exact):
            return ExistQuerySet()

        class ExistQuerySet:
            def exists(self):
                return True
        
        monkeypatch.setattr(Account.objects, 'filter', does_exist)

        list_ = ['email_exists@email.com']

        assert UserEmailValidator._email_filter(list_) == list_


    def test__email_filter_not_exist_no_raise(self, monkeypatch):
        def doesnt_exist(email__exact):
            return ExistQuerySet()

        class ExistQuerySet:
            def exists(self):
                return False
        
        monkeypatch.setattr(Account.objects, 'filter', doesnt_exist)

        list_ = ['email_no_exist@email.com']
    
        assert UserEmailValidator._email_filter(list_) != list_


    def test__email_filter_not_exist_w_raise(self, monkeypatch):
        def doesnt_exist(email__exact):
            return ExistQuerySet()

        class ExistQuerySet:
            def exists(self):
                return False
        
        monkeypatch.setattr(Account.objects, 'filter', doesnt_exist)

        list_ = ['email_no_exist@email.com']
    
        with pytest.raises(ValidationError):
            UserEmailValidator._email_filter(list_, raise_=True)