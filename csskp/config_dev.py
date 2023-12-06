import os

PUBLIC_URL = os.getenv("PUBLIC_URL") \
    if os.getenv("PUBLIC_URL") is not None \
    else ""
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(",") \
    if os.getenv("ALLOWED_HOSTS") is not None \
    else ["127.0.0.1", locals().get("PUBLIC_URL", "")]

OPERATOR_CONTACT = {
    "name": "Luxembourg house of Cybersecurity (LHC)",
    "street": "122 Rue Adolphe Fischer",
    "zip_code": "1521",
    "country": "Luxembourg",
    "phone": "(+352) 274 00 98 601",
    "website": "https://www.lhc.lu",
    "contact_email": "contact@lhc.lu",
    "privacy_email": "privacy@lhc.lu",
}

# The generic site/tool name. Used to load specific config, templates, styles, logo.
SITE_NAME = "fstp_registration"

SECRET_KEY = "u__*z&=urjtc0t)b)@5qbt_a#3-354=k9x(j)@eu#h7sb=-66s"

HASH_KEY = b"KnX5YN3hvP54jOIMkacWdqxFX1RKk8cjqVZjGJbAscM="

DEBUG = os.getenv("DEBUG").split(",") \
    if os.getenv("ALLOWED_HOSTS") is not None \
    else True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": os.getenv("DATABASE_PASSWORD")
            if os.getenv("DATABASE_PASSWORD") is not None
            else "password",
        "HOST": "db",
        "PORT": 5432,
    }
}

CORS_ALLOWED_ORIGINS = os.getenv("CORS_ALLOWED_ORIGINS").split(",") \
    if os.getenv("CORS_ALLOWED_ORIGINS") is not None else []
CORS_ALLOWED_ORIGIN_REGEXES = []
CORS_ALLOW_METHODS = [
    "GET",
    "OPTIONS",
]


EMAIL_HOST = "localhost"
EMAIL_PORT = 25

REPORT_TEMPLATE_DIR = "./templates/report/"

# Logging mechanism
LOG_DIRECTORY = "./logs"
LOG_FILE = "django.log"
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "root": {"level": "INFO", "handlers": ["file"]},
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": os.path.join(LOG_DIRECTORY, LOG_FILE),
            "formatter": "app",
        },
    },
    "loggers": {
        "django": {"handlers": ["file"], "level": "INFO", "propagate": True},
    },
    "formatters": {
        "app": {
            "format": (
                "%(asctime)s [%(levelname)-8s] (%(module)s.%(funcName)s) %(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
}
