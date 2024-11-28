<?php
$db = include './utils.php';
include 'tab.php';

?>

<style>
    .change-password-container {
        background-color: #fff;
        padding: 20px;
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }

    .change-password-container h2 {
        margin-bottom: 20px;
    }

    .change-password-container input[type="password"] {
        width: 100%;
        padding: 10px;
        margin: 10px 0;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    .change-password-container input[type="submit"] {
        width: 100%;
        padding: 10px;
        background-color: #5cb85c;
        border: none;
        border-radius: 5px;
        color: #fff;
        font-size: 16px;
        cursor: pointer;
    }

    .change-password-container input[type="submit"]:hover {
        background-color: #4cae4c;
    }

    .error {
        color: red;
        margin-bottom: 20px;
    }
</style>


    <div class="change-password-container">
        <h2>Change Password</h2>
        <form action="./modifyPassword.php" method="post" onsubmit="return validateForm()">
            <input type="password" id="oldPassword" name="oldPassword" placeholder="Old Password" required>
            <input type="password" id="newPassword" name="newPassword" placeholder="New Password" required>
            <input type="password" id="confirmPassword" name="confirmPassword" placeholder="Confirm New Password"
                   required>
            <div id="error" class="error"></div>
            <input type="submit" value="Change Password">
        </form>
    </div>

    <script>
        function validateForm() {
            const oldPassword = document.getElementById('oldPassword').value;
            const newPassword = document.getElementById('newPassword').value;
            const confirmPassword = document.getElementById('confirmPassword').value;
            const errorElement = document.getElementById('error');

            if (oldPassword === newPassword) {
                errorElement.textContent = 'Old password and new password cannot be the same.';
                return false;
            }

            if (newPassword !== confirmPassword) {
                errorElement.textContent = 'New password and confirm password do not match.';
                return false;
            }

            return true;
        }
    </script>
<?php
if (postMappingRequest()) {
    $oldPassword = $_POST['oldPassword'] ?? null;
    $newPassword = $_POST['newPassword'] ?? null;
    if ($oldPassword == null || $newPassword == null) {
        exit('<script>alert(\'invalid old-password or new-password\')</script>');
    }
    //if admin
    if ($_SESSION['role'] == 'admin') {
        recordActionOperate('Admin changed password');
        $update = 'update `Admins` set `Password` = "' . $newPassword . '" where `Username` = "' . $_SESSION['loginUsername'] . '" and `Password` = "' . $oldPassword . '"';
    }else{
        recordActionOperate('Officer changed password');
        $update = 'update `Officers` set `Password` = "' . $newPassword . '" where `Username` = "' . $_SESSION['loginUsername'] . '" and `Password` = "' . $oldPassword . '"';
    }
    $r = $db->update($update);
    // var_dump($r);
    if(!$r) exit('<script>alert(\'invalid old password\')</script>');
    exit('<script>
    window.location.href = "./logout.php"
</script>');
}
?>

</div>
</body>
</html>
