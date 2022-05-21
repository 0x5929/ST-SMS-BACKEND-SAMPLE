import uuid

from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.core.exceptions import ImproperlyConfigured
from django.contrib.postgres.fields import ArrayField

from djmoney.models.fields import MoneyField

from .managers import SchoolManager, ProgramManager, RotationManager, StudentManager
from .google_sheets import GoogleSheet
from .utils import DataHandler

from .constants import ENTITY_NAMES, EMPLOYMENT_STATUS_CHOICES, SHEET_MIGRATION_ISSUES

SCHOOL_NAMES = getattr(settings, 'SCHOOL_NAMES')
PROGRAM_NAMES = getattr(settings, 'PROGRAM_NAMES')


class School(models.Model):
    class Meta:
        app_label = 'sms'
        verbose_name = 'Main/Satellite School'

    school_uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    school_name = models.CharField(max_length=10, choices=SCHOOL_NAMES)

    school_code = models.CharField(max_length=50)
    school_address = models.CharField(max_length=150)

    year_founded = models.DateField()

    objects = SchoolManager()

    def __str__(self):
        return self.school_name


class Program(models.Model):
    class Meta:
        app_label = 'sms'
        verbose_name = 'Education Program'

    program_uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    program_name = models.CharField(max_length=4, choices=PROGRAM_NAMES)

    approval_entities = ArrayField(
        models.CharField(max_length=10, choices=ENTITY_NAMES))

    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True,
                               related_name='programs', related_query_name='program')

    objects = ProgramManager()

    def __str__(self):
        return f'{self.school.school_name}: {self.program_name}'


class Rotation(models.Model):
    class Meta:
        app_label = 'sms'
        verbose_name = 'Program Rotations or Classe'

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
        return f'{self.program} Rotation# {str(self.rotation_number)}'


class Student(models.Model):
    class Meta:
        app_label = 'sms'
        verbose_name = 'Students and Graduate'

    student_uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    # student ID follows the format: RO-(CNA|HHA|SG|ESOL)-###-MMDD-FL
    # ### -> rotation number, MMDD -> 2 digit months and dates, FL -> First/Last name initials
    student_id = models.CharField(max_length=19, null=False, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    phone_regex = RegexValidator(
        regex=r'^(\+\d-)?\d{3}-\d{3}-\d{4}$', message="Phone number must be entered in the format: '+1-888-888-8888'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=15, blank=True)

    email = models.EmailField()
    mailing_address = models.CharField(max_length=200)
    course = models.CharField(max_length=4, choices=PROGRAM_NAMES)
    start_date = models.DateField()
    completion_date = models.DateField()
    date_enrollment_agreement_signed = models.DateField()

    third_party_payer_info = models.CharField(max_length=10, blank=True)

    course_cost = MoneyField(
        max_digits=10, decimal_places=2, default_currency='USD')

    total_charges_charged = MoneyField(
        max_digits=10, decimal_places=2, default_currency='USD')

    total_charges_paid = MoneyField(
        max_digits=10, decimal_places=2, default_currency='USD')

    paid = models.BooleanField(default=False)
    graduated = models.BooleanField(default=False)
    passed_first_exam = models.BooleanField(default=False)
    passed_second_or_third_exam = models.BooleanField(default=False)
    employed = models.BooleanField(default=False)

    place_of_employment = models.CharField(max_length=100, blank=True)
    employment_address = models.CharField(max_length=150, blank=True)
    position = models.CharField(max_length=50, blank=True)
    starting_wage = MoneyField(
        max_digits=10, decimal_places=2, default_currency='USD', blank=True, default='0.00')

    hours_worked_weekly = models.CharField(
        max_length=1, choices=EMPLOYMENT_STATUS_CHOICES, blank=True)

    description_of_attempts_to_contact_student = models.TextField(
        blank=True, default='Information provided by ST office contacting students via phone/text/email.')

    google_sheet_migrated = models.BooleanField(default=False)

    google_sheet_migration_issue = models.CharField(
        max_length=4, choices=SHEET_MIGRATION_ISSUES,  blank=True)

    rotation = models.ForeignKey(Rotation, on_delete=models.SET_NULL,
                                 null=True, related_name='students', related_query_name='student')

    objects = StudentManager()

    @property
    def full_name(self):
        return f'{self.first_name.lower()}_{self.last_name.lower()}'

    @property
    def school_name(self):
        return str(self.rotation.program.school.school_name)

    def migrate_google(self, method):

        if not hasattr(settings, 'MIGRATE_GOOGLE_SHEET') or \
                hasattr(settings, 'MIGRATE_GOOGLE_SHEET') and \
                not getattr(settings, 'MIGRATE_GOOGLE_SHEET'):
            self.google_sheet_migrated = False
            self.google_sheet_migration_issue = method

            return True

        data = DataHandler.data_conversion(self)

        try:
            if method == 'DEL':
                GoogleSheet.master_sheet_del(data=data)
            else:
                GoogleSheet.master_sheet_save(data=data)
                self.google_sheet_migrated = True

            return True

        except Exception:
            self.google_sheet_migrated = False
            self.google_sheet_migration_issue = method

            return False

    def payment_and_date_attr_logic(self):
        # check student charges, if they paid up (technically not needed for delete)
        self.paid = True if self.total_charges_charged <= self.total_charges_paid else False

        # check dates
        self.date_enrollment_agreement_signed = self.start_date if \
            self.date_enrollment_agreement_signed > self.start_date else \
            self.date_enrollment_agreement_signed

    def pre_hook(self, action):
        self.payment_and_date_attr_logic()

        # migrate to google (if disable in setting, this will have no side effect)
        if action == 'save':
            return self.migrate_google('POST/PUT/PATCH')
        elif action == 'delete':
            return self.migrate_google('DEL')
        return False

    def save(self, *args, **kwargs):
        if self.pre_hook('save'):
            return super(Student, self).save(*args, **kwargs)
        raise ImproperlyConfigured(
            'Did not save the data in Master DB on Google Sheet, cancelling the save operation, please try again.')

    def delete(self, *args, **kwargs):
        if self.pre_hook('delete'):
            return super(Student, self).delete(*args, **kwargs)
        raise ImproperlyConfigured(
            'Did not delete the data in Master DB on Google Sheet, cancelling the delete operation, please try again.')

    def __str__(self):
        return self.full_name
