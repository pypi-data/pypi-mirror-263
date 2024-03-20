import os

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.postgresql"),
        "NAME": os.environ.get("SQL_DATABASE", "mtt_backend_django"),
        "USER": os.environ.get("SQL_USER", "mtt_backend_django"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "mtt_backend_django"),
        "HOST": os.environ.get("SQL_HOST", "db"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}