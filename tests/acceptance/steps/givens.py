from behave import given

from constants import (TEST_SUPERUSER,
                       TEST_ADMIN_USER,
                       TEST_ADMIN_OFF_USER,
                       TEST_STAFF_USER,
                       TEST_STAFF_OFF_USER,
                       TEST_REG_USER,
                       TEST_REG_OFF_USER,
                       TEST_REG_INST_CNA_USER,
                       TEST_REG_INST_HHA_USER)

LOGIN_PATH = '/auth/login/'
LOGIN_PW = 'ye_rui_hu_xiao'

# Logging on as:

# NOTE: BELOW ARE SMS RELATED @GIVENS


@given('logged on as regular office user')
def logged_on_as_reg_user_is_office_true(context):
    # POST to login
    auth_resp = context.test.client.post(f'{LOGIN_PATH}', {
                                         'email': f'{TEST_REG_OFF_USER}@localhost', 'password': LOGIN_PW})

    context.access_token = auth_resp.data['access_token']
    context.csrf_token = auth_resp.cookies['csrftoken']


@given('logged on as regular user with is_office set to false')
def logged_on_as_reg_user_is_office_false(context):
    # POST to login
    auth_resp = context.test.client.post(f'{LOGIN_PATH}', {
                                         'email': f'{TEST_REG_USER}@localhost', 'password': LOGIN_PW})

    context.access_token = auth_resp.data['access_token']
    context.csrf_token = auth_resp.cookies['csrftoken']


@given('logged on as staff office user')
def logged_on_as_staff_user_is_office_true(context):
    # POST to login
    auth_resp = context.test.client.post(f'{LOGIN_PATH}', {
                                         'email': f'{TEST_STAFF_OFF_USER}@localhost', 'password': LOGIN_PW})

    context.access_token = auth_resp.data['access_token']
    context.csrf_token = auth_resp.cookies['csrftoken']


@given('logged on as staff user with is_office set to false')
def logged_on_as_staff_user_is_office_false(context):
    # POST to login
    auth_resp = context.test.client.post(f'{LOGIN_PATH}', {
                                         'email': f'{TEST_STAFF_USER}@localhost', 'password': LOGIN_PW})

    context.access_token = auth_resp.data['access_token']
    context.csrf_token = auth_resp.cookies['csrftoken']


@given('logged on as admin office user')
def logged_on_as_admin_user_is_office_true(context):
    # POST to login
    auth_resp = context.test.client.post(f'{LOGIN_PATH}', {
                                         'email': f'{TEST_ADMIN_OFF_USER}@localhost', 'password': LOGIN_PW})

    context.access_token = auth_resp.data['access_token']
    context.csrf_token = auth_resp.cookies['csrftoken']


@given('logged on as admin user with is_office set to false')
def logged_on_as_admin_user_is_office_false(context):
    # POST to login
    auth_resp = context.test.client.post(f'{LOGIN_PATH}', {
                                         'email': f'{TEST_ADMIN_USER}@localhost', 'password': LOGIN_PW})

    context.access_token = auth_resp.data['access_token']
    context.csrf_token = auth_resp.cookies['csrftoken']


@given('logged on as superuser')
def logged_on_as_superuser(context):
    # POST to login
    auth_resp = context.test.client.post(
        f'{LOGIN_PATH}', {'email': f'{TEST_SUPERUSER}@localhost', 'password': LOGIN_PW}, format='json')

    context.access_token = auth_resp.data['access_token']
    context.csrf_token = auth_resp.cookies['csrftoken']


@given('no initial logon')
def no_user_logon(context):
    pass


# NOTE: BELOW ARE GMS RELATED @GIVENS
#

@given('logged on as cna instructor user')
def logged_on_as_reg_cna_inst(context):
    # POST to login
    auth_resp = context.test.client.post(f'{LOGIN_PATH}', {
                                         'email': f'{TEST_REG_INST_CNA_USER}@localhost', 'password': LOGIN_PW})

    context.access_token = auth_resp.data['access_token']
    context.csrf_token = auth_resp.cookies['csrftoken']


@given('logged on as hha instructor user')
def logged_on_as_reg_hha_inst(context):
    # POST to login
    auth_resp = context.test.client.post(f'{LOGIN_PATH}', {
                                         'email': f'{TEST_REG_INST_HHA_USER}@localhost', 'password': LOGIN_PW})

    context.access_token = auth_resp.data['access_token']
    context.csrf_token = auth_resp.cookies['csrftoken']
