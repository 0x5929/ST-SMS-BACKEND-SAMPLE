from django.db import models

#from .utils import DatabaseHandler


class SchoolManager(models.Manager):

    def get_query(self, request):
        if request.user.is_superuser:
            return super(SchoolManager, self).get_queryset().all()

        return super(SchoolManager, self).get_queryset().filter(school_name__exact=request.user.school_name)


class ProgramManager(models.Manager):

    def get_query(self, request):
        if request.user.is_superuser:
            return super(ProgramManager, self).get_queryset().all()

        return super(ProgramManager, self).get_queryset().filter(school__school_name__exact=request.user.school_name)


class RotationManager(models.Manager):

    def get_query(self, request):
        if request.user.is_superuser:
            return super(RotationManager, self).get_queryset().all()
        return super(RotationManager, self).get_queryset().filter(program__school__school_name__exact=request.user.school_name)


class StudentManager(models.Manager):

    def get_query(self, request):
        if request.user.is_superuser:
            return super(StudentManager, self).get_queryset().all()
        return super(StudentManager, self).get_queryset().filter(rotation__program__school__school_name__exact=request.user.school_name)
