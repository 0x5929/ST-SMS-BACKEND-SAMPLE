import uuid
from django.db import models

from django.core.exceptions import ImproperlyConfigured
from django.contrib.postgres.fields import ArrayField
from djmoney.models.fields import MoneyField

from .managers import SchoolManager, ProgramManager, RotationManager, StudentManager


from google_sheet_connector.utils import GoogleSheet

# global constants
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

SHEET_MIGRATION_ISSUES = (
    ('POST', 'Could not add new record to Google Sheet'),
    ('PUT', 'Could not update existing record on Google Sheet'),
    ('DEL', 'Could not delete existing record on Google Sheet'),

)

# NOTE: not every student property/field is saved to google, some is used internally by postgresql DB.
# NOTE NOTE: this is the exact order of the database sheet columns from A to Y, if we add more columns in the future,
# MAKE SURE we update this as well.
STUDENT_RECORD_HEADERS = (
    'student_id',
    'full_name',
    'last_name',
    'first_name',
    'phone_number',
    'email',
    'mailing_address',
    'course',
    'start_date',
    'completion_date',
    'date_enrollment_agreement_signed',
    'third_party_payer_info',
    'course_cost',
    'total_charges_charged',
    'total_charges_paid',
    'graduated',
    'passed_first_exam',
    'passed_second_or_third_exam',
    'employed',
    'place_of_employment',
    'employment_address',
    'position',
    'starting_wage',
    'hours_worked_weekly',
    'description_of_attempts_to_contact_student',
    'school_name',

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
    student_id = models.CharField(max_length=11, unique=True, null=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    phone_number = models.CharField(max_length=12)
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

    paid = models.BooleanField(default=False)
    graduated = models.BooleanField(default=False)
    passed_first_exam = models.BooleanField(default=False)
    passed_second_or_third_exam = models.BooleanField(default=False)
    employed = models.BooleanField(default=False)

    place_of_employment = models.CharField(max_length=100, blank=True)
    employment_address = models.CharField(max_length=150, blank=True)
    position = models.CharField(max_length=50, blank=True)
    starting_wage = MoneyField(
        max_digits=5, decimal_places=2, default_currency='USD', blank=True)

    hours_worked_weekly = models.CharField(
        max_length=1, choices=EMPLOYMENT_STATUS_CHOICES, blank=True)

    description_of_attempts_to_contact_student = models.TextField(blank=True)

    google_sheet_migrated = models.BooleanField(default=False)

    google_sheet_migration_issue = models.CharField(
        max_length=4, choices=SHEET_MIGRATION_ISSUES,  blank=True)

    rotation = models.ForeignKey(Rotation, on_delete=models.SET_NULL,
                                 null=True, related_name='students', related_query_name='student')

    objects = StudentManager()

    @property
    def full_name(self):
        return '%s_%s' % (self.first_name.lower(), self.last_name.lower())

    @property
    def school_name(self):
        return str(self.rotation.program.school.school_name)

    def migrate_google(self, method):
        data = GoogleSheet.data_conversion(
            self, STUDENT_RECORD_HEADERS)

        try:
            if method == 'DEL':
                GoogleSheet.master_sheet_del(data=data)
            else:
                GoogleSheet.master_sheet_save(data=data)
                self.google_sheet_migrated = True

        except Exception as e:
            self.google_sheet_migration_issue = method
            msg = 'Did not save the data in Master DB on Google Sheet, cancelling the %s operation, please try again. Error: %s ' % \
                (method, repr(e))
            raise ImproperlyConfigured(msg=msg, code='Canceled-due-to-GSC')

    def save(self, *args, **kwargs):

        self.paid = True if self.total_charges_charged < self.total_charges_paid else False

        self.migrate_google('POST')

        return super(Student, self).save(*args, **kwargs)

    def update(self, *args, **kwargs):

        self.paid = True if self.total_charges_charged == self.total_charges_paid else False

        self.migrate_google('PUT')

        return super(Student, self).update(*args, **kwargs)

    def delete(self, *args, **kwargs):

        self.migrate_google('DEL')

        return super(Student, self).delete(*args, **kwargs)

    def __str__(self):
        return str(self.student_uuid)
