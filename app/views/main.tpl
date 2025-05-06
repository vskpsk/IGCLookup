<!DOCTYPE html>
<html>
<head>
    <title>IGC Lookup</title>
    <script src="https://cdn.plot.ly/plotly-2.32.0.min.js"></script>
    <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
    <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
    <link rel="stylesheet" href="/static/style2.css" />

</head>
<body>
  <h1 class="title">IGC Lookup</h1>
  <br><br>
  <h1>Flight info:</h1>
  <div class="heads">
    % for head in heads:
    <li>{{head}}: {{heads[head]}}</li>
    % end
  </div>

  <div id="map" style="height: 50em; width: 70em; margin: auto; border-radius: 15px;"></div>


  <script>
    var map = L.map('map').setView([{{first["lat"]}}, {{first["lon"]}}], 13);
  
    L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/' +
        'World_Imagery/MapServer/tile/{z}/{y}/{x}', {
    attribution: 'Tiles © Esri'
    }).addTo(map);

    var route = [
      % for point in flight.values():
        [{{point["lat"]}}, {{point["lon"]}}],
      % end
    ];

    var line = L.polyline(route, {color: "red"}).addTo(map)

  </script>
  
  
</body>
</html>
