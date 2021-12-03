import pytest

from sms.permissions import IsAuthenticatedOfficeUserToReadOnly, IsAuthenticatedOfficeUserButCannotDelete, IsAuthenticatedOfficeStaff, IsAuthenticatedOfficeAdmin, IsSuperuser


class User:
    def __init__(self, superuser=False):
        self.is_superuser = superuser
        self.school_name = 'STI'
        self.is_authenticated = None
        self.is_office = None
        self.is_staff = None
        self.is_admin = None

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


    def test_IsAuthenticatedOfficeUserButCannotDelete_message(self):
        assert IsAuthenticatedOfficeUserButCannotDelete.message == 'Sorry, you must be an office user to perform this action.'


    def test_IsAuthenticatedOfficeUserButCannotDelete_has_permission(self, get_request_obj, get_view_obj):
        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = True
        get_request_obj.method = 'GET'

        assert IsAuthenticatedOfficeUserButCannotDelete(
        ).has_permission(get_request_obj, get_view_obj) == True

        get_request_obj.user.is_authenticated = False
        get_request_obj.user.is_office = True
        get_request_obj.method = 'GET'

        assert IsAuthenticatedOfficeUserButCannotDelete(
        ).has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = False
        get_request_obj.method = 'GET'

        assert IsAuthenticatedOfficeUserButCannotDelete(
        ).has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = True
        get_request_obj.method = 'POST'

        assert IsAuthenticatedOfficeUserButCannotDelete(
        ).has_permission(get_request_obj, get_view_obj) == True

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = True
        get_request_obj.method = 'PUT'

        assert IsAuthenticatedOfficeUserButCannotDelete(
        ).has_permission(get_request_obj, get_view_obj) == True

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = True
        get_request_obj.method = 'PATCH'

        assert IsAuthenticatedOfficeUserButCannotDelete(
        ).has_permission(get_request_obj, get_view_obj) == True

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = True
        get_request_obj.method = 'DELETE'

        assert IsAuthenticatedOfficeUserButCannotDelete(
        ).has_permission(get_request_obj, get_view_obj) == False


    def test_IsAuthenticatedOfficeStaff_message(self):
        assert IsAuthenticatedOfficeStaff.message == 'Sorry, you must be an office administrator to perform this action.'

    def test_IsAuthenticatedOfficeStaff_has_permission(self, get_request_obj, get_view_obj):
        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = True
        get_request_obj.user.is_staff = True
        get_request_obj.method = 'GET'

        assert IsAuthenticatedOfficeStaff(
        ).has_permission(get_request_obj, get_view_obj) == True

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = True
        get_request_obj.user.is_staff = True
        get_request_obj.method = 'POST'

        assert IsAuthenticatedOfficeStaff(
        ).has_permission(get_request_obj, get_view_obj) == True

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = True
        get_request_obj.user.is_staff = True
        get_request_obj.method = 'PUT'

        assert IsAuthenticatedOfficeStaff(
        ).has_permission(get_request_obj, get_view_obj) == True

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = True
        get_request_obj.user.is_staff = True
        get_request_obj.method = 'PATCH'

        assert IsAuthenticatedOfficeStaff(
        ).has_permission(get_request_obj, get_view_obj) == True

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = True
        get_request_obj.user.is_staff = True
        get_request_obj.method = 'DELETE'

        assert IsAuthenticatedOfficeStaff(
        ).has_permission(get_request_obj, get_view_obj) == True

        get_request_obj.user.is_authenticated = False
        get_request_obj.user.is_office = True
        get_request_obj.user.is_staff = True
        get_request_obj.method = 'GET'

        assert IsAuthenticatedOfficeStaff(
        ).has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = False
        get_request_obj.user.is_staff = True
        get_request_obj.method = 'GET'

        assert IsAuthenticatedOfficeStaff(
        ).has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = True
        get_request_obj.user.is_staff = False
        get_request_obj.method = 'GET'

        assert IsAuthenticatedOfficeStaff(
        ).has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = False
        get_request_obj.user.is_office = True
        get_request_obj.user.is_staff = True
        get_request_obj.method = 'POST'

        assert IsAuthenticatedOfficeStaff(
        ).has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = False
        get_request_obj.user.is_staff = True
        get_request_obj.method = 'POST'

        assert IsAuthenticatedOfficeStaff(
        ).has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = True
        get_request_obj.user.is_staff = False
        get_request_obj.method = 'POST'

        assert IsAuthenticatedOfficeStaff(
        ).has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = False
        get_request_obj.user.is_office = True
        get_request_obj.user.is_staff = True
        get_request_obj.method = 'PATCH'

        assert IsAuthenticatedOfficeStaff(
        ).has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = False
        get_request_obj.user.is_staff = True
        get_request_obj.method = 'PATCH'

        assert IsAuthenticatedOfficeStaff(
        ).has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = True
        get_request_obj.user.is_staff = False
        get_request_obj.method = 'PATCH'

        assert IsAuthenticatedOfficeStaff(
        ).has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = False
        get_request_obj.user.is_office = True
        get_request_obj.user.is_staff = True
        get_request_obj.method = 'PUT'

        assert IsAuthenticatedOfficeStaff(
        ).has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = False
        get_request_obj.user.is_staff = True
        get_request_obj.method = 'PUT'

        assert IsAuthenticatedOfficeStaff(
        ).has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = True
        get_request_obj.user.is_staff = False
        get_request_obj.method = 'PUT'

        assert IsAuthenticatedOfficeStaff(
        ).has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = False
        get_request_obj.user.is_office = True
        get_request_obj.user.is_staff = True
        get_request_obj.method = 'DELETE'

        assert IsAuthenticatedOfficeStaff(
        ).has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = False
        get_request_obj.user.is_staff = True
        get_request_obj.method = 'DELETE'

        assert IsAuthenticatedOfficeStaff(
        ).has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = True
        get_request_obj.user.is_staff = False
        get_request_obj.method = 'DELETE'

        assert IsAuthenticatedOfficeStaff(
        ).has_permission(get_request_obj, get_view_obj) == False

    def test_IsAuthenticatedOfficeAdmin_message(self):
        assert IsAuthenticatedOfficeAdmin.message == 'Sorry, you must be an office administrator to perform this action.'

    def test_IsAuthenticatedOfficeAdmin_has_permission(self, get_request_obj, get_view_obj):
        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = True
        get_request_obj.user.is_admin = True
        get_request_obj.method = 'GET'

        assert IsAuthenticatedOfficeAdmin(
        ).has_permission(get_request_obj, get_view_obj) == True

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = True
        get_request_obj.user.is_admin = True
        get_request_obj.method = 'POST'

        assert IsAuthenticatedOfficeAdmin(
        ).has_permission(get_request_obj, get_view_obj) == True

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = True
        get_request_obj.user.is_admin = True
        get_request_obj.method = 'PUT'

        assert IsAuthenticatedOfficeAdmin(
        ).has_permission(get_request_obj, get_view_obj) == True

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = True
        get_request_obj.user.is_admin = True
        get_request_obj.method = 'PATCH'

        assert IsAuthenticatedOfficeAdmin(
        ).has_permission(get_request_obj, get_view_obj) == True

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = True
        get_request_obj.user.is_admin = True
        get_request_obj.method = 'DELETE'

        assert IsAuthenticatedOfficeAdmin(
        ).has_permission(get_request_obj, get_view_obj) == True

        get_request_obj.user.is_authenticated = False
        get_request_obj.user.is_office = True
        get_request_obj.user.is_admin = True
        get_request_obj.method = 'GET'

        assert IsAuthenticatedOfficeAdmin(
        ).has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = False
        get_request_obj.user.is_admin = True
        get_request_obj.method = 'GET'

        assert IsAuthenticatedOfficeAdmin(
        ).has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = True
        get_request_obj.user.is_admin = False
        get_request_obj.method = 'GET'

        assert IsAuthenticatedOfficeAdmin(
        ).has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = False
        get_request_obj.user.is_office = True
        get_request_obj.user.is_admin = True
        get_request_obj.method = 'POST'

        assert IsAuthenticatedOfficeAdmin(
        ).has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = False
        get_request_obj.user.is_admin = True
        get_request_obj.method = 'POST'

        assert IsAuthenticatedOfficeAdmin(
        ).has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = True
        get_request_obj.user.is_admin = False
        get_request_obj.method = 'POST'

        assert IsAuthenticatedOfficeAdmin(
        ).has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = False
        get_request_obj.user.is_office = True
        get_request_obj.user.is_admin = True
        get_request_obj.method = 'PATCH'

        assert IsAuthenticatedOfficeAdmin(
        ).has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = False
        get_request_obj.user.is_admin = True
        get_request_obj.method = 'PATCH'

        assert IsAuthenticatedOfficeAdmin(
        ).has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = True
        get_request_obj.user.is_admin = False
        get_request_obj.method = 'PATCH'

        assert IsAuthenticatedOfficeAdmin(
        ).has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = False
        get_request_obj.user.is_office = True
        get_request_obj.user.is_admin = True
        get_request_obj.method = 'PUT'

        assert IsAuthenticatedOfficeAdmin(
        ).has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = False
        get_request_obj.user.is_admin = True
        get_request_obj.method = 'PUT'

        assert IsAuthenticatedOfficeAdmin(
        ).has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = True
        get_request_obj.user.is_admin = False
        get_request_obj.method = 'PUT'

        assert IsAuthenticatedOfficeAdmin(
        ).has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = False
        get_request_obj.user.is_office = True
        get_request_obj.user.is_admin = True
        get_request_obj.method = 'DELETE'

        assert IsAuthenticatedOfficeAdmin(
        ).has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = False
        get_request_obj.user.is_admin = True
        get_request_obj.method = 'DELETE'

        assert IsAuthenticatedOfficeAdmin(
        ).has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_office = True
        get_request_obj.user.is_admin = False
        get_request_obj.method = 'DELETE'

        assert IsAuthenticatedOfficeAdmin(
        ).has_permission(get_request_obj, get_view_obj) == False

    def test_IsSuperuser_message(self):
        assert IsSuperuser.message == 'Sorry, you must be a superuser to perform this action.'

    def test_IsSuperuser_has_permission(self,get_request_obj, get_view_obj):
        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_superuser = True

        assert IsSuperuser(
        ).has_permission(get_request_obj, get_view_obj) == True

        get_request_obj.user.is_authenticated = False
        get_request_obj.user.is_superuser = True

        assert IsSuperuser(
        ).has_permission(get_request_obj, get_view_obj) == False

        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_superuser = False

        assert IsSuperuser(
        ).has_permission(get_request_obj, get_view_obj) == False