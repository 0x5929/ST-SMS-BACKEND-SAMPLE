import sys
import os
import environ

from datetime import timedelta
from pathlib import Path


# Take environment variables from .env file
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# To tell django all apps will live in apps/ dir
sys.path.insert(0, os.path.join(BASE_DIR, '../apps'))

# Application definition
INSTALLED_APPS = [
    # REST FRAMEWORK
    'rest_framework',
    'rest_framework.authtoken',

    # DJANGO
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # 3rd PARTY
    'djmoney',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'django_filters',
    'corsheaders',

    # PROJECT APPS
    'authentication',
    'sms',
    'cms',
    'gms',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

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

FIXTURE_DIRS = [os.path.join(BASE_DIR, '../fixtures')]

ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'

SECRET_KEY = env('SECRET_KEY')
GITHOOK_SECRET = env('SECRET_TOKEN')

DEBUG = True

# contrib.sites settings
SITE_ID = 1

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# custom user model
AUTH_USER_MODEL = 'authentication.Account'

# custom authenication backends
AUTHENTICATION_BACKENDS = [
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
    'core.auth.EmailOrUsernameBackend',
]


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
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = int(env('EMAIL_PORT'))


# rest framework settings
REST_FRAMEWORK = {

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ],

}

# JWT settings
REST_USE_JWT = True
JWT_AUTH_COOKIE = 'sms-auth'
JWT_AUTH_REFRESH_COOKIE = 'sms-refresh-token'
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=2),
    'REFRESH_TOKEN_LIFETIME': timedelta(minutes=15),
}

# custom REST_AUTH serializers
REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'authentication.serializers.RegisterSerializer',
}

REST_AUTH_SERIALIZERS = {
    'LOGIN_SERIALIZER': 'authentication.serializers.LoginSerializer',
}


# Google Sheet Migration (can be False for dev and debug purpose)
MIGRATE_GOOGLE_SHEET = True

# cors settings, ie for react apps
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'testserver']
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000'
]
#from corsheaders.defaults import default_headers
# CORS_ALLOW_HEADERS = list(default_headers) + ['Set-Cookie']


# CSRF_COOKIE_SECURE = False
# CSRF_COOKIE_HTTPONLY = True
# CSRF_COOKIE_SAMESITE = None

# SESSION_COOKIE_SECURE = False
# SESSION_COOKIE_HTTPONLY = True
# SESSION_COOKIE_SAMESITE = None

# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True


# SHARED APP CONSTANT SETTINGS:
SCHOOL_NAMES = (
    ('STI', 'Select Therapy Institute'),
    ('ST2', 'Select Therapy Institute Location 2'),
    ('ST3', 'Select Therapy Institute Location 3'),
)

PROGRAM_NAMES = (
    ('CNA', 'Certified Nurse Assistant'),
    ('HHA', 'Home Health Aide'),
    ('SG', 'Security Guard'),
    ('CG', 'Caregiver'),
    ('ESOL', 'English to Speakers of Other Language'),
    ('BLS', 'Basic Life Support'),
    ('HSFA', 'Heartsaver First Aid'),
)
