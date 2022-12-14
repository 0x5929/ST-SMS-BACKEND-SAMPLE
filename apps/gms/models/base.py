import uuid

from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField

SCHOOL_NAMES = getattr(settings, 'SCHOOL_NAMES')


class BaseRotation(models.Model):
    class Meta:
        app_label = 'gms'

    rotation_uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    school_name = models.CharField(max_length=10, choices=SCHOOL_NAMES)

    start_date = models.DateField()
    end_date = models.DateField()

    instructor_email = ArrayField(models.EmailField())

    def __str__(self):
        return self.rotation_uuid


class BaseStudent(models.Model):
    class Meta:
        app_label = 'gms'

    student_uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    makeup_student = models.BooleanField(default=False)

    def __str__(self):
        return self.student_uuid


class BaseRecord(models.Model):
    class Meta:
        app_label = 'gms'

    record_uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)
