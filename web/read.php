<?php
include 'libs/dblib.php';

$conn = dbConnect();

$sql = "SELECT * FROM valuesType";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    echo "id: " . $row["idvaluesType"]. "<br>";
  }
} else {
  echo "0 results";
}
$conn->close();

?>
