<?php
$db = include './utils.php';
include 'tab.php';
?>
<style>
    .search-container {
        margin: 20px;
    }

    .search-container input[type="text"] {
        width: 300px;
        padding: 10px;
        margin-right: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    .search-container input[type="password"] {
        width: 300px;
        padding: 10px;
        margin-right: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    .search-container input[type="submit"] {
        padding: 10px 20px;
        background-color: #409eff;
        border: none;
        border-radius: 5px;
        color: #fff;
        cursor: pointer;
    }

    .search-container input[type="submit"]:hover {
        background-color: #409eff;
        opacity: 0.8;
    }

    .results-table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 20px;
    }

    .results-table th, .results-table td {
        border: 1px solid #ddd;
        padding: 8px;
    }

    .results-table th {
        background-color: #f2f2f2;
    }
</style>


<?php


$content = $_GET['search'] ?? '';
$queryOutput = [];
$page = $_GET['page'] ?? 1;
$page = intval($page);

if ($content) {
    $sql = 'select * from log where username = "' . $content . '" order by id desc limit ' . ($page - 1) * 10 . ', 10';
    $queryOutput = $db->get_rows($sql);
} else {
    $sql = 'select * from log order by id desc limit ' . ($page - 1) * 10 . ', 10';
    $queryOutput = $db->get_rows($sql);
}

$pre = 'logger.php?page=' . max($page - 1, 1) . ($content ? '&search=' . $content : '');
$next = 'logger.php?page=' . ($page + 1) . ($content ? '&search=' . $content : '');
?>

<div class="search-container">
    <form action="logger.php" method="get">
        <input type="text" name="search" placeholder="Search by Username"
               value="<?= htmlspecialchars($content) ?>">
        <input type="submit" value="Search">
    </form>
</div>


<table class="results-table">
    <thead>
    <tr>
        <th>ID</th>
        <th>Username</th>
        <th>Reason</th>
        <th>Time</th>
    </tr>
    </thead>
    <tbody>
    <?php foreach ($queryOutput as $row): ?>
        <tr style="text-align: center">
            <td><?= htmlspecialchars($row['id']) ?></td>
            <td><?= htmlspecialchars($row['username']) ?></td>
            <td><?= htmlspecialchars($row['reason']) ?></td>
            <td><?= htmlspecialchars($row['time']) ?></td>
        </tr>
    <?php endforeach; ?>
    </tbody>
</table>

<style>
    .page {
        padding: 10px 20px;
        background-color: #409eff;
        border: none;
        border-radius: 5px;
        color: #fff;
        cursor: pointer;
    }

    a {
        text-decoration: none;
        color: #fff;
    }
</style>
<div style="float: right;margin-top: 20px;">
    <button class="page"><a href="<?= $pre ?>">Previous</a></button>
    <button class="page"><a href="<?= $next ?>">Next</a></button>
</div>

</div>
</body>
</html>