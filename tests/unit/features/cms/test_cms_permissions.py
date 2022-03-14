import pytest

from cms.permissions import IsSuperuser, IsAuthenticatedAndRecruit

from .cms_constants import AUTH_SUPERUSER_MSG, AUTH_AUTH_RECRUIT_MSG


class User:
    def __init__(self, superuser=False, admin=False):
        self.school_name = 'STI'
        self.is_superuser = superuser
        self.is_admin = admin
        self.is_authenticated = None
        self.programs = None

class Request:
    def __init__(self, superuser=False, admin=False):
        self.user = User(superuser=superuser, admin=admin)
        self.method = None

class View:
    def __init__(self):
        self.view = None

@pytest.mark.cms
class TestCMSPermissions:
    @pytest.fixture
    def get_request_obj(self):
        return Request()

    @pytest.fixture
    def get_request_super_obj(self):
        return Request(superuser=True)

    @pytest.fixture
    def get_request_admin_obj(self):
        return Request(admin=True)

    @pytest.fixture
    def get_view_obj(self):
        return View()

    def test_IsSuperuser_message(self):
        assert IsSuperuser.message == AUTH_SUPERUSER_MSG

    def test_IsSuperuser_has_permission(self,get_request_super_obj, get_view_obj):
        get_request_super_obj.user.is_authenticated = True

        assert IsSuperuser(
        ).has_permission(get_request_super_obj, get_view_obj) == True

        get_request_super_obj.user.is_authenticated = False
        get_request_super_obj.user.is_superuser = True

        assert IsSuperuser(
        ).has_permission(get_request_super_obj, get_view_obj) == False

        get_request_super_obj.user.is_authenticated = True
        get_request_super_obj.user.is_superuser = False

        assert IsSuperuser(
        ).has_permission(get_request_super_obj, get_view_obj) == False

    def test_IsAuthenticatedAndRecruit_message(self):
        assert IsAuthenticatedAndRecruit.message == AUTH_AUTH_RECRUIT_MSG

    def test_IsAuthenticatedAndRecruit_has_permission_success(self, get_request_obj, get_view_obj):
        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_recruit = True

        assert IsAuthenticatedAndRecruit().has_permission(get_request_obj, get_view_obj)  == True

    def test_IsAuthenticatedAndRecruit_has_permission_failure_not_auth(self, get_request_obj, get_view_obj):
        get_request_obj.user.is_authenticated = False
        get_request_obj.user.is_recruit = True

        assert IsAuthenticatedAndRecruit().has_permission(get_request_obj, get_view_obj)  == False

    def test_IsAuthenticatedAndRecruit_has_permission_failure_not_recruit(self, get_request_obj, get_view_obj):
        get_request_obj.user.is_authenticated = True
        get_request_obj.user.is_recruit = False

        assert IsAuthenticatedAndRecruit().has_permission(get_request_obj, get_view_obj)  == False