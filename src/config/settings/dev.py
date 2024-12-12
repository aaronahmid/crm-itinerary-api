"""dev.py
settings for dev environments

WARNING: This settings must not be used in production
to use this settings: set your the environment variable ENV=dev
"""

from config.settings.base import *
from config.settings.base import REST_FRAMEWORK, INSTALLED_APPS, STORAGES
from config.settings import getenv
from django.core.exceptions import ImproperlyConfigured
import environ
import os
from datetime import timedelta

TOKEN_EXPIRE_AT = 60

ALLOWED_HOSTS = ["*"]

# DEV APPS
# NOT ALL LIBRARIES
# HERE MIGHT MAKE IT TO
# STAGING OR PRODUCTION
DEV_APPS = [
    "knox",
    "drf_yasg",
    "coreapi",
    "drf_standardized_errors",
]

INSTALLED_APPS.extend(DEV_APPS)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env(DEBUG=(bool, True))
env_file = os.path.join(BASE_DIR, "envs/.env.dev")
env.read_env(env_file)


def getvar(name: str):
    """tries to get the environmental vairable using\
         env or getenv.

        env is bound to this settings while getenv is global.
        getenv gets global, dynamic or user specific environmental\
            variables.
    """
    # first try getting the variable using env
    # if failed, then use getenv
    try:
        var = env(name)
    except ImproperlyConfigured:
        var = getenv(name)
    return var


SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": getvar("POSTGRES_DB"),
        "USER": getvar("POSTGRES_USER"),
        "PASSWORD": getvar("POSTGRES_PASSWORD"),
        "HOST": getvar("POSTGRES_HOST_OR_URI"),
        "PORT": getvar("POSTGRES_DB_PORT"),
        "CONN_MAX_AGE": 600,
    }
}

CORS_ORIGIN_ALLOW_ALL = True

# REST FRAMEWORK DEV SETTINGS
REST_FRAMEWORK.update(
    {
        "TEST_REQUEST_DEFAULT_FORMAT": "json",
        "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.NamespaceVersioning",
    }
)

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": "your-secret-key",
    "AUTH_HEADER_TYPES": ("Bearer",),
}

REST_FRAMEWORK = {"EXCEPTION_HANDLER": "api.exceptions.handler.exception_handler"}

# OAUTH2 DEV SETTINGS
OAUTH2_PROVIDER = {
    # parses OAuth2 data from application/json requests
    "OAUTH2_BACKEND_CLASS": "oauth2_provider.oauth2_backends.JSONOAuthLibCore",
    # this is the list of available scopes
    "SCOPES": {"read": "Read scope", "write": "Write scope"},
}

# STATIC_URL = "/static/"
# BASE_DIR = BASE_DIR.split("/")
# BASE_DIR.pop()
# BASE_DIR = "/".join(BASE_DIR)
# # STATIC_ROOT = BASE_DIR + "/static"
# STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

STATIC_URL = "static/"

CACHES = {
    # "default": {
    #     "BACKEND": "django.c33ore.cache.backends.redis.RedisCache",
    #     "LOCATION": getvar("REDIS_URI"),
    #     # "OPTIONS": {"ssl_cert_reqs": None},
    # },
    # "fallback": {
    #     "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    #     "LOCATION": "unique-snowflake",
    # },
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique-snowflake",
    },
}

SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "Bearer": {"type": "apiKey", "name": "Authorization", "in": "header"}
    }
}


EMAIL_HOST_USER = getvar("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = getvar("EMAIL_HOST_PASSWORD")

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = "None"

TRUSTED_ORIGINS = ["http://127.0.0.1:8000"]

CSRF_TRUSTED_ORIGINS = TRUSTED_ORIGINS

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
