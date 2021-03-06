# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Placeholder settings, for use when running tests.
SECRET_KEY = 'notagoodsecret'

# Runs via ./manage.py test
DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': os.path.join(BASE_DIR, 'test_db.sqlite3'),
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django_adelaidex.util',
    'django_adelaidex.util.tests',
)   

MIDDLEWARE_CLASSES = (
    'django_adelaidex.util.middleware.WsgiLogErrors',
    'django_adelaidex.util.middleware.P3PMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'tests', 'templates'), 
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.static',
                'django_adelaidex.util.context_processors.analytics',
                'django_adelaidex.util.context_processors.referer',
                'django_adelaidex.util.context_processors.base_url',
            ],
        },
    },
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'tests', 'static', 'gen')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'tests', 'static'),
)

ROOT_URLCONF = 'django_adelaidex.util.tests.urls'
