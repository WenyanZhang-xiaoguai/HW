<?php
$db = require './utils.php';
?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .login-container {
            background-color: #fff;
            padding: 40px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        .login-container h2 {
            margin-bottom: 20px;
        }

        .login-container input[type="text"],
        .login-container input[type="password"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        .login-container input[type="submit"] {
            width: 100%;
            padding: 10px;
            background-color: #5cb85c;
            border: none;
            border-radius: 5px;
            color: #fff;
            font-size: 16px;
            cursor: pointer;
        }

        .login-container input[type="submit"]:hover {
            background-color: #4cae4c;
        }
    </style>
</head>
<body>
<?php
//process login request
$error = false;
if (postMappingRequest()) {
    $username = $_POST['username'] ?? null;
    $password = $_POST['password'] ?? null;
    if (!$username || !$password) {
        $error = true;
    } else {
        //first query officers
        $sql = "SELECT * FROM `Officers` WHERE username = '$username' AND password = '$password'";
        $result = $db->get_row($sql);
        if ($result == null) {
            $sql = "SELECT * FROM `Admins` WHERE username = '$username' AND password = '$password'";
            $result = $db->get_row($sql);
            if($result == null){
                $error = true;
            }else{
                $_SESSION['loginUsername'] = $result['Username'];
                $_SESSION['role'] = 'admin';
                recordActionOperate("Admin logged in");
                echo "<script>alert('Login success');window.location.href=\"./index.php\"</script>";
            }
        }else{
            $_SESSION['loginUsername'] = $result['Username'];
            $_SESSION['role'] = 'officer';
            recordActionOperate("Officer logged in");
            echo "<script>alert('Login success');window.location.href=\"./index.php\"</script>";
        }
    }
}
?>
<div class="login-container">
    <h2>Login</h2>
    <form action="login.php" method="post">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>

        <?php if ($error): ?>
            <div style="margin-bottom: 20px;color: red">
                Incorrect username or password
            </div>
        <?php endif; ?>
        <input type="submit" value="Login">
    </form>
</div>
</body>
</html>