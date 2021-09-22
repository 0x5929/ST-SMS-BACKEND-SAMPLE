from django.db import models
from .utils import DatabaseHelper


class SchoolManager(models.Manager):
    def create_or_update_school(self, validated_data, instance=None):
        return DatabaseHelper.create_or_update(validated_data, instance, self.model)

class ProgramManager(models.Manager):
    def create_or_update_program(self, validated_data, instance=None):
        return DatabaseHelper.create_or_update(validated_data, instance, self.model)

class RotationManager(models.Manager):
    def create_or_update_rotation(self, validated_data, instance=None):
        return DatabaseHelper.create_or_update(validated_data, instance, self.model)

class StudentManager(models.Manager):
    def create_or_update_student(self, validated_data, instance=None):
        return DatabaseHelper.create_or_update(validated_data, instance, self.model)