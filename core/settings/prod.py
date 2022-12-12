
from .base import *

# base settings overrides for PROD environment

DEBUG = False

# Static dir where basic API and admin files are served
# NOTE: before deployment, remember to execute : $ python manage.py collectstatic  
# this will create the static directory in project dir (BASE_DIR)
STATIC_ROOT = os.path.join(BASE_DIR, '../static')

# email verification settings
LOGIN_URL = env('LOGIN_URL')


# cors settings, ie for react apps
ALLOWED_HOSTS = ALLOWED_HOSTS + [ env('SERVER_HOST'), ]
CORS_ALLOWED_ORIGINS = CORS_ALLOWED_ORIGINS + [
    env('CORS_ALLOWED_HOST_1'), 
    env('CORS_ALLOWED_HOST_2'), 
]


# production security settings
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Lax'

# already in place by cloudflare, this if set to true will cause infinite redirects
# caused by flexible SSL connection between cloudflare and server
# as well as this setting below, thus commented out
SECURE_SSL_REDIRECT = True

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True

ENV = env('ENV')
