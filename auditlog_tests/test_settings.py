"""
Settings file for the Auditlog test suite.
"""
import os

SECRET_KEY = 'test'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.admin',
    'auditlog',
    'auditlog_tests',
    'multiselectfield',
]

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'auditlog.middleware.AuditlogMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('TEST_DB_NAME', 'auditlog' + os.environ.get("TOX_PARALLEL_ENV", "")),
        'USER': os.getenv('TEST_DB_USER', 'postgres'),
        'PASSWORD': os.getenv('TEST_DB_PASS', ''),
        'HOST': os.getenv('TEST_DB_HOST', '127.0.0.1'),
        'PORT': os.getenv('TEST_DB_PORT', '5432'),
    }
}

TEMPLATES = [
    {
        'APP_DIRS': True,
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        },
    },
]

ROOT_URLCONF = 'auditlog_tests.urls'

USE_TZ = True
