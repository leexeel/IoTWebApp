<?php
//include 'include.php';

function dbConnect() {
  $dbServer = "192.168.10.66";
  $dbUser = "iot_user";
  $dbPassword = "init1234";
  $dbDataBase = "iot";
  $conn = new mysqli($dbServer, $dbUser, $dbPassword, $dbDataBase);
    // Check connection
  if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }
  return $conn;
}

function dbSelect($sqlString){

}

function dbInsert($sqlString){

}

?>

