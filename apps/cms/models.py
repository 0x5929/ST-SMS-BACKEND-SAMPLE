import uuid
from django.db import models

from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.core.validators import RegexValidator
from djmoney.models.fields import MoneyField

from .managers import ClientManager, NoteManager


SCHOOL_NAMES = getattr(settings, 'SCHOOL_NAMES')
PROGRAM_NAMES = getattr(settings, 'PROGRAM_NAMES')


class Client(models.Model):
    class Meta:
        app_label = 'cms'
        verbose_name = 'Clientele'

    client_uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    phone_regex = RegexValidator(
        regex=r'^(\+\d-)?\d{3}-\d{3}-\d{4}$', message="Phone number must be entered in the format: '+1-888-888-8888'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=15, blank=True)

    initial_contact = models.DateField(auto_now_add=True)

    email = models.EmailField()
    city = models.CharField(max_length=200)

    success = models.BooleanField(default=False)

    # will determine permission on who can view clients and their notes
    recruit_emails = ArrayField(models.EmailField())

    school_name = models.CharField(max_length=10, choices=SCHOOL_NAMES)

    objects = ClientManager()

    @property
    def full_name(self):
        return f'{self.first_name.lower()}_{self.last_name.lower()}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Note(models.Model):
    class Meta:
        app_label = 'cms'
        verbose_name = 'Client\'s note'

    note_uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    date = models.DateField(auto_now_add=True)

    product = models.CharField(max_length=4, choices=PROGRAM_NAMES)

    price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')

    content = models.TextField(blank=True)

    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name='notes', related_query_name='note')

    objects = NoteManager()

    def __str__(self):
        return str(self.note_uuid)
