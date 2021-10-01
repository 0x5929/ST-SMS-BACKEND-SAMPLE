from django.db import models

from .utils import DatabaseHelper


class SchoolManager(models.Manager):
    def create_or_update_school(self, validated_data, instance=None):
        return DatabaseHelper.create_or_update(validated_data, instance, self.model)

    def get_query(self, request):
        return super(SchoolManager, self).get_queryset().filter(school_name__exact=request.user.school_name)


class ProgramManager(models.Manager):
    def create_or_update_program(self, validated_data, instance=None):
        return DatabaseHelper.create_or_update(validated_data, instance, self.model)

    def get_query(self, request):
        return super(ProgramManager, self).get_queryset().filter(school__school_name__exact=request.user.school_name)


class RotationManager(models.Manager):
    def create_or_update_rotation(self, validated_data, instance=None):
        return DatabaseHelper.create_or_update(validated_data, instance, self.model)

    def get_query(self, request):
        return super(RotationManager, self).get_queryset().filter(program__school__school_name__exact=request.user.school_name)


class StudentManager(models.Manager):
    def create_or_update_student(self, validated_data, instance=None):
        return DatabaseHelper.create_or_update(validated_data, instance, self.model)

    def get_query(self, request):
        return super(StudentManager, self).get_queryset().filter(rotation__program__school__school_name__exact=request.user.school_name)
