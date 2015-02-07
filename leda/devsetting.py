import os
from .settings import BASE_DIR

SECRET_KEY = ''
ALLOWED_HOSTS = ['']
STATIC_ROOT = os.path.join(BASE_DIR, "staticfile")
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'air',
        'USER': 'postgre',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '',
    }
}
