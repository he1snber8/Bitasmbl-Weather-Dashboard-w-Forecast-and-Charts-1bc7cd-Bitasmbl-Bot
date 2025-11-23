<?php
$city = $_GET['city'] ?? 'London';
$apiBase = 'http://localhost:8000/api/weather';
$curJson = file_get_contents("$apiBase/current/?city=".urlencode($city));
$cur = json_decode($curJson, true);
?><!DOCTYPE html>
<html><head><title>Weather Dashboard</title></head>
<body>
<form method="get">
<input name="city" value="<?= htmlspecialchars($city) ?>" />
<button type="submit">Search</button>
</form>
<section id="current">
<h2>Current Weather</h2>
<pre><?php print_r($cur); ?></pre>
</section>
<section id="forecast"></section>
</body></html>
