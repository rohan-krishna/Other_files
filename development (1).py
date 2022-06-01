from bgportal.settings.base import *
import os

SECRET_KEY = os.getenv('PORTAL_SECRET_KEY', "ABCD1234")
DEBUG = True
ALLOWED_HOSTS = os.getenv('PORTAL_ALLOWED_HOSTS', '127.0.0.1').split(',')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('PORTAL_DB_NAME', 'desk_stage2'),
        'USER': os.environ.get('PORTAL_DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('PORTAL_DB_PASSWORD', '1234'),
        'HOST': os.environ.get('PORTAL_DB_HOST', 'localhost'),
        'PORT': os.environ.get('PORTAL_DB_PORT', '5432'),
    }
}


# Static assets
STATIC_ROOT = os.getenv('PORTAL_STATIC_ROOT', os.path.join(PROJECT_ROOT, 'staticfiles'))

# User uploads
MEDIA_ROOT = os.getenv('PORTAL_MEDIA_ROOT', os.path.join(PROJECT_ROOT, 'media'))

if DEBUG:
    AWS_DIR = 'stage-media/media'
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST="mail.bimagarage.com"
    EMAIL_PORT=587
    EMAIL_HOST_USER="mail@bimagarage.com"
    EMAIL_HOST_PASSWORD="~O)mudqyfz1W"
    DEFAULT_FROM_EMAIL  = 'deskadmin@bimagarage.com'
    SERVER_EMAIL    = 'deskadmin@bimagarage.com'

    EMAIL_USE_SSL = False
    EMAIL_USE_TLS = True
else:
    AWS_DIR = 'media/media'
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST="mail.bimagarage.com"
    EMAIL_PORT=587
    EMAIL_HOST_USER="mail@bimagarage.com"
    EMAIL_HOST_PASSWORD="~O)mudqyfz1W"
    DEFAULT_FROM_EMAIL  = 'deskadmin@bimagarage.com'
    SERVER_EMAIL    = 'deskadmin@bimagarage.com'

    EMAIL_USE_SSL = False
    EMAIL_USE_TLS = True




ALGOLIA = {
    'APPLICATION_ID': '5G581LIJLZ',
    'API_KEY': '7f245e45e93192ba0e93894cdb0e5dfa'
}
