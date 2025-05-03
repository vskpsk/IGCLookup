<!DOCTYPE html>
<html>
<head>
    <title>IGC Lookup</title>
    <script src="https://cdn.plot.ly/plotly-2.32.0.min.js"></script>
</head>
<body>
  <h1>Flight info:</h1>
  % for head in heads:
  <li>{{head}}: {{heads[head]}}</li>
  % end

  
</body>
</html>