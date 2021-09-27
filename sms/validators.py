import re
from .utils import ExceptionHelper

"""
    Custom Validators for serializers.py
"""


class ReferenceObjDoesNotChangeOnUpdates:
    requires_context = True

    def __init__(self, reference):
        self.reference = reference
        self.err_msg = "This field is immutable once set."

    def __call__(self, value, serializer):
        # updates
        if serializer.instance:
            return value if str(getattr(serializer.instance, self.referece)) == value else ExceptionHelper.raise_verror(self.err_msg)
        # creates
        else:
            return value


class NoSpecialCharactersAndCapitalizeString:
    requires_context = True

    def __init__(self, fields):
        self.fields = fields
        self.err_msg = 'Only limited special characters are allowed, please only enter alphanumeric characters and (, . #).'
        self.pattern = '[A-Za-z0-9,.#\s]{1,150}'

    def __call__(self, value, serializer):
        for field in self.fields:
            if not bool(re.match(self.pattern, serializer[self.fields].value())):
                ExceptionHelper.raise_verror(self.err_msg)
            else:
                self.clean(value)

    def clean(value):
        return value.strip().capitalize()


# to encourage human intervention, allow for Student ID entry
# otherwise, write a @property for Student.studentID to return desire format
class StudentIDFormat:

    def __init__(self):
        self.err_msg = 'Please follow the following format for the student ID: "###-MMYY-FL"'
        self.pattern = '^[0-9]{1,3}-[0-9]{4}-[A-Z]{2}$'

    def __call__(self, value):
        return value if bool(re.match(self.pattern, value)) else ExceptionHelper.raise_verror(self.err_msg)


class StrictPhoneNumberFormat:
    def __init__(self):
        self.err_msg = 'Please follow the following example format for the phone number: "888-888-8888"'
        self.pattern = '^[0-9]{3}-[0-9]{3}-[0-9]{4}$'

    def __call__(self, value):
        return value if bool(re.match(self.pattern, value)) else ExceptionHelper.raise_verror(self.err_msg)
