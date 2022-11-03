<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <meta name="description" content="Zcavenger Official Page">
	<meta name="keywords" content="Zcavenger, Zombie, Shooter, Games">
	<meta name="author" content="Pablo Flores">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="icon" type="image/x-icon" href="Img/favicon.ico">
	
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
	<link href="https://fonts.googleapis.com/css2?family=Anton&display=swap" rel="stylesheet">

	<link rel="stylesheet" href="Styles.css">
	<script src="https://kit.fontawesome.com/f97f302caa.js" crossorigin="anonymous"></script>

    <title>Zcavenger-Forum</title>
</head>

<body>

<script src="Nav.js"></script>


<?php
$conexion = mysqli_connect("zcavengerdb.ctla8z4b9mhj.sa-east-1.rds.amazonaws.com","garri87","Garris877!","Zcavenger_Page")or
die("Problemas con la conexión");

if($conexion){
    echo "Connected";
    echo "<br>";
}

$registro = mysqli_query($conexion, "SELECT userName
from users where userID = 1")or
die("select problems:" . mysqli_error($conexion));


if ($reg = mysqli_fetch_array($registro))
{
    echo "username is: ";
    echo $reg['userName'] . "<br>";
}
else {
	echo "no existe el usuario";
}

mysqli_close($conexion);	

?>



</body>

</html>