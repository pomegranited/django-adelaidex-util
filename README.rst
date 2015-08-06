django\_adelaidex
=================

Utilities used by the AdelaideX Django applications.

Usage
-----

1. If you wish to use the django\_adelaidex.templatetags, add django\_adelaidex
   to your settings.INSTALLED\_APPS::

    INSTALLED_APPS = ( 
        ... 
        'django_adelaidex', 
    )

2. Optionally add django\_adelaidex.middleware to MIDDLEWARE\_CLASSES::

    MIDDLEWARE_CLASSES = ( 
        'django_adelaidex.middleware.WsgiLogErrors', # listed first, so we can see all errors 
        ...
        'django_adelaidex.middleware.P3PMiddleware',
        'django_adelaidex.lti.middleware.TimezoneMiddleware', 
    )

3. Optionally add django\_adelaidex.context\_processors to TEMPLATE\_CONTEXT\_PROCESSORS::

    TEMPLATE_CONTEXT_PROCESSORS = ( 
        ...
        'django_adelaidex.context_processors.analytics',
        'django_adelaidex.context_processors.referer',
        'django_adelaidex.context_processors.base_url', 
    )

4. If you plan to use django_adelaidex.templatetags, append this to your TEMPLATE_DIRS::

    TEMPLATE_DIRS = (
        ...
        # TODO Hopefully fixed in Django 1.8
        os.path.join( SITE_PACKAGES_INSTALL_DIR, 'django_adelaidex', 'templates' ),
    )

Test
----

To run the tests::

    python manage.py test


Build
-----

To build the pip package::

   python setup.py sdist

