from rest_framework.exceptions import ValidationError


# class ExceptionHandler():

#     @staticmethod
#     def raise_verror(self, msg):
#         raise ValidationError(msg)


class FilterHandler:

    @staticmethod
    def is_valid_query_params(query_params, fields):
        for key in query_params.keys():
            if key not in fields:
                return False
        return True