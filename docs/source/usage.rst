=====
Usage
=====

Bootstrap your project
----------------------

First, get and install cookiecutter in your virtualenv::

    $ pip install cookiecutter

Now run it against this repo::

    $ cookiecutter https://github.com/lanshark/cc-django-cms.git --checkout 0.2.4

You'll be prompted for some project configurations::

    full_name (default is "Scott Sharkey")?
    email (default is "ssharkey@lanshark.com")?
    github_username (default is "lanshark")?
    year (default is "2014")?
    version (default is "0.1.0")?
    project_name (default is "Django CMS Sample Project")?
    repo_name (default is "client-django-cms")?
    django_cms_app (default is "cms-app")?
    project_short_description (default is "Django CMS boilerplate to start your website in 5 minutes.")?
    languages (default is "en")?
    site_name (default is "lanshark.com")?
    django_filer (default is "y")?
    heroku (default is "n")?

Now you are ready to use Django CMS!

Initial configurations
----------------------

Like any other Django project you should do these extra steps (if you are a Djangonaut, skip this).

Install all development requirements in your virtualenv::

    $ pip install -r requirements/development.txt

Sync your database with migrations::

    $ python manage.py syncdb --all --settings={{ cookiecutter.django_cms_app }}.settings.dev
    $ python manage.py migrate --fake --settings={{ cookiecutter.django_cms_app }}.settings.dev

Run all Django CMS checks and start django runserver::

    $ python manage.py cms check --settings={{ cookiecutter.django_cms_app }}.settings.dev
    $ python manage.py runserver --settings={{ cookiecutter.django_cms_app }}.settings.dev

Open http://localhost:8000 and create your first page with Django CMS admin!

.. note::
   You can avoid to use ``--settings`` parameter if you export ``DJANGO_SETTINGS_MODULE={{ cookiecutter.django_cms_app }}.settings.dev`` in your environment

More configurations
-------------------

For more Django CMS configurations, check official `documentation`_ (still in beta).

.. _documentation: http://docs.django-cms.org/en/develop/getting_started/configuration.html
