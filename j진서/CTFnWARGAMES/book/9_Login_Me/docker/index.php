<?php
/*

FLAG_{EasySQLiForBeginners}

*/

ini_set( 'display_errors', 0);
$pdo = null;


try {
	$pdo = new PDO("mysql:dbname=ctf;host=127.0.0.1;charset=utf8","root","SeC-0n4b");
} catch(Exception $e){
	system("cat /tmp/sql.sql | mysql --socket=/tmp/mysqld/mysqld.sock -u root -pSeC-0n4b");
}


if(isset($_POST["id"]) && $pdo){
    $uq = $pdo->query("SELECT id,loginid,auth_bit,lasttime FROM users WHERE loginid = '{$_POST['id']}' AND password = '{$_POST['pw']}'")->fetchAll();
    if(count($uq) > 0){$uq = $uq[0];}
    if(isset($uq["auth_bit"])){
        if($uq["auth_bit"] == "1023"){
            print "If you want to read the Flag. Read ME!";
            phpinfo();
            exit();
        }

        printLoginForm($uq["loginid"] . " is Not Admin User.");
        exit();
    }
    printLoginForm($_POST["id"] . "  Not Found");
} else {
    printLoginForm();
}


function printLoginForm($error=""){
?>
<!doctype html>
<html>
<head>
<title>Login</title>
<style>
#wrapper {
    width: 800px;
    margin: 0 auto;
    text-align : center ;
    border:1px ridge;
}
fieldset {
    border:0px;
}
</style>
</head>
<body>
<div id="wrapper">
<?php if($error != ""){print h($error); } ?>
<form method="POST">
    <fieldset>
        <label>ID</label>
        <input type="text" name="id" size="30">
    </fieldset>
    <fieldset>
        <label>PW</label>
        <input type="password" name="pw" size="30">
    </fieldset>
    <input type="submit" value="Login">
</form>
</div>
</body>
</html>
<?php
}


function h($str){
    return htmlspecialchars($str,ENT_QUOTES,"UTF-8");
}

?>

