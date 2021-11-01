
from behave import fixture, use_fixture
import django
from django.core.management import call_command
from django.test.runner import DiscoverRunner
from django.test.testcases import TestCase, LiveServerTestCase
from rest_framework.test import APIClient
import os

# This is necessary for all installed apps to be recognized, for some reason.
os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings.dev-settings'


def before_all(context):
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
                             'test-initial-accountEmails.json', 'initial-test-sms-data.json']

    context.test.setUpClass()

    context.test.client = APIClient()


def after_scenario(context, scenario):
    context.test.tearDownClass()
    del context.test
