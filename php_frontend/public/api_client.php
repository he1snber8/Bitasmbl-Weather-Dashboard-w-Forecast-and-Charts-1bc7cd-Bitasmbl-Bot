<?php
function call_weather_api($path, $params = []) {
    $base = 'http://localhost:8000/api/weather';
    $url = $base . $path . '?' . http_build_query($params);
    $resp = file_get_contents($url);
    return json_decode($resp, true);
}
