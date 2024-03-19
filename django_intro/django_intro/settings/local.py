from .base import *
from decouple import config


DEBUG = True

SITE_ID = 2

INSTALLED_APPS += ["debug_toolbar"]  # noqa: F405

INTERNAL_IPS = ["127.0.0.1", "::1"]

SESSION_COOKIE_SECURE = False

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware"
] + MIDDLEWARE  # noqa: F405

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DATABASE_NAME"),
        "USER": config("DATABASE_USER"),
        "PASSWORD": config("DATABASE_PASSWORD"),
        "HOST": config("DATABASE_HOST"),
        "PORT": config("DATABASE_PORT"),
    }
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": os.path.join(BASE_DIR, "debug.log"),  # noqa: F405
        },
        "console": {"level": "WARNING", "class": "logging.StreamHandler"},
    },
    "loggers": {
        "": {"handlers": ["file"], "level": "DEBUG", "propagate": True},
        "django": {"handlers": ["file"], "level": "DEBUG", "propagate": True},
        "django.template": {"handlers": ["file"], "level": "DEBUG", "propagate": True},
    },
}

SELECT2_JS = "/static/select2/dist/js/select2.min.js"
SELECT2_CSS = "/static/select2/dist/css/select2.css"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique-snowflake",
    }
}
DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.logging.LoggingPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
    "cachalot.panels.CachalotPanel",
]

CACHALOT_ENABLED = False