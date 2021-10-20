from rest_framework.test import APIClient
from seleniumrequests import Chrome

from ...fixtures.users import UserTestHelper

import os
# This is necessary for all installed apps to be recognized, for some reason.
os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings.dev-settings'


def django_ready(context, scenario):
    context.test.client = APIClient()
    context.browser = Chrome()
    context.browser.implicitly_wait(1)
    context.server_url = 'http://localhost:8000'


def before_all(context):
    context.fixtures = ['all-initial-data.json', 'initial-test-sms-data.json']

    UserTestHelper.create_user_fixtures()


def after_all(context):
    context.fixtures = []
    context.browser.quit()
