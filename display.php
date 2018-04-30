<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>display</title>
    <script>
    </script>
  </head>
  <body>
  <a href="index.html"><input type="button" value="upload !"/></a>
  <script>
  <?php
     $files = glob($dir . 'images/*.*');
        $file = array_rand($files, 1);
   ?>
   var oui = window.setInterval(reload, 7000);
   function reload(){
   location.reload();
   }
   </script>
    <img src="<?=$files[$file]?>">
  </body>
  </html>
