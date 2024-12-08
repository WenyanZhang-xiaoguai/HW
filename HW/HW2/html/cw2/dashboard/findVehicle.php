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
<style>
    .page {
        padding: 10px 20px;
        background-color: #409eff;
        border: none;
        border-radius: 5px;
        color: #fff;
        cursor: pointer;
    }

    .linka {
        text-decoration: none;
        color: #fff;
    }
</style>
<?php


$content = $_GET['search'] ?? '';
$queryOutput = [];
$page = $_GET['page'] ?? 1;
$page = intval($page);

if ($content) {
    $sql = "SELECT Vehicle.Vehicle_plate, Vehicle.Vehicle_ID, Vehicle.Vehicle_make,Vehicle.Vehicle_model, Vehicle.Vehicle_colour, Vehicle.Vehicle_plate, People.People_name, People.People_licence
                FROM Vehicle
                LEFT JOIN Ownership ON Vehicle.Vehicle_ID = Ownership.Vehicle_ID
                LEFT JOIN People ON Ownership.People_ID = People.People_ID
                WHERE Vehicle.Vehicle_plate = '$content'".' group by Vehicle_ID  order by Vehicle.Vehicle_ID desc limit ' . ($page - 1) * 10 . ', 10';

    $queryOutput = $db->get_rows($sql);
    $pre = 'findVehicle.php?page=' . max($page - 1, 1).'&search='.$content;
    $next = 'findVehicle.php?page=' . ($page + 1).'&search='.$content;
    recordActionOperate('search vehicle');
    // var_dump($queryOutput);
}else{
 
    $sql = "SELECT Vehicle.Vehicle_plate, Vehicle.Vehicle_ID, Vehicle.Vehicle_make,Vehicle.Vehicle_model,Vehicle.Vehicle_colour, Vehicle.Vehicle_plate, People.People_name, People.People_licence
    FROM Vehicle
    LEFT JOIN Ownership ON Vehicle.Vehicle_ID = Ownership.Vehicle_ID
    LEFT JOIN People ON Ownership.People_ID = People.People_ID group by Vehicle_ID  order by Vehicle.Vehicle_ID desc limit " . ($page - 1) * 10 . ', 10';
    $queryOutput = $db->get_rows($sql);
    $pre = 'findVehicle.php?page=' . max($page - 1, 1);
    $next = 'findVehicle.php?page=' . ($page + 1);
}
// var_dump($queryOutput);
?>

    <div class="search-container">
        <form action="findVehicle.php" method="get">
            <input type="text" name="search" placeholder="Please use car plate to search"
                   value="<?= htmlspecialchars($content) ?>">
            <input type="submit" value="Search">
        </form>
    </div>

<?php if ($queryOutput): ?>
    <table class="results-table">
        <thead>
        <tr>
            <th>ID</th>
            <th>Car-owner Name</th>
            <th>Car-owner Licence</th>
            <th>Vehicle Plate</th>
            <th>Vehicle Color</th>
            <th>Vehicle Type</th>
            <th>Incidences</th>
        </tr>
        </thead>
        <tbody>
        <?php foreach ($queryOutput as $row): ?>
            <tr>
                <td><?= htmlspecialchars($row['Vehicle_ID']) ?></td>
                <td><?= (htmlspecialchars($row['People_name'] ?? 'unknown')) ?></td>
                <td> <?= (htmlspecialchars($row['People_licence'] ?? 'unknown')) ?></td>
                <td><?= htmlspecialchars($row['Vehicle_plate']) ?></td>
                <td><?= htmlspecialchars($row['Vehicle_colour']) ?></td>
                <td><?= htmlspecialchars($row['Vehicle_make']) ?> <?= htmlspecialchars($row['Vehicle_model']) ?></td>
                <td><a href="./searchIncidents.php?search=<?= htmlspecialchars($row['Vehicle_ID']) ?>">show detail</a></td>
            </tr>
        <?php endforeach; ?>
        </tbody>
    </table>
<?php elseif ($content): ?>
    <p>Search data is empty</p>
<?php endif; ?>

<div style="float: right;margin-top: 20px;">
    <button class="page"><a href="<?= $pre ?>" class="linka">Previous</a></button>
    <button class="page"><a href="<?= $next ?>" class="linka">Next</a></button>
</div>

</div>
</body>
</html>