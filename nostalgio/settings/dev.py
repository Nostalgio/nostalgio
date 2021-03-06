# flake8: noqa
from .base import *


TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

INSTALLED_APPS += (
    # 'debug_toolbar',
    'django_extensions',
)

INTERNAL_IPS = ('127.0.0.1',)

INSTALLED_APPS += (
    'django_medusa',
    'wagtail.contrib.wagtailmedusa',
    )

# Medusa settings
MEDUSA_RENDERER_CLASS = 'django_medusa.renderers.DiskStaticSiteRenderer'
MEDUSA_DEPLOY_DIR = os.path.join(PROJECT_ROOT, 'static_build')
SENDFILE_BACKEND = 'sendfile.backends.simple'

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
MIDDLEWARE_CLASSES += (
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# Process all tasks synchronously.
# Helpful for local development and running tests
# CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
# CELERY_ALWAYS_EAGER = True

try:
    from .local import *
except ImportError:
    pass

# Use Redis as the cache backend for extra performance

