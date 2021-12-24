"""
Configuration for build with Docker - local simulation of production.
"""
import os

from core.settings.base import *

SECRET_KEY = os.environ.get('SECRET_KEY', 'development')

DEBUG = False

ALLOWED_HOSTS = ["backend", "localhost", "127.0.0.1"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'postgres'),
        'USER': os.environ.get('DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('DB_USER', 'postgres'),
        'HOST': os.environ.get('DB_HOST', 'db'),
        'PORT': os.environ.get('DB_PORT', 5432)
    }
}

# project directory
ROOT_DIR = BASE_DIR.parent.parent

# cors headers configuration
CORS_ALLOW_ALL_ORIGINS = False

# whitenoise middleware - has to be first in the list
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

# directories with templates or html files
TEMPLATES[0]["DIRS"] = [os.path.join(ROOT_DIR, "frontend", "build")]

# directory where Django can find html, js, css, and other static assets
STATICFILES_DIRS = [os.path.join(ROOT_DIR, "frontend", "build", "static")]

# directory where WhiteNoise can find all non-html static assets (.ico, .json, .txt files etc.)
WHITENOISE_ROOT = os.path.join(ROOT_DIR, "frontend", "build", "root")

# directory to which Django will move those static assets and from which it will serve them when the app is running
STATIC_ROOT = os.path.join(ROOT_DIR, "staticfiles")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATIC_URL = "/static/"
