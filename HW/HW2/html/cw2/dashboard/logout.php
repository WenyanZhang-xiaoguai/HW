<?php
include 'utils.php';
recordActionOperate('logout');
unset($_SESSION['loginUsername']);
header('Location: login.php');
?>
