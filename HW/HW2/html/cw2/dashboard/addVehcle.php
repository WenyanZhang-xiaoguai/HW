<?php
$db = require './utils.php';
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

    .form-container input[type="text"], .form-container select {
        width: 100%;
        padding: 10px;
        margin-bottom: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    .form-container input[type="date"], .form-container select {
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


$owners = $db->get_rows("SELECT People_ID, People_name FROM People");

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $vehicle_plate = $_POST['vehicle_plate'] ?? null;
    $vehicle_brand = $_POST['vehicle_brand'] ?? null;
    $vehicle_model = $_POST['vehicle_model'] ?? null;
    $vehicle_color = $_POST['vehicle_color'] ?? null;
    $owner_id = $_POST['owner_id'] ?? null;
    $new_owner_name = $_POST['new_owner_name'] ?? null;
    $new_owner_address = $_POST['new_owner_address'] ?? null;
    $new_owner_licence = $_POST['new_owner_licence'] ?? null;

    // $vehicle_type = $vehicle_brand . ' ' . $vehicle_model;

    if ($new_owner_name) {
        $latest_id_sql = 'select max(People_ID) as max_id from People';
        $latest_id = $db->get_row($latest_id_sql)['max_id'] + 1;
        $sql = 'insert into People (People_ID, People_name,People_address,People_licence) values (' . $latest_id . ', "' . $new_owner_name . '","' . $new_owner_address . '","' . $new_owner_licence . '")';
        if (!$db->update($sql)) exit('Error: ' . $db->error);
        recordActionOperate('add people record');
        $owner_id = $latest_id;
    }

    $latest_id_sql = 'select max(Vehicle_ID) as max_id from Vehicle';
    $latest_id_car = $db->get_row($latest_id_sql)['max_id'] + 1;
    if($latest_id_car < 800) $latest_id_car = $db->get_row($latest_id_sql)['max_id'] + 1 + 200;
    else $latest_id_car = $db->get_row($latest_id_sql)['max_id'] + 1;

    $sql = "INSERT INTO Vehicle (Vehicle_make,Vehicle_model, Vehicle_colour, Vehicle_plate,Vehicle_ID) VALUES ('$vehicle_brand','$vehicle_model', '$vehicle_color', '$vehicle_plate',$latest_id_car)";
    // echo $sql;

    if (!$db->update($sql)) exit('Error: ' . $db->error);

    $sql = "INSERT INTO Ownership (People_ID, Vehicle_ID) VALUES ('$owner_id', '$latest_id_car')";
    if (!$db->update($sql)) exit('Error: ' . $db->error);

    echo '<script>alert("Vehicle added successfully");window.location.href="addVehcle.php"</script>';
    recordActionOperate('add vehicle');
    exit();
}
?>


<div class="form-container">
    <form action="addVehcle.php" method="post">
        <label for="vehicle_plate"><b>Vehicle Plate</b></label>
        <input type="text" id="vehicle_plate" name="vehicle_plate" placeholder="Vehicle Plate" required>

        <label for="vehicle_brand"><b>Vehicle Brand</b></label>
        <input type="text" id="vehicle_brand" name="vehicle_brand" placeholder="Vehicle Brand" required>


        <label for="vehicle_model"><b>Vehicle Model</b></label>
        <input type="text" id="vehicle_model" name="vehicle_model" placeholder="Vehicle Model" required>

        <label for="vehicle_color"><b>Vehicle Color</b></label>
        <input type="text" id="vehicle_color" name="vehicle_color" placeholder="Vehicle Color" required>

        <hr>
        <label for="owner_id"><b>Owner</b></label>
        <select id="owner_id" name="owner_id" onchange="toggleNewOwnerInput()">

            <option value="new">Create New Owner</option>
            <?php foreach ($owners as $owner): ?>
                <option value="<?= htmlspecialchars($owner['People_ID']) ?>"><?= htmlspecialchars($owner['People_name']) ?></option>
            <?php endforeach; ?>
        </select>

        <div id="new_owner_container">
            <label for="new_owner_name"><b>New Owner Name</b></label>
            <input type="text" id="new_owner_name" name="new_owner_name" placeholder="New Owner Name">


            <label for="new_owner_name"><b>Owner Address</b></label>
            <input type="text" id="new_owner_name" name="new_owner_address" placeholder="Owner Address">

            <label for="new_owner_name"><b>Owner licence</b></label>
            <input type="text" id="new_owner_name" name="new_owner_licence" placeholder="Owner licence">
        </div>

        <input type="submit" value="Add Vehicle">
    </form>
</div>

<script>
    function toggleNewOwnerInput() {
        var ownerSelect = document.getElementById('owner_id');
        var newOwnerContainer = document.getElementById('new_owner_container');
        if (ownerSelect.value === 'new') {
            newOwnerContainer.style.display = 'block';
        } else {
            newOwnerContainer.style.display = 'none';
        }
    }
</script>

</div>
</body>
</html>