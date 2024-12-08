<?php
$db = include './utils.php';
include 'tab.php';
?>
<style>
    .form-container {
        margin: 40px auto;
        max-width: 400px;
        padding: 40px;
        border: 1px solid #ccc;
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }

    .form-container input[type="text"],.form-container input[type="date"], .form-container select {
        width: 100%;
        padding: 10px;
        margin-bottom: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    .form-container input[type="submit"] {
        width: 100%;
        padding: 10px;
        background-color: #5cb85c;
        border: none;
        border-radius: 5px;
        color: #fff;
        cursor: pointer;
    }

    .form-container input[type="submit"]:hover {
        background-color: #4cae4c;
    }
</style>

<?php

if (postMappingRequest()) {
    $incident_date = $_POST['incident_date'] ?? null;
    $incident_report = $_POST['incident_report'] ?? null;
    $offence_id = $_POST['offence_id'] ?? null;
    $vehicle_id = $_POST['vehicle_id'] ?? null;
    $people_id = $_POST['people_id'] ?? null;
    $incident_date = date('Y-m-d', strtotime($incident_date));
    $fine_amount = $_POST['fine_amount'] ?? null;
    $fine_points = $_POST['fine_points'] ?? null;
    $id = $_POST['id'] ?? null;

    $sql = "UPDATE `Incident` SET Incident_Date = '$incident_date', Incident_Report = '$incident_report', Offence_ID = '$offence_id', Vehicle_ID = '$vehicle_id', People_ID = '$people_id' WHERE Incident_ID = '$id'";
    // echo $sql;
    $db->update($sql);

    if ($_SESSION['role'] == 'admin') {
        $has_fine = $db->get_row("SELECT * from `Fines` where Incident_ID = $id");
        if (!$has_fine) {
            $latest_id_sql = 'select max(Fine_ID) as max_id from Fines';
            $latest_id = $db->get_row($latest_id_sql)['max_id'] + 1;
            $sql = "INSERT INTO `Fines` (Fine_ID, Fine_Amount, Fine_Points, Incident_ID) VALUES ('$latest_id', '$fine_amount', '$fine_points', '$id')";
            $db->update($sql);
        } else {
            $sql = "UPDATE `Fines` SET Fine_Amount = '$fine_amount', Fine_Points = '$fine_points' WHERE Incident_ID = $id";
            $db->update($sql);
        }
    }

    echo '<script>alert("Report updated successfully");window.location.href="searchIncidents.php"</script>';
    recordActionOperate('update report');
}
$row = $db->get_row("SELECT incident.Incident_ID,Vehicle_ID,People_ID,Incident_Date,Incident_Report,Offence_ID,Fine_Amount,Fine_Points from `Incident` left join fines on fines.Incident_ID = incident.Incident_ID where incident.Incident_ID = " . $_GET['id']);
if (!$row) {
    echo '<script>alert("Report not found");window.location.href="searchIncidents.php"</script>';
    exit();
}
// var_dump($row);
?>

<div class="form-container">
    <form action="editFine.php" method="post">


        <label for="incident_date"><b>Incident Date</b></label>
        <input type="date" id="incident_date" name="incident_date" placeholder="Incident Date" required
               value="<?= $row['Incident_Date'] ?>">

        <label for="incident_report"><b>Incident Report</b></label>
        <input type="text" id="incident_report" name="incident_report" placeholder="Incident Report" required
               value="<?= $row['Incident_Report'] ?>">


        <label for="offence_id"><b>Offence</b></label>
        <select id="offence_id" name="offence_id">
            <?php

            $offence = $db->get_rows("SELECT * from `Offence`");

            ?>
            <?php foreach ($offence as $owner): ?>
                <option value="<?= htmlspecialchars($owner['Offence_ID']) ?>"><?= htmlspecialchars($owner['Offence_description']) ?></option>
            <?php endforeach; ?>
            <script>
                document.getElementById('offence_id').value = '<?=$row['Offence_ID']?>';
            </script>
        </select>

        <label for="vehicle_id"><b>Vehicle</b></label>
        <select id="vehicle_id" name="vehicle_id">
            <?php

            $vehicle = $db->get_rows("SELECT * from `Vehicle`");

            ?>
            <?php foreach ($vehicle as $owner): ?>
                <option value="<?= htmlspecialchars($owner['Vehicle_ID']) ?>"><?= htmlspecialchars($owner['Vehicle_plate']) ?></option>
            <?php endforeach; ?>
            <script>
                document.getElementById('vehicle_id').value = '<?=$row['Vehicle_ID']?>';
            </script>
        </select>

        <label for="people_id"><b>People</b></label>
        <select id="people_id" name="people_id">
            <?php

            $people = $db->get_rows("SELECT * from `People`");

            ?>
            <?php foreach ($people as $owner): ?>
                <option value="<?= htmlspecialchars($owner['People_ID']) ?>"><?= htmlspecialchars($owner['People_name']) ?></option>
            <?php endforeach; ?>
            <script>
                document.getElementById('people_id').value = '<?=$row['People_ID']?>';
            </script>
        </select>

        <input type="hidden" name="id" value="<?= $_GET['id'] ?>">


        <?php if ($_SESSION['role'] == 'admin'): ?>
            <label for="fine_amount"><b>Fine Amount</b></label>
            <input type="text" id="fine_amount" name="fine_amount" placeholder="Fine Amount" required
                   value="<?= $row['Fine_Amount'] ?>">

            <label for="fine_points"><b>Fine Points</b></label>
            <input type="text" id="fine_points" name="fine_points" placeholder="Fine Points" required
                   value="<?= $row['Fine_Points'] ?>">

        <?php endif; ?>


        <input type="submit" value="create report">
    </form>
</div>

</div>
</body>
</html>