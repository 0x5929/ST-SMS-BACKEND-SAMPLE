from django.apps import apps
from rest_framework.exceptions import ValidationError


class GMSValidator:

    # used by RecordSerializers
    @staticmethod
    def reference_does_not_change_on_updates(value, instance, reference):
        err_msg = 'This field is immutable once set.'

        if not instance:
            return value
        # note we may need to convert into str(UUID) if this complains
        if instance and str(getattr(instance, reference)) == str(value):
            return value

        raise ValidationError(err_msg)

    @staticmethod
    def get_current_rot_id(serializer, data):
        err_msg = 'Cannot find the corresponding student\'s rotation uuid to the school record.'

        # get current student obj
        current_student_uuid = data.get('student').student_uuid

        if 'CNA' in serializer.Meta.model.__name__:
            StudentModel = apps.get_model('gms', 'CNAStudent')

        elif 'HHA' in serializer.Meta.model.__name__:
            StudentModel = apps.get_model('gms', 'HHAStudent')

        else:
            raise ValidationError(err_msg)

        return StudentModel.objects.get(
            student_uuid__exact=current_student_uuid).rotation.rotation_uuid

    @classmethod
    def no_duplicate_records(cls, serializer, data):
        err_msg = 'The record you are trying to add already exist in this rotation.'

        if serializer.partial and \
                not data.get('student') or \
                not data.get('topic'):

            return data

        # first get current rotation ID:
        current_rot_id = cls.get_current_rot_id(serializer, data)

        # second, grab topic
        current_topic = data.get('topic')

        # third, check if record exist with rotation_id and record topic
        # apps.get_model is like import
        RecordModel = apps.get_model('gms', serializer.Meta.model.__name__)
        record_exists = RecordModel.objects.filter(student__rotation__rotation_uuid__exact=current_rot_id,
                                                   topic__exact=current_topic).exists()

        # if we are POSTing a record that already exists
        if not serializer.instance and record_exists:

            raise ValidationError(err_msg)

        elif serializer.instance and \
                record_exists and \
                getattr(serializer.instance, 'topic') != current_topic:

            raise ValidationError(err_msg)

        return data

    @staticmethod
    def no_duplicate_students(serializer, data):
        err_msg = 'The student you are trying to add already exist in this rotation.'

        if serializer.partial and \
            (not data.get('rotation') or
             not data.get('first_name') or
             not data.get('last_name')):
            return data

        current_rot_id = data.get('rotation').rotation_uuid
        first_name = data.get('first_name')
        last_name = data.get('last_name')

        # check if the current rotation has a student with the same first and last name
        # checking for both CNAStudent and HHAStudent models
        StudentModel = apps.get_model('gms', serializer.Meta.model.__name__)
        student_exists = StudentModel.objects.filter(
            rotation__rotation_uuid__exact=current_rot_id,
            first_name__iexact=first_name,
            last_name__iexact=last_name).exists()

        # raise validationError, duplicate student in rotation
        if student_exists:
            raise ValidationError(err_msg)

        return data

    # used by RotationSerializers

    @staticmethod
    def date_checker(data, instance, partial=False):
        err_msg = 'Please enter an end date after the start date of the program rotation.'

        if partial and (not data.get('start_date') and not data.get('end_date')):
            return data

        elif partial and not data.get('start_date'):
            data['start_date'] = getattr(instance, 'start_date')

        elif partial and not data.get('end_date'):
            data['end_date'] = getattr(instance, 'end_date')

        if data.get('start_date') > data.get('end_date'):
            raise ValidationError(err_msg)

        return data

    # used by RotationSerializers
    @staticmethod
    def ensure_same_school_name(data, request, lvl, partial=False):

        err_msg = 'You may only work on your own school\'s resource, please try changing the school name.'

        if lvl == 'Rotation':

            if partial and not data.get('school_name'):
                return data

            if request.user.school_name == data.get('school_name') or request.user.is_superuser:
                return data

            else:
                raise ValidationError(err_msg)

        if lvl == 'Student':
            # student.rotation.school_name
            if partial: 
                if not data.get('rotation') or \
                        data.get('rotation') and not getattr(data.get('rotation'), 'school_name'):
                    return data

            if request.user.school_name == getattr(data.get('rotation'), 'school_name') or request.user.is_superuser:
                return data

            else:
                raise ValidationError(err_msg)

        if lvl == 'Record':
            # record.student.rotation.school_name
            if partial:
                if not data.get('student') or \
                        data.get('student') and \
                        not getattr(getattr(data.get('student'), 'rotation'), 'school_name'):
                    return data

            if request.user.school_name == getattr(getattr(data.get('student'), 'rotation'), 'school_name') or request.user.is_superuser:
                return data

            else:
                raise ValidationError(err_msg)

    @staticmethod
    def ensure_no_dup_rot(data, model_name, instance, partial):
        err_msg = 'You are adding/updating a rotation number that already exists, please try again.'

        if partial and (not data.get('school_name') or not data.get('rotation_num')):
            return data

        RotationModel = apps.get_model('gms', model_name)
        rot_exists = RotationModel.objects.filter(
            school_name__exact=data.get('school_name'), rotation_num__exact=data.get('rotation_num')).exists()

        # if we are updating, then there should be exactly one rotation pulled from our request as per school_name and rotation number
        # also that the rotation number did not change from original one, meaning we cannot update rot number once rotation is created!
        if instance and rot_exists and str(data.get('rotation_num')) == str(getattr(instance, 'rotation_num')):
            return data

        elif instance and not rot_exists:
            return data
        # if we are not updating, then there should be exactly 0 rotation, and we cannot duplicate rotations in the same school
        elif not instance and not rot_exists:
            return data
        else:
            raise ValidationError(err_msg)

    @classmethod
    def final_rot_validation(cls, serializer, data):
        request = serializer.context.get('request')
        data = cls.date_checker(data, serializer.instance,
                                partial=serializer.partial)

        same_school_verified = cls.ensure_same_school_name(
            data, request, 'Rotation', partial=serializer.partial)

        return cls.ensure_no_dup_rot(same_school_verified, serializer.Meta.model.__name__, serializer.instance, partial=serializer.partial)

    @classmethod
    def final_student_validation(cls, serializer, data):
        request = serializer.context.get('request')

        same_school_verified_data = cls.ensure_same_school_name(
            data, request, 'Student', partial=serializer.partial)

        return cls.no_duplicate_students(serializer, same_school_verified_data)

    @classmethod
    def final_record_validation(cls, serializer, data):
        request = serializer.context.get('request')

        same_school_verified_data = cls.ensure_same_school_name(
            data, request, 'Record', partial=serializer.partial)

        return cls.no_duplicate_records(serializer, same_school_verified_data)
