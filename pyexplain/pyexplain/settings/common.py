# Common settings
import os
import unipath

VERSION = "0.1.2"

#:  pyexplain -- PROJECT_ROOT
#:      pyexplain > -- PROJECT_DIR
#:          settings >
#:              common.py
#:      <app_name>
#:      <app_name>

PROJECT_ROOT = unipath.Path(__file__).ancestor(3)
PROJECT_DIR = unipath.Path(__file__).ancestor(2) #os.path.dirname(os.path.dirname(__file__))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Lucas Magnum', 'contato@lucasmagnum.com.br'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('EXPLAIN_DB'),
        'USER': os.environ.get('EXPLAIN_DB_USER'),
        'PASSWORD': os.environ.get('EXPLAIN_DB_PASS')
    }
}


MANAGERS = ADMINS

ALLOWED_HOSTS = ['pyexplain'] # pyexplain it's used on development machine to simulate prd settings

TIME_ZONE = 'America/Sao_Paulo'
LANGUAGE_CODE = 'pt-BR'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = PROJECT_DIR.child('media') #os.path.join(PROJECT_DIR, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = PROJECT_DIR.child('static') #os.path.join(PROJECT_DIR, 'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    MEDIA_ROOT,
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '%__a0u*5e@f0tcy1-fr*$^4er+((=v$j6l$(!8u!1v9$g8t$yt'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.static',

    # external processors
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',

    # local processors
    'website.context_processors.form_search',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'pyexplain.urls'
WSGI_APPLICATION = 'pyexplain.wsgi.application'

TEMPLATE_DIRS = (
    PROJECT_DIR.child('templates') #os.path.join(PROJECT_DIR, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'suit',  # django-suit app placed before admin
    'django.contrib.admin',

    # external apps
    'selectable', # autocompletes
    'south', # south for migrations
    'social.apps.django_app.default', # social auth connections
    'bootstrap3', # bootstrap-toolkit 3

    # local apps
    'website',
    'attach',
    'attach.links',
    'attach.examples',
)

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

# settings for django-suit
SUIT_CONFIG = {
    'ADMIN_NAME': 'PyExplain'
}


SESSION_EXPIRE_AT_BROWSER_CLOSE = True

from .social import *