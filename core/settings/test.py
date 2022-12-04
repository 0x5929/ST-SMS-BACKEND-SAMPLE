from .base import *
import environ

# base settings overrides for TEST environment
# OVERRIDING only settings that could be different in a test environ

# while .env is used either for DEV or PROD, a separate .test-env is needed for environments
# that run tests either manually or via CI/CD
# Thus, while alot of settings is not needed to override dev or prod,
# test lives on its own and is separate and therefore needs additional overides
env = environ.Env()
environ.Env.read_env('core/settings/.test-env')

SECRET_KEY = env('SECRET_KEY')

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


ENV = env('ENV')
