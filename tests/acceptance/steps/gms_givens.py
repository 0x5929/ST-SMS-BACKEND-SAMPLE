from behave import given


from constants import TEST_REG_INST_CNA_USER, TEST_REG_INST_HHA_USER


LOGIN_PATH = '/auth/login/'
LOGIN_PW = 'ye_rui_hu_xiao'


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
