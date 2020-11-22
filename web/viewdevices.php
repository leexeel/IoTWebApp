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

$conn = dbConnect();

$sql = "SELECT * FROM devices";
$result = $conn->query($sql);
echo "<div class=tableList>";
if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    echo "id: " . $row["idDevice"].$row["dvName"].$row["dvLocation"].$row["sensNumber"].$row["devDescription"]. "<br>";
  }
} else {
  echo "0 results";
}
echo "</div>";
$conn->close();

drawFooter();
?>
