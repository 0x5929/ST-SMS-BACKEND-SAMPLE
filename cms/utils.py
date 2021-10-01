from rest_framework.exceptions import ValidationError


class ExceptionHandler():

    @staticmethod
    def raise_verror(self, msg):
        raise ValidationError(msg)
