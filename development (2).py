from bgportal.settings.base import *
import os
from bgportal.settings.base import PROJECT_ROOT

SECRET_KEY = os.getenv('PORTAL_SECRET_KEY', "ABCD1234")
DEBUG = True
ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': '5432',
    }
}

# Static assets
STATIC_ROOT     = os.getenv('PORTAL_STATIC_ROOT', os.path.join(PROJECT_ROOT, 'staticfiles'))

# User uploads
MEDIA_ROOT      = os.getenv('PORTAL_MEDIA_ROOT', os.path.join(PROJECT_ROOT, 'media'))

AWS_DIR             = 'stage-media/media' if DEBUG else 'media/media'
EMAIL_HOST          = "mail.bimagarage.com"
EMAIL_HOST_USER     = "mail@bimagarage.com"
EMAIL_USE_TLS       = True
EMAIL_PORT          = 587
SERVER_EMAIL        = 'deskadmin@bimagarage.com'

EMAIL_HOST_PASSWORD = "~O)mudqyfz1W"
EMAIL_BACKEND       = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL  = 'deskadmin@bimagarage.com'
EMAIL_USE_SSL       = False




import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://142db884405b4b3e810f0ca3fa0ba44e@o1189906.ingest.sentry.io/6310867",
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

