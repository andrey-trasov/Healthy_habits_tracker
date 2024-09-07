import os
from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-buctfza0*h)(_om$chhj@-w4dx@9$gr^nj#!3^+heh((72lay5"

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",
    "rest_framework_simplejwt",
    'drf_yasg',
    'corsheaders',
    "tracker",
    "user",

]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = "myprogect.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "myprogect.wsgi.application"

# DATABASES = {
#    "default": {
#        "ENGINE": "django.db.backends.postgresql_psycopg2", # тут не меняем
#        'NAME': os.getenv('NAME'),
#        'USER':  os.getenv('USER'),
#        'PASSWORD': os.getenv('PASSWORD'),
#        'HOST': os.getenv('HOST'),
#        'PORT': os.getenv('PORT')
#    }
# }

DATABASES = {
   "default": {
       "ENGINE": "django.db.backends.postgresql_psycopg2", # тут не меняем
       'NAME': "tracker",
       'USER':  "postgres",
       'PASSWORD': "12345",
       'HOST': "127.0.0.1",
       'PORT': 5432
   }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


STATIC_URL = "static/"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AUTH_USER_MODEL = 'user.User'

REST_FRAMEWORK = {
    # "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_AUTHENTICATION_CLASSES": ("rest_framework_simplejwt.authentication.JWTAuthentication",),
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticated",],
}

SIMPLE_JWT = {
   'ACCESS_TOKEN_LIFETIME': timedelta(minutes=500),   # вернуть на 5 минут
   'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

CORS_ALLOWED_ORIGINS = [
    "https://read-only.example.com",
    "https://read-and-write.example.com",
]

CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:8000/",
]

