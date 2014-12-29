from os import environ
from os.path import join, abspath, dirname

# Root directory of our project
PROJECT_ROOT = abspath(join(abspath(dirname(__file__)), "..", ".."))

# Django settings for {{ cookiecutter.django_cms_app }} project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ( '{{ cookiecutter.full_name }}', '{{ cookiecutter.email }}' ),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                       # Or path to database file if using sqlite3.
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                       # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                       # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = '{{ cookiecutter.timezone }}'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = join(PROJECT_ROOT, "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = join(PROJECT_ROOT, "static")

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = environ.get('DJANGO_SECRET_KEY')

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',

    # Custom context processors
    'core.context_processor.debug_state',
    'core.context_processor.google_analytics',
)

ROOT_URLCONF = '{{ cookiecutter.django_cms_app }}.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = '{{ cookiecutter.django_cms_app }}.wsgi.application'

TEMPLATE_DIRS = (
    join(PROJECT_ROOT, "templates"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Django CMS
    'core',
    'djangocms_text_ckeditor',
    'cms',
    'mptt',
    'menus',
    'south',
    'sekizai',
    'djangocms_admin_style',
    'django-admin-shortcuts',
    'django-classy-tags',
    'django-messages',

    # Django CMS extra plugins
    'djangocms_column',
    'djangocms_googlemap',
    'djangocms_grid',
    'djangocms_link',
    'djangocms_oembed',
    # 'djangocms_snippet', # security warning (see: http://docs.django-cms.org/en/develop/getting_started/plugin_reference.html#snippets-plugin)
    'djangocms_style',
    'djangocms_table',
    'djangocms_twitter',

    # Django filer
    'filer',
    'easy_thumbnails',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',
    'reversion',

    # Django admin
    'django.contrib.admin',

    # Useful Tools
    'copyright',

    # Your Applications

)

# Copyright ...
COPY_START_YEAR = 2015


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Dummy gettext function
gettext = lambda s: s

# Django CMS configurations
CMS_TEMPLATES = (
    ('single_page.html', gettext('Single page')),
)

LANGUAGES = [
    {% for language in cookiecutter.languages.strip().split(',') -%}
    ('{{ language|trim }}', gettext('{{ language|trim }}')),
    {% endfor %}
]

# Django-Filer Settings:
THUMBNAIL_HIGH_RESOLUTION = True
TEXT_SAVE_IMAGE_FUNCTION='cmsplugin_filer_image.integrations.ckeditor.create_image_plugin'

CMSPLUGIN_FILER_IMAGE_STYLE_CHOICES = (
            ('default', 'Default'),
                ('boxed', 'Boxed'),
                )
CMSPLUGIN_FILER_IMAGE_DEFAULT_STYLE = 'default'
FILER_IMAGE_USE_ICON =

# Analytics
GOOGLE_ANALYTICS = environ.get('GOOGLE_ANALYTICS', '')


# Django-CMS specific settings...

CMS_TEMPLATE_INHERITANCE = True

CMS_TEMPLATES = (
    ('homepage.html', 'Homepage'),
    ('carousel-full-under.html', 'Carousel, Full Width Under'),
    ('full-page-no-feature.html', 'Full Width, no Feature'),
    ('full-top-right-feature.html', 'Full Width 1st, Feature Right'),
    ('right-feature.html', 'Text, Right Feature'),
    ('search.html', 'Search Page'),
)

LANGUAGES = [
    ('en', 'English'),
]

CMS_PERMISSION = True

#SAS - this needs configured eventually...
CMS_PLACEHOLDER_CONF = {}

CMS_MENU_TITLE_OVERWRITE = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

CMS_LANGUAGES = {
    'default': {
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    },
    1: [
        {
            'public': True,
            'code': 'en',
            'hide_untranslated': False,
            'name': gettext('en'),
            'redirect_on_fallback': True,
        },
    ],
}


