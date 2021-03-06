<?php

function guidv4()
{
    if (function_exists('com_create_guid') === true)
        return trim(com_create_guid(), '{}');

    $data = openssl_random_pseudo_bytes(16);
    $data[6] = chr(ord($data[6]) & 0x0f | 0x40); // set version to 0100
    $data[8] = chr(ord($data[8]) & 0x3f | 0x80); // set bits 6-7 to 10
    return vsprintf('%s%s-%s-%s-%s-%s%s%s', str_split(bin2hex($data), 4));
}

function getPasswordHash($password){
    return(hash("sha256",$password,FALSE));
}

function drawPage(){
echo " 
<div class=mainPage>
    <div class=\"mainLeft\">
        <a class= meniu href=index.php>Main page</a><br>
        <a class= meniu href=newdevice.php>Register new device</a>
        <a class= meniu href=viewdevices.php>Manage devices</a>
    </div>

";
}

function drawHeader(){
    echo " 
    <div class=\"mainTop\">
    IoT@Home NetPLUS Consult V1.0
    </div>
    ";
}

function drawFooter(){
    echo "
    </div> 
    <div class=\"mainBottom\">
    IoT@Home NetPLUS Consult V1.0
    </div>
    ";
}


?>

