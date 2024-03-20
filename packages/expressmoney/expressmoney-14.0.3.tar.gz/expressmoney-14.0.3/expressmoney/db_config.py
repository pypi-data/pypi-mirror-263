import os


DATABASES = {
    'auth_db': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'rc1a-0bt9ky542yxiq5az.mdb.yandexcloud.net',
        'PORT': '6432',
        'NAME': 'auth',
        'USER': 'default',
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'CONN_MAX_AGE': 60,
    },
    'ru_scoring_db': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'rc1a-0bt9ky542yxiq5az.mdb.yandexcloud.net',
        'PORT': '6432',
        'NAME': 'ru_scoring',
        'USER': 'default',
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'CONN_MAX_AGE': 60,
    },
}
