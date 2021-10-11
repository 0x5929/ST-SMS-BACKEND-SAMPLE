from rest_framework.test import APIClient
from selenium import webdriver

import os
# This is necessary for all installed apps to be recognized, for some reason.
os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings.dev-settings'


def django_ready(context, scenario):
    context.test.client = APIClient()
    context.browser = webdriver.PhantomJS()
    context.browser.implicitly_wait(1)
    context.server_url = 'http://localhost:8000'


def before_all(context):
    context.fixtures = ['all-initial-data.json']


def after_all(context):
    context.fixtures = []
    context.browser.quit()
