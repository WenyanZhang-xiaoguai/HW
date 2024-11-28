<?php

@session_start();
$configDriver = include './db.inc.php';
include 'databaseUtils.php';
function postMappingRequest(): bool
{
    return $_SERVER['REQUEST_METHOD'] === 'POST';
}

function getConnect()
{
    global $configDriver;
    return new DB(
        $configDriver[0],
        $configDriver[1],
        $configDriver[2],
        $configDriver[3],
        3306
    );
}
$db = getConnect();

function recordActionOperate($description)
{
    global $db;
    $db->update('insert into log (username,reason) value ("' . $_SESSION['loginUsername'] . '","' . $description . '")');
}

return $db;