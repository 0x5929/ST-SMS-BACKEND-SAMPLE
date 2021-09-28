from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from phonenumber_field.modelfields import PhoneNumberField


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, username, first_name, last_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
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
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    date_joined = models.DateTimeField(auto_now_add=True)

    phone_number = PhoneNumberField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.username
