from django.db import models

# proposed change:
# changed 12/28/2021 @2150
# behave tests: passed 12/28/2021 @2154
# pytest tests: passed 12/28/2021 @2157
# if request.user.is_superuser:
#     return super(HHARotationManager, self).get_queryset().all()

# can see all course in the same school (done in permission and views)
# elif request.user.is_admin:
#     return super(HHARotationManager, self).get_queryset().filter(
#         school_name__exact=request.user.school_name)

# limited by only its assigned course (done in permission and views)
# elif request.user.is_staff:
#     return super(HHARotationManager, self).get_queryset().filter(
#         school_name__exact=request.user.school_name)
# limited by only its assigned course and assigned email (done in permission and views)
# else:
#     return super(HHARotationManager, self).get_queryset().filter(
#         school_name__exact=request.user.school_name,
#         instructor_email__exact=request.user.email)


class HHARotationManager(models.Manager):
    def get_query(self, request):
        if request.user.is_superuser:
            return super(HHARotationManager, self).get_queryset().all()

        elif request.user.is_admin:
            return super(HHARotationManager, self).get_queryset().filter(
                school_name__exact=request.user.school_name)

        elif request.user.is_staff:
            return super(HHARotationManager, self).get_queryset().filter(
                school_name__exact=request.user.school_name)
        else:
            return super(HHARotationManager, self).get_queryset().filter(
                school_name__exact=request.user.school_name,
                instructor_email__contains=[request.user.email])


class HHAStudentManager(models.Manager):
    def get_query(self, request):
        if request.user.is_superuser:
            return super(HHAStudentManager, self).get_queryset().all()

        elif request.user.is_admin:
            return super(HHAStudentManager, self).get_queryset().filter(
                rotation__school_name__exact=request.user.school_name)

        elif request.user.is_staff:
            return super(HHAStudentManager, self).get_queryset().filter(
                rotation__school_name__exact=request.user.school_name)
        else:
            return super(HHAStudentManager, self).get_queryset().filter(
                rotation__school_name__exact=request.user.school_name,
                rotation__instructor_email__contains=[request.user.email])


class HHATheoryRecordManager(models.Manager):
    def get_query(self, request):
        if request.user.is_superuser:
            return super(HHATheoryRecordManager, self).get_queryset().all()

        elif request.user.is_admin:
            return super(HHATheoryRecordManager, self).get_queryset().filter(
                student__rotation__school_name__exact=request.user.school_name)

        elif request.user.is_staff:
            return super(HHATheoryRecordManager, self).get_queryset().filter(
                student__rotation__school_name__exact=request.user.school_name)
        else:
            return super(HHATheoryRecordManager, self).get_queryset().filter(
                student__rotation__school_name__exact=request.user.school_name,
                student__rotation__instructor_email__contains=[request.user.email])


class HHAClinicalRecordManager(models.Manager):
    def get_query(self, request):
        if request.user.is_superuser:
            return super(HHAClinicalRecordManager, self).get_queryset().all()

        elif request.user.is_admin:
            return super(HHAClinicalRecordManager, self).get_queryset().filter(
                student__rotation__school_name__exact=request.user.school_name)

        elif request.user.is_staff:
            return super(HHAClinicalRecordManager, self).get_queryset().filter(
                student__rotation__school_name__exact=request.user.school_name)
        else:
            return super(HHAClinicalRecordManager, self).get_queryset().filter(
                student__rotation__school_name__exact=request.user.school_name,
                student__rotation__instructor_email__contains=[request.user.email])
