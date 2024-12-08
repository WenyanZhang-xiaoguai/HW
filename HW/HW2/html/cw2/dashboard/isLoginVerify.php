<?php

if (!isset($_SESSION['loginUsername'])) {
    echo '<script language="javascript">window.location = "login.php";</script>';
    exit;
}

function isCurrentPage($page)
{
    return (basename($_SERVER['PHP_SELF']) == $page)  ? 'class="active"' : '';
}

return $_SESSION['loginUsername'];