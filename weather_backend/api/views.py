from django.http import JsonResponse
import requests, time

_CACHE = {}
TTL = 300

def _get_cached(key):
    v = _CACHE.get(key)
    if v and time.time() - v[1] < TTL:
        return v[0]

def _set_cached(key, data):
    _CACHE[key] = (data, time.time())

def weather_current(request):
    city = request.GET.get("city", "London")
    key = f"cur:{city}"
    data = _get_cached(key)
    if not data:
        r = requests.get("https://api.open-meteo.com/v1/forecast", params={"latitude":0,"longitude":0})
        data = r.json()
        _set_cached(key, data)
    return JsonResponse(data)
