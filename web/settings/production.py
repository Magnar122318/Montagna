from .base import *


DEBUG = True

ALLOWED_HOSTS = ['montagnadeveloper.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd3fhn53ajvtu94',
        'USER' : 'iblddxfsugelim',
        'PASSWORD': '57e0841438cfec8fd9017c5760eaa37e17d4d9e60f706ad6f9bccc8dd476c1cc',
        'HOST': 'ec2-54-162-211-113.compute-1.amazonaws.com',
        'PORT': '5432'
    }
}

