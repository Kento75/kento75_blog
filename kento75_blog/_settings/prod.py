from .common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# ユニコーンで動かす
INSTALLED_APPS += (
    'gunicorn',
)

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'kento75_blog',
        'USER': 'kento75_blog',
        'PASSWORD': 'kento75_blog',
    }
}
