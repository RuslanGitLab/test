"""
Django settings for soaqaz project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
import logging

from django.urls import reverse_lazy
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%H:%M:%S')


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--22a3=63py*mv_nfodepzeqqdvsna&eb@m%8y+7i8joha9jnyr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [os.getenv("ALLOWED_HOST"), ]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "core",
    "django_celery_results",
    "django_celery_beat",
    "web",
    "mptt",
    "fias",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'soaqaz.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'soaqaz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.getenv('POSTGRES_HOST', 'localhost'),
        'PORT': os.getenv('POSTGRES_PORT', 5432),
        'USER': os.getenv('POSTGRES_USER', 'soaqa'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'NAME': os.getenv('POSTGRES_DB', "db01")
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = [
    ('en', 'English'),
    ('ru', 'Russian'),
]

LOCALE_PATHS = [
    BASE_DIR / "web" / "locale"
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'
MEDIA_ROOT = 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "core.Buyer"

CELERY_BROKER_URL = 'redis://127.0.0.1:16379/0'

CELERY_RESULT_BACKEND = 'django-db'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:16379/1',
    }
}

# celery setting.
CELERY_CACHE_BACKEND = 'default'

CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

LOGIN_REDIRECT_URL = reverse_lazy("web:profile")

SECURE_CROSS_ORIGIN_OPENER_POLICY = None

CSRF_TRUSTED_ORIGINS = []
if scrf_subdomain := os.getenv("SCRF_SUBDOMAIN"):
    CSRF_TRUSTED_ORIGINS += [f'http://{scrf_subdomain}', f'https://{scrf_subdomain}']
