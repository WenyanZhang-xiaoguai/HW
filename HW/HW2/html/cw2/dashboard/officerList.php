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

// $content = $_GET['search'] ?? '';
if (postMappingRequest()) {
    $username = $_POST['username'] ?? null;
    $password = $_POST['password'] ?? null;
    if (!$username || !$password) {
        echo '<script>alert("Please fill in all fields");window.location.href="officerList.php"</script>';
        exit();
    }
    if ($db->get_row("SELECT * from `officers` where Username = '$username'")) {
        echo '<script>alert("Officer already exists");window.location.href="officerList.php"</script>';
        exit();
    }
    $sql = "INSERT INTO `officers` (Username, Password) VALUES ('$username', '$password')";
    $db->update($sql);
    recordActionOperate('add officer');
    echo '<script>alert("Officer added successfully");window.location.href="officerList.php"</script>';
    exit();
}

$sql = 'select * from officers';
$queryOutput = $db->get_rows($sql);
?>

    <div class="search-container">
        <h2>
            create a new officer
        </h2>
        <form action="officerList.php" method="post">
            <input type="text" name="username" placeholder="Username">


            <input type="password" name="password" placeholder="Password">
            <input type="submit" value="Create">
        </form>
    </div>

    <h2>Officer List</h2>
    <table class="results-table">
        <thead>
        <tr>
            <th>Username</th>
            <th>Password</th>
            <th>Actions</th>
        </tr>
        </thead>
        <tbody>
        <?php foreach ($queryOutput as $row): ?>
            <tr style="text-align: center">
                <td><?= htmlspecialchars($row['Username']) ?></td>
                <td><?= htmlspecialchars($row['Password']) ?></td>
                <td>
                    <form action="login.php" method="post">
                        <input type="hidden" name="username" value="<?= htmlspecialchars($row['Username']) ?>">
                        <input type="hidden" name="password" value="<?= htmlspecialchars($row['Password']) ?>">
                        <input type="submit" value="Login">
                    </form>
                </td>

            </tr>
        <?php endforeach; ?>
        </tbody>
    </table>
</div>
</body>
</html>