import os
from datetime import timedelta
from typing import List


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-$63hpaio#iyq#xq7&^_b&^%&)&+o*^!f5zsdi-zav)miitpu&p"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.humanize",
    "rest_framework",
    "rest_framework.authtoken",
    "django_filters",
    "crispy_forms",
    "bootstrap3",
    "bootstrap4",
    "fontawesome",
    "django_select2",
    "django_tables2",
    "django_jsonform",
    "extra_views",
    "cachalot",
    "corsheaders",
    "blog_user.apps.BlogUserConfig",
    "blog_post.apps.BlogPostConfig",
    "allauth",
    "allauth.account",
    # "api.apps.ApiConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'allauth.account.middleware.AccountMiddleware',
    "stronghold.middleware.LoginRequiredMiddleware",
]

ROOT_URLCONF = "django_intro.urls"

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
            ]
        },
    }
]

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

WSGI_APPLICATION = "django_intro.wsgi.application"




# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Africa/Kampala"

USE_I18N = True

USE_L10N = True

USE_TZ = True

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 1200
SESSION_SAVE_EVERY_REQUEST = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = "/static/"


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "DEFAULT_FILTER_BACKENDS": (
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
    ),
    "SEARCH_PARAM": "q",
    "PAGE_SIZE": 150,
}

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATIC_ROOT = os.path.join(BASE_DIR, "assets")

LOGIN_REDIRECT_URL = "posts"
LOGOUT_REDIRECT_URL = "account_login"
DJANGO_TABLES2_TEMPLATE = "django_tables2/bootstrap.html"
ACCOUNT_AUTHENTICATION_METHOD ="email"
ACCOUNT_EMAIL_REQUIRED=True


STRONGHOLD_PUBLIC_NAMED_URLS = (
    "admin:login",
    "account_change_password",
    "account_confirm_email",
    "account_email",
    "account_email_verification_sent",
    "account_inactive",
    "account_login",
    "account_logout",
    "account_reset_password",
    "account_reset_password_done",
    "account_reset_password_from_key",
    "account_reset_password_from_key_done",
    "account_set_password",
    "account_signup",
    "google_callback",
    "google_login",
    "socialaccount_connections",
    "socialaccount_login_cancelled",
    "socialaccount_login_error",
    "socialaccount_signup",
)

STRONGHOLD_PUBLIC_URLS = ("/api/", "/select2/")
CORS_ALLOW_HEADERS = ("content-type", "authorization", "x-csrf-token")

CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    "http://localhost",
    "http://127.0.0.1",
)
CORS_ALLOW_CREDENTIALS = True

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "npm.finders.NpmFinder",
]

AUTH_USER_MODEL = "blog_user.User"
ACCOUNT_ADAPTER = "blog_user.adapter.NoNewUsersAccountAdapter"