import pytest

from sms.permissions import IsAuthenticatedOfficeUserToReadOnly, IsAuthenticatedOfficeUserToReadOnly, IsAuthenticatedOfficeStaff, IsAuthenticatedOfficeAdmin, IsSuperuser


class User:
    def __init__(self, superuser=False):
        self.is_superuser = superuser
        self.school_name = 'STI'
        self.is_authenticated = None
        self.is_office = None


class Request:
    def __init__(self, superuser=False):
        self.user = User(superuser=superuser)
        self.method = None


class View:
    def __init__(self):
        self.view = None


@pytest.mark.current
@pytest.mark.sms
class TestSMSPermissions:
    @pytest.fixture
    def get_request_obj(self):
        return Request(superuser=False)

    @pytest.fixture
    def get_request_super_obj(self):
        return Request(superuser=True)

    @pytest.fixture
    def get_view_obj(self):
        return View()

    def test_IsAuthenticatedOfficeUserToReadOnly_message(self):
        assert IsAuthenticatedOfficeUserToReadOnly.message == 'Sorry, you must be at least authenticated and an office user to perform this action.'

    def test_test_IsAuthenticatedOfficeUserToReadOnly_message_has_permission(self, get_request_obj, get_view_obj):
        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = True
        get_request_obj.method = 'GET'

        assert IsAuthenticatedOfficeUserToReadOnly(
        ).has_permission(get_request_obj, get_view_obj) == True

        get_request_obj.user.is_authenticated = False
        get_request_obj.user.is_office = True
        get_request_obj.method = 'GET'

        assert IsAuthenticatedOfficeUserToReadOnly(
        ).has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = False
        get_request_obj.method = 'GET'

        assert IsAuthenticatedOfficeUserToReadOnly(
        ).has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = True
        get_request_obj.method = 'POST'

        assert IsAuthenticatedOfficeUserToReadOnly(
        ).has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = True
        get_request_obj.method = 'PUT'

        assert IsAuthenticatedOfficeUserToReadOnly(
        ).has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = True
        get_request_obj.method = 'PATCH'

        assert IsAuthenticatedOfficeUserToReadOnly(
        ).has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = True
        get_request_obj.method = 'DELETE'

        assert IsAuthenticatedOfficeUserToReadOnly(
        ).has_permission(get_request_obj, get_view_obj) == False
