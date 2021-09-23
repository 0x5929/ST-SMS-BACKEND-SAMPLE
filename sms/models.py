import uuid
from django.db import models

from django.contrib.postgres.fields import ArrayField
from djmoney.models.fields import MoneyField
from phonenumber_field.modelfields import PhoneNumberField

from .managers import SchoolManager, ProgramManager, RotationManager, StudentManager

# can be refactored, so we can easily add on new programs in the future
PROGRAM_NAMES = (
    ('CNA', 'Certified Nurse Assistant'),
    ('HHA', 'Home Health Aide'),
    ('SG', 'Security Guard'),
    ('ESOL', 'English to Speakers of Other Language'),
)
ENTITY_NAMES = (
    ('CDPH', 'California Department of Public Health'),
    ('BPPE', 'Bureau of Postsecondary and for Private Education'),
    ('BSIS', 'Bureau of Security and Investigative Services'),
)
EMPLOYMENT_STATUS_CHOICES = (
    ('F', 'Full time employee, more than 32 hours a week'),
    ('P', 'Part time employee, less than 32 hours a week'),
)


class School(models.Model):
    school_uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    school_name = models.CharField(max_length=100)
    school_code = models.CharField(max_length=50)
    school_address = models.CharField(max_length=150)

    year_founded = models.DateField()

    objects = SchoolManager()

    def __str__(self):
        return str(self.school_uuid)


class Program(models.Model):
    program_uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    program_name = models.CharField(max_length=4, choices=PROGRAM_NAMES)

    approval_entities = ArrayField(
        models.CharField(max_length=10, choices=ENTITY_NAMES))

    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True,
                               related_name='programs', related_query_name='program')

    objects = ProgramManager()

    def __str__(self):
        return str(self.program_uuid)


class Rotation(models.Model):
    rotation_uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    rotation_number = models.IntegerField()

    program = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True,
                                related_name='rotations', related_query_name='rotation')

    objects = RotationManager()

    # note this could be an issue
    @property
    def size(self):
        return Student.objects.filter(rotation__rotation_uuid__exact=self.rotation_uuid).count()

    def __str__(self):
        return str(self.rotation_uuid)


class Student(models.Model):
    student_uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    # student ID follows the format: ###-MMDD-FL
    # ### -> rotation number, MMDD -> 2 digit months and dates, FL -> First/Last name initials
    student_id = models.CharField(max_length=11)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    phone_number = PhoneNumberField()
    email = models.EmailField()
    mailing_address = models.CharField(max_length=200)
    course = models.CharField(max_length=4, choices=PROGRAM_NAMES)
    start_date = models.DateField()
    completion_date = models.DateField()
    date_enrollment_agreement_signed = models.DateField()

    third_party_payer_info = models.CharField(max_length=10, blank=True)

    course_cost = MoneyField(
        max_digits=5, decimal_places=2, default_currency='USD')

    total_charges_charged = MoneyField(
        max_digits=5, decimal_places=2, default_currency='USD')

    total_charges_paid = MoneyField(
        max_digits=5, decimal_places=2, default_currency='USD')

    graduated = models.BooleanField(default=False)
    passed_first_exam = models.BooleanField(default=False)
    passed_second_or_third_exam = models.BooleanField(default=False)
    employed = models.BooleanField(default=False)

    place_of_employment = models.CharField(max_length=100, blank=True)
    employment_address = models.CharField(max_length=200, blank=True)
    position = models.CharField(max_length=100, blank=True)
    starting_wage = MoneyField(
        max_digits=5, decimal_places=2, default_currency='USD', blank=True)

    hours_worked_weekly = models.CharField(
        max_length=1, choices=EMPLOYMENT_STATUS_CHOICES, blank=True)

    description_of_attempts_to_contact_student = models.TextField(blank=True)

    rotation = models.ForeignKey(Rotation, on_delete=models.SET_NULL,
                                 null=True, related_name='students', related_query_name='student')

    objects = StudentManager()

    @property
    def full_name(self):
        return '%s_%s' % (self.first_name, self.last_name)

    def __str__(self):
        return str(self.student_uuid)
