import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-adelaidex-util',
    version='0.4.2',
    packages=['django_adelaidex', 'django_adelaidex.util'],
    include_package_data=True,
    license='Copyright The University of Adelaide, All rights reserved',
    description='Utilities used by the AdelaideX Django applications',
    long_description=README,
    url='http://adelaide.edu.au/adelaidex',
    author='Jillian Vogel',
    author_email='jill.vogel@adelaide.edu.au',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'Django>=1.7,<1.10',
        'pytz>=2015.2',
    ],
    tests_require=[
        'selenium>=2.44.0',
        'PyVirtualDisplay>=0.1.5',
        'mock==1.0.1',
    ],
    zip_safe=False,
)
