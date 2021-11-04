
from django.test.testcases import TestCase
import os
import django
from django.test.runner import DiscoverRunner


def before_all(context):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings.test'
    django.setup()
    context.test_runner = DiscoverRunner()
    context.test_runner.setup_test_environment()
    context.old_db_config = context.test_runner.setup_databases()


def after_all(context):
    context.test_runner.teardown_databases(context.old_db_config)
    context.test_runner.teardown_test_environment()


def before_scenario(context, scenario):

    context.test = TestCase
    context.test.fixtures = ['test-initial-users.json',
                             'test-initial-accountEmails.json', 'test-initial-sms-data.json']

    context.test.setUpClass()

    from rest_framework.test import APIClient
    context.test.client = APIClient()


def after_scenario(context, scenario):
    context.test.tearDownClass()
    del context.test
