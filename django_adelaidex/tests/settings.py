# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Placeholder settings, for use when running tests.
SECRET_KEY = 'notagoodsecret'

# Runs via ./manage.py test
DEBUG = False
TEMPLATE_DEBUG = False
DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': os.path.join(BASE_DIR, 'test_db.sqlite3'),
    }
}

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',

    'django_adelaidex',
)   

MIDDLEWARE_CLASSES = (
    'django_adelaidex.middleware.WsgiLogErrors',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'csp.middleware.CSPMiddleware',
    'django_adelaidex.middleware.P3PMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'django_adelaidex.context_processors.analytics',
    'django_adelaidex.context_processors.referer',
    'django_adelaidex.context_processors.base_url',
)

ROOT_URLCONF = 'django_adelaidex.tests.urls'
