from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'reviews_analysis',
        'USER': 'reviews_analysis',
        'PASSWORD': 'r3v13w2',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
