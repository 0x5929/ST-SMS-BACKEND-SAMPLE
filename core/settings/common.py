import sys
import os

from datetime import timedelta
from pathlib import Path

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

ROOT_URLCONF = 'core.urls'

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

FIXTURE_DIRS = [os.path.join(BASE_DIR, '../fixtures')]

WSGI_APPLICATION = 'core.wsgi.application'


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

# rest framework settings
REST_FRAMEWORK = {

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ],

}

# contrib.sites settings
SITE_ID = 1

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
