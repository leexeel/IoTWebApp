<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="include/style.css">
</head>
<body>

<?php
include "libs/functions.php";
drawPage();
$devName=$_POST["devName"];
$devLocation=$_POST["devLocation"];
$devNumber=$_POST["devNumber"];
$devPassword=$_POST["devPassword"];
$devDescr=$_POST["devDescr"];

echo "
<div class=\"container\">
aici ar trebui sa fie:
";
echo $_POST["devName"];
echo "
</div>
";

?>