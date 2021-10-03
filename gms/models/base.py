import uuid
from django.db import models


class BaseRotation(models.Model):
    class Meta:
        app_label = 'gms'

    rotation_uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    start_date = models.DateField()
    end_date = models.DateField()

    instructor_email = models.EmailField()


class BaseStudent(models.Model):
    class Meta:
        app_label = 'gms'

    student_uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
