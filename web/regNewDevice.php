<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="include/style.css">
</head>
<body>

<?php
include "libs/functions.php";
drawPage();
echo "
<div class=\"container\">
aici ar trebui sa fie:
";
echo $_POST["devName"];
echo "
</div>
";

?>