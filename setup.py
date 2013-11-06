#!/usr/bin/env python

from setuptools import setup

setup(
    name='YourAppName',
    version='1.0',
    description='OpenShift App',
    author='Your Name',
    author_email='example@example.com',
    url='http://www.python.org/sigs/distutils-sig/',
    install_requires=[
        'Django==1.5.4',
        'Markdown==2.3.1',
        'Pygments==1.6',
        'South==0.8.2',
        'django-generic-aggregation==0.3.2',
        'django-haystack>=2.1',
        'django-pagination==1.0.7',
        'django-registration==1.0',
        'django-taggit==0.10',
        'django-simple-ratings==0.3.2',
        'django-taggit-autosuggest==0.2',
        'django-epiceditor==0.2.1.2',
        'django-codemirror-widget==0.3.0',
        'python-openid==2.2.5',
        'requests==2.0.1',
        'requests-oauthlib==0.4.0',
        'django-allauth==0.14.1',
        'Whoosh==2.5.0',
        'psycopg2==2.5.1'
        ],
)
