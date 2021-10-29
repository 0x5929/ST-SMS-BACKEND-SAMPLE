import json
from behave import given

from tests.factories.accounts import AccountFactory
from fixtures.users import UserTestHelper

LOGIN_PATH = '/auth/login/'
LOGIN_PW = AccountFactory.password

# Logging on as:


@given('logged on as regular office user')
def logged_on_as_reg_user_is_office_true(context):
    # POST to login
    auth_resp = context.browser.request(
        'POST', f'{context.server_url}{LOGIN_PATH}', data={'email': f'{UserTestHelper.TEST_REG_OFF_USER}@localhost', 'password': LOGIN_PW})

    # add server response access token as a cookie of browser
    context.browser.add_cookie(
        {"name": "sms-auth", "value": auth_resp.access_token})

    # making sure that browser's cookie and our authentication response token value are the same
    context.test.assertEqual(context.browser.get_cookie(
        "sms-auth"), auth_resp.access_token)


@given('logged on as regular user with is_office set to false')
def logged_on_as_reg_user_is_office_false(context):
    # POST to login
    auth_resp = context.browser.request(
        'POST', f'{context.server_url}{LOGIN_PATH}', data={'email': f'{UserTestHelper.TEST_REG_USER}@localhost', 'password': LOGIN_PW})

    # add server response access token as a cookie of browser
    context.browser.add_cookie(
        {"name": "sms-auth", "value": auth_resp.access_token})

    # making sure that browser's cookie and our authentication response token value are the same
    context.test.assertEqual(context.browser.get_cookie(
        "sms-auth"), auth_resp.access_token)


@given('logged on as staff office user')
def logged_on_as_staff_user_is_office_true(context):
    # POST to login
    auth_resp = context.browser.request(
        'POST', f'{context.server_url}{LOGIN_PATH}', data={'email': f'{UserTestHelper.TEST_STAFF_OFF_USER}@localhost', 'password': LOGIN_PW})

    # add server response access token as a cookie of browser
    context.browser.add_cookie(
        {"name": "sms-auth", "value": auth_resp.access_token})

    # making sure that browser's cookie and our authentication response token value are the same
    context.test.assertEqual(context.browser.get_cookie(
        "sms-auth"), auth_resp.access_token)


@given('logged on as staff user with is_office set to false')
def logged_on_as_staff_user_is_office_false(context):
    # POST to login
    auth_resp = context.browser.request(
        'POST', f'{context.server_url}{LOGIN_PATH}', data={'email': f'{UserTestHelper.TEST_STAFF_USER}@localhost', 'password': LOGIN_PW})

    # add server response access token as a cookie of browser
    context.browser.add_cookie(
        {"name": "sms-auth", "value": auth_resp.access_token})

    # making sure that browser's cookie and our authentication response token value are the same
    context.test.assertEqual(context.browser.get_cookie(
        "sms-auth"), auth_resp.access_token)


@given('logged on as admin office user')
def logged_on_as_admin_user_is_office_true(context):
    # POST to login
    auth_resp = context.browser.request(
        'POST', f'{context.server_url}{LOGIN_PATH}', data={'email': f'{UserTestHelper.TEST_ADMIN_OFF_USER}@localhost', 'password': LOGIN_PW})

    # add server response access token as a cookie of browser
    context.browser.add_cookie(
        {"name": "sms-auth", "value": auth_resp.access_token})

    # making sure that browser's cookie and our authentication response token value are the same
    context.test.assertEqual(context.browser.get_cookie(
        "sms-auth"), auth_resp.access_token)


@ given('logged on as admin user with is_office set to false')
def logged_on_as_admin_user_is_office_false(context):
    # POST to login
    auth_resp = context.browser.request(
        'POST', f'{context.server_url}{LOGIN_PATH}', data={'email': f'{UserTestHelper.TEST_ADMIN_USER}@localhost', 'password': LOGIN_PW})

    # add server response access token as a cookie of browser
    context.browser.add_cookie(
        {"name": "sms-auth", "value": auth_resp.access_token})

    # making sure that browser's cookie and our authentication response token value are the same
    context.test.assertEqual(context.browser.get_cookie(
        "sms-auth"), auth_resp.access_token)


@ given('logged on as superuser')
def logged_on_as_superuser(context):
    # POST to login
    auth_resp = context.browser.request(
        'POST', f'{context.server_url}{LOGIN_PATH}', json={'email': f'{UserTestHelper.TEST_SUPERUSER}@localhost', 'password': LOGIN_PW})

    print('hello world: ', auth_resp.status_code)
    print('path: ', f'{context.server_url}{LOGIN_PATH}')
    print('data:', {
          'email': f'{UserTestHelper.TEST_SUPERUSER}@localhost', 'password': LOGIN_PW})

    # add server response access token as a cookie of browser
    context.browser.add_cookie(
        {"name": "sms-auth", "value": auth_resp.access_token})

    # making sure that browser's cookie and our authentication response token value are the same
    context.test.assertEqual(context.browser.get_cookie(
        "sms-auth"), auth_resp.access_token)
