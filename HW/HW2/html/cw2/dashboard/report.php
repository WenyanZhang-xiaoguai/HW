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

    .form-container input[type="text"], .form-container select,.form-container input[type="date"] {
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

    $latest_id_sql = 'select max(Incident_ID) as max_id from Incident';
    $latest_id = $db->get_row($latest_id_sql)['max_id'] + 1;

    $sql = "INSERT INTO `Incident` (Incident_ID, Incident_Date, Incident_Report, Offence_ID, Vehicle_ID, People_ID) VALUES ('$latest_id', '$incident_date', '$incident_report', '$offence_id', '$vehicle_id', '$people_id')";
    if (!$db->update($sql)) exit('Error: ' . $db->error);
    recordActionOperate('add report');
    echo '<script>alert("Report added successfully");window.location.href="report.php"</script>';
    exit();
}
?>

<div class="form-container">
    <form action="report.php" method="post">


        <label for="incident_date"><b>Incident Date</b></label>
        <input type="date" id="incident_date" name="incident_date" placeholder="Incident Date" required>

        <label for="incident_report"><b>Incident Report</b></label>
        <input type="text" id="incident_report" name="incident_report" placeholder="Incident Report" required>


        <label for="offence_id"><b>Offence</b></label>
        <select id="offence_id" name="offence_id">
            <?php

            $offence = $db->get_rows("SELECT * from `Offence`");

            ?>
            <?php foreach ($offence as $owner): ?>
                <option value="<?= htmlspecialchars($owner['Offence_ID']) ?>"><?= htmlspecialchars($owner['Offence_description']) ?></option>
            <?php endforeach; ?>
        </select>

        <label for="vehicle_id"><b>Vehicle</b></label>
        <select id="vehicle_id" name="vehicle_id">
            <?php

            $vehicle = $db->get_rows("SELECT * from `Vehicle`");

            ?>
            <?php foreach ($vehicle as $owner): ?>
                <option value="<?= htmlspecialchars($owner['Vehicle_ID']) ?>"><?= htmlspecialchars($owner['Vehicle_plate']) ?></option>
            <?php endforeach; ?>
        </select>

        <label for="people_id"><b>People</b></label>
        <select id="people_id" name="people_id">
            <?php

            $people = $db->get_rows("SELECT * from `People`");

            ?>
            <?php foreach ($people as $owner): ?>
                <option value="<?= htmlspecialchars($owner['People_ID']) ?>"><?= htmlspecialchars($owner['People_name']) ?></option>
            <?php endforeach; ?>
        </select>


        <input type="submit" value="create report">
    </form>
</div>

</div>
</body>
</html>