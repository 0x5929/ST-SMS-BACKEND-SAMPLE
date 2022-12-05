
from .base import *

# base settings overrides for PROD environment

DEBUG = False

# Static dir where basic API and admin files are served
# NOTE: before deployment, remember to execute : $ python manage.py collectstatic  
# this will create the static directory in project dir (BASE_DIR)
STATIC_ROOT = os.path.join(BASE_DIR, '../static')

# email verification settings
LOGIN_URL = 'https://0x5929.pythonanywhere.com/auth/login' # needs to be changed


# cors settings, ie for react apps
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'testserver', '0x5929.pythonanywhere.com']
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000', # needs to be changed 
    'http://127.0.0.1:3000', # needs to be changed
]


# production security settings
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Lax'

SECURE_SSL_REDIRECT = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True

ENV = env('ENV')
