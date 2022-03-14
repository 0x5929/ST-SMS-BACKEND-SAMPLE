from tests.common_constants import *


CLIENT_STR = 'Test A'
NOTE_STR = 'd598af07-bbab-44f0-9ba2-94cd58f4ecdf'

TEST_CLIENT = '__TEST_CLIENT__'
TEST_NOTE = '__TEST_NOTE__'

TEST_CLIENT_QUERY_PARAMS_SUCCESS = {
    'first_name' : 'Test',
    'last_name' : 'A',
    'phone_number' : '888-888-8888',
    'email' : 'test@email.com',
    'city' : 'Test',
    'success' : 'false',
    'initial_contact': '2020-11-20'
}

TEST_NOTE_QUERY_PARAMS_SUCCESS = {
    'date' : '2021-10-11',
    'content' : 'Test'
}

TEST_QUERY_PARAMS_FAILURE = {
    '__INCORRECT_PARAM_NAME__': '__RANDOM_STRING__'
}

AUTH_SUPERUSER_MSG = 'Sorry, you must be a superuser to perform this action.'
AUTH_AUTH_RECRUIT_MSG = 'Please be sure to log in with a recruit account and try again.'