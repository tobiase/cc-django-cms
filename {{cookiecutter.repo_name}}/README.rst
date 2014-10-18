===============================
{{ cookiecutter.project_name }}
===============================

.. image:: https://badge.fury.io/py/{{ cookiecutter.repo_name }}.png
    :target: http://badge.fury.io/py/{{ cookiecutter.repo_name }}

.. image:: https://pypip.in/d/{{ cookiecutter.repo_name }}/badge.png
    :target: https://crate.io/packages/{{ cookiecutter.repo_name }}?version=latest


{{ cookiecutter.project_short_description}}

* Free software: BSD license

Requirements
------------

* Django 1.6+
* Python 2.7
* `django-cms`_ 3.0.6

.. _django-cms: https://github.com/divio/django-cms

Installation
------------

Enter the ``{{ cookiecutter.repo_name }}`` folder and install all requirements inside a virtualenv:

.. code-block:: python

    pip install -r requirements/development.txt

Enter the ``{{ cookiecutter.django_cms_app }}`` then prepare your database (sqlite as default) and run the server:

.. code-block:: python

    python manage.py syncdb --all --settings={{ cookiecutter.django_cms_app }}.settings.dev
    python manage.py migrate --fake --settings={{ cookiecutter.django_cms_app }}.settings.dev
    python manage.py cms check --settings={{ cookiecutter.django_cms_app }}.settings.dev
    python manage.py runserver --settings={{ cookiecutter.django_cms_app }}.settings.dev

Create your first page with Django CMS admin (``http://localhost:8000/admin``)!

Features
--------

TODO
