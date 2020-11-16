<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="include/style.css">
</head>
<body>

<?php
include "libs/functions.php";

drawPage();
?>

<div class="container">  
  <form id="contact" action="regNewDevice.php" method="post">
    <h3>Register new IoT device</h3>
    <fieldset>
      <input name=devName placeholder="Device name" type="text" tabindex="1" required autofocus>
    </fieldset>
    <fieldset>
      <input name=devLocation placeholder="Device location" type="text" tabindex="2" required>
    </fieldset>
    <fieldset>
      <input name=devNumber placeholder="Sensors number" type="number" tabindex="3" required>
    </fieldset>
    <fieldset>
      <input name=devPassword placeholder="Password" type="password" tabindex="4" required>
    </fieldset>
    <fieldset>
      <textarea name=devDescr placeholder="Custom description" tabindex="5" required></textarea>
    </fieldset>
    <fieldset>
      <button name="submit" type="submit" id="contact-submit" data-submit="...Sending">Submit</button>
    </fieldset>
    <p class="copyright">Designed by <a href="https://hdt.ro" target="_blank" title="NetPLUS Consult" style=a>NetPLUS Consult</a></p>
  </form>
</div>
