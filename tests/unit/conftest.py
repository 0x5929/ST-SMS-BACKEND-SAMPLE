import pytest

from django.core.management import call_command


@pytest.fixture(scope='session')
def api_client():
    from rest_framework.test import APIClient

    client = APIClient()
    yield client
    del client


@pytest.fixture(scope='session', autouse=True)
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'test-initial-users.json',
                     'test-initial-accountEmails.json', 'test-initial-sms-data.json', 'test-initial-gms-data.json')


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass