import sys

from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'reviews_analysis',
        'USER': 'postgres',
        # 'ADMINUSER':'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '37821',
    }
}

