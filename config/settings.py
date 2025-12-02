import os
from dotenv import load_dotenv
load_dotenv()
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# SECURITY WARNING: don't run with debug turned on in production!


# ------------------------

SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG","False") == "True"
DIGITAL_OCEAN_KEY = os.getenv ("DIGITAL_OCEAN_KEY_ID")
DIGITAL_OCEAN_SECRET = os.getenv ("DIGITAL_OCEAN_SECRET_KEY")


ALLOWED_HOSTS = ['*']


STATIC_URL = 'static/'
STATIC_ROOT = os.path.join (BASE_DIR, "staticfiles")
STATICFILES_DIRS = [
    BASE_DIR / 'external_staticfiles',
]

# ------------------------
# MEDIA_FILES_SETTİNGS ⬇️
# ------------------------
AWS_DEFAULT_ACL = 'public-read'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = DIGITAL_OCEAN_KEY
AWS_SECRET_ACCESS_KEY = DIGITAL_OCEAN_SECRET
AWS_STORAGE_BUCKET_NAME = "weblogbucket"
AWS_S3_ENDPOINT_URL = "https://nyc3.digitaloceanspaces.com"
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = "media_sub_dir"

MEDIA_URL = f"https://{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/{AWS_LOCATION}/"
MEDIA_ROOT = os.path.join(BASE_DIR,"mediafiles")

# ------------------------

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "weblog",
    "storages",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
