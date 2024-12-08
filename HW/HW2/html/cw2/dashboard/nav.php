<?php
$username = require 'security.php';
?>
<!DOCTYPE html>
<html lang="">
<head>
    <style>
        body {
            display: flex;
            margin: 0;
            font-family: Arial, sans-serif;
        }

        .sidebar {
            height: 100vh;
            width: 250px;
            position: fixed;
            top: 0;
            left: 0;
            background-color: #6c6c6c;
            padding-top: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .sidebar a {
            padding: 15px;
            text-align: center;
            text-decoration: none;
            font-size: 18px;
            color: white;
            display: block;
            width: 100%;
        }

        .sidebar a:hover {
            background-color: #575757;
        }

        .active {
            background-color: #373737;
        }

        .content {
            margin-left: 250px;
            padding: 20px;
            width: 100%;
        }

        .profile {
            margin-top: auto;
            padding: 20px;
            text-align: center;
        }

        .profile img {
            border-radius: 50%;
            width: 60px;
            height: 60px;
        }

        .profile span {
            display: block;
            color: white;
            margin-top: 10px;
        }

        .dropdown-content {
            display: none;
            position: absolute;
            background-color: #f9f9f9;
            min-width: 160px;
            box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
            z-index: 1;
        }

        .dropdown-content a {
            color: black;
            padding: 12px 16px;
            text-decoration: none;
            display: block;
        }

        .dropdown-content a:hover {
            background-color: #f1f1f1;
        }

        .dropdown:hover .dropdown-content {
            display: block;
        }
    </style>
</head>
<body>
<?php

function checkActive($page): string
{
    $current = basename($_SERVER['PHP_SELF']);
    if ($current == $page) {
        return 'class="active"';
    }
    return '';
}

?>
<div class="sidebar">
    <nav>
        <a href="index.php" <?= checkActive('index.php'); ?> >Index</a>
        <a href="findPeople.php" <?= checkActive('findPeople.php'); ?>>Search People</a>
        <a href="findVehicle.php" <?= checkActive('findVehicle.php'); ?>>Search Vehicle</a>
        <a href="addVehcle.php" <?= checkActive('addVehcle.php'); ?>>Add Vehicle</a>
        <a href="report.php" <?= checkActive('report.php'); ?>>Report Incident</a>
        <a href="searchIncidents.php" <?= checkActive('searchIncidents.php'); ?> <?= checkActive('editFine.php'); ?>>Search Incidents</a>
        <?php if ($_SESSION['role'] == 'admin') { ?>
            <a href="police.php" <?= checkActive('police.php'); ?>>Police Manage</a>
        <?php } ?>
        <a href="logger.php" <?= checkActive('logger.php'); ?>>Security Log</a>

        <a href="modifyPassword.php" <?= checkActive('modifyPassword.php'); ?>>Modify Password</a>

        <a href="logout.php" style="font-size: 0.8rem;color: red">Logout</a>
    </nav>
    <div class="profile">
        <img src="../image/user.png" alt="Profile Picture">
        <span><?php echo $username; ?></span>
<!--        <div class="dropdown-content">-->
<!--            <a href="modifyPassword.php">Modify Password</a>-->
<!--            <a href="logout.php">Logout</a>-->
<!--        </div>-->
    </div>
</div>
<div class="content">
