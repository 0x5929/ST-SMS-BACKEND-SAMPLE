import pytest
import pytest
from django.db import models

from cms.managers import ClientManager, NoteManager

from .cms_constants import TEST_CLIENT, TEST_NOTE

from tests.common_constants import TEST_SCHOOL_NAME

class User:
    def __init__(self, superuser=False, admin=False):
        self.is_superuser = superuser
        self.is_admin = admin
        self.school_name = TEST_SCHOOL_NAME
        self.email = '__TEST_EMAIL__'


class Request:
    def __init__(self, superuser=False, admin=False):
        self.user = User(superuser=superuser, admin=admin)


@pytest.mark.cms
@pytest.mark.current
class TestCMSManagers:

    @pytest.fixture
    def get_request_obj(self):
        return Request()

    @pytest.fixture
    def get_request_super_obj(self):
        return Request(superuser=True)

    @pytest.fixture
    def get_request_admin_obj(self):
        return Request(admin=True)

    
    def test_client_get_superuser(self, get_request_super_obj, monkeypatch):
        class GetClientQuerySet:
            def all(self):
                return TEST_CLIENT

        def get_client_qs(self):
            return GetClientQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset', get_client_qs)

        assert ClientManager().get_query(get_request_super_obj) == TEST_CLIENT


    def test_client_get_admin(self, get_request_admin_obj, monkeypatch):
        class GetClientQuerySet:
            def filter(self, school_name__exact):
                return TEST_CLIENT

        def get_client_qs(self):
            return GetClientQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset', get_client_qs)

        assert ClientManager().get_query(get_request_admin_obj) == TEST_CLIENT


    def test_client_get_reg_user(self, get_request_obj, monkeypatch):
        class GetClientQuerySet:
            def filter(self, school_name__exact, recruit_emails__overlap):
                return TEST_CLIENT

        def get_client_qs(self):
            return GetClientQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset', get_client_qs)

        assert ClientManager().get_query(get_request_obj) == TEST_CLIENT



    def test_note_get_superuser(self, get_request_super_obj, monkeypatch):
        class GetClientQuerySet:
            def all(self):
                return TEST_NOTE

        def get_note_qs(self):
            return GetClientQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset', get_note_qs)

        assert NoteManager().get_query(get_request_super_obj) == TEST_NOTE


    def test_note_get_admin(self, get_request_admin_obj, monkeypatch):
        class GetClientQuerySet:
            def filter(self, client__school_name__exact):
                return TEST_NOTE

        def get_note_qs(self):
            return GetClientQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset', get_note_qs)

        assert NoteManager().get_query(get_request_admin_obj) == TEST_NOTE


    def test_note_get_reg_user(self, get_request_obj, monkeypatch):
        class GetClientQuerySet:
            def filter(self, client__school_name__exact, client__recruit_emails__overlap):
                return TEST_NOTE

        def get_note_qs(self):
            return GetClientQuerySet()

        monkeypatch.setattr(models.Manager, 'get_queryset', get_note_qs)

        assert NoteManager().get_query(get_request_obj) == TEST_NOTE





