<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="include/style.css">
</head>
<body>

<?php
include 'libs/dblib.php';
include "libs/functions.php";
drawHeader();
drawPage();

$devName=$_POST["devName"];
$devLocation=$_POST["devLocation"];
$devNumber=$_POST["devNumber"];
$devPassword=$_POST["devPassword"];
$devDescr=$_POST["devDescr"];

$conn = dbConnect();

$sql = "insert into devices values(0,\"".$devName."\",\"".$devLocation."\",".$devNumber.",\"".guidv4()."\",\"".getPasswordHash($devPassword)."\",\"".$devDescr."\")";
if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
  } else {
    echo "Error: " . $sql . "<br>" . $conn->error;
  }
drawFooter();
?>