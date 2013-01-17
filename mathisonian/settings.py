import os

# Make Celery work
from celery.schedules import crontab
import djcelery
djcelery.setup_loader()

PROJECT_PATH = os.path.realpath(os.path.join(os.path.dirname(__file__), os.path.pardir))
# PROJECT_PATH = ""

VERSION = '0.1'

FORCE_SCRIPT_NAME = ''

LOCAL = os.environ.get('DJANGO_LOCAL', 'False') == 'True'
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'

# DEBUG = True

TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Matt Conlen', 'matt.conlen@huffingtonpost.com')
)

MANAGERS = ADMINS

DATABASES = {
    # 'production': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'mathisonian',
    #     'USER': 'mathisonian',
    #     'PASSWORD': 'mathisonian',
    #     'HOST': '127.0.0.1',
    #     'PORT': '3306'
    # },

    'local': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'mathisonian.db',                    # Or path to database file if using sqlite3.
        'USER': '',                             # Not used with sqlite3.
        'PASSWORD': '',                         # Not used with sqlite3.
        'HOST': '',                             # Set to empty string for localhost. Not used with sqlite3.
        'PORT': ''                              # Set to empty string for default. Not used with sqlite3.
    }
}

if LOCAL:
    DOMAIN = 'localhost:8000'
    DEBUG_FILENAME = 'mathisonian-local-debug.log'
    VERSION += " (Local)"
    DATABASES['default'] = DATABASES['local']

    # precompilation will run every time otherwise
    COMPRESS_ENABLED = True
    COMPRESS_MTIME_DELAY = 0

    # Use the django db for dev, but do something better for
    # production, you know what I'm sayin'?
    BROKER_URL = 'django://'

else:
    DOMAIN = 'www.mathisonian.com'
    DEBUG_FILENAME = 'mathisonian-debug.log'
    VERSION += " (Production)"
    import dj_database_url
    DATABASES['default'] = dj_database_url.config()

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = PROJECT_PATH + '/var/assets/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = PROJECT_PATH + '/var/assets/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    PROJECT_PATH + '/static',
    'static'
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder'
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '3514+7&amp;^q)l6b6w5#&amp;%=s@qy&amp;vywh!poxi0-+&amp;n(nhkk)dvf4$'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    ('pyjade.ext.django.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
        'django.template.loaders.eggs.Loader',
    )),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mathisonian.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'mathisonian.wsgi.application'

TEMPLATE_DIRS = (
    PROJECT_PATH + '/templates/',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

FIXTURE_DIRS = (
    PROJECT_PATH + '/fixtures/',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.markup',
    'mathisonian.blog',
    'mathisonian.base',
    'mathisonian.project',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'widget_tweaks',
    # 'compressor',
    'djcelery',
    'djkombu',
    'django.contrib.humanize',
    'storages',
)

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

TEMPLATE_CONTEXT_PROCESSORS = [
  'django.core.context_processors.debug',
  'django.core.context_processors.i18n',
  'django.core.context_processors.media',
  'django.core.context_processors.static',
  'django.contrib.auth.context_processors.auth',
  'django.contrib.messages.context_processors.messages'
]

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': 'mathisonian-cache'
#     }
# }

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)

# COMPRESS_PRECOMPILERS = (
# #    ('text/coffeescript', 'coffee --compile --stdio'),
# #    ('text/less', 'lessc {infile} {outfile}'),
# #    ('text/x-sass', 'sass {infile} {outfile}'),
#     ('text/x-scss', 'sass --compass --scss {infile} {outfile}'),
# )

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
AUTH_PROFILE_MODULE = 'account.UserProfile'

CELERYBEAT_SCHEDULE = {
    'send-email-digest': {
        'task': 'mathisonian.synergy.tasks.send_email_digest',
        'schedule': crontab(minute='*/5'),
        'args': (),
    }
}

'''
http://django-social-auth.readthedocs.org/en/latest/configuration.html
TODO: Make apps and api key shit
'''
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)


AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 's3.mathisonian.com'
STATIC_URL = 'http://' + 's3.mathisonian.com/'
MEDIA_URL = STATIC_URL
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
AWS_QUERYSTRING_AUTH = False

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'


#
# APPLICATION
#

from mathisonian.app_settings import *

#
# API
#

from mathisonian.api_settings import *
