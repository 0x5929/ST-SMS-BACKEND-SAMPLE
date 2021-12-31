from django.db import models


class CNARotationManager(models.Manager):
    def get_query(self, request):
        if request.user.is_superuser:
            return super(CNARotationManager, self).get_queryset().all()

        elif request.user.is_admin:
            return super(CNARotationManager, self).get_queryset().filter(
                school_name__exact=request.user.school_name)

        elif request.user.is_staff:
            return super(CNARotationManager, self).get_queryset().filter(
                school_name__exact=request.user.school_name)
        else:
            return super(CNARotationManager, self).get_queryset().filter(
                school_name__exact=request.user.school_name,
                instructor_email__contains=[request.user.email])


class CNAStudentManager(models.Manager):

    def get_query(self, request):
        if request.user.is_superuser:
            return super(CNAStudentManager, self).get_queryset().all()

        elif request.user.is_admin:
            return super(CNAStudentManager, self).get_queryset().filter(
                rotation__school_name__exact=request.user.school_name)

        elif request.user.is_staff:
            return super(CNAStudentManager, self).get_queryset().filter(
                rotation__school_name__exact=request.user.school_name)
        else:
            return super(CNAStudentManager, self).get_queryset().filter(
                rotation__school_name__exact=request.user.school_name,
                rotation__instructor_email__contains=[request.user.email])


class CNATheoryRecordManager(models.Manager):

    def get_query(self, request):
        if request.user.is_superuser:
            return super(CNATheoryRecordManager, self).get_queryset().all()

        elif request.user.is_admin:
            return super(CNATheoryRecordManager, self).get_queryset().filter(
                student__rotation__school_name__exact=request.user.school_name)

        elif request.user.is_staff:
            return super(CNATheoryRecordManager, self).get_queryset().filter(
                student__rotation__school_name__exact=request.user.school_name)
        else:
            return super(CNATheoryRecordManager, self).get_queryset().filter(
                student__rotation__school_name__exact=request.user.school_name,
                student__rotation__instructor_email__contains=[request.user.email])


class CNAClinicalRecordManager(models.Manager):

    def get_query(self, request):
        if request.user.is_superuser:
            return super(CNAClinicalRecordManager, self).get_queryset().all()

        elif request.user.is_admin:
            return super(CNAClinicalRecordManager, self).get_queryset().filter(
                student__rotation__school_name__exact=request.user.school_name)

        elif request.user.is_staff:
            return super(CNAClinicalRecordManager, self).get_queryset().filter(
                student__rotation__school_name__exact=request.user.school_name)
        else:
            return super(CNAClinicalRecordManager, self).get_queryset().filter(
                student__rotation__school_name__exact=request.user.school_name,
                student__rotation__instructor_email__contains=[request.user.email])
