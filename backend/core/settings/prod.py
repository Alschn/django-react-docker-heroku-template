"""
Configuration for deployment to Heroku with Dockerfile.prod
"""
import os

import dj_database_url
from core.settings.base import *

# project directory
ROOT_DIR = BASE_DIR.parent.parent

# set SECRET_KEY for production
SECRET_KEY = os.environ.get("SECRET_KEY", "")

# add heroku app url or create env var with url
ALLOWED_HOSTS = [os.environ.get("PRODUCTION_HOST")]

# debug has to be false in production
DEBUG = False

# cors headers configuration
CORS_ALLOW_ALL_ORIGINS = False

INSTALLED_APPS.extend(["whitenoise.runserver_nostatic"])

# whitenoise middle - has to be first in the list
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

# directories with templates or html files
TEMPLATES[0]["DIRS"] = [os.path.join(ROOT_DIR, "frontend", "build")]

# directory where Django can find html, js, css, and other static assets
STATICFILES_DIRS = [os.path.join(ROOT_DIR, "frontend", "build", "static")]

# directory to which Django will move those static assets and from which it will serve them when the app is running
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATIC_ROOT = os.path.join(ROOT_DIR, "staticfiles")

STATIC_URL = "/static/"

# directory where WhiteNoise can find all non-html static assets
WHITENOISE_ROOT = os.path.join(ROOT_DIR, "frontend", "build", "root")

# database url set at env variable in Heroku
DATABASE_URL = os.environ.get('DATABASE_URL')

# db config
db_from_env = dj_database_url.config(
    default=DATABASE_URL, conn_max_age=500, ssl_require=True
)

DATABASES['default'].update(db_from_env)
