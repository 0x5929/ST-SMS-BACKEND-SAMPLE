from .common import *

import environ


env = environ.Env()

# Take environment variables from .env file
environ.Env.read_env('core/settings/.test-env')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# dev database
DATABASES = {
    'default': {
        'ENGINE': env('DATABASE_ENGINE'),
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT'),
    }
}


# email verification settings
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
LOGIN_URL = 'http://localhost:8000/auth/login'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587


# Google Sheet Migration (can be False for dev and debug purpose)
MIGRATE_GOOGLE_SHEET = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'testserver']
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000'
]


ENV = env('ENV')
