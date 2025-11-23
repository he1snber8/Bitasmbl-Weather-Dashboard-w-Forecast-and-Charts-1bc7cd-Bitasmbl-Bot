<?php
require 'api_client.php';
$city = $_GET['city'] ?? 'London';
$forecast = call_weather_api('/forecast/', ['city'=>$city]);
?><!DOCTYPE html>
<html><head><title>Forecast</title></head>
<body>
<canvas id="tempChart" width="400" height="150"></canvas>
<script id="forecast-data" type="application/json"><?= json_encode($forecast) ?></script>
<script src="charts.js"></script>
</body></html>
