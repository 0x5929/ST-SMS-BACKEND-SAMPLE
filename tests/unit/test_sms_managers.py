import pytest

from sms.managers import SchoolManager, ProgramManager, RotationManager, StudentManager

class User:
    def __init__(self, superuser=False):
        self.is_superuser = superuser
        self.school_name = None


class Request:
    def __init__(self, superuser=False):
        self.user = User(superuser=superuser)


class GetSchoolQuerySet:
    def filter(self, school_name__exact):
        pass

    def all(self):
        pass

class GetProgramQuerySet:
    def filter(self, school__school_name__exact):
        pass

    def all(self):
        pass

class GetRotationQuerySet:
    def filter(self, program__school__school_name__exact):
        pass

    def all(self):
        pass

class GetStudentQuerySet:
    def filter(self, rotation__program__school__school_name__exact):
        pass

    def all(self):
        pass


@pytest.fixture(scope='class')
def get_request_obj():
    return Request(superuser=False)

@pytest.fixture(scope='class')
def get_request_super_obj():
    return Request(superuser=True)

@pytest.fixture(scope='class')
def get_queryset_obj(mocker):
    pass 

@pytest.mark.current
@pytest.mark.usefixtures('get_request_obj', 'get_request_super_obj')
class TestSchoolManager:
    def test_get_query_reg_user(self, get_request_obj, mocker):
        mocked_super = mocker.patch('django.db.models.Manager.get_queryset')
    def test_get_query_super_user(self, get_request_super_obj):
        pass

class TestProgramManager:
    def test_get_query(self):
        pass

class TestRotationManager:
    def test_get_query(self):
        pass

class TestStudentManager:
    def test_get_query(self):
        pass