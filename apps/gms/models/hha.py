import uuid

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from .base import BaseRotation, BaseStudent, BaseRecord
from ..managers import HHARotationManager, HHAStudentManager, HHATheoryRecordManager, HHAClinicalRecordManager

from ..constants import CNA_HHA_INSTRUCTOR_TITLES, CLINICAL_SITE_NAMES, HHA_THEORY_TOPICS, HHA_CLINICAL_TOPICS

# NOTE Please remember to import the ModelClasses below on __init__.py file


class HHARotation(BaseRotation):
    class Meta:
        app_label = 'gms'
        verbose_name = 'HHA Rotation'

    rotation_num = models.PositiveIntegerField()

    instructor_title = models.CharField(
        max_length=50, choices=CNA_HHA_INSTRUCTOR_TITLES)

    clinical_site = models.CharField(
        max_length=50, choices=CLINICAL_SITE_NAMES)

    objects = HHARotationManager()

    @property
    def id_(self):
        return f'HHA Rotation #{self.rotation_num}'

    def __str__(self):
        return self.id_


class HHAStudent(BaseStudent):
    class Meta:
        app_label = 'gms'
        verbose_name = 'HHA Student'

    rotation = models.ForeignKey(
        HHARotation,
        on_delete=models.CASCADE,
        related_name='hha_students',
        related_query_name='hha_student')

    objects = HHAStudentManager()

    def __str__(self):
        full_name = f'{self.first_name} {self.last_name}'
        return f'{full_name.capitalize()}'


class HHATheoryRecord(BaseRecord):
    class Meta:
        app_label = 'gms'
        verbose_name = 'HHA Theory Record'

    # hha_theory_record_uuid = models.UUIDField(
    #     primary_key=True, default=uuid.uuid4, editable=False)

    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)

    hours_spent = models.PositiveIntegerField()

    test_score = models.IntegerField(validators=[MinValueValidator(0),
                                                 MaxValueValidator(100)], blank=True, null=True)

    topic = models.CharField(max_length=200, choices=HHA_THEORY_TOPICS)

    student = models.ForeignKey(
        HHAStudent,
        on_delete=models.CASCADE,
        related_name='hha_theory_records',
        related_query_name='hha_theory_record')

    objects = HHATheoryRecordManager()

    def __str__(self):
        return str(self.hha_theory_record_uuid)


class HHAClinicalRecord(BaseRecord):
    class Meta:
        app_label = 'gms'
        verbose_name = 'HHA Clinical Record'

    # hha_clinical_record_uuid = models.UUIDField(
    #     primary_key=True, default=uuid.uuid4, editable=False)

    hours_spent = models.PositiveIntegerField()
    comments = models.CharField(max_length=200, blank=True)
    performance_satisfied = models.BooleanField(default=True)

    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)

    start_date = models.DateField()
    end_date = models.DateField()

    topic = models.CharField(max_length=200, choices=HHA_CLINICAL_TOPICS)

    student = models.ForeignKey(
        HHAStudent,
        on_delete=models.CASCADE,
        related_name='hha_clinical_records',
        related_query_name='hha_clinical_record')

    objects = HHAClinicalRecordManager()

    def __str__(self):
        return str(self.hha_clinical_record_uuid)
