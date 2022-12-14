from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.postgres.fields import ArrayField


from django.conf import settings

SCHOOL_NAMES = getattr(settings, 'SCHOOL_NAMES')
PROGRAM_NAMES = getattr(settings, 'PROGRAM_NAMES')


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, username, first_name, last_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_admin', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        # tehcnically these three arent necessary since program permissions work even if these three are set to false
        other_fields.setdefault('is_office', True)
        other_fields.setdefault('is_recruit', True)
        other_fields.setdefault('is_instructor', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        elif other_fields.get('is_admin') is not True:
            raise ValueError('Superuser must be assigned to is_admin=True')
        elif other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')
        elif other_fields.get('is_active') is not True:
            raise ValueError('Superuser must be assigned to is_active=True.')

        return self.create_user(email, username, first_name, last_name, password, **other_fields)

    def create_user(self, email, username, first_name, last_name, password, **other_fields):

        if not email:
            raise ValueError('You must provide an email address')
        elif not username:
            raise ValueError('You must provide an username')
        elif not first_name:
            raise ValueError('You must provide a first name')
        elif not last_name:
            raise ValueError('You must provide a last name')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, first_name=first_name,
                          last_name=last_name, **other_fields)

        user.set_password(password)
        user.save()

        return user

    def update_user(self, user, validated_data):
        user.email = validated_data.get('email', user.email)
        user.username = validated_data.get('username', user.username)
        user.first_name = validated_data.get('first_name', user.email)
        user.last_name = validated_data.get('last_name', user.username)
        password = validated_data.get('password', user.password)

        if validated_data.get('phone_number'):
            user.phone_number = validated_data.get(
                'phone_number', user.phone_number)

        user.set_password(password)
        user.save()

        return user


class Account(AbstractBaseUser, PermissionsMixin):
    class Meta:
        app_label = 'authentication'
        verbose_name = 'User Accounts'

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    date_joined = models.DateTimeField(auto_now_add=True)

    phone_regex = RegexValidator(
        regex=r'^(\+\d-)?\d{3}-\d{3}-\d{4}$', message="Phone number must be entered in the format: '+1-888-888-8888'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=15, blank=True)

    is_office = models.BooleanField(default=False)
    is_recruit = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)

    programs = ArrayField(models.CharField(
        max_length=5, choices=PROGRAM_NAMES, blank=True), blank=True, null=True)
    school_name = models.CharField(
        max_length=10, choices=SCHOOL_NAMES, blank=True)

    # django related fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.username
