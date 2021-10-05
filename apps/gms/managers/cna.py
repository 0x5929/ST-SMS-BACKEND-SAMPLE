import uuid
from django.db import models


class CNARotationManager(models.Manager):
    def get_query(self, request):
        if request.user.is_superuser:
            return super(CNARotationManager, self).get_queryset().all()

        elif request.user.is_admin:
            return super(CNARotationManager, self).get_queryset().all()

        elif request.use.is_staff:
            return super(CNARotationManager, self).get_queryset().filter(
                school_name__exact=request.user.school_name)
        else:
            return super(CNARotationManager, self).get_queryset().filter(
                school_name__exact=request.user.school_name,
                instructor_email__exact=request.user.email)


class CNAStudentManager(models.Manager):

    def get_query(self, request):
        if request.user.is_superuser:
            return super(CNAStudentManager, self).get_queryset().all()

        elif request.user.is_admin:
            return super(CNAStudentManager, self).get_queryset().all()

        elif request.use.is_staff:
            return super(CNAStudentManager, self).get_queryset().filter(
                rotation__school_name__exact=request.user.school_name)
        else:
            return super(CNAStudentManager, self).get_queryset().filter(
                rotation__school_name__exact=request.user.school_name,
                rotation__instructor_email__exact=request.user.email)

    def create_or_update(self, validated_data, instance=None):
        # grab rotation ID from request
        rotation_id = uuid.UUID(str(validated_data.get('rotation')))

        # retrieve rotation from DB
        from ..models import CNARotation
        rotation = CNARotation.objects.get(rotation_uuid__exact=rotation_id)

        # add rotation to student obj
        validated_data['rotation'] = rotation

        return (instance, validated_data) if instance else validated_data


class CNATheoryRecordManager(models.Manager):

    def get_query(self, request):
        if request.user.is_superuser:
            return super(CNATheoryRecordManager, self).get_queryset().all()

        elif request.user.is_admin:
            return super(CNATheoryRecordManager, self).get_queryset().all()

        elif request.use.is_staff:
            return super(CNATheoryRecordManager, self).get_queryset().filter(
                student__rotation__school_name__exact=request.user.school_name)
        else:
            return super(CNATheoryRecordManager, self).get_queryset().filter(
                student__rotation__school_name__exact=request.user.school_name,
                student__rotation__instructor_email__exact=request.user.email)

    def create_or_update(self, validated_data, instance=None):
        # grab student ID from request
        student_id = uuid.UUID(str(validated_data.get('student')))

        # retrive student from DB
        from ..models import CNAStudent
        student = CNAStudent.objects.get(student_uuid__exact=student_id)

        # add student to record object
        validated_data['student'] = student

        return (instance, validated_data) if instance else validated_data


class CNAClinicalRecordManager(models.Manager):

    def get_query(self, request):
        if request.user.is_superuser:
            return super(CNAClinicalRecordManager, self).get_queryset().all()

        elif request.user.is_admin:
            return super(CNAClinicalRecordManager, self).get_queryset().all()

        elif request.use.is_staff:
            return super(CNAClinicalRecordManager, self).get_queryset().filter(
                student__rotation__school_name__exact=request.user.school_name)
        else:
            return super(CNAClinicalRecordManager, self).get_queryset().filter(
                student__rotation__school_name__exact=request.user.school_name,
                student__rotation__instructor_email__exact=request.user.email)

    def create_or_update(self, validated_data, instance=None):
        # grab student ID from request
        student_id = uuid.UUID(str(validated_data.get('student')))

        # retrive student from DB
        from ..models import CNAStudent
        student = CNAStudent.objects.get(student_uuid__exact=student_id)

        # add student to record object
        validated_data['student'] = student

        return (instance, validated_data) if instance else validated_data
