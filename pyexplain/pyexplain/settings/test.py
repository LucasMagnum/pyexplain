"""
    Test settings file.

    Run: python manage.py test <app_name>> --settings=pyexplain.settings.test

"""

from .dev import *


#### TEST SETTINGS
TEST_RUNNER = 'discover_runner.DiscoverRunner'
TEST_DISCOVER_TOP_LEVEL = PROJECT_ROOT
TEST_DISCOVER_ROOT = PROJECT_ROOT
TEST_DISCOVER_PATTERN = 'test_*'


#### Memory database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory'
    }
}
