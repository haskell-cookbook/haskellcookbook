#!/usr/bin/env python

from setuptools import setup

setup(
    name='Haskell Cookbook',
    version='1.0',
    description='Site for sharing haskell code snippets',
    author='Lakshmi Narasimhan',
    author_email='badri.dilbert@gmail.com',
    url='http://www.haskellcookbook.com',
    install_requires=[
        'Django>=1.4.3',
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
        'psycopg2==2.5.1',
        'django-recaptcha==0.0.6',
        'django-comments-spamfighter',
        'akismet>=0.2.0'
        ],
)
