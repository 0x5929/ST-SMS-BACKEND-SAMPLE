import uuid

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.fields import related


from .base import BaseRotation, BaseStudent
from core.settings.constants import CLINICAL_SITE_NAMES, CNA_INSTRUCTOR_TITLES, CNA_THEORY_TOPICS, CNA_CLINICAL_TOPICS


class CNARotation(BaseRotation):
    class Meta:
        app_label = 'gms'

    instructor_title = models.CharField(
        max_length=50, choices=CNA_INSTRUCTOR_TITLES)

    clinical_site = models.CharField(
        max_length=50, chocies=CLINICAL_SITE_NAMES)


class CNAStudent(BaseStudent):
    class Meta:
        app_label = 'gms'

    rotation = models.ForeignKey(
        CNARotation,
        on_delete=models.CASCADE,
        related_name='cna_students',
        related_query_name='cna_student')


class CNATheoryRecord(models.Model):
    class Meta:
        app_label = 'gms'

    date = models.DateField()
    hours_spent = models.PositiveIntegerField()
    completed = models.BooleanField(default=False)
    test_score = models.IntegerField(validators=[MinValueValidator(0),
                                                 MaxValueValidator(100)], blank=True, null=True)

    topic = models.CharField(max_length=200, choices=CNA_THEORY_TOPICS)

    student = models.ForeignKey(
        CNAStudent,
        on_delete=models.CASCADE,
        related_name='cna_theory_records',
        related_query_name='cna_theory_record')


class CNAClinicalRecord(models.Model):
    class Meta:
        app_label = 'gms'

    date = models.DateField()
    completed = models.BooleanField(default=False)
    comments = models.CharField(max_length=200, blank=True)
    performance_satisfied = models.BooleanField(default=True)

    topic = models.CharField(max_length=200, choices=CNA_CLINICAL_TOPICS)

    student = models.ForeignKey(
        CNAStudent,
        on_delete=models.CASCADE,
        related_name='cna_clinical_records',
        related_query_name='cna_clinical_record')
