import uuid

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


from .base import BaseRotation, BaseStudent, BaseRecord
from ..managers import CNARotationManager, CNAStudentManager, CNATheoryRecordManager, CNAClinicalRecordManager

from ..constants import CLINICAL_SITE_NAMES, CNA_HHA_INSTRUCTOR_TITLES, CNA_THEORY_TOPICS, CNA_CLINICAL_TOPICS


# NOTE Please remember to import the ModelClasses below on __init__.py file
class CNARotation(BaseRotation):
    class Meta:
        app_label = 'gms'
        verbose_name = 'CNA Rotation'

    rotation_num = models.PositiveIntegerField()

    instructor_title = models.CharField(
        max_length=50, choices=CNA_HHA_INSTRUCTOR_TITLES)

    clinical_site = models.CharField(
        max_length=50, choices=CLINICAL_SITE_NAMES)

    objects = CNARotationManager()

    # @property
    # def id_(self):
    #     return f'{self.school_name}: CNA Rotation #{self.rotation_num}'

    # def __str__(self):
    #     return self.id_

    def __str__(self):
        return f'{self.school_name}: CNA Rotation #{self.rotation_num}'

class CNAStudent(BaseStudent):
    class Meta:
        app_label = 'gms'
        verbose_name = 'CNA Student'

    rotation = models.ForeignKey(
        CNARotation,
        on_delete=models.CASCADE,
        related_name='cna_students',
        related_query_name='cna_student')

    objects = CNAStudentManager()

    def __str__(self):
        return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'


class CNATheoryRecord(BaseRecord):
    class Meta:
        app_label = 'gms'
        verbose_name = 'CNA Theory Record'

    # cna_theory_record_uuid = models.UUIDField(
    #     primary_key=True, default=uuid.uuid4, editable=False)

    hours_spent = models.PositiveIntegerField()
    test_score = models.IntegerField(validators=[MinValueValidator(0),
                                                 MaxValueValidator(100)], blank=True, null=True)

    topic = models.CharField(max_length=200, choices=CNA_THEORY_TOPICS)

    student = models.ForeignKey(
        CNAStudent,
        on_delete=models.CASCADE,
        related_name='cna_theory_records',
        related_query_name='cna_theory_record')

    objects = CNATheoryRecordManager()

    def __str__(self):
        return str(self.record_uuid)


class CNAClinicalRecord(BaseRecord):
    class Meta:
        app_label = 'gms'
        verbose_name = 'CNA Clinical Record'

    # cna_clinical_record_uuid = models.UUIDField(
    #     primary_key=True, default=uuid.uuid4, editable=False)

    comments = models.CharField(max_length=200, blank=True)
    performance_satisfied = models.BooleanField(default=True)

    topic = models.CharField(max_length=200, choices=CNA_CLINICAL_TOPICS)

    student = models.ForeignKey(
        CNAStudent,
        on_delete=models.CASCADE,
        related_name='cna_clinical_records',
        related_query_name='cna_clinical_record')

    objects = CNAClinicalRecordManager()

    def __str__(self):
        return str(self.record_uuid)
