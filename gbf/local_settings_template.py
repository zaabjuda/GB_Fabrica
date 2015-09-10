# coding=utf-8
__author__ = "Dmitry Zhiltsov"
__copyright__ = "Copyright 2015, Dmitry Zhiltsov"


SECRET_KEY = 'df6eyj57itthefg&^&*^Wgedh&I(EG(49Bejv)(*0ey%Esbc'

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'NAME': 'gbf',
        'USER': 'gbf',
        'PASSWORD': "gbf",
    }
}


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'
