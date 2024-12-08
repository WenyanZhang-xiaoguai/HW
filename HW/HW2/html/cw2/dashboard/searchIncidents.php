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
    $sql = "select incident.Incident_ID,Vehicle_plate,people.People_name,People_licence,Incident_Report,Offence_description,Fine_Amount,Fine_Points from Incident
    left join vehicle on vehicle.Vehicle_ID = incident.Vehicle_ID = vehicle.Vehicle_ID
    left join people on people.People_ID = incident.People_ID
    left join offence on offence.Offence_ID = incident.Offence_ID
    left join fines on fines.Incident_ID = incident.Incident_ID
    where incident.Incident_ID = '" . $content . "' or incident.Vehicle_ID = '" . $content . "'";
    $queryOutput = $db->get_rows($sql);
    // var_dump($queryOutput);
} else {
    $sql = "select incident.Incident_ID,Vehicle_plate,people.People_name,People_licence,Incident_Report,Offence_description,Fine_Amount,Fine_Points from Incident
    left join vehicle on vehicle.Vehicle_ID = incident.Vehicle_ID = vehicle.Vehicle_ID
    left join people on people.People_ID = incident.People_ID
    left join offence on offence.Offence_ID = incident.Offence_ID
    left join fines on fines.Incident_ID = incident.Incident_ID order by incident.Incident_ID";
    $queryOutput = $db->get_rows($sql);
}
?>


<div class="search-container">
    <form action="searchIncidents.php" method="get">
        <input type="text" name="search" placeholder="Search by incident ID"
               value="<?= htmlspecialchars($content) ?>">
        <input type="submit" value="Search">
    </form>
</div>

<?php if ($queryOutput): ?>
    <table class="results-table">
        <thead>
        <tr>
            <th>ID</th>
            <th>Vehicle Plate</th>
            <th>Driver Name</th>
            <th>Driver Licence</th>
            <th>Information</th>
            <th>Incident Report</th>
            <th>Points</th>
            <th>Fine Amount</th>

            <th>Action</th>
        </tr>
        </thead>
        <tbody>
        <?php foreach ($queryOutput as $row): ?>
            <tr>
                <td><?= htmlspecialchars($row['Incident_ID']) ?></td>
                <td><?= htmlspecialchars($row['Vehicle_plate'] ?? 'unknown') ?></td>
                <td><?= htmlspecialchars($row['People_name']) ?></td>
                <td><?= htmlspecialchars($row['People_licence']) ?></td>
                <td><?= htmlspecialchars($row['Offence_description']) ?></td>
                <td><?= htmlspecialchars($row['Incident_Report']) ?></td>
                <td><?= htmlspecialchars($row['Fine_Points'] ?? 'none') ?></td>
                <td><?= htmlspecialchars($row['Fine_Amount'] ?? 'none') ?></td>
                <!--                if admin can operate it-->

                <td>
                    <button>
                        <a href="./editFine.php?id=<?= $row['Incident_ID'] ?>">Edit</a></button>
                </td>

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