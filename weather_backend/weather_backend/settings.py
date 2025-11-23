from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "change-me"
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = ["django.contrib.contenttypes","django.contrib.staticfiles","api"]
MIDDLEWARE = ["django.middleware.common.CommonMiddleware"]
ROOT_URLCONF = "weather_backend.urls"
WSGI_APPLICATION = "weather_backend.wsgi.application"
