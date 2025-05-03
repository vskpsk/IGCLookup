<!DOCTYPE html>
<html>
<head>
    <title>IGC Lookup</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>

  <div class="centered">
    <div class="content">
      <h1 class="title">IGC Lookup</h1>
    
        <form id="uploadForm" action="/upload" method="POST" enctype="multipart/form-data" class="box">
          <label for="myfile">Select your file</label>
          <input type="file" id="myfile" name="myfile" accept=".igc">
        </form>
      
    </div>
     
  </div>


  <div class="info">
    <span>Some things and features may not work :(</span>
    <a href="https://github.com/vskpsk/IGCLookup">GitHub</a>
  </div>

  <script>
    document.getElementById('myfile').addEventListener('change', () => {
      document.getElementById('uploadForm').submit();
    });
  </script>
  
</body>
</html>