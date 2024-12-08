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

    .search-container input[type="submit"] {
        padding: 10px 20px;
        background-color: #5cb85c;
        border: none;
        border-radius: 5px;
        color: #fff;
        cursor: pointer;
    }

    .search-container input[type="submit"]:hover {
        background-color: #4cae4c;
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

if ($content) {
    $sql = "SELECT * FROM People WHERE People_name LIKE '%$content%' OR People_licence = '$content'";
    $queryOutput = $db->get_rows($sql);
    recordActionOperate('search people');
}
?>


    <div class="search-container">
        <form action="findPeople.php" method="get">
            <input type="text" name="search" placeholder="Search by licence number or name" value="<?= htmlspecialchars($content) ?>">
            <input type="submit" value="Search">
        </form>
    </div>

<?php if ($queryOutput): ?>
    <table class="results-table">
        <thead>
        <tr>
            <th>ID</th>
            <th>licence Number</th>
            <th>Name</th>
            <th>Address</th>
        </tr>
        </thead>
        <tbody>
        <?php foreach ($queryOutput as $row): ?>
            <tr>
                <td><?= htmlspecialchars($row['People_ID']) ?></td>
                <td><?= htmlspecialchars($row['People_licence']) ?></td>
                <td><?= htmlspecialchars($row['People_name']) ?></td>
                <td><?= htmlspecialchars($row['People_address']) ?></td>
            </tr>
        <?php endforeach; ?>
        </tbody>
    </table>
<?php elseif ($content): ?>
    <p>Search data is empty</p>
<?php endif; ?>

</div>
</body>
</html>
