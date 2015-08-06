django\_adelaidex
=================

Utilities used by the AdelaideX Django applications.

Usage
-----

1. If you wish to use the django\_adelaidex.templatetags, add django\_adelaidex
   to your settings.INSTALLED\_APPS: ::
   INSTALLED\_APPS = ( 
        ... 
        'django\_adelaidex', 
   )

2. Optionally add django\_adelaidex.middleware to MIDDLEWARE\_CLASSES: ::
   MIDDLEWARE\_CLASSES = ( 
        'django\_adelaidex.middleware.WsgiLogErrors', # listed first, so we can see all errors 
        ...
        'django\_adelaidex.middleware.P3PMiddleware',
        'django\_adelaidex.lti.middleware.TimezoneMiddleware', 
    )

3. Optionally add django\_adelaidex.context\_processors to TEMPLATE\_CONTEXT\_PROCESSORS: ::
    TEMPLATE\_CONTEXT\_PROCESSORS = ( 
        ...
        'django\_adelaidex.context\_processors.analytics',
        'django\_adelaidex.context\_processors.referer',
        'django\_adelaidex.context\_processors.base\_url', 
    )

4. If you plan to use django_adelaidex.templatetags, append this to your TEMPLATE_DIRS: ::
    TEMPLATE_DIRS = (
        ...
        # TODO Hopefully fixed in Django 1.8
        os.path.join( SITE_PACKAGES_INSTALL_DIR, 'django_adelaidex', 'templates' ),
    )
