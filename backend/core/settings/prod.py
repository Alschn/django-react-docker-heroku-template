import os

import dj_database_url
from core.settings.base import *

SECRET_KEY = os.environ.get("SECRET_KEY", "")  # set SECRET_KEY for production

ALLOWED_HOSTS = [os.environ.get("PRODUCTION_HOST")]  # add heroku app url or create env var with url

DEBUG = False

INSTALLED_APPS.extend(["whitenoise.runserver_nostatic"])

# Must insert after SecurityMiddleware, which is first in settings/common.py
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

'''
TEMPLATES: directories with templates (e.g. Jinja) or html files
STATICFILES_DIRS: directory where Django can find html, js, css, and other static assets
STATIC_ROOT: directory to which Django will move those static assets and from which it will serve them when the app is running
WHITENOISE_ROOT: directory where WhiteNoise can find all non-html static assets
'''

TEMPLATES[0]["DIRS"] = [os.path.join(BASE_DIR, "../", "frontend", "build")]

STATICFILES_DIRS = [os.path.join(BASE_DIR, "../", "frontend", "build", "static")]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATIC_URL = "/static/"

WHITENOISE_ROOT = os.path.join(BASE_DIR, "../", "frontend", "build", "root")

DATABASE_URL = os.environ.get('DATABASE_URL')

db_from_env = dj_database_url.config(
    default=DATABASE_URL, conn_max_age=500, ssl_require=True
)

DATABASES['default'].update(db_from_env)
