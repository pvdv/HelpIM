# Django settings for helpim project.
# do a "apache2 reload" after changing this file.

from os.path import dirname, join, abspath

ADMINS = (
    ('Helpdesk', 'helpdesk@e-hulp.nl'),
)

MANAGERS = ADMINS
SERVER_EMAIL = 'MAILRECIPIENT'
SEND_BROKEN_LINK_EMAILS = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'CHATX',                       # Or path to database file if using sqlite3.
        'USER': 'CHATX',                       # Not used with sqlite3.
        'PASSWORD': 'PASSWD',                 # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Add fixtures dir for fixtures over al submodules

FIXTURE_DIRS = (
 #  abspath(join(dirname(__file__), 'fixtures')),
   abspath(join(dirname('/usr/local/share/helpim/'), 'fixtures')),
)

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Amsterdam'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'nl-NL'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    abspath(join(dirname(__file__), 'static')),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'SECRETKEY'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'helpim.urls'

TEMPLATE_DIRS = (
#   abspath(join(dirname(__file__), 'templates')),
    abspath(join(dirname('/usr/local/share/helpim/'), 'templates')),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'helpim.conversations',
    #'helpim.groups',
    'helpim.rooms',
    'south',
    'threadedcomments',
    'rosetta',
    'helpim.common',
    'forms_builder.forms',
    'helpim.questionnaire',
)

AUTH_PROFILE_MODULE = 'common.AdditionalUserInformation'

CHAT = {
#    'mode': 'light',
    'domain': 'localhost',
    'httpbase': '/http-bind/',
    'authtype': 'saslanon',
    'composing_timeout': 10,
    }

BOT = {
    'connection': {
        'domain': 'localhost',
        'username': 'CHATX',
        'resource': 'HelpIM',
        'password': 'BOTPW',
        'nick': 'HelpIM',
        'port': 5222
        },
    'muc': {
        'domain': 'muc.localhost',
        'poolsize': 10,
        'nick': 'HelpIM',
        'whoisaccess': 'moderators',
        'allowchangesubject': 'yes',
        'history_maxchars': 2000,
        'history_maxstanzas': 10,
        'history_seconds': 120,
        'allocation_timeout': 0, # how long a room will be reserved for a client
        'max_chats_per_staff': 3,
        'http_domain': 'DOMAIN',
        },
    'mainloop': {
        'timeout': 1,
        'reconnectdelay': 5,
        'cleanup': 600,
        },
    'logging': {
        'destination': 'file:/var/log/helpim/CHATX.log',
        'level': 'debug',
        'level_pyxmpp': 'info',
        }
    }

ROOMS = {
    'access_token_timeout': 24*60*60
    }

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request':{
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

LOCALE_PATHS = (
    '/usr/local/share/helpim/locale',
)


DEBUG = False
FORMS_BUILDER_USE_SITES = False
