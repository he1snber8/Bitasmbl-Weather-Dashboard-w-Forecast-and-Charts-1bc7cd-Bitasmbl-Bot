from django.urls import path
from api import views

urlpatterns = [
    path("api/weather/current/", views.weather_current, name="weather_current"),
    path("api/weather/forecast/", views.weather_current, name="weather_forecast"),
]
