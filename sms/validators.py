from rest_framework.serializers import ValidationError

"""
    Custom Validators for serializers.py
"""

class ReferenceObjDoesNotChangeOnUpdates:
    requires_context =True
    def __init__(self, reference):
        self.reference = reference
        self.error_details = {self.reference: "This field is immutable once set."}

    def __call__(self, value, serializer):
        # updates
        if serializer.instance:
            return value if str(getattr(serializer.instance, self.referece)) == value else self.raise_error(self.error_details)
        # creates
        else : return value

    
    def raise_error(self, details):
        raise ValidationError(details)