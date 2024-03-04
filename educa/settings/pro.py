from .base import *

DEBUG = False

TIME_ZONE = 'UTC' 

ADMINS = (
    ('Antonio M', 'email@mydomain.com'),
)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'kadhir',
        'PASSWORD': 'welcome',
    },
}
