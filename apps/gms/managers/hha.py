import uuid
from django.db import models


class HHARotationManager(models.Manager):
    def get_query(self, request):
        if request.user.is_superuser:
            return super(HHARotationManager, self).get_queryset().all()

        elif request.user.is_admin:
            return super(HHARotationManager, self).get_queryset().all()

        elif request.user.is_staff:
            return super(HHARotationManager, self).get_queryset().filter(
                school_name__exact=request.user.school_name)
        else:
            return super(HHARotationManager, self).get_queryset().filter(
                school_name__exact=request.user.school_name,
                instructor_email__exact=request.user.email)


class HHAStudentManager(models.Manager):
    def get_query(self, request):
        if request.user.is_superuser:
            return super(HHAStudentManager, self).get_queryset().all()

        elif request.user.is_admin:
            return super(HHAStudentManager, self).get_queryset().all()

        elif request.user.is_staff:
            return super(HHAStudentManager, self).get_queryset().filter(
                rotation__school_name__exact=request.user.school_name)
        else:
            return super(HHAStudentManager, self).get_queryset().filter(
                rotation__school_name__exact=request.user.school_name,
                rotation__instructor_email__exact=request.user.email)

    # def create_or_update(self, validated_data, instance=None):
    #     # grab rotation ID from request
    #     rotation_id = uuid.UUID(
    #         str(validated_data.get('rotation').rotation_uuid))

    #     # retrieve rotation from DB
    #     from ..models import HHARotation
    #     rotation = HHARotation.objects.get(rotation_uuid__exact=rotation_id)

    #     # add rotation to student obj
    #     validated_data['rotation'] = rotation

    #     return (instance, validated_data) if instance else validated_data


class HHATheoryRecordManager(models.Manager):
    def get_query(self, request):
        if request.user.is_superuser:
            return super(HHATheoryRecordManager, self).get_queryset().all()

        elif request.user.is_admin:
            return super(HHATheoryRecordManager, self).get_queryset().all()

        elif request.user.is_staff:
            return super(HHATheoryRecordManager, self).get_queryset().filter(
                student__rotation__school_name__exact=request.user.school_name)
        else:
            return super(HHATheoryRecordManager, self).get_queryset().filter(
                student__rotation__school_name__exact=request.user.school_name,
                student__rotation__instructor_email__exact=request.user.email)

    # def create_or_update(self, validated_data, instance=None):
    #     # grab student ID from request
    #     student_id = uuid.UUID(str(validated_data.get('student').student_uuid))

    #     # retrive student from DB
    #     from ..models import HHAStudent
    #     student = HHAStudent.objects.get(student_uuid__exact=student_id)

    #     # add student to record object
    #     validated_data['student'] = student

    #     return (instance, validated_data) if instance else validated_data


class HHAClinicalRecordManager(models.Manager):
    def get_query(self, request):
        if request.user.is_superuser:
            return super(HHAClinicalRecordManager, self).get_queryset().all()

        elif request.user.is_admin:
            return super(HHAClinicalRecordManager, self).get_queryset().all()

        elif request.user.is_staff:
            return super(HHAClinicalRecordManager, self).get_queryset().filter(
                student__rotation__school_name__exact=request.user.school_name)
        else:
            return super(HHAClinicalRecordManager, self).get_queryset().filter(
                student__rotation__school_name__exact=request.user.school_name,
                student__rotation__instructor_email__exact=request.user.email)

    # def create_or_update(self, validated_data, instance=None):
    #     # grab student ID from request
    #     student_id = uuid.UUID(str(validated_data.get('student').student_uuid))

    #     # retrive student from DB
    #     from ..models import HHAStudent
    #     student = HHAStudent.objects.get(student_uuid__exact=student_id)

    #     # add student to record object
    #     validated_data['student'] = student

    #     return (instance, validated_data) if instance else validated_data
