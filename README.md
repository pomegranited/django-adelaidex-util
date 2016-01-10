django\_adelaidex.util
======================

Utilities used by the AdelaideX Django applications.

Usage
-----

1. If you wish to use the `django_adelaidex.templatetags`, add `django_adelaidex`
   to your `settings.INSTALLED_APPS`.

        INSTALLED_APPS = ( 
            'django_adelaidex.util', 
            ... 
        )

2. Optionally add `django_adelaidex.middleware` to `settings.MIDDLEWARE_CLASSES`.

        MIDDLEWARE_CLASSES = ( 
            'django_adelaidex.util.middleware.WsgiLogErrors', # list first, so we can see all errors 
            ...
            'django_adelaidex.util.middleware.P3PMiddleware',
        )

3. Optionally add `django_adelaidex.context_processors` to `settings.TEMPLATES`.

        TEMPLATES = [
            {
                ...
                'OPTIONS': {
                    'context_processors': [
                        'django_adelaidex.util.context_processors.analytics',
                        'django_adelaidex.util.context_processors.referer',
                        'django_adelaidex.util.context_processors.base_url', 
                        ... 
                    ],
                },
            },
        ] 

Test
----

To set up the virtualenv::

    virtualenv .virtualenv
    source .virtualenv/bin/activate
    pip install -U -r django_adelaidex/util/tests/pip.txt

To run the tests::

    python manage.py test

To check coverage::

    coverage run --include=django_adelaidex/*  python manage.py test     
    coverage report

    Name                                                 Stmts   Miss  Cover
    ------------------------------------------------------------------------
    django_adelaidex/__init__                                2      0   100%
    django_adelaidex/util/__init__                           0      0   100%
    django_adelaidex/util/context_processors                10      1    90%
    django_adelaidex/util/fields                             8      0   100%
    django_adelaidex/util/middleware                        18      0   100%
    django_adelaidex/util/templatetags/__init__              0      0   100%
    django_adelaidex/util/templatetags/dict_filters          8      0   100%
    django_adelaidex/util/templatetags/pagination           22      0   100%
    django_adelaidex/util/test                             227    164    28%
    django_adelaidex/util/tests/__init__                     0      0   100%
    django_adelaidex/util/tests/settings                    12      0   100%
    django_adelaidex/util/tests/test_contextprocessors      16      0   100%
    django_adelaidex/util/tests/test_fields                 18      0   100%
    django_adelaidex/util/tests/test_middleware             47      0   100%
    django_adelaidex/util/tests/test_templatetags          164      0   100%
    django_adelaidex/util/tests/urls                         3      0   100%
    django_adelaidex/util/tests/views                        4      0   100%
    ------------------------------------------------------------------------
    TOTAL                                                  559    165    70%

Build
-----

To build the pip package::

    python setup.py sdist

