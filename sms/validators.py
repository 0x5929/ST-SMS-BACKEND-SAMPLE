import re


from rest_framework.serializers import ValidationError
from .utils import ExceptionHelper, ValidationHelper

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

    def __init__(self):
        self.err_msg = 'Only limited special characters are allowed, please only enter alphanumeric characters and (, . #).'
        self.pattern = '[A-Za-z0-9,.#\s]{1,150}'

    def __call__(self, value):

        return ValidationHelper.capitalize_string(value) if bool(re.match(self.pattern, value)) else ExceptionHelper.raise_verror(self.err_msg)


# to encourage human intervention, allow for Student ID entry
# otherwise, write a @property for Student.studentID to return desire format
class StudentIDFormat:

    def __init__(self):
        self.err_msg = 'Please follow the following format for the Student ID: "###-MMYY-FL"'
        self.pattern = '^[0-9]{1,3}-[0-9]{4}-[A-Z]{2}$'

    def __call__(self, value):
        return value if bool(re.match(self.pattern, value)) else ExceptionHelper.raise_verror(self.err_msg)
