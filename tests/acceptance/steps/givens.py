from behave import given


# Logging on as:
@given('logged on as regular office user')
def logged_on_as_reg_user_is_office_true(context):
    pass


@given('logged on as regular user with is_office set to false')
def logged_on_as_reg_user_is_office_false(context):
    pass

@given('logged on as staff office user')
def logged_on_as_staff_user_is_office_true(context):
    pass


@given('logged on as staff user with is_office set to false')
def logged_on_as_staff_user_is_office_false(context):
    pass
