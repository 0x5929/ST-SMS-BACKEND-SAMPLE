import re

from django.db.models.expressions import Value
from rest_framework.exceptions import ValidationError


class GMSCNAValidator:

    @staticmethod
    def reference_does_not_change_on_updates(value, instance, reference):
        err_msg = 'This field is immutable once set.'

        if not instance:
            return value
        # note we may need to convert into str(UUID) if this complains
        if instance and str(getattr(instance, reference)) == str(value):
            return value

        raise ValidationError(err_msg)

    # used by CNAStudentSerializer
    @staticmethod
    def no_duplicate_students(data):
        err_msg = 'The student you are trying to add already exist in this rotation.'

        current_rot_id = data.get('rotation').get('rotation_uuid')
        first_name = data.get('first_name')
        last_name = data.get('last_name')

        # check if the current rotation has a student with the same first and last name
        from .models import CNAStudent, CNARotation
        student = CNAStudent.objects.filter(
            rotation__rotation_id__exact=current_rot_id,
            first_name__iexact=first_name,
            last_name__iexact=last_name)

        # raise validationError, duplicate student in rotation
        if len(student) > 0:
            raise ValidationError(err_msg)

        return data

    # used by CNARotationSerializer
    @staticmethod
    def date_checker(data):
        err_msg = 'Please enter an end date after the start date of the program rotation.'

        if data.get('start_date') > data.get('end_date'):
            raise ValidationError(err_msg)

        return data

    # used by CNARotationSerializer

    @staticmethod
    def ensure_same_school_name(data, request):
        err_msg = 'You may only work on your own school\'s resource, please try changing the school name.'
        request_user_school = request.user.school_name
        school_name = data.get('school_name')

        if request_user_school == school_name:
            return data
        else:
            raise ValidationError(err_msg)
